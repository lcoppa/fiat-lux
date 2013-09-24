"""fire_indicator_t standard enumeration type, originally defined in resource
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


class fire_indicator_t(base.Enumeration):
    """fire_indicator_t standard enumeration."""

    # Invalid Value.
    FN_NUL = -1

    # Undefined indicator.
    FN_UNDEFINED = 0

    # The indicator is un-synchronized.
    FN_STROBE_U = 1

    # The indicator is synchronized.
    FN_STROBE_S = 2

    # The indicator is a DC input, pre coded Horn.
    FN_HORN = 3

    # The indicator is a DC input, pre coded Chime.
    FN_CHIME = 4

    # The indicator is a DC input.
    FN_BELL = 5

    # The indicator is powered from the device.
    FN_SOUNDER = 6

    # The indicator is an AC input for the speaker.
    FN_SPEAKER = 7

    # General purpose indicator.
    FN_UNIVERSAL = 8

    def __init__(self):
        super().__init__(
            key=28,
            scope=0,
            prefix='FN_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = fire_indicator_t()
    pass
