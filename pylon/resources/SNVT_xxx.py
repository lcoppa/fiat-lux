"""
    SNVT_xxx
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

from pylon.resources import base
from pylon.device import toolkit


class SNVT_xxx(base.DataType):
    """SNVT_xxx placeholder type.

    SNVT_xxx does not implement an actual datapoint type. It is sometimes used
    in profile definitions to indicate that a member may use any interoperable
    datapoint type in the implementation,

    For example, the SFPTopenLoopSensor profile defines a simple and generic
    sensor, using SNVT_xxx for the sensor's output. The profile definition is
    thus useful for a variety of sensor data, such as temperature, velocity or
    torque measurements.

    This SNVT_xxx class provides a valid datapoint type which cannot be
    instantiated."""

    def __init__(self):
        raise toolkit.PylonInterfaceError(
            toolkit.PylonInterfaceError.SNVT_XXX,
            'SNVT_xxx cannot be implemented'
        )

    def _signature(self):
        """Return a 32-bit signature for this item.

        SNVT_xxx reports a constant signature. This contributes to the
        calculation of a profile's signature, but does not affect the
        block's and the overall application signature.
        """
        return 0x78787878

    def __str__(self):
        return 'SNVT_xxx'
