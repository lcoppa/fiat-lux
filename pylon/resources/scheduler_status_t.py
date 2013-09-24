"""scheduler_status_t standard enumeration type, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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


class scheduler_status_t(base.Enumeration):
    """scheduler_status_t standard enumeration."""

    # Invalid value.
    SCH_NUL = -1

    # Daily schedule (lowest priority).
    SCH_DAILY_SCHEDULE = 0

    # Scheduled vacation or holiday event.
    SCH_SCHED_SPECIAL = 1

    # Scheduled exception event.
    SCH_SCHED_EXCEPTION = 2

    # Local occupancy override.
    SCH_LOCAL_OCC_OVERRIDE = 3

    # Exception schedule override.
    SCH_EXCEPTION_SCH_OVERRIDE = 4

    # Manual override (highest priority).
    SCH_MANUAL_OVERRIDE = 5

    # Undefined override.
    SCH_OTHER = 6

    def __init__(self):
        super().__init__(
            key=87,
            scope=0,
            prefix='SCH_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = scheduler_status_t()
    pass
