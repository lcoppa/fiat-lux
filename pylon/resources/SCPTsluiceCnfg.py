"""SCPTsluiceCnfg standard property type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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

from pylon.resources.master_slave_t import master_slave_t
from pylon.resources.standard import standard


class SCPTsluiceCnfg(master_slave_t):
    """SCPTsluiceCnfg standard property type.  Sluice-lock master/slave
    control.  Role of a device in a sluice-lock connection.  A sluice-lock is
    an interlock mechanism between two entry/exit devices, or a sluice
    manager and several entry/exit devices, to ensure that only one single
    entry/exit device is opened at any point in time."""

    def __init__(self):
        super().__init__(
        )
        self._override_scope(0)
        self._override_key(259)
        self._default_bytes = b'\x00'
        self._property_scope, self._property_key = 0, 259
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = SCPTsluiceCnfg()
    pass