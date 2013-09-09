"""
    SNVT_abs_humid
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


class SNVT_abs_humid(base.Scaled):
    """SNVT_abs_humid standard datapoint type.

    Absolute humidity  (gram/kilogram).

    Used for optimal control in heating, ventilation, and air conditioning
    applications, where
    Absolute_Humidity [g/kg] = max_abs_Humidity [g/kg] x relative_Humidity
    Relative Humidity is specified by SNVT_lev_percent.
    See also SNVT_enthalpy.
    """

    def __init__(self, default_value=0):
        super().__init__(
            size=2,
            signed=False,
            key=160,
            scope=0,
            default=default_value,
            scaling=(0.01, 0),
            minimum=0,
            maximum=655.35,
            invalid=655.35
        )
        self._definition = standard.add(self)