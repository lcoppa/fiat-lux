"""SNVT_trans_table standard datapoint type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0.  """


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


class SNVT_trans_table(base.Structure):
    """SNVT_trans_table standard datapoint type.  Translation table.
    (points, interpolation.)."""

    def __init__(self):
        super().__init__(
            key=96,
            scope=0
        )

        self.__point = base.Array(
            [
                base.Float(
                    single=True,
                    minimum=-3.40282E+038,
                    maximum=3.40282E+038
                ) for i in range(7)
            ]
        )
        self._register(('point', self.__point))

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


    def __set_point(self, v):
        self.__point._value = v

    point = property(
        lambda self: self.__point._value,
        __set_point,
        None,
        """Points (array of 7 points.)."""
    )
    def __set_interp_pts_0_to_1(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=2,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_interp_pts_0_to_1(self):
        return self.___bf00._getbits(
            size=2,
            offset=0,
            signed=False
        )

    interp_pts_0_to_1 = property(
        __get_interp_pts_0_to_1,
        __set_interp_pts_0_to_1,
        None,
        """interpolation method code."""
    )

    def __set_interp_pts_1_to_2(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=2,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_interp_pts_1_to_2(self):
        return self.___bf00._getbits(
            size=2,
            offset=2,
            signed=False
        )

    interp_pts_1_to_2 = property(
        __get_interp_pts_1_to_2,
        __set_interp_pts_1_to_2,
        None,
        """interpolation method code."""
    )

    def __set_interp_pts_2_to_3(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=2,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_interp_pts_2_to_3(self):
        return self.___bf00._getbits(
            size=2,
            offset=4,
            signed=False
        )

    interp_pts_2_to_3 = property(
        __get_interp_pts_2_to_3,
        __set_interp_pts_2_to_3,
        None,
        """interpolation method code."""
    )

    def __set_interp_pts_3_to_4(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=2,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_interp_pts_3_to_4(self):
        return self.___bf00._getbits(
            size=2,
            offset=6,
            signed=False
        )

    interp_pts_3_to_4 = property(
        __get_interp_pts_3_to_4,
        __set_interp_pts_3_to_4,
        None,
        """interpolation method code."""
    )

    def __set_interp_pts_4_to_5(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=2,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_interp_pts_4_to_5(self):
        return self.___bf01._getbits(
            size=2,
            offset=0,
            signed=False
        )

    interp_pts_4_to_5 = property(
        __get_interp_pts_4_to_5,
        __set_interp_pts_4_to_5,
        None,
        """interpolation method code."""
    )

    def __set_interp_pts_5_to_6(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=2,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_interp_pts_5_to_6(self):
        return self.___bf01._getbits(
            size=2,
            offset=2,
            signed=False
        )

    interp_pts_5_to_6 = property(
        __get_interp_pts_5_to_6,
        __set_interp_pts_5_to_6,
        None,
        """interpolation method code."""
    )

    def __set_interp_pts_6_to_0(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=2,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_interp_pts_6_to_0(self):
        return self.___bf01._getbits(
            size=2,
            offset=4,
            signed=False
        )

    interp_pts_6_to_0 = property(
        __get_interp_pts_6_to_0,
        __set_interp_pts_6_to_0,
        None,
        """Interpolation for point 6 to point 0.  This field is used when
        multiple interpolation tables are linked.  (interpolation method
        code.)"""
    )


    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_point(v.__point)
        self.__set_interp_pts_0_to_1(v.__interp_pts_0_to_1)
        self.__set_interp_pts_1_to_2(v.__interp_pts_1_to_2)
        self.__set_interp_pts_2_to_3(v.__interp_pts_2_to_3)
        self.__set_interp_pts_3_to_4(v.__interp_pts_3_to_4)
        self.__set_interp_pts_4_to_5(v.__interp_pts_4_to_5)
        self.__set_interp_pts_5_to_6(v.__interp_pts_5_to_6)
        self.__set_interp_pts_6_to_0(v.__interp_pts_6_to_0)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 30


if __name__ == '__main__':
    # unit test code.
    item = SNVT_trans_table()
    pass
