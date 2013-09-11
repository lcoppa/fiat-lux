"""SNVT_reg_val standard datapoint type, originally defined in resource file
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.reg_val_unit_t import reg_val_unit_t


class SNVT_reg_val(base.Structure):
    """SNVT_reg_val standard datapoint type.  Register value.  (raw value,
    unit code, number of decimals.)."""

    def __init__(self):
        super().__init__(
            key=136,
            scope=0
        )

        self.__raw = base.Scaled(
            size=4,
            signed=True,
            minimum=-2147483648,
            maximum=2147483647
        )
        self._register(('raw', self.__raw))

        self.__unit = reg_val_unit_t(
        )
        self._register(('unit', self.__unit))

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))
        self._definition = standard.add(self)


    def __set_raw(self, v):
        self.__raw._value = v

    raw = property(
        lambda self: self.__raw._value,
        __set_raw,
        None,
        """Raw value."""
    )

    def __set_unit(self, v):
        self.__unit._value = v

    unit = property(
        lambda self: self.__unit._value,
        __set_unit,
        None,
        """Unit code.  (defines unit of measure.)."""
    )
    def __set_nr_decimals(self, v):
        if 0 <= v <= 7:
            self.___bf00._setbits(
                value=v,
                size=3,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..7')

    def __get_nr_decimals(self):
        return self.___bf00._getbits(
            size=3,
            offset=0,
            signed=False
        )

    nr_decimals = property(
        __get_nr_decimals,
        __set_nr_decimals,
        None,
        """digits to right of decimal point."""
    )


    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_raw(v.__raw)
        self.__set_unit(v.__unit)
        self.__set_nr_decimals(v.__nr_decimals)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = SNVT_reg_val()
    pass
