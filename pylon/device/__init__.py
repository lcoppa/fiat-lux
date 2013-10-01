"""    pylon module for Python, version 0.0

This is the pylon.device package, version 0.0

To create a pylon application object, instantiate a single object of
the Application class:

app = pylon.device.application.Application()

Then specify additional attributes such as the unique ID, and properties of
the physical media and logical channel, and create interoperable constructs
from the application's factory methods, e.g.

import pylon.resources.datapoints.count

nviCount = app.InputDataPoint(
   pylon.resources.datapoints.count.count, 'nviCount'
)

Attach event handlers as necessary and start the application:

app.start()

During the lifetime of your script, call app.service() frequently and
periodically.

Call app.stop() to shutdown the stack and the runtime kit.

"""

#
# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.
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

import sys

# noinspection PyUnresolvedReferences
import pylon.device.application
# noinspection PyUnresolvedReferences
import pylon.device.event
# noinspection PyUnresolvedReferences
import pylon.device.interface
# noinspection PyUnresolvedReferences
import pylon.device.isi
# noinspection PyUnresolvedReferences
import pylon.device.stack
# noinspection PyUnresolvedReferences
import pylon.device.system
# noinspection PyUnresolvedReferences
import pylon.device.toolkit


def version_check(minimum):
    major, minor, micro, level, serial = sys.version_info
    if major < minimum:
        raise ImportError(
            'pylon requires Python version {0}.0.0 or better'.format(minimum)
        )


version_check(3)

# noinspection PyUnresolvedReferences
__all__ = [
    'application',
    'event',
    'interface',
    'isi',
    'stack',
    'system',
    'toolkit'
]
