"""
    SNVT_temp_p
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
from pylon.resources.standard import standard


class SNVT_temp_p(base.Scaled):
    """SNVT_temp_p standard datapoint type.

    Temperature  (degrees Celsius).

    To be used for heating, ventilation, and air-conditioning (HVAC)
    applications."""

    def __init__(self, default_value=0):
        super().__init__(
            size=2,
            signed=True,
            key=105,
            scope=0,
            default=default_value,
            scaling=(0.01, 0),
            minimum=-273.17,
            maximum=327.67,
            invalid=327.67
        )
        self._definition = standard.add(self)
