"""trnsTblX2 standard property type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 23-Sep-2013 09:14.

import pylon.resources.datapoints.trans_table
from pylon.resources.standard import standard


class trnsTblX2(pylon.resources.datapoints.trans_table.trans_table):
    """trnsTblX2 standard property type.  Valve-Plug Characteristic Table X.
    This configuration property will be used in conjunction with the
    translation-table Y configuration property to create a translation table
    that dictates how to scale the flow with respect to the mechanical
    stroke."""

    def __init__(self):
        super().__init__(
        )
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self._original_name = 'SCPTtrnsTblX2'
        self._property_scope, self._property_key = 0, 285
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = trnsTblX2()
    pass
