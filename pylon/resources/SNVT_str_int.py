"""SNVT_str_int standard datapoint type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0.  """


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


class SNVT_str_int(base.Structure):
    """SNVT_str_int standard datapoint type.  Wide character string with
    locale code (15 characters max) (Wide character string.)."""

    def __init__(self):
        super().__init__(
            key=37,
            scope=0
        )

        self.__char_set = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('char_set', self.__char_set))

        self.__wide_char = base.Array(
            [
                base.Scaled(
                    size=2,
                    signed=False,
                    minimum=0,
                    maximum=65535
                ) for i in range(15)
            ]
        )
        self._register(('wide_char', self.__wide_char))
        self._definition = standard.add(self)


    def __set_char_set(self, v):
        self.__char_set._value = v

    char_set = property(
        lambda self: self.__char_set._value,
        __set_char_set,
        None,
        """Locale code.  (code value.)."""
    )

    def __set_wide_char(self, v):
        self.__wide_char._value = v

    wide_char = property(
        lambda self: self.__wide_char._value,
        __set_wide_char,
        None,
        """Wide character string.  (array of 15 wide characters.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_char_set(v.__char_set)
        self.__set_wide_char(v.__wide_char)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 31


if __name__ == '__main__':
    # unit test code.
    item = SNVT_str_int()
    pass
