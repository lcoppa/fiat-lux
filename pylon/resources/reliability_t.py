"""reliability_t userdefined enumeration type, originally defined in resource
file set iot 90:00:00:05:00:00:00:00-1."""


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
# Generated at 12-Sep-2013 11:24.

from pylon.resources import base
from pylon.resources.userdefined import userdefined


class reliability_t(base.Enumeration):
    """reliability_t userdefined enumeration."""

    # Invalid value.
    DVR_NUL = -1

    # No fault detected (normal operation).
    DVR_NO_FAULT_DETECTED = 0

    # No sensor present.
    DVR_NO_SENSOR = 1

    # Overrange value.
    DVR_OVER_RANGE = 2

    # Underrange value.
    DVR_UNDER_RANGE = 3

    # Open loop sensor.
    DVR_OPEN_LOOP = 4

    # Shorted loop.
    DVR_SHORTED_LOOP = 5

    # No output from sensor.
    DVR_NO_OUTPUT = 6

    # Other unreliable condition.
    DVR_UNRELIABLE_OTHER = 7

    # Process error.
    DVR_PROCESS_ERROR = 8

    # Multiple faults.
    DVR_MULTI_STATE_FAULT = 9

    # Configuration error.
    DVR_CONFIGURATION_ERROR = 10

    # Reserved.
    DVR_RESERVED = 11

    # Communication failure.
    DVR_COMMUNICATION_FAILURE = 12

    # Member fault.
    DVR_MEMBER_FAULT = 13

    # Monitored object fault.
    DVR_MONITORED_OBJECT_FAULT = 14

    # Tripped.
    DVR_TRIPPED = 15

    def __init__(self):
        super().__init__(
            key=10,
            scope=1,
            prefix='DVR_'
        )
        self._definition = userdefined.add(self)


if __name__ == '__main__':
    # unit test code.
    item = reliability_t()
    pass
