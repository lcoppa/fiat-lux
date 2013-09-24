"""object_request_t standard enumeration type, originally defined in resource
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class object_request_t(base.Enumeration):
    """object_request_t standard enumeration."""

    # Invalid Value.
    RQ_NUL = -1

    # Enable object and remove override.
    RQ_NORMAL = 0

    # Disable object.
    RQ_DISABLED = 1

    # Report object status.
    RQ_UPDATE_STATUS = 2

    # Perform object self-test.
    RQ_SELF_TEST = 3

    # Update alarm status.
    RQ_UPDATE_ALARM = 4

    # Report status bit mask.
    RQ_REPORT_MASK = 5

    # Override object.
    RQ_OVERRIDE = 6

    # Enable object.
    RQ_ENABLE = 7

    # Remove object override.
    RQ_RMV_OVERRIDE = 8

    # Clear object status.
    RQ_CLEAR_STATUS = 9

    # Clear object alarm.
    RQ_CLEAR_ALARM = 10

    # Enable alarm notification.
    RQ_ALARM_NOTIFY_ENABLED = 11

    # Disable alarm notification.
    RQ_ALARM_NOTIFY_DISABLED = 12

    # Enable object for manual control.
    RQ_MANUAL_CTRL = 13

    # Enable object for remote control.
    RQ_REMOTE_CTRL = 14

    # Enable programming of special configuration properties.
    RQ_PROGRAM = 15

    # Clear reset-complete flag (reset_complete).
    RQ_CLEAR_RESET = 16

    # Execute reset-sequence of object.
    RQ_RESET = 17

    # Clear data log.
    RQ_CLEAR_LOG = 18

    # Load the program specified in SCPTprogSelect.
    RQ_LOAD_PROGRAM = 19

    # Run the currently loaded program.  If the program was halted manually,
    # this will resume running from the point is was halted.
    RQ_RUN_PROGRAM = 20

    # Halt the currently loaded program.  This will preserve the program
    # state and a subsequent Run command will resume the program from where
    # it was halted.
    RQ_HALT_PROGRAM = 21

    # Restart the currently loaded program from the beginning.
    RQ_RESTART_PROGRAM = 22

    # Unload the currently loaded program.
    RQ_UNLOAD_PROGRAM = 23

    # Executes the next logical operation (line, statement, instruction,
    # logic block, etc.) of the currently loaded program.  The program state
    # must be "idle" or "halted" to accept this command, otherwise it will be
    # ignored.  The program returns to "halted" state after execution of this
    # command.
    RQ_STEP_PROGRAM = 24

    def __init__(self):
        super().__init__(
            key=10,
            scope=0,
            prefix='RQ_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = object_request_t()
    pass
