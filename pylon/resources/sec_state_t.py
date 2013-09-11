"""sec_state_t standard enumeration type, originally defined in resource file
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard


class sec_state_t(base.Enumeration):
    """sec_state_t standard enumeration."""

    SSE_NUL = -1

    SSE_OFF = 0

    SSE_ON = 1

    SSE_INHIBIT_RESET = 2

    SSE_INHIBIT = 3

    SSE_WALK_TEST_OFF = 4

    SSE_WALK_TEST_ON = 5

    SSE_TEST_MODE_OFF = 6

    SSE_TEST_MODE_ON = 7

    SSE_POLL_STATUS = 8

    SSE_POLL_STATE = 9

    SSE_CONFIRM_ALARM_RESET = 10

    SSE_CONFIRM_ALARM = 11

    SSE_CONFIRM_TAMPER_RESET = 12

    SSE_CONFIRM_TAMPER = 13

    SSE_CONFIRM_MAINTENANCE = 14

    SSE_CONFIRM_TROUBLE = 15

    SSE_CONFIRM_FAULT = 16

    SSE_CONFIRM_RECOVERED_SENSOR = 17

    SSE_LOST_SENSOR = 18

    SSE_CONFIRM_UNSUPPORTED = 19

    def __init__(self):
        super().__init__(
            key=57,
            scope=0,
            prefix='SSE_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = sec_state_t()
    pass
