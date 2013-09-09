"""priority_level_t standard enumeration type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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

from pylon.resources import base
from pylon.resources.standard import standard


class priority_level_t(base.Enumeration):
    """priority_level_t standard enumeration."""

    # Invalid Value.
    PR_NUL = -1

    # Lowest alarm priority level.
    PR_LEVEL_0 = 0

    PR_LEVEL_1 = 1

    PR_LEVEL_2 = 2

    # Highest alarm priority level.
    PR_LEVEL_3 = 3

    # Life Safety Fire Alarms (BACnet Priority 2).
    PR_1 = 4

    # Property Safety Fire Alarms (BACnet Priority 3).
    PR_2 = 5

    # Fire Supervisory Alarm (BACnet Priority 4).
    PR_3 = 6

    # Fire Trouble/Fault (Display) (BACnet Priority 5).
    PR_4 = 7

    # Fire Pre-Alarm, HVAC Critical Equipment Alarm (BACnet Priority 6).
    PR_6 = 8

    # HVAC Alarms (BACnet Priority 8).
    PR_8 = 9

    # HVAC Critical Equipment RTN, Fire RTN (Display) (BACnet Priority 10).
    PR_10 = 10

    # HVAC RTN (lowest priority) (BACnet Priority 16).
    PR_16 = 11

    def __init__(self):
        super().__init__(
            key=8,
            scope=0,
            prefix='PR_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = priority_level_t()
    pass
