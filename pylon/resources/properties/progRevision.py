"""progRevision standard property type, originally defined in resource file
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
# Generated at 23-Sep-2013 09:14.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.time_stamp


class progRevision(pylon.resources.base.Structure):
    """progRevision standard property type.  Program Revision.  Revision
    number and date of currently loaded program."""

    def __init__(self):
        super().__init__(
            key=352,
            scope=0
        )

        self.__major_version = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('major_version', self.__major_version))

        self.__minor_version = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('minor_version', self.__minor_version))

        self.__build_number = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('build_number', self.__build_number))

        self.__build_date = pylon.resources.datapoints.time_stamp.time_stamp(
        )
        self._register(('build_date', self.__build_date))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._original_name = 'SCPTprogRevision'
        self._property_scope, self._property_key = 0, 352
        self._definition = standard.add(self)

    def __set_major_version(self, v):
        self.__major_version._value = v

    major_version = property(
        lambda self: self.__major_version._value,
        __set_major_version,
        None,
        """."""
    )

    def __set_minor_version(self, v):
        self.__minor_version._value = v

    minor_version = property(
        lambda self: self.__minor_version._value,
        __set_minor_version,
        None,
        """."""
    )

    def __set_build_number(self, v):
        self.__build_number._value = v

    build_number = property(
        lambda self: self.__build_number._value,
        __set_build_number,
        None,
        """."""
    )

    def __set_build_date(self, v):
        self.__build_date._value = v

    build_date = property(
        lambda self: self.__build_date._value,
        __set_build_date,
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
        self.__set_major_version(v.__major_version)
        self.__set_minor_version(v.__minor_version)
        self.__set_build_number(v.__build_number)
        self.__set_build_date(v.__build_date)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 11


if __name__ == '__main__':
    # unit test code.
    item = progRevision()
    pass
