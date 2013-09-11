"""hvac_t standard enumeration type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0."""


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


class hvac_t(base.Enumeration):
    """hvac_t standard enumeration."""

    # Invalid value.
    HVAC_NUL = -1

    # Controller automatically changes between application modes.
    HVAC_AUTO = 0

    # Heating only.
    HVAC_HEAT = 1

    # Application-specific morning warm-up.
    HVAC_MRNG_WRMUP = 2

    # Cooling only.
    HVAC_COOL = 3

    # Application-specific night purge.
    HVAC_NIGHT_PURGE = 4

    # Application-specific pre-cool.
    HVAC_PRE_COOL = 5

    # Controller not controlling outputs.
    HVAC_OFF = 6

    # Equipment being tested.
    HVAC_TEST = 7

    # Emergency heat mode (heat pump).
    HVAC_EMERG_HEAT = 8

    # Air not conditioned, fan turned on.
    HVAC_FAN_ONLY = 9

    # Cooling with compressor not running.
    HVAC_FREE_COOL = 10

    # Ice-making mode.
    HVAC_ICE = 11

    # Maximum heating mode.
    HVAC_MAX_HEAT = 12

    # Economic Heat/Cool mode.
    HVAC_ECONOMY = 13

    # Dehumidification mode.
    HVAC_DEHUMID = 14

    # Calibration mode.
    HVAC_CALIBRATE = 15

    # Emergency cool mode.
    HVAC_EMERG_COOL = 16

    # Emergency steam mode.
    HVAC_EMERG_STEAM = 17

    HVAC_MAX_COOL = 18

    HVAC_HVC_LOAD = 19

    HVAC_NO_LOAD = 20

    def __init__(self):
        super().__init__(
            key=14,
            scope=0,
            prefix='HVAC_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = hvac_t()
    pass
