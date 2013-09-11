"""SNVT_lev_percent standard datapoint type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0.  """


# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software" to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# This file is generated from device resource files using an automated
# database to source code conversion process.  Grammar and punctuation within
# the embedded documentation may not be correct, as this data is gathered and
# combined from several sources.  The machine-generated code may not meet
# compliance with PEP-8 and PEP-257 recommendations at all times.
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard


class SNVT_lev_percent(base.Scaled):
    """SNVT_lev_percent standard datapoint type.  Percentage level.  Level
    percent.  SNVT_switch should be used instead of SNVT_lev_percent, with
    the exception of network variables that are used to communicate a
    percentage value and that require the additional resolution provided by
    SNVT_lev_percent;  or for network variable members of functional profiles
    that are designed primarily for interfacing with SNVT_lev_percent members
    of other profiles.  (% of full level.)."""

    def __init__(self):
        super().__init__(
            size=2,
            signed=True,
            scaling=(0.005, 0),
            invalid=163.835,
            minimum=-163.84,
            maximum=163.835,
            scope=0,
            key=81
        )
        self._definition = standard.add(self)



if __name__ == '__main__':
    # unit test code.
    item = SNVT_lev_percent()
    pass
