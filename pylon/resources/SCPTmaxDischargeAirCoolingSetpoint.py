"""SCPTmaxDischargeAirCoolingSetpoint standard property type, originally
defined in resource file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 06-Sep-2013 08:58.

from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.standard import standard


class SCPTmaxDischargeAirCoolingSetpoint(SNVT_temp_p):
    """SCPTmaxDischargeAirCoolingSetpoint standard property type.  Maximum
    discharge air cooling.  Setpoint for the maximum discharge air
    cooling."""

    def __init__(self):
        super().__init__(
        )
        self._default_bytes = b'\x07\xd0'
        self._property_scope, self._property_key = 0, 205
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = SCPTmaxDischargeAirCoolingSetpoint()
    pass
