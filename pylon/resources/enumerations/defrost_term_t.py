"""defrost_term_t standard enumeration type, originally defined in resource
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


class defrost_term_t(pylon.resources.base.Enumeration):
    """defrost_term_t standard enumeration."""

    # Invalid Value.
    DFT_NUL = -1

    # Terminate on temperature.
    DFT_TERM_TEMP = 0

    # Terminate on time.
    DFT_TERM_TIME = 1

    # Terminate on first occurring.
    DFT_TERM_FIRST = 2

    # Terminate on last occurring.
    DFT_TERM_LAST = 3

    # Terminate on sensor.
    DFT_TERM_SENSOR = 4

    # Terminate on discharge.
    DFT_TERM_DISCHARGE = 5

    # Terminate on return.
    DFT_TERM_RETURN = 6

    # Terminate on "Switch Open".
    DFT_TERM_SW_OPEN = 7

    # Terminate on "Switch Closed".
    DFT_TERM_SW_CLOSE = 8

    # Manufacturer-Defined termination state.
    DFT_TERM_MANUF = 100

    def __init__(self):
        super().__init__(
            key=23,
            scope=0,
            prefix='DFT_'
        )
        self._original_name = 'defrost_term_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = defrost_term_t()
    pass
