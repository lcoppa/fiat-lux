"""hvac_hvt_t standard enumeration type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class hvac_hvt_t(base.Enumeration):
    """hvac_hvt_t standard enumeration."""

    # Invalid Value.
    HVT_NUL = -1

    # Generic.
    HVT_GENERIC = 0

    # Fan Coil.
    HVT_FAN_COIL = 1

    # Variable Air Volume Terminal.
    HVT_VAV = 2

    # Heat Pump.
    HVT_HEAT_PUMP = 3

    # Rooftop Unit.
    HVT_ROOFTOP = 4

    # Unit Ventilator.
    HVT_UNIT_VENT = 5

    # Chilled Ceiling.
    HVT_CHILL_CEIL = 6

    # Radiator.
    HVT_RADIATOR = 7

    # Air Handling Unit.
    HVT_AHU = 8

    # Self-Contained Unit.
    HVT_SELF_CONT = 9

    def __init__(self):
        super().__init__(
            key=31,
            scope=0,
            prefix='HVT_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = hvac_hvt_t()
    pass
