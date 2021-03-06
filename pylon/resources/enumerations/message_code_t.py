"""message_code_t standard enumeration type, originally defined in resource
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


class message_code_t(pylon.resources.base.Enumeration):
    """message_code_t standard enumeration."""

    # Invalid value;  this enumeration is not currently used in any SNVTs or
    # SCPTs.
    MC_NUL = -1

    # First reserved standard message code.  Codes 48 - 62 are reserved for
    # standard message codes.
    MC_FIRST_RESERVED_CODE = 48

    # Broadcast message.  See profile documentation for message data format.
    MC_BROADCAST = 59

    # Data log access request.  See log_response_code_t for response codes.
    MC_DATA_LOG_ACCESS = 60

    # Interoperable self-installation (ISI) message.
    MC_ISI = 61

    # File transfer message.
    MC_FILE_TRANSFER = 62

    def __init__(self):
        super().__init__(
            key=78,
            scope=0,
            prefix='MC_'
        )
        self._original_name = 'message_code_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = message_code_t()
    pass
