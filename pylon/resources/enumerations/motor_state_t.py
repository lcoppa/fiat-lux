"""motor_state_t standard enumeration type, originally defined in resource
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard


class motor_state_t(pylon.resources.base.Enumeration):
    """motor_state_t standard enumeration."""

    # The state of the motor is unknown (invalid value).
    MOTOR_NUL = -1

    # The motor is not running.
    MOTOR_STOPPED = 0

    # The motor is performing its start-up sequence.
    MOTOR_STARTING = 1

    # The motor is running.  Speed is increasing.
    MOTOR_ACCELERATING = 2

    # The motor is running in its standby mode.
    MOTOR_AT_STANDBY = 3

    # The motor is running in its normal operational mode.
    MOTOR_AT_NORMAL = 4

    # The motor is running at its reference speed.
    MOTOR_AT_REFERENCE = 5

    # The motor is running.  Speed is decreasing.
    MOTOR_DECELERATING = 6

    # The motor is running, beginning its shutdown sequence.
    MOTOR_STOPPING = 7

    def __init__(self):
        super().__init__(
            key=40,
            scope=0,
            prefix='MOTOR_'
        )
        self._original_name = 'motor_state_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = motor_state_t()
    pass
