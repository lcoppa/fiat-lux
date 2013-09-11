"""SNVT_state_64 standard datapoint type, originally defined in resource file
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


class SNVT_state_64(base.Structure):
    """SNVT_state_64 standard datapoint type.  State vector.  Each state is a
    boolean single-bit value.  (64 individual bit values.)."""

    def __init__(self):
        super().__init__(
            key=165,
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

        self.___bf02 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf02', self.___bf02))

        self.___bf03 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf03', self.___bf03))

        self.___bf04 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf04', self.___bf04))

        self.___bf05 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf05', self.___bf05))

        self.___bf06 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf06', self.___bf06))

        self.___bf07 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf07', self.___bf07))
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

    def __set_bit16(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit16(self):
        return self.___bf02._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit16 = property(
        __get_bit16,
        __set_bit16,
        None,
        """boolean"""
    )

    def __set_bit17(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit17(self):
        return self.___bf02._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit17 = property(
        __get_bit17,
        __set_bit17,
        None,
        """boolean"""
    )

    def __set_bit18(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit18(self):
        return self.___bf02._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit18 = property(
        __get_bit18,
        __set_bit18,
        None,
        """boolean"""
    )

    def __set_bit19(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit19(self):
        return self.___bf02._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit19 = property(
        __get_bit19,
        __set_bit19,
        None,
        """boolean"""
    )

    def __set_bit20(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit20(self):
        return self.___bf02._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit20 = property(
        __get_bit20,
        __set_bit20,
        None,
        """boolean"""
    )

    def __set_bit21(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit21(self):
        return self.___bf02._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit21 = property(
        __get_bit21,
        __set_bit21,
        None,
        """boolean"""
    )

    def __set_bit22(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit22(self):
        return self.___bf02._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit22 = property(
        __get_bit22,
        __set_bit22,
        None,
        """boolean"""
    )

    def __set_bit23(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit23(self):
        return self.___bf02._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit23 = property(
        __get_bit23,
        __set_bit23,
        None,
        """boolean"""
    )

    def __set_bit24(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit24(self):
        return self.___bf03._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit24 = property(
        __get_bit24,
        __set_bit24,
        None,
        """boolean"""
    )

    def __set_bit25(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit25(self):
        return self.___bf03._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit25 = property(
        __get_bit25,
        __set_bit25,
        None,
        """boolean"""
    )

    def __set_bit26(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit26(self):
        return self.___bf03._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit26 = property(
        __get_bit26,
        __set_bit26,
        None,
        """boolean"""
    )

    def __set_bit27(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit27(self):
        return self.___bf03._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit27 = property(
        __get_bit27,
        __set_bit27,
        None,
        """boolean"""
    )

    def __set_bit28(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit28(self):
        return self.___bf03._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit28 = property(
        __get_bit28,
        __set_bit28,
        None,
        """boolean"""
    )

    def __set_bit29(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit29(self):
        return self.___bf03._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit29 = property(
        __get_bit29,
        __set_bit29,
        None,
        """boolean"""
    )

    def __set_bit30(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit30(self):
        return self.___bf03._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit30 = property(
        __get_bit30,
        __set_bit30,
        None,
        """boolean"""
    )

    def __set_bit31(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit31(self):
        return self.___bf03._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit31 = property(
        __get_bit31,
        __set_bit31,
        None,
        """boolean"""
    )

    def __set_bit32(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit32(self):
        return self.___bf04._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit32 = property(
        __get_bit32,
        __set_bit32,
        None,
        """boolean"""
    )

    def __set_bit33(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit33(self):
        return self.___bf04._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit33 = property(
        __get_bit33,
        __set_bit33,
        None,
        """boolean"""
    )

    def __set_bit34(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit34(self):
        return self.___bf04._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit34 = property(
        __get_bit34,
        __set_bit34,
        None,
        """boolean"""
    )

    def __set_bit35(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit35(self):
        return self.___bf04._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit35 = property(
        __get_bit35,
        __set_bit35,
        None,
        """boolean"""
    )

    def __set_bit36(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit36(self):
        return self.___bf04._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit36 = property(
        __get_bit36,
        __set_bit36,
        None,
        """boolean"""
    )

    def __set_bit37(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit37(self):
        return self.___bf04._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit37 = property(
        __get_bit37,
        __set_bit37,
        None,
        """boolean"""
    )

    def __set_bit38(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit38(self):
        return self.___bf04._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit38 = property(
        __get_bit38,
        __set_bit38,
        None,
        """boolean"""
    )

    def __set_bit39(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit39(self):
        return self.___bf04._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit39 = property(
        __get_bit39,
        __set_bit39,
        None,
        """boolean"""
    )

    def __set_bit40(self, v):
        if 0 <= v <= 1:
            self.___bf05._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit40(self):
        return self.___bf05._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit40 = property(
        __get_bit40,
        __set_bit40,
        None,
        """boolean"""
    )

    def __set_bit41(self, v):
        if 0 <= v <= 1:
            self.___bf05._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit41(self):
        return self.___bf05._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit41 = property(
        __get_bit41,
        __set_bit41,
        None,
        """boolean"""
    )

    def __set_bit42(self, v):
        if 0 <= v <= 1:
            self.___bf05._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit42(self):
        return self.___bf05._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit42 = property(
        __get_bit42,
        __set_bit42,
        None,
        """boolean"""
    )

    def __set_bit43(self, v):
        if 0 <= v <= 1:
            self.___bf05._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit43(self):
        return self.___bf05._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit43 = property(
        __get_bit43,
        __set_bit43,
        None,
        """boolean"""
    )

    def __set_bit44(self, v):
        if 0 <= v <= 1:
            self.___bf05._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit44(self):
        return self.___bf05._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit44 = property(
        __get_bit44,
        __set_bit44,
        None,
        """boolean"""
    )

    def __set_bit45(self, v):
        if 0 <= v <= 1:
            self.___bf05._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit45(self):
        return self.___bf05._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit45 = property(
        __get_bit45,
        __set_bit45,
        None,
        """boolean"""
    )

    def __set_bit46(self, v):
        if 0 <= v <= 1:
            self.___bf05._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit46(self):
        return self.___bf05._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit46 = property(
        __get_bit46,
        __set_bit46,
        None,
        """boolean"""
    )

    def __set_bit47(self, v):
        if 0 <= v <= 1:
            self.___bf05._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit47(self):
        return self.___bf05._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit47 = property(
        __get_bit47,
        __set_bit47,
        None,
        """boolean"""
    )

    def __set_bit48(self, v):
        if 0 <= v <= 1:
            self.___bf06._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit48(self):
        return self.___bf06._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit48 = property(
        __get_bit48,
        __set_bit48,
        None,
        """boolean"""
    )

    def __set_bit49(self, v):
        if 0 <= v <= 1:
            self.___bf06._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit49(self):
        return self.___bf06._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit49 = property(
        __get_bit49,
        __set_bit49,
        None,
        """boolean"""
    )

    def __set_bit50(self, v):
        if 0 <= v <= 1:
            self.___bf06._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit50(self):
        return self.___bf06._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit50 = property(
        __get_bit50,
        __set_bit50,
        None,
        """boolean"""
    )

    def __set_bit51(self, v):
        if 0 <= v <= 1:
            self.___bf06._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit51(self):
        return self.___bf06._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit51 = property(
        __get_bit51,
        __set_bit51,
        None,
        """boolean"""
    )

    def __set_bit52(self, v):
        if 0 <= v <= 1:
            self.___bf06._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit52(self):
        return self.___bf06._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit52 = property(
        __get_bit52,
        __set_bit52,
        None,
        """boolean"""
    )

    def __set_bit53(self, v):
        if 0 <= v <= 1:
            self.___bf06._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit53(self):
        return self.___bf06._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit53 = property(
        __get_bit53,
        __set_bit53,
        None,
        """boolean"""
    )

    def __set_bit54(self, v):
        if 0 <= v <= 1:
            self.___bf06._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit54(self):
        return self.___bf06._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit54 = property(
        __get_bit54,
        __set_bit54,
        None,
        """boolean"""
    )

    def __set_bit55(self, v):
        if 0 <= v <= 1:
            self.___bf06._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit55(self):
        return self.___bf06._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit55 = property(
        __get_bit55,
        __set_bit55,
        None,
        """boolean"""
    )

    def __set_bit56(self, v):
        if 0 <= v <= 1:
            self.___bf07._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit56(self):
        return self.___bf07._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit56 = property(
        __get_bit56,
        __set_bit56,
        None,
        """boolean"""
    )

    def __set_bit57(self, v):
        if 0 <= v <= 1:
            self.___bf07._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit57(self):
        return self.___bf07._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit57 = property(
        __get_bit57,
        __set_bit57,
        None,
        """boolean"""
    )

    def __set_bit58(self, v):
        if 0 <= v <= 1:
            self.___bf07._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit58(self):
        return self.___bf07._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit58 = property(
        __get_bit58,
        __set_bit58,
        None,
        """boolean"""
    )

    def __set_bit59(self, v):
        if 0 <= v <= 1:
            self.___bf07._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit59(self):
        return self.___bf07._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit59 = property(
        __get_bit59,
        __set_bit59,
        None,
        """boolean"""
    )

    def __set_bit60(self, v):
        if 0 <= v <= 1:
            self.___bf07._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit60(self):
        return self.___bf07._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit60 = property(
        __get_bit60,
        __set_bit60,
        None,
        """boolean"""
    )

    def __set_bit61(self, v):
        if 0 <= v <= 1:
            self.___bf07._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit61(self):
        return self.___bf07._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit61 = property(
        __get_bit61,
        __set_bit61,
        None,
        """boolean"""
    )

    def __set_bit62(self, v):
        if 0 <= v <= 1:
            self.___bf07._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit62(self):
        return self.___bf07._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit62 = property(
        __get_bit62,
        __set_bit62,
        None,
        """boolean"""
    )

    def __set_bit63(self, v):
        if 0 <= v <= 1:
            self.___bf07._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit63(self):
        return self.___bf07._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit63 = property(
        __get_bit63,
        __set_bit63,
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
        self.__set_bit0(v.__bit0)
        self.__set_bit1(v.__bit1)
        self.__set_bit2(v.__bit2)
        self.__set_bit3(v.__bit3)
        self.__set_bit4(v.__bit4)
        self.__set_bit5(v.__bit5)
        self.__set_bit6(v.__bit6)
        self.__set_bit7(v.__bit7)
        self.__set_bit8(v.__bit8)
        self.__set_bit9(v.__bit9)
        self.__set_bit10(v.__bit10)
        self.__set_bit11(v.__bit11)
        self.__set_bit12(v.__bit12)
        self.__set_bit13(v.__bit13)
        self.__set_bit14(v.__bit14)
        self.__set_bit15(v.__bit15)
        self.__set_bit16(v.__bit16)
        self.__set_bit17(v.__bit17)
        self.__set_bit18(v.__bit18)
        self.__set_bit19(v.__bit19)
        self.__set_bit20(v.__bit20)
        self.__set_bit21(v.__bit21)
        self.__set_bit22(v.__bit22)
        self.__set_bit23(v.__bit23)
        self.__set_bit24(v.__bit24)
        self.__set_bit25(v.__bit25)
        self.__set_bit26(v.__bit26)
        self.__set_bit27(v.__bit27)
        self.__set_bit28(v.__bit28)
        self.__set_bit29(v.__bit29)
        self.__set_bit30(v.__bit30)
        self.__set_bit31(v.__bit31)
        self.__set_bit32(v.__bit32)
        self.__set_bit33(v.__bit33)
        self.__set_bit34(v.__bit34)
        self.__set_bit35(v.__bit35)
        self.__set_bit36(v.__bit36)
        self.__set_bit37(v.__bit37)
        self.__set_bit38(v.__bit38)
        self.__set_bit39(v.__bit39)
        self.__set_bit40(v.__bit40)
        self.__set_bit41(v.__bit41)
        self.__set_bit42(v.__bit42)
        self.__set_bit43(v.__bit43)
        self.__set_bit44(v.__bit44)
        self.__set_bit45(v.__bit45)
        self.__set_bit46(v.__bit46)
        self.__set_bit47(v.__bit47)
        self.__set_bit48(v.__bit48)
        self.__set_bit49(v.__bit49)
        self.__set_bit50(v.__bit50)
        self.__set_bit51(v.__bit51)
        self.__set_bit52(v.__bit52)
        self.__set_bit53(v.__bit53)
        self.__set_bit54(v.__bit54)
        self.__set_bit55(v.__bit55)
        self.__set_bit56(v.__bit56)
        self.__set_bit57(v.__bit57)
        self.__set_bit58(v.__bit58)
        self.__set_bit59(v.__bit59)
        self.__set_bit60(v.__bit60)
        self.__set_bit61(v.__bit61)
        self.__set_bit62(v.__bit62)
        self.__set_bit63(v.__bit63)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 8


if __name__ == '__main__':
    # unit test code.
    item = SNVT_state_64()
    pass