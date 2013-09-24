"""time_source_t standard enumeration type, originally defined in resource
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


class time_source_t(base.Enumeration):
    """time_source_t standard enumeration."""

    # Invalid value.
    TMS_NUL = -1

    # Time source is scheduler NV input.
    TMS_SCHEDULER_NV = 0

    # Time source is Node Object NV input.
    TMS_NODE_OBJECT_NV = 1

    # Time source is Smart Energy 2.0 Time Client NV input.
    TMS_SE2_TIME_CLIENT_NV = 2

    # Time source is local hardware real time clock.
    TMS_HARDWARE = 3

    # Alternate time source such as an SNTP server.
    TMS_ALTERNATE = 4

    def __init__(self):
        super().__init__(
            key=86,
            scope=0,
            prefix='TMS_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = time_source_t()
    pass
