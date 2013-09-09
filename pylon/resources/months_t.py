"""months_t standard enumeration type, originally defined in resource file
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class months_t(base.Enumeration):
    """months_t standard enumeration."""

    # Invalid value.
    MN_NUL = -1

    # Every month.
    MN_EVERY_MONTH = 0

    # January.
    MN_JAN = 1

    # February.
    MN_FEB = 2

    # March.
    MN_MAR = 3

    # April.
    MN_APR = 4

    # May.
    MN_MAY = 5

    # June.
    MN_JUN = 6

    # July.
    MN_JUL = 7

    # August.
    MN_AUG = 8

    # September.
    MN_SEP = 9

    # October.
    MN_OCT = 10

    # November.
    MN_NOV = 11

    # December.
    MN_DEC = 12

    # Every other month.
    MN_EVERY_2_MONTH = 13

    # Every third month.
    MN_QUARTERLY = 14

    # Every fourth month.
    MN_EVERY_4_MONTH = 15

    # Every fifth month.
    MN_EVERY_5_MONTH = 16

    # Every sixth month.
    MN_EVERY_6_MONTH = 17

    # Every seventh month.
    MN_EVERY_7_MONTH = 18

    # Every eighth month.
    MN_EVERY_8_MONTH = 19

    # Every ninth month.
    MN_EVERY_9_MONTH = 20

    # Every tenth month.
    MN_EVERY_10_MONTH = 21

    # Every eleventh month.
    MN_EVERY_11_MONTH = 22

    # Jan, Mar, May, Jul, Sep, Nov.
    MN_EVERY_ODD_MONTH = 23

    # Feb, Apr, Jun, Aug, Oct, Dec.
    MN_EVERY_EVEN_MONTH = 24

    def __init__(self):
        super().__init__(
            key=55,
            scope=0,
            prefix='MN_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = months_t()
    pass
