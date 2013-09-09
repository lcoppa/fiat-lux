"""SNVT_muldiv standard datapoint type, originally defined in resource file
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


class SNVT_muldiv(base.Structure):
    """SNVT_muldiv standard datapoint type.  Multiply/Divide Gain factor.
    (multiplier, divisor.)."""

    def __init__(self):
        super().__init__(
            key=91,
            scope=0
        )

        self.__multiplier = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('multiplier', self.__multiplier))

        self.__divisor = base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=65535
        )
        self._register(('divisor', self.__divisor))
        self._definition = standard.add(self)


    def __set_multiplier(self, v):
        self.__multiplier._value = v

    multiplier = property(
        lambda self: self.__multiplier._value,
        __set_multiplier,
        None,
        """Multiplier (16-bit unsigned value.)."""
    )

    def __set_divisor(self, v):
        self.__divisor._value = v

    divisor = property(
        lambda self: self.__divisor._value,
        __set_divisor,
        None,
        """Divisor (16-bit unsigned value.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_multiplier(v.__multiplier)
        self.__set_divisor(v.__divisor)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = SNVT_muldiv()
    pass
