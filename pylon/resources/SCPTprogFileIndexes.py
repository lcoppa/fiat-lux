"""SCPTprogFileIndexes standard property type, originally defined in resource
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class SCPTprogFileIndexes(base.Structure):
    """SCPTprogFileIndexes standard property type.  File Indexes.  Indexes of
    first and last LonMark files where programs may be stored."""

    def __init__(self):
        super().__init__(
            key=355,
            scope=0
        )

        self.__first_file_index = base.Scaled(
            size=1,
            signed=False,
            minimum=3,
            maximum=255
        )
        self._register(('first_file_index', self.__first_file_index))

        self.__last_file_index = base.Scaled(
            size=1,
            signed=False,
            minimum=3,
            maximum=255
        )
        self._register(('last_file_index', self.__last_file_index))
        self._default_bytes = b'\x03\x03'
        self._property_scope, self._property_key = 0, 355
        self._definition = standard.add(self)

    def __set_first_file_index(self, v):
        self.__first_file_index._value = v

    first_file_index = property(
        lambda self: self.__first_file_index._value,
        __set_first_file_index,
        None,
        """."""
    )

    def __set_last_file_index(self, v):
        self.__last_file_index._value = v

    last_file_index = property(
        lambda self: self.__last_file_index._value,
        __set_last_file_index,
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
        self.__set_first_file_index(v.__first_file_index)
        self.__set_last_file_index(v.__last_file_index)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 2


if __name__ == '__main__':
    # unit test code.
    item = SCPTprogFileIndexes()
    pass
