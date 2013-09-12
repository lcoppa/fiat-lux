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
Pilon IP-C Server Local Host Collector Class

This module contains a Pilon Collector class that collects
Device and Datapoint resources from the local host.
Device instances include the local clock, and performance
monitoring objects for the CPU, memory and disk.
Datapoints describe various statistics associated with
these 'devices'.
"""

__version__ = "$Revision: #4 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/collectors/localhost.py $


import logging
import psutil
import time

from django.core.exceptions import ValidationError

from api.models.datapoint   import Datapoint
from api.models.device      import Device
from collectors.collector   import Collector
from shared                 import NAMESPACE


__all__ = ['LocalhostCollector', 'DEFAULT_LOCALHOST_POLL']


# default Localhost collector parameters
DEFAULT_LOCALHOST_POLL = 5
""" Default poll interval for collecting localhost statistics."""

# names of Localhost collector datapoints
LOCALHOST_DATAPOINT_CPU    = "cpu"
LOCALHOST_DATAPOINT_MEMORY = "memory"
LOCALHOST_DATAPOINT_DISK   = "disk"


# our logger
logger = logging.getLogger(NAMESPACE('collectors.localhost'))


class LocalhostCollector(Collector):
    """
    'Collector' class that collects information from the local host.
    """

    # this Collector is read-only, so does not need a task queue
    needs_queue = False

    def __init__(self, name, poll=DEFAULT_LOCALHOST_POLL):
        """
        Initialize a new LocalhostCollector.
        
        Arguments:
            name -- the name of this Collector instance (identifies source of collected data)
            poll -- the poll interval for collecting statistics (default: 5)
        """
        super().__init__(name)
        self.poll = poll


    def __repr__(self):
        return "%s(name=%r, poll=%r)" % (self.__class__.__name__, self.name, self.poll)
    
    
    def run(self):
        """
        Entry point for the Localhost collector thread.
        """
        
        # fetch/create/save our devices, as necessary
        devices = {
            name: Device.get_device(name=name,
                                    type=name,
                                    source=self.name)[0]
            for name in (LOCALHOST_DATAPOINT_CPU,
                         LOCALHOST_DATAPOINT_MEMORY,
                         LOCALHOST_DATAPOINT_DISK)
        }

        while not Collector.shutdown:
            # collect CPU utilization
            self.collect_cpu(devices[LOCALHOST_DATAPOINT_CPU])
            
            # delay before next collection
            wait = self.poll
            while wait >= 1.0 and not Collector.shutdown:
                time.sleep(1.0)
                wait -= 1.0
            if not Collector.shutdown:
                if wait > 0.0:
                    time.sleep(wait)
            
        # shutdown and close connection to LonBridge Server
        print("Shutting down Localhost Collector")


    def collect_cpu(self, device):
        # fetch/create datapoint (we'll save it to the database below)
        datapoint = device.get_datapoint("utilization", read_only=True, save=False)[0]
        
        # fetch CPU utilization (over 1.0 second interval)
        logger.debug("Retrieving value for datapoint: %s...", datapoint)
        cpu = psutil.cpu_percent(1.0)
        
        # update the datapoint value
        old_value = datapoint.value
        new_value = "%.1f" % cpu
        if old_value != new_value:
            logger.info("Updating value for datapoint: %s: %r -> %r",
                        datapoint, old_value, new_value)
        datapoint.value = cpu
        
        try:
            # validate and save the new datapoint value
            datapoint.full_clean()
            datapoint.save()
            logger.info("Updated datapoint: %s", datapoint)
            
        except ValidationError as e:
            # datapoint update failed
            logger.error("Data for updated datapoint (%s) failed validation: %s", datapoint, e)
