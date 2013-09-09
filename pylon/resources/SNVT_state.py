"""SNVT_state standard datapoint type, originally defined in resource file
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


class SNVT_state(base.Structure):
    """SNVT_state standard datapoint type.  State vector.  Each state is a
    boolean single bit value.  SNVT_state_64 is preferred.  (16 individual
    bit values.)."""

    def __init__(self):
        super().__init__(
            key=83,
            scope=0
        )

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.___bf01 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf01', self.___bf01))
        self._definition = standard.add(self)

    def __set_bit0(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit0(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit0 = property(
        __get_bit0,
        __set_bit0,
        None,
        """boolean"""
    )

    def __set_bit1(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit1(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit1 = property(
        __get_bit1,
        __set_bit1,
        None,
        """boolean"""
    )

    def __set_bit2(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit2(self):
        return self.___bf00._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit2 = property(
        __get_bit2,
        __set_bit2,
        None,
        """boolean"""
    )

    def __set_bit3(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit3(self):
        return self.___bf00._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit3 = property(
        __get_bit3,
        __set_bit3,
        None,
        """boolean"""
    )

    def __set_bit4(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit4(self):
        return self.___bf00._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit4 = property(
        __get_bit4,
        __set_bit4,
        None,
        """boolean"""
    )

    def __set_bit5(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit5(self):
        return self.___bf00._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit5 = property(
        __get_bit5,
        __set_bit5,
        None,
        """boolean"""
    )

    def __set_bit6(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit6(self):
        return self.___bf00._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit6 = property(
        __get_bit6,
        __set_bit6,
        None,
        """boolean"""
    )

    def __set_bit7(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit7(self):
        return self.___bf00._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit7 = property(
        __get_bit7,
        __set_bit7,
        None,
        """boolean"""
    )

    def __set_bit8(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit8(self):
        return self.___bf01._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit8 = property(
        __get_bit8,
        __set_bit8,
        None,
        """boolean"""
    )

    def __set_bit9(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit9(self):
        return self.___bf01._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit9 = property(
        __get_bit9,
        __set_bit9,
        None,
        """boolean"""
    )

    def __set_bit10(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit10(self):
        return self.___bf01._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit10 = property(
        __get_bit10,
        __set_bit10,
        None,
        """boolean"""
    )

    def __set_bit11(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit11(self):
        return self.___bf01._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit11 = property(
        __get_bit11,
        __set_bit11,
        None,
        """boolean"""
    )

    def __set_bit12(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit12(self):
        return self.___bf01._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit12 = property(
        __get_bit12,
        __set_bit12,
        None,
        """boolean"""
    )

    def __set_bit13(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit13(self):
        return self.___bf01._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit13 = property(
        __get_bit13,
        __set_bit13,
        None,
        """boolean"""
    )

    def __set_bit14(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit14(self):
        return self.___bf01._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit14 = property(
        __get_bit14,
        __set_bit14,
        None,
        """boolean"""
    )

    def __set_bit15(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit15(self):
        return self.___bf01._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit15 = property(
        __get_bit15,
        __set_bit15,
        None,
        """boolean"""
    )


    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.___bf01(v.___bf01)
        self.___bf00(v.___bf00)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 2


if __name__ == '__main__':
    # unit test code.
    item = SNVT_state()
    pass
