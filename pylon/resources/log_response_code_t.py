"""log_response_code_t standard enumeration type, originally defined in
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


class log_response_code_t(base.Enumeration):
    """log_response_code_t standard enumeration."""

    # Invalid value;  this enumeration is not currently used in any SNVTs or
    # SCPTs.
    LRC_NUL = -1

    # The operation was successful.  The payload is the requested record.
    LRC_SUCCESS = 48

    # The end of the log has been reached.  No payload.
    LRC_END_OF_LOG = 49

    # Protocol version mismatch.  The payload is the supported version number
    # closest to the requested version number.
    LRC_VER_MISMATCH = 50

    # Unknown request type.  No payload.
    LRC_BAD_REQUEST = 51

    # Index is out of range.  Payload will contain the number of logs in the
    # device.
    LRC_BAD_LOG_INDEX = 52

    def __init__(self):
        super().__init__(
            key=80,
            scope=0,
            prefix='LRC_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = log_response_code_t()
    pass
