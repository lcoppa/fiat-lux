"""SNVT_color standard datapoint type, originally defined in resource file
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class SNVT_color(base.Structure):
    """SNVT_color standard datapoint type.  CIELAB color.  (L*,a*,b*)."""

    def __init__(self):
        super().__init__(
            key=70,
            scope=0
        )

        self.__L_star = base.Scaled(
            size=2,
            signed=False,
            scaling=(0.1, 0),
            minimum=0,
            maximum=100
        )
        self._register(('L_star', self.__L_star))

        self.__a_star = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.1, 0),
            minimum=-200,
            maximum=200
        )
        self._register(('a_star', self.__a_star))

        self.__b_star = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.1, 0),
            minimum=-200,
            maximum=200
        )
        self._register(('b_star', self.__b_star))
        self._definition = standard.add(self)


    def __set_L_star(self, v):
        self.__L_star._value = v

    L_star = property(
        lambda self: self.__L_star._value,
        __set_L_star,
        None,
        """L*."""
    )

    def __set_a_star(self, v):
        self.__a_star._value = v

    a_star = property(
        lambda self: self.__a_star._value,
        __set_a_star,
        None,
        """a*."""
    )

    def __set_b_star(self, v):
        self.__b_star._value = v

    b_star = property(
        lambda self: self.__b_star._value,
        __set_b_star,
        None,
        """b*."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_L_star(v.__L_star)
        self.__set_a_star(v.__a_star)
        self.__set_b_star(v.__b_star)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = SNVT_color()
    pass
