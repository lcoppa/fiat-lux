#
# Copyright (c) 2013 Echelon Corporation.  All rights reserved.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""
Pilon IP-C Server LonBridge Collector Class

This module contains a Pilon Collector class that collects and updates
Device and Datapoint resources from a LonBridge Server.
"""

__version__ = "$Revision: #13 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/collectors/lonbridge.py $


import logging
import socket

from xml.etree              import ElementTree as xml

from django.core.exceptions import ValidationError

from api.models.device      import Device
from shared                 import NAMESPACE

from .collector             import Collector
from .task                  import DeviceUpdateTask, DeviceCommandTask, DatapointUpdateTask


__all__ = ['DEFAULT_LONBRIDGE_HOST', 'DEFAULT_LONBRIDGE_PORT',
           'LonBridgeCollector', 'DeviceUpdateTask', 'DatapointUpdateTask']


# default LonBridge Server parameters
DEFAULT_LONBRIDGE_HOST = 'localhost'
DEFAULT_LONBRIDGE_PORT = 3050


# our logger
logger = logging.getLogger(NAMESPACE('collectors.lonbridge'))


# a function that returns the function name of the caller
#import sys
#def __func__():
#    return sys._getframe().f_back.f_code.co_name


def trace_socket(sock, dirn, msg):
    """
    Trace a text-based socket message to the log.
    
    Arguments:
        sock -- the socket
        dirn -- a direction tag for the log (e.g. either 'SEND' or 'RECV')
        msg  -- the text-based message to be sent or that was received (type is either 'str' or 'bytes')
    """
    # decode message from 'bytes', if appropriate
    if isinstance(msg, bytes):
        msg = msg.decode()

    # log socket message
    logger.debug("SOCKET #%d: %s: %s", sock.fileno(), dirn, msg)
    
    
def socket_send(sock, msg):
    """
    Send a message to a socket and trace the message to the log.
    """

    # encode message to 'bytes', if appropriate
    if isinstance(msg, str):
        msg = msg.encode()

    # trace the message to be sent
    trace_socket(sock, 'SEND', msg)
    
    # send the message to the socket
    sock.send(msg)
    
    
class LonBridgeCollector(Collector):
    """
    'Collector' class that collects information from a LonBridge Server.
    """

    # a non-blank value for devid is required for LonBridge-based devices
    requires_devid = True

    # LonBridge attributes that map to Device fields
    device_attribs = ('name', 'brand', 'type', 'active', 'category')
    
    # dictionary that maps LonBridge attribute names to Device fields
    device_attrib_map = {'category': 'categories'}
    
    def __init__(self, name, host=DEFAULT_LONBRIDGE_HOST, port=DEFAULT_LONBRIDGE_PORT):
        """
        Initialize a new LonBridgeCollector.
        
        Arguments:
            name -- the name of this Collector instance (identifies source/target of collected data)
            host -- the host name or IP address of the LonBridge Server (default: "localhost")
            port -- the TCP port number of the LonBridge Server (default: 3050)        
        """
        super().__init__(name)
        self.host = host
        self.port = port
        
        self.sock = None


    def __repr__(self):
        return "%s(name=%r, host=%r, port=%r)" % (self.__class__.__name__, self.name, self.host, self.port)
    
    
    def run(self):
        """
        Entry point for the LonBridge collector thread.
        """
        
        # connect to the LonBridge Server
        logger.debug("Connecting to LonBridge Server at %s:%d...", self.host, self.port)
        self.sock = socket.socket()
        try:
            self.sock.connect((self.host, self.port))
        except socket.error as e:
            logger.error("Failed to connect to LonBridge Server at %s:%d!  %s", self.host, self.port, e)
            return
        logger.info("Connected to LonBridge Server at %s:%d", self.host, self.port)
        
        # set a timeout on socket operations so that we can check for the shutdown flag
        self.sock.settimeout(0.1)
        
        # send request to LonBridge Server for all known objects
        socket_send(self.sock, b'<lon><get/></lon>')
        
        buffer = b''
        while not Collector.shutdown:
            # process task queue
            self.process_queue()
                
            try:
                buffer += self.sock.recv(1024)
            except socket.timeout:
                # timeout - go around again
                continue
            
            # split on NUL bytes (LonBridge Server separates messages with one)
            msgs = buffer.split(b'\x00')
            buffer = msgs.pop()
            
            # process each new message
            for msg in msgs:
                # convert to a string (assumes UTF-8 encoding)
                s = msg.decode()

                # trace unpacked socket message
                trace_socket(self.sock, 'RECV', msg)
                
                # parse the resulting XML string
                lon = xml.XML(s)
                assert lon.tag == 'lon'
                for elem in lon:
                    # extract the command and the (optional) argument(s) from the tag
                    args = elem.tag.rsplit('.', 1)
                    cmd  = args.pop()
                    
                    # handle the 'is' commands
                    if cmd == 'is' or cmd == 'is_new' or cmd == 'is_pending':
                        # argument is the LonBridge Server device ID (including network interface name prefix)
                        devid = args[0]
                        assert devid.startswith('lon1.')
                        #for attrib in elem.attrib:
                        #    print('IS: (%s) %s = %s' % (devid, attrib, elem.attrib[attrib]))
                        
                        # process device-specific data
                        # (device attributes will be removed from the attribute list)
                        device = self.process_device(devid, elem.attrib)
                        if not device:
                            # failure processing device - skip it
                            continue
                         
                        # process datapoints-specific data for this device
                        self.process_datapoints(device, elem.attrib)
                    
                    elif cmd == "error":
                        logger.error("Error #%s from LonBridge Server: %s", elem.attrib['code'], elem.attrib['description'])
                        
                    else:
                        assert False, "Unrecognized LonBridge command: %s" % cmd
                
        # shutdown and close connection to LonBridge Server
        print("Shutting down LonBridge Collector")
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
    
    
    def process_device(self, devid, attribs):
        """
        Given a device ID and a list of LonBridge attributes, create and/or
        update the corresponding Device resource.  Removes the device-specific
        attributes from the list passed in, and on successful creation/update,
        returns the Device object.  The list of LonBridge attributes that
        map to Device fields is specified in 'device_attribs'.
        """
        
        # fetch/create device (we'll save it to the database below)
        device = Device.get_device(save=False, devid=devid, source=self.name)[0]
        
        logger.debug("Updating data for device: %s...", device)
        updates = 0
        unprocessed_attribs = {}
        for attrib in attribs:
            # check whether this is a Device-based attribute
            if not attrib in LonBridgeCollector.device_attribs:
                # this is not a Device attribute (it's probably a Datapoint attribute)
                # - save it and continue with next attribute
                unprocessed_attribs[attrib] = attribs[attrib]
                continue
            
            # this is a Device attribute
            attrib = LonBridgeCollector.device_attrib_map[attrib] or attrib
            old_value = device.__dict__[attrib]
            new_value = attribs[attrib]
            if old_value != new_value:
                if updates == 0:
                    logger.info("Updating data for device: %s...", device)
                updates += 1
                logger.info("  %s: %r -> %r", attrib, old_value, new_value)
                device.__dict__[attrib] = new_value

        try:
            # validate and save the new/updated device
            # NOTE: SQLite ignores 'max_length' and 'choices' are not enforced
            #       (except when creating them from forms),
            #       so use 'full_clean()' to validate the data before saving it.
            #       See <http://stackoverflow.com/questions/8478054/django-model-charfield-max-length-does-not-work>
            #       and <http://stackoverflow.com/questions/2520598/check-if-django-model-field-choices-exists?rq=1>.
            device.full_clean()
            device.save()
            #logger.info("Created/updated device: %s", device)
            
        except ValidationError as e:
            # device creation/update failed
            logger.error("Data for new/updated device (%s) failed validation: %s", device, e)
            
            # send a request for the full object details
            # TODO: fix this so it can't lead to run-away failures
            logger.debug("Requesting full information for device '%s'...", device)
            socket_send(self.sock, '<lon><%s.get/></lon>' % (devid))
            
            return None

        # update the list of attributes that still need to be processed
        attribs.clear()
        attribs.update(unprocessed_attribs)
        
        # device creation/update succeeded
        return device
        
        
    def process_datapoints(self, device, attribs):
        """
        Given a device and a list of LonBridge attributes, create and/or update
        the corresponding Datapoint resources.
        """

        for attrib in attribs:
            # fetch/create datapoint (we'll save it to the database below)
            datapoint = device.get_datapoint(attrib, save=False)[0]

            logger.debug("Updating value for datapoint: %s...", datapoint)
            old_value = datapoint.value
            new_value = attribs[attrib]
            if old_value != new_value:
                logger.info("Updating value for datapoint: %s...", datapoint)
                logger.info("  %s: %r -> %r", attrib, old_value, new_value)
                datapoint.value = new_value
                
            try:
                # validate and save the new/updated datapoint
                # NOTE: SQLite ignores 'max_length' and 'choices' are not enforced
                #       (except when creating them from forms),
                #       so use 'full_clean()' to validate the data before saving it.
                #       See <http://stackoverflow.com/questions/8478054/django-model-charfield-max-length-does-not-work>
                #       and <http://stackoverflow.com/questions/2520598/check-if-django-model-field-choices-exists?rq=1>.
                datapoint.full_clean()
                datapoint.save()
                #logger.info("Created/updated datapoint: %s", datapoint)
            except ValidationError as e:
                # datapoint creation/update failed
                # - skip to next datapoint
                logger.error("Data for new/updated datapoint (%s) failed validation: %s", datapoint, e)
   
   
    def process_queue(self):
        """
        Processes the queue of pending tasks.
        """
        # process queued up tasks, if any
        while not self.queue.empty():
            # fetch the next task
            task = self.queue.get_nowait()
            
            if isinstance(task, DeviceUpdateTask):
                self.update_device(task)
            elif isinstance(task, DeviceCommandTask):
                self.command_device(task)
            elif isinstance(task, DatapointUpdateTask):
                self.update_datapoint(task)
            else:
                assert False, "Unrecognized LonBridge task object: %r" % task

            # signal that this task has been completed
            self.queue.task_done()


    def update_device(self, task):
        """ Update the attributes of a device in the LonBridge Server. """
        device = task.device
        
        # fetch LonBridge device ID
        devid = device.devid
        
        # generate the list of attributes to be set
        #fields = ['%s="%s"' % (field, value) for field, value in device.__dict__.items()]
        fields = ('name="%s"' % device.name, )

        # send request to LonBridge Server to update the device
        socket_send(self.sock,
                    '<lon><%s.set %s /></lon>' %
                    (devid, " ".join(fields)))


    def command_device(self, task):
        """ Send a command to a device. """
        device = task.device
        command = task.command
        
        # fetch LonBridge device ID
        devid = device.devid
        
        # send request to LonBridge Server to send command to the device
        socket_send(self.sock,
                    '<lon><%s.%s /></lon>' %
                    (devid, command))


    def update_datapoint(self, task):
        """ Update the attributes of a datapoint in the LonBridge Server. """
        datapoint = task.datapoint
        
        # fetch (related) LonBridge device ID
        devid = datapoint.device.devid
        
        # send request to LonBridge Server to update the datapoint (device attribute)
        socket_send(self.sock,
                    '<lon><%s.set %s="%s" /></lon>' %
                    (devid, datapoint.name, datapoint.value))
