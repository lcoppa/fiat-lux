"""hvac_overid_t standard enumeration type, originally defined in resource
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class hvac_overid_t(base.Enumeration):
    """hvac_overid_t standard enumeration."""

    # Invalid Value.
    HVO_NUL = -1

    # Not overridden.
    HVO_OFF = 0

    HVO_POSITION = 1

    # Override flow in liters/sec - use flow field.
    HVO_FLOW_VALUE = 2

    # Override flow percentage - use percent field.
    HVO_FLOW_PERCENT = 3

    # Override to position = 100%.
    HVO_OPEN = 4

    # Override to position = 0%.
    HVO_CLOSE = 5

    # Override to configured minimum.
    HVO_MINIMUM = 6

    # Override to configured maximum.
    HVO_MAXIMUM = 7

    HVO_UNUSED8 = 8

    HVO_UNUSED9 = 9

    HVO_UNUSED10 = 10

    HVO_UNUSED11 = 11

    HVO_UNUSED12 = 12

    HVO_UNUSED13 = 13

    HVO_UNUSED14 = 14

    HVO_UNUSED15 = 15

    HVO_UNUSED16 = 16

    HVO_POSITION_1 = 17

    # Override flow in liters/sec - use flow field.
    HVO_FLOW_VALUE_1 = 18

    # Override flow percentage - use percent field.
    HVO_FLOW_PERCENT_1 = 19

    # Override to position = 100%.
    HVO_OPEN_1 = 20

    # Override to position = 0%.
    HVO_CLOSE_1 = 21

    # Override to configured minimum.
    HVO_MINIMUM_1 = 22

    # Override to configured maximum.
    HVO_MAXIMUM_1 = 23

    HVO_UNUSED24 = 24

    HVO_UNUSED25 = 25

    HVO_UNUSED26 = 26

    HVO_UNUSED27 = 27

    HVO_UNUSED28 = 28

    HVO_UNUSED29 = 29

    HVO_UNUSED30 = 30

    HVO_UNUSED31 = 31

    HVO_UNUSED32 = 32

    HVO_POSITION_2 = 33

    # Override flow in liters/sec - use flow field.
    HVO_FLOW_VALUE_2 = 34

    # Override flow percentage - use percent field.
    HVO_FLOW_PERCENT_2 = 35

    # Override to position = 100%.
    HVO_OPEN_2 = 36

    # Override to position = 0%.
    HVO_CLOSE_2 = 37

    # Override to configured minimum.
    HVO_MINIMUM_2 = 38

    # Override to configured maximum.
    HVO_MAXIMUM_2 = 39

    HVO_UNUSED40 = 40

    HVO_UNUSED41 = 41

    HVO_UNUSED42 = 42

    HVO_UNUSED43 = 43

    HVO_UNUSED44 = 44

    HVO_UNUSED45 = 45

    HVO_UNUSED46 = 46

    HVO_UNUSED47 = 47

    HVO_UNUSED48 = 48

    def __init__(self):
        super().__init__(
            key=16,
            scope=0,
            prefix='HVO_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = hvac_overid_t()
    pass
