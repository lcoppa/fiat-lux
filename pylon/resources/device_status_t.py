"""device_status_t userdefined enumeration type, originally defined in
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
# Generated at 06-Sep-2013 08:57.

from pylon.resources import base
from pylon.resources.userdefined import userdefined


class device_status_t(base.Enumeration):
    """device_status_t userdefined enumeration."""

    # Invalid value.
    DVS_NUL = -1

    # Reserved.
    DVS_RESERVED = 0

    # Operational.
    DVS_OPERATIONAL = 1

    # Operational with network inputs disabled.
    DVS_OPERATIONAL_READ_ONLY = 2

    # Application download required.
    DVS_DOWNLOAD_REQUIRED = 3

    # Application download in progress.
    DVS_DOWNLOAD_IN_PROGRESS = 4

    # Non-operational.
    DVS_NON_OPERATIONAL = 5

    # Application backup in progress.
    DVS_BACKUP_IN_PROGRESS = 6

    # Startup in progress.
    DVS_STARTING_UP = 7

    # Shutdown in progress.
    DVS_SHUTTING_DOWN = 8

    def __init__(self):
        super().__init__(
            key=5,
            scope=1,
            prefix='DVS_'
        )
        self._definition = userdefined.add(self)


if __name__ == '__main__':
    # unit test code.
    item = device_status_t()
    pass
