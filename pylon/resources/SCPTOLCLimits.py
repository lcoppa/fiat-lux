"""SCPTOLCLimits standard property type, originally defined in resource file
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
from pylon.resources.SNVT_amp_ac_mil import SNVT_amp_ac_mil
from pylon.resources.SNVT_volt_ac import SNVT_volt_ac
from pylon.resources.SNVT_pwr_fact import SNVT_pwr_fact
from pylon.resources.SNVT_power import SNVT_power


class SCPTOLCLimits(base.Structure):
    """SCPTOLCLimits standard property type.  OLC Limits Setpoints.  MIN/MAX
    values for the status report are set here."""

    def __init__(self):
        super().__init__(
            key=345,
            scope=0
        )

        self.__lamp_current_high = SNVT_amp_ac_mil(
        )
        self._register(('lamp_current_high', self.__lamp_current_high))

        self.__lamp_current_low = SNVT_amp_ac_mil(
        )
        self._register(('lamp_current_low', self.__lamp_current_low))

        self.__main_current_high = SNVT_amp_ac_mil(
        )
        self._register(('main_current_high', self.__main_current_high))

        self.__main_current_low = SNVT_amp_ac_mil(
        )
        self._register(('main_current_low', self.__main_current_low))

        self.__lamp_voltage_high = SNVT_volt_ac(
        )
        self._register(('lamp_voltage_high', self.__lamp_voltage_high))

        self.__lamp_voltage_low = SNVT_volt_ac(
        )
        self._register(('lamp_voltage_low', self.__lamp_voltage_low))

        self.__main_voltage_high = SNVT_volt_ac(
        )
        self._register(('main_voltage_high', self.__main_voltage_high))

        self.__main_voltage_low = SNVT_volt_ac(
        )
        self._register(('main_voltage_low', self.__main_voltage_low))

        self.__power_factor_low = SNVT_pwr_fact(
        )
        self._register(('power_factor_low', self.__power_factor_low))

        self.__power_high = SNVT_power(
        )
        self._register(('power_high', self.__power_high))

        self.__power_low = SNVT_power(
        )
        self._register(('power_low', self.__power_low))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 345
        self._definition = standard.add(self)

    def __set_lamp_current_high(self, v):
        self.__lamp_current_high._value = v

    lamp_current_high = property(
        lambda self: self.__lamp_current_high._value,
        __set_lamp_current_high,
        None,
        """Limit high current."""
    )

    def __set_lamp_current_low(self, v):
        self.__lamp_current_low._value = v

    lamp_current_low = property(
        lambda self: self.__lamp_current_low._value,
        __set_lamp_current_low,
        None,
        """Limit low current."""
    )

    def __set_main_current_high(self, v):
        self.__main_current_high._value = v

    main_current_high = property(
        lambda self: self.__main_current_high._value,
        __set_main_current_high,
        None,
        """Limit main current high."""
    )

    def __set_main_current_low(self, v):
        self.__main_current_low._value = v

    main_current_low = property(
        lambda self: self.__main_current_low._value,
        __set_main_current_low,
        None,
        """Limit main current low."""
    )

    def __set_lamp_voltage_high(self, v):
        self.__lamp_voltage_high._value = v

    lamp_voltage_high = property(
        lambda self: self.__lamp_voltage_high._value,
        __set_lamp_voltage_high,
        None,
        """Limit lamp voltage high."""
    )

    def __set_lamp_voltage_low(self, v):
        self.__lamp_voltage_low._value = v

    lamp_voltage_low = property(
        lambda self: self.__lamp_voltage_low._value,
        __set_lamp_voltage_low,
        None,
        """Limit lamp voltage low."""
    )

    def __set_main_voltage_high(self, v):
        self.__main_voltage_high._value = v

    main_voltage_high = property(
        lambda self: self.__main_voltage_high._value,
        __set_main_voltage_high,
        None,
        """Limit main voltage high."""
    )

    def __set_main_voltage_low(self, v):
        self.__main_voltage_low._value = v

    main_voltage_low = property(
        lambda self: self.__main_voltage_low._value,
        __set_main_voltage_low,
        None,
        """Limit main voltage low."""
    )

    def __set_power_factor_low(self, v):
        self.__power_factor_low._value = v

    power_factor_low = property(
        lambda self: self.__power_factor_low._value,
        __set_power_factor_low,
        None,
        """Limit power factor low."""
    )

    def __set_power_high(self, v):
        self.__power_high._value = v

    power_high = property(
        lambda self: self.__power_high._value,
        __set_power_high,
        None,
        """Limit power high."""
    )

    def __set_power_low(self, v):
        self.__power_low._value = v

    power_low = property(
        lambda self: self.__power_low._value,
        __set_power_low,
        None,
        """Limit power low."""
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
        self.__set_power_high(v.__power_high)
        self.__set_power_low(v.__power_low)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 22


if __name__ == '__main__':
    # unit test code.
    item = SCPTOLCLimits()
    pass
