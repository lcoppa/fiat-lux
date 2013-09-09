"""command_priority_t userdefined enumeration type, originally defined in
resource file set iot 90:00:00:05:00:00:00:00-1."""


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
# Generated at 06-Sep-2013 08:57.

from pylon.resources import base
from pylon.resources.userdefined import userdefined


class command_priority_t(base.Enumeration):
    """command_priority_t userdefined enumeration."""

    # Invalid value.
    CPL_NUL = -1

    # Reserved.
    CPL_RESERVED = 0

    # Manual life safety.
    CPL_MANUAL_LIFE_SAFETY = 1

    # Automatic life safety.
    CPL_AUTOMATIC_LIFE_SAFETY = 2

    # Level 3.
    CPL_LEVEL_3 = 3

    # Level 4.
    CPL_LEVEL_4 = 4

    # Critical equipment control.
    CPL_CRITICAL_EQUIPMENT_CONTROL = 5

    # Minimum on/off.
    CPL_MINIMUM_ON_OFF = 6

    # Level 7.
    CPL_LEVEL_7 = 7

    # Manual operator.
    CPL_MANUAL_OPERATOR = 8

    # Level 9.
    CPL_LEVEL_9 = 9

    # Level 10.
    CPL_LEVEL_10 = 10

    # Level 11.
    CPL_LEVEL_11 = 11

    # Level 12.
    CPL_LEVEL_12 = 12

    # Level 13.
    CPL_LEVEL_13 = 13

    # Level 14.
    CPL_LEVEL_14 = 14

    # Level 15.
    CPL_LEVEL_15 = 15

    # Level 16.
    CPL_LEVEL_16 = 16

    def __init__(self):
        super().__init__(
            key=4,
            scope=1,
            prefix='CPL_'
        )
        self._definition = userdefined.add(self)


if __name__ == '__main__':
    # unit test code.
    item = command_priority_t()
    pass
