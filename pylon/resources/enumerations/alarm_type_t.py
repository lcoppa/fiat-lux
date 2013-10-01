"""alarm_type_t standard enumeration type, originally defined in resource
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


class alarm_type_t(pylon.resources.base.Enumeration):
    """alarm_type_t standard enumeration."""

    # Update sequence header.
    AL_HEADER = -13

    # Update sequence footer.
    AL_FOOTER = -12

    # Debug information (not an alarm).
    AL_DEBUG = -11

    # Information update (not an alarm).
    AL_INFO = -10

    # System information (not an alarm).
    AL_SYSTEM_INFO = -6

    # The value is invalid.
    AL_VALUE_INVALID = -5

    # The value is a constant value (not an alarm).
    AL_CONSTANT = -4

    # The device is offline.
    AL_OFFLINE = -3

    # Alarm condition unknown (may be due to a communication failure or
    # hardware failure).
    AL_UNKNOWN = -2

    # Invalid alarm type value (alarm condition not specified).
    AL_NUL = -1

    # No alarm condition present.
    AL_NO_CONDITION = 0

    # Unspecified alarm condition present.
    AL_ALM_CONDITION = 1

    # Total/service interval alarm 1 (component requires service or
    # maintenance).
    AL_TOT_SVC_ALM_1 = 2

    # Total/service interval alarm 2.
    AL_TOT_SVC_ALM_2 = 3

    # Total/service interval alarm 3.
    AL_TOT_SVC_ALM_3 = 4

    # Alarm low limit alarm clear 1.
    AL_LOW_LMT_CLR_1 = 5

    # Alarm low limit alarm clear 2.
    AL_LOW_LMT_CLR_2 = 6

    # Alarm high limit alarm clear 1.
    AL_HIGH_LMT_CLR_1 = 7

    # Alarm high limit alarm clear 2.
    AL_HIGH_LMT_CLR_2 = 8

    # Alarm low limit alarm 1.
    AL_LOW_LMT_ALM_1 = 9

    # Alarm low limit alarm 2.
    AL_LOW_LMT_ALM_2 = 10

    # Alarm high limit alarm 1.
    AL_HIGH_LMT_ALM_1 = 11

    # Alarm high limit alarm 2.
    AL_HIGH_LMT_ALM_2 = 12

    # Fire alarm condition.
    AL_FIR_ALM = 13

    # Fire pre-alarm condition.
    AL_FIR_PRE_ALM = 14

    # Fire-related trouble (fault) condition.
    AL_FIR_TRBL = 15

    # Fire-related supervisory condition (e.g., sprinkler pressure).
    AL_FIR_SUPV = 16

    # Fire-related test-mode alarm condition.
    AL_FIR_TEST_ALM = 17

    # Fire-related test-mode pre-alarm condition.
    AL_FIR_TEST_PRE_ALM = 18

    # Fire-related maximum environmental compensation level reached.
    AL_FIR_ENVCOMP_MAX = 19

    # Fire-related abnormal input condition.
    AL_FIR_MONITOR_COND = 20

    # Fire-related maintenance alert.
    AL_FIR_MAINT_ALERT = 21

    # Fatal application error.
    AL_FATAL_ERROR = 30

    # Other error condition.
    AL_ERROR = 31

    # Other warning condition.
    AL_WARNING = 32

    def __init__(self):
        super().__init__(
            key=7,
            scope=0,
            prefix='AL_'
        )
        self._original_name = 'alarm_type_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = alarm_type_t()
    pass
