"""backup_and_restore_states_t userdefined enumeration type, originally
defined in resource file set iot 90:00:00:05:00:00:00:00-1."""


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


class backup_and_restore_states_t(base.Enumeration):
    """backup_and_restore_states_t userdefined enumeration."""

    # Invalid value.
    BRS_NUL = -1

    # Idle state -- no backup or restore operations in process.
    BRS_IDLE = 0

    # Preparing for backup.
    BRS_PREPARING_FOR_BACKUP = 1

    # Preparing for restore.
    BRS_PREPARING_FOR_RESTORE = 2

    # Performing a backup.
    BRS_PERFORMING_A_BACKUP = 3

    # Performing a restore.
    BRS_PERFORMING_A_RESTORE = 4

    # Backup failure.
    BRS_BACKUP_FAILURE = 5

    # Restore failure.
    BRS_RESTORE_FAILURE = 6

    def __init__(self):
        super().__init__(
            key=2,
            scope=1,
            prefix='BRS_'
        )
        self._definition = userdefined.add(self)


if __name__ == '__main__':
    # unit test code.
    item = backup_and_restore_states_t()
    pass
