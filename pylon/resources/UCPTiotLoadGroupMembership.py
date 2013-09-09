"""UCPTiotLoadGroupMembership userdefined property type, originally defined
in resource file set iot 90:00:00:05:00:00:00:00-1."""


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


class UCPTiotLoadGroupMembership(base.Structure):
    """UCPTiotLoadGroupMembership userdefined property type.  Load group
    membership.  Load groups that a block is a member of;  load group 0
    applies to all devices;  the LSB of index 0 represents load group 0;  the
    MSB of index 7 represents load group 63."""

    def __init__(self):
        super().__init__(
            key=6,
            scope=1
        )

        self.__flags = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(8)
            ]
        )
        self._register(('flags', self.__flags))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 1, 6
        self._definition = userdefined.add(self)

    def __set_flags(self, v):
        self.__flags._value = v

    flags = property(
        lambda self: self.__flags._value,
        __set_flags,
        None,
        """."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_flags(v.__flags)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 8


if __name__ == '__main__':
    # unit test code.
    item = UCPTiotLoadGroupMembership()
    pass
