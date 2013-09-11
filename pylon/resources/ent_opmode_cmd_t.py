"""ent_opmode_cmd_t standard enumeration type, originally defined in resource
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


class ent_opmode_cmd_t(base.Enumeration):
    """ent_opmode_cmd_t standard enumeration."""

    # Invalid Value.
    EM_NUL = -1

    # Operation mode is not defined.
    EM_UNDEFINED = 0

    # Operation mode is AUTOMATIC.
    EM_AUTO = 1

    # Operation mode is AUTOMATIC with reduced width.
    EM_AUTO_RED = 2

    # Operation mode is CLOSE AND LOCK.
    EM_CLOSE_LOCK = 3

    # Operation mode is CLOSE AND UNLOCK.
    EM_CLOSE_UNLOCK = 4

    # Operation mode is EXIT ONLY.
    EM_EXIT_ONLY = 5

    # Operation mode is OPEN.
    EM_OPEN = 6

    # Operation mode is OPEN AND CLOSE ONCE.
    EM_OPEN_ONCE = 7

    # Operation mode is MANUAL.
    EM_MANUAL = 8

    # Operation mode is FIRE.
    EM_FIRE = 9

    # Operation mode is EVACUATION.
    EM_EVAC = 10

    # Operation mode is WEATHER MODE.
    EM_WEATHER = 11

    # Operation mode is DAY_LOCKING, locking with reduced level of security.
    EM_DAY_LOCKING = 12

    # Operation mode is NIGHT_LOCKING, locking with maximum level of
    # security.
    EM_NIGHT_LOCKING = 13

    # Operation mode is BLOCKED, no operations is allowed.
    EM_BLOCKED = 14

    # Operation mode is SERVICE.
    EM_SERVICE = 15

    # Operation mode is ENTRY_ONLY.
    EM_ENTRY_ONLY = 16

    def __init__(self):
        super().__init__(
            key=47,
            scope=0,
            prefix='EM_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = ent_opmode_cmd_t()
    pass
