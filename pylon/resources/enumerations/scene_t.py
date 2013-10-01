"""scene_t standard enumeration type, originally defined in resource file set
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard


class scene_t(pylon.resources.base.Enumeration):
    """scene_t standard enumeration."""

    # Invalid value.
    SC_NUL = -1

    # Recall a specified scene.
    SC_RECALL = 0

    # Store the current setting in the specified scene.
    SC_LEARN = 1

    # Display the current scene.
    SC_DISPLAY = 2

    # Report current group is off.
    SC_GROUP_OFF = 3

    # Report current group is on.
    SC_GROUP_ON = 4

    # Report current status is off.
    SC_STATUS_OFF = 5

    # Report current status is on.
    SC_STATUS_ON = 6

    # Report current status is mixed.
    SC_STATUS_MIXED = 7

    # Get group status.
    SC_GROUP_STATUS = 8

    # Toggle state off and then on.
    SC_FLICK = 9

    # Report a timeout occured.
    SC_TIMEOUT = 10

    # Report a timeout occured for a flick warning.
    SC_TIMEOUT_FLICK = 11

    # Set the state to off after a delay.
    SC_DELAYOFF = 12

    # Flick and then set the state to off after a delay.
    SC_DELAYOFF_FLICK = 13

    # Set the state to on after a delay.
    SC_DELAYON = 14

    # Enable the current group.
    SC_ENABLE_GROUP = 15

    # Disable the current group.
    SC_DISABLE_GROUP = 16

    # Recall the cleaning scene.
    SC_CLEANON = 17

    # Restore the previous scene.
    SC_CLEANOFF = 18

    # Toggle to the opposite state and then restore the state.
    SC_WINK = 19

    # Restore the factory default scene table.
    SC_RESET = 20

    # Manufacturer-specific mode 1.
    SC_MODE1 = 21

    # Manufacturer-specific mode 2.
    SC_MODE2 = 22

    # Manufacturer-specific mode 3.
    SC_MODE3 = 23

    def __init__(self):
        super().__init__(
            key=17,
            scope=0,
            prefix='SC_'
        )
        self._original_name = 'scene_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = scene_t()
    pass
