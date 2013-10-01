"""nv_type_category_t standard enumeration type, originally defined in
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard


class nv_type_category_t(pylon.resources.base.Enumeration):
    """nv_type_category_t standard enumeration."""

    # Invalid Value.
    NVT_CAT_NUL = -1

    NVT_CAT_INITIAL = 0

    # 8-bit signed character.
    NVT_CAT_SIGNED_CHAR = 1

    # 8-bit unsigned character.
    NVT_CAT_UNSIGNED_CHAR = 2

    # 8-bit signed integer.
    NVT_CAT_SIGNED_SHORT = 3

    # 8-bit unsigned integer.
    NVT_CAT_UNSIGNED_SHORT = 4

    # 16-bit signed integer.
    NVT_CAT_SIGNED_LONG = 5

    # 16-bit unsigned integer.
    NVT_CAT_UNSIGNED_LONG = 6

    # 8-bit enumeration.
    NVT_CAT_ENUM = 7

    # Array.
    NVT_CAT_ARRAY = 8

    # Structure.
    NVT_CAT_STRUCT = 9

    # Union.
    NVT_CAT_UNION = 10

    # Bitfield.
    NVT_CAT_BITFIELD = 11

    # 32-bit IEC 60559 (IEEE 754) floating-point value.
    NVT_CAT_FLOAT = 12

    # 32-bit signed integer.
    NVT_CAT_SIGNED_QUAD = 13

    # Reference type.
    NVT_CAT_REFERENCE = 14

    # 32-bit unsigned integer.
    NVT_CAT_UNSIGNED_QUAD = 15

    # 64-bit floating-point value.
    NVT_CAT_DOUBLE_FLOAT = 16

    # 64-bit signed integer.
    NVT_CAT_SIGNED_INT64 = 17

    # 64-bit unsigned integer.
    NVT_CAT_UNSIGNED_INT64 = 18

    def __init__(self):
        super().__init__(
            key=46,
            scope=0,
            prefix='NVT_'
        )
        self._original_name = 'nv_type_category_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = nv_type_category_t()
    pass
