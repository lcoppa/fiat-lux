"""file_status_t standard enumeration type, originally defined in resource
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


class file_status_t(pylon.resources.base.Enumeration):
    """file_status_t standard enumeration."""

    # Invalid Value.
    FS_NUL = -1

    # File transfer successful.
    FS_XFER_OK = 0

    # Directory lookup successful.
    FS_LOOKUP_OK = 1

    # Error on opening file.
    FS_OPEN_FAIL = 2

    # Error on directory lookup.
    FS_LOOKUP_ERR = 3

    # File transfer in progress.
    FS_XFER_UNDERWAY = 4

    # Error on reading/writing file.
    FS_IO_ERR = 5

    # File transfer timed out.
    FS_TIMEOUT_ERR = 6

    # Window sequence error.
    FS_WINDOW_ERR = 7

    # Authentication failure.
    FS_AUTH_ERR = 8

    # Access mode not supported.
    FS_ACCESS_UNAVAIL = 9

    # Random access beyond EOF.
    FS_SEEK_INVALID = 10

    FS_SEEK_WAIT = 11

    def __init__(self):
        super().__init__(
            key=6,
            scope=0,
            prefix='FS_'
        )
        self._original_name = 'file_status_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = file_status_t()
    pass
