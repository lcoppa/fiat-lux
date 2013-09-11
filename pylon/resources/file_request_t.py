"""file_request_t standard enumeration type, originally defined in resource
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard


class file_request_t(base.Enumeration):
    """file_request_t standard enumeration."""

    # Invalid Value.
    FR_NUL = -1

    # Sequential access read.
    FR_OPEN_TO_SEND = 0

    # Sequential access write.
    FR_OPEN_TO_RECEIVE = 1

    # Close and save file.
    FR_CLOSE_FILE = 2

    # Close and delete file.
    FR_CLOSE_DELETE_FILE = 3

    # Retrieve directory entry.
    FR_DIRECTORY_LOOKUP = 4

    # Random access read.
    FR_OPEN_TO_SEND_RA = 5

    # Random access write.
    FR_OPEN_TO_RECEIVE_RA = 6

    def __init__(self):
        super().__init__(
            key=5,
            scope=0,
            prefix='FR_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = file_request_t()
    pass
