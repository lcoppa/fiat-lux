"""ISO_7811 standard datapoint type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0.  Note this resource is marked as
obsolete.  It should not be used for new development, but continued use in
existing designs is permitted."""


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


class ISO_7811(pylon.resources.base.Structure):
    """ISO_7811 standard datapoint type.  ISO 7811.  This SNVT is obsolete.
    Use SNVT_magcard instead.  (38 hexadecimal digits.)."""

    def __init__(self):
        super().__init__(
            key=80,
            scope=0
        )

        self.___bf00 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.___bf01 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf01', self.___bf01))

        self.___bf02 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf02', self.___bf02))

        self.___bf03 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf03', self.___bf03))

        self.___bf04 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf04', self.___bf04))

        self.___bf05 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf05', self.___bf05))

        self.___bf06 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf06', self.___bf06))

        self.___bf07 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf07', self.___bf07))

        self.___bf08 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf08', self.___bf08))

        self.___bf09 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf09', self.___bf09))

        self.___bf10 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf10', self.___bf10))

        self.___bf11 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf11', self.___bf11))

        self.___bf12 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf12', self.___bf12))

        self.___bf13 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf13', self.___bf13))

        self.___bf14 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf14', self.___bf14))

        self.___bf15 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf15', self.___bf15))

        self.___bf16 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf16', self.___bf16))

        self.___bf17 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf17', self.___bf17))

        self.___bf18 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf18', self.___bf18))
        self._original_name = 'SNVT_ISO_7811'
        self._mark_obsolete()
        self._definition = standard.add(self)

    def __set_digit1(self, v):
        if 0 <= v <= 15:
            self.___bf00._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit1(self):
        return self.___bf00._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit1 = property(
        __get_digit1,
        __set_digit1,
        None,
        """hexadecimal digit."""
    )

    def __set_digit2(self, v):
        if 0 <= v <= 15:
            self.___bf00._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit2(self):
        return self.___bf00._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit2 = property(
        __get_digit2,
        __set_digit2,
        None,
        """hexadecimal digit."""
    )

    def __set_digit3(self, v):
        if 0 <= v <= 15:
            self.___bf01._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit3(self):
        return self.___bf01._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit3 = property(
        __get_digit3,
        __set_digit3,
        None,
        """hexadecimal digit."""
    )

    def __set_digit4(self, v):
        if 0 <= v <= 15:
            self.___bf01._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit4(self):
        return self.___bf01._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit4 = property(
        __get_digit4,
        __set_digit4,
        None,
        """hexadecimal digit."""
    )

    def __set_digit5(self, v):
        if 0 <= v <= 15:
            self.___bf02._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit5(self):
        return self.___bf02._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit5 = property(
        __get_digit5,
        __set_digit5,
        None,
        """hexadecimal digit."""
    )

    def __set_digit6(self, v):
        if 0 <= v <= 15:
            self.___bf02._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit6(self):
        return self.___bf02._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit6 = property(
        __get_digit6,
        __set_digit6,
        None,
        """hexadecimal digit."""
    )

    def __set_digit7(self, v):
        if 0 <= v <= 15:
            self.___bf03._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit7(self):
        return self.___bf03._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit7 = property(
        __get_digit7,
        __set_digit7,
        None,
        """hexadecimal digit."""
    )

    def __set_digit8(self, v):
        if 0 <= v <= 15:
            self.___bf03._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit8(self):
        return self.___bf03._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit8 = property(
        __get_digit8,
        __set_digit8,
        None,
        """hexadecimal digit."""
    )

    def __set_digit9(self, v):
        if 0 <= v <= 15:
            self.___bf04._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit9(self):
        return self.___bf04._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit9 = property(
        __get_digit9,
        __set_digit9,
        None,
        """hexadecimal digit."""
    )

    def __set_digit10(self, v):
        if 0 <= v <= 15:
            self.___bf04._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit10(self):
        return self.___bf04._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit10 = property(
        __get_digit10,
        __set_digit10,
        None,
        """hexadecimal digit."""
    )

    def __set_digit11(self, v):
        if 0 <= v <= 15:
            self.___bf05._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit11(self):
        return self.___bf05._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit11 = property(
        __get_digit11,
        __set_digit11,
        None,
        """hexadecimal digit."""
    )

    def __set_digit12(self, v):
        if 0 <= v <= 15:
            self.___bf05._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit12(self):
        return self.___bf05._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit12 = property(
        __get_digit12,
        __set_digit12,
        None,
        """hexadecimal digit."""
    )

    def __set_digit13(self, v):
        if 0 <= v <= 15:
            self.___bf06._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit13(self):
        return self.___bf06._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit13 = property(
        __get_digit13,
        __set_digit13,
        None,
        """hexadecimal digit."""
    )

    def __set_digit14(self, v):
        if 0 <= v <= 15:
            self.___bf06._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit14(self):
        return self.___bf06._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit14 = property(
        __get_digit14,
        __set_digit14,
        None,
        """hexadecimal digit."""
    )

    def __set_digit15(self, v):
        if 0 <= v <= 15:
            self.___bf07._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit15(self):
        return self.___bf07._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit15 = property(
        __get_digit15,
        __set_digit15,
        None,
        """hexadecimal digit."""
    )

    def __set_digit16(self, v):
        if 0 <= v <= 15:
            self.___bf07._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit16(self):
        return self.___bf07._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit16 = property(
        __get_digit16,
        __set_digit16,
        None,
        """hexadecimal digit."""
    )

    def __set_digit17(self, v):
        if 0 <= v <= 15:
            self.___bf08._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit17(self):
        return self.___bf08._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit17 = property(
        __get_digit17,
        __set_digit17,
        None,
        """hexadecimal digit."""
    )

    def __set_digit18(self, v):
        if 0 <= v <= 15:
            self.___bf08._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit18(self):
        return self.___bf08._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit18 = property(
        __get_digit18,
        __set_digit18,
        None,
        """hexadecimal digit."""
    )

    def __set_digit19(self, v):
        if 0 <= v <= 15:
            self.___bf09._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit19(self):
        return self.___bf09._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit19 = property(
        __get_digit19,
        __set_digit19,
        None,
        """hexadecimal digit."""
    )

    def __set_digit20(self, v):
        if 0 <= v <= 15:
            self.___bf09._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit20(self):
        return self.___bf09._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit20 = property(
        __get_digit20,
        __set_digit20,
        None,
        """hexadecimal digit."""
    )

    def __set_digit21(self, v):
        if 0 <= v <= 15:
            self.___bf10._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit21(self):
        return self.___bf10._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit21 = property(
        __get_digit21,
        __set_digit21,
        None,
        """hexadecimal digit."""
    )

    def __set_digit22(self, v):
        if 0 <= v <= 15:
            self.___bf10._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit22(self):
        return self.___bf10._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit22 = property(
        __get_digit22,
        __set_digit22,
        None,
        """hexadecimal digit."""
    )

    def __set_digit23(self, v):
        if 0 <= v <= 15:
            self.___bf11._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit23(self):
        return self.___bf11._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit23 = property(
        __get_digit23,
        __set_digit23,
        None,
        """hexadecimal digit."""
    )

    def __set_digit24(self, v):
        if 0 <= v <= 15:
            self.___bf11._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit24(self):
        return self.___bf11._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit24 = property(
        __get_digit24,
        __set_digit24,
        None,
        """hexadecimal digit."""
    )

    def __set_digit25(self, v):
        if 0 <= v <= 15:
            self.___bf12._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit25(self):
        return self.___bf12._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit25 = property(
        __get_digit25,
        __set_digit25,
        None,
        """hexadecimal digit."""
    )

    def __set_digit26(self, v):
        if 0 <= v <= 15:
            self.___bf12._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit26(self):
        return self.___bf12._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit26 = property(
        __get_digit26,
        __set_digit26,
        None,
        """hexadecimal digit."""
    )

    def __set_digit27(self, v):
        if 0 <= v <= 15:
            self.___bf13._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit27(self):
        return self.___bf13._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit27 = property(
        __get_digit27,
        __set_digit27,
        None,
        """hexadecimal digit."""
    )

    def __set_digit28(self, v):
        if 0 <= v <= 15:
            self.___bf13._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit28(self):
        return self.___bf13._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit28 = property(
        __get_digit28,
        __set_digit28,
        None,
        """hexadecimal digit."""
    )

    def __set_digit29(self, v):
        if 0 <= v <= 15:
            self.___bf14._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit29(self):
        return self.___bf14._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit29 = property(
        __get_digit29,
        __set_digit29,
        None,
        """hexadecimal digit."""
    )

    def __set_digit30(self, v):
        if 0 <= v <= 15:
            self.___bf14._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit30(self):
        return self.___bf14._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit30 = property(
        __get_digit30,
        __set_digit30,
        None,
        """hexadecimal digit."""
    )

    def __set_digit31(self, v):
        if 0 <= v <= 15:
            self.___bf15._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit31(self):
        return self.___bf15._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit31 = property(
        __get_digit31,
        __set_digit31,
        None,
        """hexadecimal digit."""
    )

    def __set_digit32(self, v):
        if 0 <= v <= 15:
            self.___bf15._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit32(self):
        return self.___bf15._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit32 = property(
        __get_digit32,
        __set_digit32,
        None,
        """hexadecimal digit."""
    )

    def __set_digit33(self, v):
        if 0 <= v <= 15:
            self.___bf16._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit33(self):
        return self.___bf16._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit33 = property(
        __get_digit33,
        __set_digit33,
        None,
        """hexadecimal digit."""
    )

    def __set_digit34(self, v):
        if 0 <= v <= 15:
            self.___bf16._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit34(self):
        return self.___bf16._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit34 = property(
        __get_digit34,
        __set_digit34,
        None,
        """hexadecimal digit."""
    )

    def __set_digit35(self, v):
        if 0 <= v <= 15:
            self.___bf17._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit35(self):
        return self.___bf17._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit35 = property(
        __get_digit35,
        __set_digit35,
        None,
        """hexadecimal digit."""
    )

    def __set_digit36(self, v):
        if 0 <= v <= 15:
            self.___bf17._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit36(self):
        return self.___bf17._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit36 = property(
        __get_digit36,
        __set_digit36,
        None,
        """hexadecimal digit."""
    )

    def __set_digit37(self, v):
        if 0 <= v <= 15:
            self.___bf18._setbits(
                value=v,
                size=4,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit37(self):
        return self.___bf18._getbits(
            size=4,
            offset=0,
            signed=False
        )

    digit37 = property(
        __get_digit37,
        __set_digit37,
        None,
        """hexadecimal digit."""
    )

    def __set_digit38(self, v):
        if 0 <= v <= 15:
            self.___bf18._setbits(
                value=v,
                size=4,
                offset=4
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_digit38(self):
        return self.___bf18._getbits(
            size=4,
            offset=4,
            signed=False
        )

    digit38 = property(
        __get_digit38,
        __set_digit38,
        None,
        """hexadecimal digit."""
    )


    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.___bf18._value = v.___bf18._value
        self.___bf17._value = v.___bf17._value
        self.___bf16._value = v.___bf16._value
        self.___bf15._value = v.___bf15._value
        self.___bf14._value = v.___bf14._value
        self.___bf13._value = v.___bf13._value
        self.___bf12._value = v.___bf12._value
        self.___bf11._value = v.___bf11._value
        self.___bf10._value = v.___bf10._value
        self.___bf09._value = v.___bf09._value
        self.___bf08._value = v.___bf08._value
        self.___bf07._value = v.___bf07._value
        self.___bf06._value = v.___bf06._value
        self.___bf05._value = v.___bf05._value
        self.___bf04._value = v.___bf04._value
        self.___bf03._value = v.___bf03._value
        self.___bf02._value = v.___bf02._value
        self.___bf01._value = v.___bf01._value
        self.___bf00._value = v.___bf00._value

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 19


if __name__ == '__main__':
    # unit test code.
    item = ISO_7811()
    pass
