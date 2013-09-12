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
Pilon IP-C Server Task Classes
"""

__version__ = "$Revision$"
# $File$


import logging

from shared                 import NAMESPACE


__all__ = ['BaseTask', 'DeviceUpdateTask', 'DeviceCommandTask', 'DatapointUpdateTask']


# our logger
logger = logging.getLogger(NAMESPACE('collectors.task'))


class BaseTask:
    """ Abstract base class for all task objects. """
    def __init__(self):
        raise NotImplementedError()


class DeviceUpdateTask(BaseTask):
    """ A `BaseTask` to update the (non-datapoint) attributes of a device. """
    def __init__(self, device):
        """
        Initialize a `DeviceUpdateTask` with information
        from the specified `Device`.
        """
        self.device = device
        

class DeviceCommandTask(BaseTask):
    """ A `BaseTask` to send a command to a device. """
    
    # The list of supported commands that can be sent to a device.
    DEVICE_WINK = 'wink'
    DEVICE_RESET = 'reset'
    DEVICE_COMMANDS = (DEVICE_WINK, DEVICE_RESET)
    
    def __init__(self, device, command):
        if not command in self.DEVICE_COMMANDS:
            raise ValueError("`command` must be one of: %s" %
                             ", ".join(self.DEVICE_COMMANDS))
        
        self.device = device
        self.command = command


class DatapointUpdateTask(BaseTask):
    """ A `BaseTask` to update the datapoint attributes of a device. """
    def __init__(self, datapoint):
        """
        Initialize a `DatapointUpdateTask` with information
        from the specified `Datapoint`.
        """
        self.datapoint = datapoint
