"""SNVT_hvac_satsts standard datapoint type, originally defined in resource
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class SNVT_hvac_satsts(base.Structure):
    """SNVT_hvac_satsts standard datapoint type.  HVAC saturation status.  A
    value of 0 in a field indicates that the resource associated with that
    field has not saturated or reached an end stop before attaining the
    required setpoint.  A value of 1 indicates that the resource associated
    with that field has saturated or reached an end stop without attaining
    the required setpoint."""

    def __init__(self):
        super().__init__(
            key=172,
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

    def __set_pri_heat(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_pri_heat(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    pri_heat = property(
        __get_pri_heat,
        __set_pri_heat,
        None,
        """Primary heating saturation status.  A value of 0 indicates primary
        heating is not saturated.  A value of 1 indicates primary heating is
        saturated.  (boolean)"""
    )

    def __set_sec_heat(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_sec_heat(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    sec_heat = property(
        __get_sec_heat,
        __set_sec_heat,
        None,
        """Secondary heating saturation status.  A value of 0 indicates
        secondary heating is not saturated.  A value of 1 indicates secondary
        heating is saturated.  (boolean)"""
    )

    def __set_pri_cool(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_pri_cool(self):
        return self.___bf00._getbits(
            size=1,
            offset=2,
            signed=False
        )

    pri_cool = property(
        __get_pri_cool,
        __set_pri_cool,
        None,
        """Primary cooling saturation status.  A value of 0 indicates primary
        cooling is not saturated.  A value of 1 indicates primary cooling is
        saturated.  (boolean)"""
    )

    def __set_sec_cool(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_sec_cool(self):
        return self.___bf00._getbits(
            size=1,
            offset=3,
            signed=False
        )

    sec_cool = property(
        __get_sec_cool,
        __set_sec_cool,
        None,
        """Secondary cooling saturation status.  A value of 0 indicates
        secondary cooling is not saturated.  A value of 1 indicates secondary
        cooling is saturated.  (boolean)"""
    )

    def __set_pri_duct_starved(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_pri_duct_starved(self):
        return self.___bf00._getbits(
            size=1,
            offset=4,
            signed=False
        )

    pri_duct_starved = property(
        __get_pri_duct_starved,
        __set_pri_duct_starved,
        None,
        """Primary duct saturation status.  A value of 0 indicates primary
        duct is not saturated (starved).  A value of 1 indicates primary duct
        is saturated (starved).  (boolean)"""
    )

    def __set_sec_duct_starved(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_sec_duct_starved(self):
        return self.___bf00._getbits(
            size=1,
            offset=5,
            signed=False
        )

    sec_duct_starved = property(
        __get_sec_duct_starved,
        __set_sec_duct_starved,
        None,
        """Secondary duct saturation status.  A value of 0 indicates
        secondary duct is not saturated (starved).  A value of 1 indicates
        secondary duct is saturated (starved).  (boolean)"""
    )

    def __set_reserved(self, v):
        if 0 <= v <= 3:
            self.___bf00._setbits(
                value=v,
                size=2,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..3')

    def __get_reserved(self):
        return self.___bf00._getbits(
            size=2,
            offset=6,
            signed=False
        )

    reserved = property(
        __get_reserved,
        __set_reserved,
        None,
        """Bitfield reserved"""
    )

    def __set_reserved1(self, v):
        if 0 <= v <= 15:
            self.___bf01._setbits(
                value=v,
                size=4,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_reserved1(self):
        return self.___bf01._getbits(
            size=4,
            offset=0,
            signed=False
        )

    reserved1 = property(
        __get_reserved1,
        __set_reserved1,
        None,
        """Bitfield reserved1"""
    )

    def __set_manufacturer_defined(self, v):
        if 0 <= v <= 15:
            self.___bf01._setbits(
                value=v,
                size=4,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..15')

    def __get_manufacturer_defined(self):
        return self.___bf01._getbits(
            size=4,
            offset=4,
            signed=False
        )

    manufacturer_defined = property(
        __get_manufacturer_defined,
        __set_manufacturer_defined,
        None,
        """Manufacturer defined.  Four manufacturer-defined bits -- please
        see product documentation for proper interpretation of these bits.
        (boolean)"""
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
    item = SNVT_hvac_satsts()
    pass
