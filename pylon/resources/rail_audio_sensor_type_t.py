"""rail_audio_sensor_type_t standard enumeration type, originally defined in
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


class rail_audio_sensor_type_t(base.Enumeration):
    """rail_audio_sensor_type_t standard enumeration."""

    # Invalid Value.
    RAST_NUL = -1

    # CU Type 1.
    RAST_CU_TYPE_1 = 0

    # CU Type 2.
    RAST_CU_TYPE_2 = 1

    RAST_CU_TYPE_3 = 2

    # CU Type 4.
    RAST_CU_TYPE_4 = 3

    # LS Line 1.
    RAST_LS_LINE_1 = 4

    # LS Line 2.
    RAST_LS_LINE_2 = 5

    # LS Line 3.
    RAST_LS_LINE_3 = 6

    # LS Line 4.
    RAST_LS_LINE_4 = 7

    # LS Line 5.
    RAST_LS_LINE_5 = 8

    # LS Line 6.
    RAST_LS_LINE_6 = 9

    # LS Line 7.
    RAST_LS_LINE_7 = 10

    # LS Line 8.
    RAST_LS_LINE_8 = 11

    # Public-Address Unit.
    RAST_PAU = 12

    # CFA Type 1.
    RAST_CFA_TYPE_1 = 13

    # CFA Type 2.
    RAST_CFA_TYPE_2 = 14

    # CFA Type 3.
    RAST_CFA_TYPE_3 = 15

    # CFA Type 4.
    RAST_CFA_TYPE_4 = 16

    # DVA.
    RAST_DVA = 17

    # ET Type 1.
    RAST_ET_TYPE_1 = 18

    # ET Type 2.
    RAST_ET_TYPE_2 = 19

    # User-defined Type 1.
    RAST_USERDEF_TYPE_1 = 20

    # User-defined Type 2.
    RAST_USERDEF_TYPE_2 = 21

    # User-defined Type 3.
    RAST_USERDEF_TYPE_3 = 22

    # User-defined Type 4.
    RAST_USERDEF_TYPE_4 = 23

    def __init__(self):
        super().__init__(
            key=61,
            scope=0,
            prefix='RAST_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = rail_audio_sensor_type_t()
    pass
