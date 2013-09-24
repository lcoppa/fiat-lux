"""SNVT_currency standard datapoint type, originally defined in resource file
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
from pylon.resources.currency_t import currency_t


class SNVT_currency(base.Structure):
    """SNVT_currency standard datapoint type.  Currency (unit, magnitude,
    value.)."""

    def __init__(self):
        super().__init__(
            key=89,
            scope=0
        )

        self.__currency = currency_t(
        )
        self._register(('currency', self.__currency))

        self.__power_of_10 = base.Scaled(
            size=1,
            signed=True,
            minimum=-128,
            maximum=127
        )
        self._register(('power_of_10', self.__power_of_10))

        self.__value = base.Scaled(
            size=4,
            signed=True,
            minimum=-2147483648,
            maximum=2147483647
        )
        self._register(('value', self.__value))
        self._definition = standard.add(self)


    def __set_currency(self, v):
        self.__currency._value = v

    currency = property(
        lambda self: self.__currency._value,
        __set_currency,
        None,
        """Currency (currency names.)."""
    )

    def __set_power_of_10(self, v):
        self.__power_of_10._value = v

    power_of_10 = property(
        lambda self: self.__power_of_10._value,
        __set_power_of_10,
        None,
        """Magnitude (power of 10.)."""
    )

    def __set_value(self, v):
        self.__value._value = v

    value = property(
        lambda self: self.__value._value,
        __set_value,
        None,
        """Value Credit is positive, debit is negative.  (currency
        value.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_currency(v.__currency)
        self.__set_power_of_10(v.__power_of_10)
        self.__set_value(v.__value)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = SNVT_currency()
    pass
