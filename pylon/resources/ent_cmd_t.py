"""ent_cmd_t standard enumeration type, originally defined in resource file
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class ent_cmd_t(base.Enumeration):
    """ent_cmd_t standard enumeration."""

    # Invalid Value.
    ES_NUL = -1

    # State is not yet defined.
    ES_UNDEFINED = 0

    # Open the device and close it when back in normal position.
    ES_OPEN_PULS = 1

    # Open the device if not locked.
    ES_OPEN = 2

    # Close the device.
    ES_CLOSE = 3

    # Stop the device.
    ES_STOP = 4

    # Continue after stop command.
    ES_STOP_RESUME = 5

    # Entry request, access in to the area.
    ES_ENTRY_REQ = 6

    # Exit request, access out from the area.
    ES_EXIT_REQ = 7

    # Exit request, access out from the area.
    ES_KEY_REQ = 8

    # Safety request, the device will go to a pre defined safety
    # position/mode.
    ES_SAFETY_EXT_REQ = 9

    # Emergency request, the device will go to an pre defined emergency
    # position/mode.
    ES_EMERGENCY_REQ = 10

    # Update the current state and mode.
    ES_UPDATE_STATE = 11

    # Resume after Safety function.
    ES_SAF_EXT_RESUME = 12

    # Resume after Emergency function.
    ES_EMERG_RESUME = 13

    def __init__(self):
        super().__init__(
            key=48,
            scope=0,
            prefix='ES_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = ent_cmd_t()
    pass
