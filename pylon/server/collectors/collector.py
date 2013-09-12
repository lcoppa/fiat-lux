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
Pilon IP-C Server Collector Base Class
"""

__version__ = "$Revision: #10 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/collectors/collector.py $


__all__     = ['Collector']


import logging
import queue
import signal

from importlib import import_module
from threading import current_thread, Thread

from django.conf import settings    
from django.core import validators

from shared import NAMESPACE


# our logger
logger = logging.getLogger(NAMESPACE('collectors'))


# helper function to return the class object
# for the specified named class in the specified named module
def _class_for_name(module_name, class_name):    
    # load the module, will raise ImportError if module cannot be loaded
    m = import_module(module_name)
    
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    
    return c


class Collector(object):
    """
    Base class for all IP-C Collector classes.
    Do not use directly.
    """

    # default value for require_devid - can be overridden by derived classes
    requires_devid = False
    """Whether a non-blank 'devid' is required."""
 
    # default value for needs_queue - can be overridden by derived classes
    needs_queue = True
    """Whether a Collector-derived class needs a task queue."""
   
    def __init__(self, name, **kwargs):
        """
        Initialize a new Collector.
        
        Arguments:
            name -- the name of this Collector instance (identifies source/target of collected data)
            no_queue -- (optional) True if a task queue is not required (default: False)
        """
        
        self.name  = name
        """Name of this `Collector` instance."""
        
        # create a (FIFO) queue for passing tasks to the collector thread
        self.queue = None
        if self.needs_queue and not kwargs.get('no_queue', False):
            self.queue = queue.Queue()


    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.name)

    
    def run(self):
        """
        Entry point for the collector thread.
        Derived classes must override this method.
        """
        raise NotImplementedError()

    
    # collection of all instantiated collectors
    _collectors = {}
    
    _default_int_handler = None
    
    # set to True in interrupt handler to shut down all collector threads
    shutdown = False
    
    @staticmethod
    def _int_handler(sig, frame):
        print("*** INTERRUPT ***  Shutting down collector threads...")
        Collector.shutdown = True
        if callable(Collector._default_int_handler):
            Collector._default_int_handler(sig, frame)
        else:
            # TODO: implement alternatives
            assert False


    @staticmethod
    def create_collectors():
        """
        Create 'Collector' objects as specified in 'settings.PILON['COLLECTORS']'.
        """
    
        # set up a signal handler to catch interrupts (e.g. from ^C)
        # that will shut down our collector threads cleanly
        # (it will do this by setting a simple global variable)
        # NOTE: can only do this from the main thread
        if current_thread().name == 'MainThread':
            try:
                Collector._default_int_handler = signal.signal(signal.SIGINT, Collector._int_handler)
            except Exception as e:
                assert False, "Unexpected exception when setting signal handler from main thread: %s" % e
        
        # iterate over the collection of configured Collector-based objects
        logger.debug("Creating collectors...")
        for name, cfg in settings.PILON['COLLECTORS'].items():
            # extract the module and class name from the full class name,
            # and the arguments
            module_name, class_name = cfg['collector'].rsplit('.', 1)
            args = cfg['args']
            #print("ModuleName: %s, ClassName: %s, Args: %s" % (module_name, class_name, args))
            
            # import and retrieve the extracted class
            collector_class = _class_for_name(module_name, class_name)
            #print("Class: %s" % collector_class)
            
            # unpack the arguments and create the collector object
            collector = collector_class(name=name, **args)         # pylint: disable=W0142
            logger.info("Created %s", collector)
            
            # keep the new collector in our collection of instantiated collector objects
            Collector._collectors[name] = collector
            
            # create and start a new (daemon) thread for the collector
            # DOC: <http://docs.python.org/3.2/library/threading.html#thread-objects>
            collector_thread = Thread(target=collector.run, name=class_name)
            #collector_thread.daemon=True
            collector_thread.start()


    @staticmethod
    def collector(name):
        """
        Return the named Collector, or None if empty.
        Raise a KeyError if the named Collector is not found.
        """
        
        if name in validators.EMPTY_VALUES:
            return None
        return Collector._collectors[name]


    @staticmethod
    def collector_type(name):
        """
        Return the type of the named Collector, or None if empty.
        Raise a KeyError if the named Collector is not found.
        """
        
        collector = Collector.collector(name)
        if collector is None:
            return None
        return type(collector)
        
        
    @staticmethod
    def enqueue_task(source, task, join=True):
        """
        Enqueue a task for a named Collector, if it uses one,
        and optionally wait for the task to be processed.
        """

        # verify the named collector exists
        if not source in Collector._collectors:
            logger.warning("Cannot enqueue task for unknown source: '%s'", source)
            return
        
        # fetch the collector's task queue, if any
        collector = Collector._collectors[source]
        queue = collector.queue
        if queue is None:
            # this (read-only) collector doesn't support a task queue
            return
        
        # enqueue the task
        queue.put(task)
        
        # optionally, wait for the task to be processed
        if join:
            queue.join()
    