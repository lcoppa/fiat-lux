"""
    SCPTmaxSndT
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

from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.standard import standard


class SCPTmaxSndT(SNVT_elapsed_tm):
    """SCPTmaxSndt standard property type.

    Maximum send time.  The maximum period of time between consecutive
    transmissions of the current value.

    This configuration property sets the maximum period of time that expires
    before the functional block automatically transmits the current value of
    the associated output network variable. This provides a heartbeat output
    that can be used by destination objects to ensure that the device is still
    healthy.

    When used with the node object, the maximum send time is used for the
    nvoStatus output network variable, and the status of each object on the
    device (including the node object) is returned sequentially in round-robin
    fashion, one object status per expiration of the timer.
    """

    def __init__(self, day=0, hour=0, minute=0, second=0, millisecond=0):
        super().__init__(
            day,
            hour,
            minute,
            second,
            millisecond
        )
        self._definition = standard.add(self)
        self._property_scope, self._property_key = 0, 22

