"""sec_status_t standard enumeration type, originally defined in resource
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


class sec_status_t(base.Enumeration):
    """sec_status_t standard enumeration."""

    SSS_NUL = -1

    SSS_POWER_UP = 0

    SSS_ALARM_RESET = 1

    SSS_ALARM = 2

    SSS_TAMPER_RESET = 3

    SSS_TAMPER = 4

    SSS_MAINTENANCE = 5

    SSS_TROUBLE = 6

    SSS_FAULT = 7

    SSS_RECOVERED_SENSOR = 8

    SSS_LOST_SENSOR = 9

    SSS_POLL_ACTIVE = 10

    SSS_POLL_INACTIVE = 11

    SSS_POLL_TAMPER = 12

    SSS_POLL_ON = 13

    SSS_POLL_OFF = 14

    SSS_POLL_INHIBIT = 15

    SSS_POLL_TEST = 16

    SSS_CONFIRM_OFF = 17

    SSS_CONFIRM_ON = 18

    SSS_CONFIRM_INHIBIT_RESET = 19

    SSS_CONFIRM_INHIBIT = 20

    SSS_CONFIRM_WALK_TEST_OFF = 21

    SSS_CONFIRM_WALK_TEST_ON = 22

    SSS_CONFIRM_TEST_MODE_OFF = 23

    SSS_CONFIRM_TEST_MODE_ON = 24

    SSS_CONFIRM_UNSUPPORTED = 25

    def __init__(self):
        super().__init__(
            key=56,
            scope=0,
            prefix='SSS_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = sec_status_t()
    pass
