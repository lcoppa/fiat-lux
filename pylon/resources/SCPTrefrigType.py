"""SCPTrefrigType standard property type, originally defined in resource file
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class SCPTrefrigType(base.Structure):
    """SCPTrefrigType standard property type.  Refrigerant type.
    (Refrigerant name, A, B, C.)."""

    def __init__(self):
        super().__init__(
            key=119,
            scope=0
        )

        self.__refrigerant = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(6)
            ]
        )
        self._register(('refrigerant', self.__refrigerant))

        self.__A = base.Float(
            single=True,
            minimum=-3.40282E+038,
            maximum=3.40282E+038
        )
        self._register(('A', self.__A))

        self.__B = base.Float(
            single=True,
            minimum=-3.40282E+038,
            maximum=3.40282E+038
        )
        self._register(('B', self.__B))

        self.__C = base.Float(
            single=True,
            minimum=-3.40282E+038,
            maximum=3.40282E+038
        )
        self._register(('C', self.__C))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 119
        self._definition = standard.add(self)

    def __set_refrigerant(self, v):
        self.__refrigerant._value = v

    refrigerant = property(
        lambda self: self.__refrigerant._value,
        __set_refrigerant,
        None,
        """Refrigerant name.  (array of 6 characters.)."""
    )

    def __set_A(self, v):
        self.__A._value = v

    A = property(
        lambda self: self.__A._value,
        __set_A,
        None,
        """Constant A."""
    )

    def __set_B(self, v):
        self.__B._value = v

    B = property(
        lambda self: self.__B._value,
        __set_B,
        None,
        """Constant B."""
    )

    def __set_C(self, v):
        self.__C._value = v

    C = property(
        lambda self: self.__C._value,
        __set_C,
        None,
        """Constant C."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_refrigerant(v.__refrigerant)
        self.__set_A(v.__A)
        self.__set_B(v.__B)
        self.__set_C(v.__C)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 18


if __name__ == '__main__':
    # unit test code.
    item = SCPTrefrigType()
    pass
