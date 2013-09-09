"""SCPTname1 standard property type, originally defined in resource file set
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.char_encoding_t import char_encoding_t


class SCPTname1(base.Structure):
    """SCPTname1 standard property type.  Name part 1.  Part 1 of the name of
    the functional block to be used by optional user interface applications.
    May optionally used with SCPTname2 and SCPTname3.  Must be implemented as
    a configuration network variable."""

    def __init__(self):
        super().__init__(
            key=306,
            scope=0
        )

        self.__encoding = char_encoding_t(
        )
        self._register(('encoding', self.__encoding))

        self.__name = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(12)
            ]
        )
        self._register(('name', self.__name))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00'
        self._property_scope, self._property_key = 0, 306
        self._definition = standard.add(self)

    def __set_encoding(self, v):
        self.__encoding._value = v

    encoding = property(
        lambda self: self.__encoding._value,
        __set_encoding,
        None,
        """Character encoding.  Character encoding method."""
    )

    def __set_name(self, v):
        self.__name._value = v

    name = property(
        lambda self: self.__name._value,
        __set_name,
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
        self.__set_encoding(v.__encoding)
        self.__set_name(v.__name)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 13


if __name__ == '__main__':
    # unit test code.
    item = SCPTname1()
    pass
