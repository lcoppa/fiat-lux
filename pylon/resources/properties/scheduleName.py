"""scheduleName standard property type, originally defined in resource file
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


class scheduleName(pylon.resources.base.Structure):
    """scheduleName standard property type.  Schedule name.  Used to create
    an array of names for schedules defined by a SCPTschedule array or a
    SCPTscheduleDates array."""

    def __init__(self):
        super().__init__(
            key=279,
            scope=0
        )

        self.__name = pylon.resources.base.Array(
            [
                pylon.resources.base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=126
                ) for i in range(22)
            ]
        )
        self._register(('name', self.__name))
        self._maximum_bytes = b'\x7e\x7e\x7e\x7e\x7e\x7e\x7e\x7e\x7e\x7e\x7e' \
            b'\x7e\x7e\x7e\x7e\x7e\x7e\x7e\x7e\x7e\x7e\x7e'
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._original_name = 'SCPTscheduleName'
        self._property_scope, self._property_key = 0, 279
        self._definition = standard.add(self)

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
        self.__set_name(v.__name)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 22


if __name__ == '__main__':
    # unit test code.
    item = scheduleName()
    pass
