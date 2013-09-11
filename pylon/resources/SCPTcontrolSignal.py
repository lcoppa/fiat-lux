"""SCPTcontrolSignal standard property type, originally defined in resource
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent


class SCPTcontrolSignal(base.Structure):
    """SCPTcontrolSignal standard property type.  Control signal.  Start and
    end points (X,Y) for a transition.  (X1, Y1, X2, Y2.)."""

    def __init__(self):
        super().__init__(
            key=245,
            scope=0
        )

        self.__x1Value = SNVT_lev_percent(
        )
        self._register(('x1Value', self.__x1Value))

        self.__y1Value = SNVT_lev_percent(
        )
        self._register(('y1Value', self.__y1Value))

        self.__x2Value = SNVT_lev_percent(
        )
        self._register(('x2Value', self.__x2Value))

        self.__y2Value = SNVT_lev_percent(
        )
        self._register(('y2Value', self.__y2Value))
        self._minimum_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 245
        self._definition = standard.add(self)

    def __set_x1Value(self, v):
        self.__x1Value._value = v

    x1Value = property(
        lambda self: self.__x1Value._value,
        __set_x1Value,
        None,
        """X1."""
    )

    def __set_y1Value(self, v):
        self.__y1Value._value = v

    y1Value = property(
        lambda self: self.__y1Value._value,
        __set_y1Value,
        None,
        """Y1."""
    )

    def __set_x2Value(self, v):
        self.__x2Value._value = v

    x2Value = property(
        lambda self: self.__x2Value._value,
        __set_x2Value,
        None,
        """X2."""
    )

    def __set_y2Value(self, v):
        self.__y2Value._value = v

    y2Value = property(
        lambda self: self.__y2Value._value,
        __set_y2Value,
        None,
        """Y2."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_x1Value(v.__x1Value)
        self.__set_y1Value(v.__y1Value)
        self.__set_x2Value(v.__x2Value)
        self.__set_y2Value(v.__y2Value)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 8


if __name__ == '__main__':
    # unit test code.
    item = SCPTcontrolSignal()
    pass
