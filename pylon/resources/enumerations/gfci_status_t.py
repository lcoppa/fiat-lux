"""gfci_status_t standard enumeration type, originally defined in resource
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


class gfci_status_t(pylon.resources.base.Enumeration):
    """gfci_status_t standard enumeration."""

    # Invalid Value.
    GFCI_NUL = -1

    # Unknown response.
    GFCI_UNKNOWN = 0

    # Normal GFCI operating condition.
    GFCI_NORMAL = 1

    # A ground-fault has caused the GFCI to interrupt the circuit.
    GFCI_TRIPPED = 2

    # The GFCI failed testing.
    GFCI_TEST_FAILED = 3

    # The GFCI passed testing.
    GFCI_TEST_PASSED = 4

    # The GFCI needs to be tested.
    GFCI_TEST_NOW = 5

    def __init__(self):
        super().__init__(
            key=39,
            scope=0,
            prefix='GFCI_'
        )
        self._original_name = 'gfci_status_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = gfci_status_t()
    pass
