"""occupancy_mode_t userdefined enumeration type, originally defined in
resource file set iot 90:00:00:05:00:00:00:00-1."""


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
from pylon.resources.userdefined import userdefined


class occupancy_mode_t(pylon.resources.base.Enumeration):
    """occupancy_mode_t userdefined enumeration."""

    # Invalid value.
    OCCM_NUL = -1

    # Automatic occupancy detection based on local input and remote sensor
    # inputs.
    OCCM_AUTO = 0

    # Force occupied.
    OCCM_OCCUPIED = 1

    # Force unoccupied.
    OCCM_UNOCCUPIED = 2

    # Occupancy based on local sensor input only with no hold time.
    OCCM_TEST = 3

    def __init__(self):
        super().__init__(
            key=9,
            scope=1,
            prefix='OCCM_'
        )
        self._original_name = 'occupancy_mode_t'
        self._definition = userdefined.add(self)


if __name__ == '__main__':
    # unit test code.
    item = occupancy_mode_t()
    pass
