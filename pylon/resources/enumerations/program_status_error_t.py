"""program_status_error_t standard enumeration type, originally defined in
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard


class program_status_error_t(pylon.resources.base.Enumeration):
    """program_status_error_t standard enumeration."""

    # Invalid value.
    PSE_NUL = -1

    # No Error.
    PSE_NO_ERROR = 0

    # Program fault (no halt).
    PSE_PROGRAM_FAULT_NOHALT = 1

    # Invalid operation (no halt).
    PSE_INVALID_OPERATION_NOHALT = 2

    # Invalid parameter (no halt).
    PSE_INVALID_PARAMETER_NOHALT = 3

    # Stack overflow (no halt).
    PSE_STACK_OVERFLOW_NOHALT = 4

    # Stack underflow (no halt).
    PSE_STACK_UNDERFLOW_NOHALT = 5

    # Insufficient memory (no halt).
    PSE_INSUFFICIENT_MEMORY_NOHALT = 6

    # Unknown error (resulted in a program halt).
    PSE_WATCHDOG_NOHALT = 7

    # Unknown error (no halt).
    PSE_UNKNOWN_ERROR_NOHALT = 31

    # Load error.
    PSE_LOAD_ERROR_HALT = 32

    # Program fault (resulted in a program halt).
    PSE_PROGRAM_FAULT_HALT = 33

    # Invalid operation (resulted in a program halt).
    PSE_INVALID_OPERATION_HALT = 34

    # Invalid operation (resulted in a program halt).
    PSE_INVALID_PARAMETER_HALT = 35

    # Invalid operation (resulted in a program halt).
    PSE_STACK_OVERFLOW_HALT = 36

    # Stack underflow (resulted in a program halt).
    PSE_STACK_UNDERFLOW_HALT = 37

    # Insufficient Memory Halt.
    PSE_INSUFFICIENT_MEMORY_HALT = 38

    # Watchdog Halt.
    PSE_WATCHDOG_HALT = 39

    # Corrupted program (resulted in a program halt).
    PSE_CORRUPTED_PROGRAM_HALT = 40

    # Unknown error (resulted in a program halt).
    PSE_UNKNOWN_ERROR_HALT = 63

    def __init__(self):
        super().__init__(
            key=85,
            scope=0,
            prefix='PSE_'
        )
        self._original_name = 'program_status_error_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = program_status_error_t()
    pass
