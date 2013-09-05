"""
    SNVT_lev_percent
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


class SNVT_lev_percent(base.Scaled):
    """SNVT_lev_percent standard datapoint type.

    Percent level  (percent of full scale, or parts-per-million).

    SNVT_switch should be used instead of SNVT_lev_percent, with the exception
    of datapoints that are used to communicate a percentage value and that
    require the additional resolution provided by SNVT_lev_percent.

    SNVT_lev_percent may also be used for variable members of functional
    profiles that are designed primary for interfacing with variable members
    of existing profiles that are defined as SNVT_lev_percent. SNVT_switch be
    used for communicating state with discrete devices as well as level with
    continuous devices.
    """

    def __init__(self, default_value=0):
        super().__init__(
            size=2,
            signed=True,
            key=81,
            scope=0,
            default=default_value,
            scaling=(0.005, 0),
            minimum=-163.84,
            maximum=163.835,
            invalid=163.835
        )
        self._definition = standard.add(self)
