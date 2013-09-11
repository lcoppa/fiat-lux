"""SCPTenableStatusMsg standard property type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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


class SCPTenableStatusMsg(base.Structure):
    """SCPTenableStatusMsg standard property type.  Enable Status Message."""

    def __init__(self):
        super().__init__(
            key=348,
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
        self._default_bytes = b'\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 348
        self._definition = standard.add(self)
    def __set_lamp_current_high(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_lamp_current_high(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    lamp_current_high = property(
        __get_lamp_current_high,
        __set_lamp_current_high,
        None,
        """Bitfield lamp_current_high"""
    )

    def __set_lamp_current_low(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_lamp_current_low(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    lamp_current_low = property(
        __get_lamp_current_low,
        __set_lamp_current_low,
        None,
        """Bitfield lamp_current_low"""
    )

    def __set_main_current_high(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_main_current_high(self):
        return self.___bf00._getbits(
            size=1,
            offset=2,
            signed=False
        )

    main_current_high = property(
        __get_main_current_high,
        __set_main_current_high,
        None,
        """Bitfield main_current_high"""
    )

    def __set_main_current_low(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_main_current_low(self):
        return self.___bf00._getbits(
            size=1,
            offset=3,
            signed=False
        )

    main_current_low = property(
        __get_main_current_low,
        __set_main_current_low,
        None,
        """Bitfield main_current_low"""
    )

    def __set_lamp_voltage_high(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_lamp_voltage_high(self):
        return self.___bf00._getbits(
            size=1,
            offset=4,
            signed=False
        )

    lamp_voltage_high = property(
        __get_lamp_voltage_high,
        __set_lamp_voltage_high,
        None,
        """Bitfield lamp_voltage_high"""
    )

    def __set_lamp_voltage_low(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_lamp_voltage_low(self):
        return self.___bf00._getbits(
            size=1,
            offset=5,
            signed=False
        )

    lamp_voltage_low = property(
        __get_lamp_voltage_low,
        __set_lamp_voltage_low,
        None,
        """Bitfield lamp_voltage_low"""
    )

    def __set_main_voltage_high(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_main_voltage_high(self):
        return self.___bf00._getbits(
            size=1,
            offset=6,
            signed=False
        )

    main_voltage_high = property(
        __get_main_voltage_high,
        __set_main_voltage_high,
        None,
        """Bitfield main_voltage_high"""
    )

    def __set_main_voltage_low(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_main_voltage_low(self):
        return self.___bf00._getbits(
            size=1,
            offset=7,
            signed=False
        )

    main_voltage_low = property(
        __get_main_voltage_low,
        __set_main_voltage_low,
        None,
        """Bitfield main_voltage_low"""
    )

    def __set_power_factor_low(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_power_factor_low(self):
        return self.___bf01._getbits(
            size=1,
            offset=0,
            signed=False
        )

    power_factor_low = property(
        __get_power_factor_low,
        __set_power_factor_low,
        None,
        """Bitfield power_factor_low"""
    )

    def __set_OLC_temp_high(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_OLC_temp_high(self):
        return self.___bf01._getbits(
            size=1,
            offset=1,
            signed=False
        )

    OLC_temp_high = property(
        __get_OLC_temp_high,
        __set_OLC_temp_high,
        None,
        """Bitfield OLC_temp_high"""
    )

    def __set_power_high(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_power_high(self):
        return self.___bf01._getbits(
            size=1,
            offset=2,
            signed=False
        )

    power_high = property(
        __get_power_high,
        __set_power_high,
        None,
        """Bitfield power_high"""
    )

    def __set_power_low(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_power_low(self):
        return self.___bf01._getbits(
            size=1,
            offset=3,
            signed=False
        )

    power_low = property(
        __get_power_low,
        __set_power_low,
        None,
        """Bitfield power_low"""
    )

    def __set_relay_failure(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_relay_failure(self):
        return self.___bf01._getbits(
            size=1,
            offset=4,
            signed=False
        )

    relay_failure = property(
        __get_relay_failure,
        __set_relay_failure,
        None,
        """Bitfield relay_failure"""
    )

    def __set_cap_failure(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_cap_failure(self):
        return self.___bf01._getbits(
            size=1,
            offset=5,
            signed=False
        )

    cap_failure = property(
        __get_cap_failure,
        __set_cap_failure,
        None,
        """Bitfield cap_failure"""
    )

    def __set_lamp_failure(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_lamp_failure(self):
        return self.___bf01._getbits(
            size=1,
            offset=6,
            signed=False
        )

    lamp_failure = property(
        __get_lamp_failure,
        __set_lamp_failure,
        None,
        """Bitfield lamp_failure"""
    )

    def __set_ballast_failure(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_ballast_failure(self):
        return self.___bf01._getbits(
            size=1,
            offset=7,
            signed=False
        )

    ballast_failure = property(
        __get_ballast_failure,
        __set_ballast_failure,
        None,
        """Bitfield ballast_failure"""
    )

    def __set_inter_com_failure(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_inter_com_failure(self):
        return self.___bf02._getbits(
            size=1,
            offset=0,
            signed=False
        )

    inter_com_failure = property(
        __get_inter_com_failure,
        __set_inter_com_failure,
        None,
        """Bitfield inter_com_failure"""
    )

    def __set_exter_com_failure(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_exter_com_failure(self):
        return self.___bf02._getbits(
            size=1,
            offset=1,
            signed=False
        )

    exter_com_failure = property(
        __get_exter_com_failure,
        __set_exter_com_failure,
        None,
        """Bitfield exter_com_failure"""
    )

    def __set_main_volt_below_spec(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_main_volt_below_spec(self):
        return self.___bf02._getbits(
            size=1,
            offset=2,
            signed=False
        )

    main_volt_below_spec = property(
        __get_main_volt_below_spec,
        __set_main_volt_below_spec,
        None,
        """Bitfield main_volt_below_spec"""
    )

    def __set_lamp_restart_count(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_lamp_restart_count(self):
        return self.___bf02._getbits(
            size=1,
            offset=3,
            signed=False
        )

    lamp_restart_count = property(
        __get_lamp_restart_count,
        __set_lamp_restart_count,
        None,
        """Bitfield lamp_restart_count"""
    )

    def __set_fading_ready(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_fading_ready(self):
        return self.___bf02._getbits(
            size=1,
            offset=4,
            signed=False
        )

    fading_ready = property(
        __get_fading_ready,
        __set_fading_ready,
        None,
        """Bitfield fading_ready"""
    )

    def __set_ballast_temp_high(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_ballast_temp_high(self):
        return self.___bf02._getbits(
            size=1,
            offset=5,
            signed=False
        )

    ballast_temp_high = property(
        __get_ballast_temp_high,
        __set_ballast_temp_high,
        None,
        """Bitfield ballast_temp_high"""
    )

    def __set_digi_in_A(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_digi_in_A(self):
        return self.___bf02._getbits(
            size=1,
            offset=6,
            signed=False
        )

    digi_in_A = property(
        __get_digi_in_A,
        __set_digi_in_A,
        None,
        """Bitfield digi_in_A"""
    )

    def __set_digi_in_B(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_digi_in_B(self):
        return self.___bf02._getbits(
            size=1,
            offset=7,
            signed=False
        )

    digi_in_B = property(
        __get_digi_in_B,
        __set_digi_in_B,
        None,
        """Bitfield digi_in_B"""
    )

    def __set_bit_25_res(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_25_res(self):
        return self.___bf03._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit_25_res = property(
        __get_bit_25_res,
        __set_bit_25_res,
        None,
        """Bitfield bit_25_res"""
    )

    def __set_bit_26_res(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_26_res(self):
        return self.___bf03._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit_26_res = property(
        __get_bit_26_res,
        __set_bit_26_res,
        None,
        """Bitfield bit_26_res"""
    )

    def __set_bit_27_res(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_27_res(self):
        return self.___bf03._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit_27_res = property(
        __get_bit_27_res,
        __set_bit_27_res,
        None,
        """Bitfield bit_27_res"""
    )

    def __set_bit_28_res(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_28_res(self):
        return self.___bf03._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit_28_res = property(
        __get_bit_28_res,
        __set_bit_28_res,
        None,
        """Bitfield bit_28_res"""
    )

    def __set_bit_29_res(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_29_res(self):
        return self.___bf03._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit_29_res = property(
        __get_bit_29_res,
        __set_bit_29_res,
        None,
        """Bitfield bit_29_res"""
    )

    def __set_bit_30_res(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_30_res(self):
        return self.___bf03._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit_30_res = property(
        __get_bit_30_res,
        __set_bit_30_res,
        None,
        """Bitfield bit_30_res"""
    )

    def __set_bit_31_res(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_31_res(self):
        return self.___bf03._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit_31_res = property(
        __get_bit_31_res,
        __set_bit_31_res,
        None,
        """Bitfield bit_31_res"""
    )

    def __set_bit_32_res(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_32_res(self):
        return self.___bf03._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit_32_res = property(
        __get_bit_32_res,
        __set_bit_32_res,
        None,
        """Bitfield bit_32_res"""
    )

    def __set_bit_33_res(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_33_res(self):
        return self.___bf04._getbits(
            size=1,
            offset=0,
            signed=False
        )

    bit_33_res = property(
        __get_bit_33_res,
        __set_bit_33_res,
        None,
        """Bitfield bit_33_res"""
    )

    def __set_bit_34_res(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_34_res(self):
        return self.___bf04._getbits(
            size=1,
            offset=1,
            signed=False
        )

    bit_34_res = property(
        __get_bit_34_res,
        __set_bit_34_res,
        None,
        """Bitfield bit_34_res"""
    )

    def __set_bit_35_res(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_35_res(self):
        return self.___bf04._getbits(
            size=1,
            offset=2,
            signed=False
        )

    bit_35_res = property(
        __get_bit_35_res,
        __set_bit_35_res,
        None,
        """Bitfield bit_35_res"""
    )

    def __set_bit_36_res(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_36_res(self):
        return self.___bf04._getbits(
            size=1,
            offset=3,
            signed=False
        )

    bit_36_res = property(
        __get_bit_36_res,
        __set_bit_36_res,
        None,
        """Bitfield bit_36_res"""
    )

    def __set_bit_37_res(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_37_res(self):
        return self.___bf04._getbits(
            size=1,
            offset=4,
            signed=False
        )

    bit_37_res = property(
        __get_bit_37_res,
        __set_bit_37_res,
        None,
        """Bitfield bit_37_res"""
    )

    def __set_bit_38_res(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_38_res(self):
        return self.___bf04._getbits(
            size=1,
            offset=5,
            signed=False
        )

    bit_38_res = property(
        __get_bit_38_res,
        __set_bit_38_res,
        None,
        """Bitfield bit_38_res"""
    )

    def __set_bit_39_res(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_39_res(self):
        return self.___bf04._getbits(
            size=1,
            offset=6,
            signed=False
        )

    bit_39_res = property(
        __get_bit_39_res,
        __set_bit_39_res,
        None,
        """Bitfield bit_39_res"""
    )

    def __set_bit_40_res(self, v):
        if 0 <= v <= 1:
            self.___bf04._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_bit_40_res(self):
        return self.___bf04._getbits(
            size=1,
            offset=7,
            signed=False
        )

    bit_40_res = property(
        __get_bit_40_res,
        __set_bit_40_res,
        None,
        """Bitfield bit_40_res"""
    )


    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_lamp_current_high(v.__lamp_current_high)
        self.__set_lamp_current_low(v.__lamp_current_low)
        self.__set_main_current_high(v.__main_current_high)
        self.__set_main_current_low(v.__main_current_low)
        self.__set_lamp_voltage_high(v.__lamp_voltage_high)
        self.__set_lamp_voltage_low(v.__lamp_voltage_low)
        self.__set_main_voltage_high(v.__main_voltage_high)
        self.__set_main_voltage_low(v.__main_voltage_low)
        self.__set_power_factor_low(v.__power_factor_low)
        self.__set_OLC_temp_high(v.__OLC_temp_high)
        self.__set_power_high(v.__power_high)
        self.__set_power_low(v.__power_low)
        self.__set_relay_failure(v.__relay_failure)
        self.__set_cap_failure(v.__cap_failure)
        self.__set_lamp_failure(v.__lamp_failure)
        self.__set_ballast_failure(v.__ballast_failure)
        self.__set_inter_com_failure(v.__inter_com_failure)
        self.__set_exter_com_failure(v.__exter_com_failure)
        self.__set_main_volt_below_spec(v.__main_volt_below_spec)
        self.__set_lamp_restart_count(v.__lamp_restart_count)
        self.__set_fading_ready(v.__fading_ready)
        self.__set_ballast_temp_high(v.__ballast_temp_high)
        self.__set_digi_in_A(v.__digi_in_A)
        self.__set_digi_in_B(v.__digi_in_B)
        self.__set_bit_25_res(v.__bit_25_res)
        self.__set_bit_26_res(v.__bit_26_res)
        self.__set_bit_27_res(v.__bit_27_res)
        self.__set_bit_28_res(v.__bit_28_res)
        self.__set_bit_29_res(v.__bit_29_res)
        self.__set_bit_30_res(v.__bit_30_res)
        self.__set_bit_31_res(v.__bit_31_res)
        self.__set_bit_32_res(v.__bit_32_res)
        self.__set_bit_33_res(v.__bit_33_res)
        self.__set_bit_34_res(v.__bit_34_res)
        self.__set_bit_35_res(v.__bit_35_res)
        self.__set_bit_36_res(v.__bit_36_res)
        self.__set_bit_37_res(v.__bit_37_res)
        self.__set_bit_38_res(v.__bit_38_res)
        self.__set_bit_39_res(v.__bit_39_res)
        self.__set_bit_40_res(v.__bit_40_res)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 5


if __name__ == '__main__':
    # unit test code.
    item = SCPTenableStatusMsg()
    pass
