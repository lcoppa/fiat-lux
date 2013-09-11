"""SNVT_clothes_w_a standard datapoint type, originally defined in resource
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


class SNVT_clothes_w_a(base.Structure):
    """SNVT_clothes_w_a standard datapoint type.  Clothes Washer Alarm.  Used
    to provide alarm status for a clothes washer."""

    class alarmType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
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

            self.__manuf_code = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=255
            )
            self._register(('manuf_code', self.__manuf_code))
        def __set_alarm_reset(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=0,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_alarm_reset(self):
            return self.___bf00._getbits(
                size=1,
                offset=0,
                signed=False
            )

        alarm_reset = property(
            __get_alarm_reset,
            __set_alarm_reset,
            None,
            """Bitfield alarm_reset"""
        )

        def __set_war_water_supply(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=1,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_water_supply(self):
            return self.___bf00._getbits(
                size=1,
                offset=1,
                signed=False
            )

        war_water_supply = property(
            __get_war_water_supply,
            __set_war_water_supply,
            None,
            """Bitfield war_water_supply"""
        )

        def __set_war_drain_slow(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=2,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_drain_slow(self):
            return self.___bf00._getbits(
                size=1,
                offset=2,
                signed=False
            )

        war_drain_slow = property(
            __get_war_drain_slow,
            __set_war_drain_slow,
            None,
            """Bitfield war_drain_slow"""
        )

        def __set_war_door_open(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=3,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_door_open(self):
            return self.___bf00._getbits(
                size=1,
                offset=3,
                signed=False
            )

        war_door_open = property(
            __get_war_door_open,
            __set_war_door_open,
            None,
            """Bitfield war_door_open"""
        )

        def __set_war_load_unbalanced(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=4,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_load_unbalanced(self):
            return self.___bf00._getbits(
                size=1,
                offset=4,
                signed=False
            )

        war_load_unbalanced = property(
            __get_war_load_unbalanced,
            __set_war_load_unbalanced,
            None,
            """Bitfield war_load_unbalanced"""
        )

        def __set_war_filter_cleaning(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=5,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_filter_cleaning(self):
            return self.___bf00._getbits(
                size=1,
                offset=5,
                signed=False
            )

        war_filter_cleaning = property(
            __get_war_filter_cleaning,
            __set_war_filter_cleaning,
            None,
            """Bitfield war_filter_cleaning"""
        )

        def __set_war_hoses_reversed(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=6,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_hoses_reversed(self):
            return self.___bf00._getbits(
                size=1,
                offset=6,
                signed=False
            )

        war_hoses_reversed = property(
            __get_war_hoses_reversed,
            __set_war_hoses_reversed,
            None,
            """Bitfield war_hoses_reversed"""
        )

        def __set_war_voltage_low(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=7,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_voltage_low(self):
            return self.___bf00._getbits(
                size=1,
                offset=7,
                signed=False
            )

        war_voltage_low = property(
            __get_war_voltage_low,
            __set_war_voltage_low,
            None,
            """Bitfield war_voltage_low"""
        )

        def __set_war_power_failure(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=0,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_power_failure(self):
            return self.___bf01._getbits(
                size=1,
                offset=0,
                signed=False
            )

        war_power_failure = property(
            __get_war_power_failure,
            __set_war_power_failure,
            None,
            """Bitfield war_power_failure"""
        )

        def __set_war_drain_open(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=1,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_drain_open(self):
            return self.___bf01._getbits(
                size=1,
                offset=1,
                signed=False
            )

        war_drain_open = property(
            __get_war_drain_open,
            __set_war_drain_open,
            None,
            """Bitfield war_drain_open"""
        )

        def __set_war_execute_fail(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=2,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_execute_fail(self):
            return self.___bf01._getbits(
                size=1,
                offset=2,
                signed=False
            )

        war_execute_fail = property(
            __get_war_execute_fail,
            __set_war_execute_fail,
            None,
            """Bitfield war_execute_fail"""
        )

        def __set_war_door_locked(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=3,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_door_locked(self):
            return self.___bf01._getbits(
                size=1,
                offset=3,
                signed=False
            )

        war_door_locked = property(
            __get_war_door_locked,
            __set_war_door_locked,
            None,
            """Bitfield war_door_locked"""
        )

        def __set_war_service(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=4,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_war_service(self):
            return self.___bf01._getbits(
                size=1,
                offset=4,
                signed=False
            )

        war_service = property(
            __get_war_service,
            __set_war_service,
            None,
            """Bitfield war_service"""
        )

        def __set_rsrvd5(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=5,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_rsrvd5(self):
            return self.___bf01._getbits(
                size=1,
                offset=5,
                signed=False
            )

        rsrvd5 = property(
            __get_rsrvd5,
            __set_rsrvd5,
            None,
            """Bitfield rsrvd5"""
        )

        def __set_rsrvd6(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=6,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_rsrvd6(self):
            return self.___bf01._getbits(
                size=1,
                offset=6,
                signed=False
            )

        rsrvd6 = property(
            __get_rsrvd6,
            __set_rsrvd6,
            None,
            """Bitfield rsrvd6"""
        )

        def __set_rsrvd7(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=7,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_rsrvd7(self):
            return self.___bf01._getbits(
                size=1,
                offset=7,
                signed=False
            )

        rsrvd7 = property(
            __get_rsrvd7,
            __set_rsrvd7,
            None,
            """Bitfield rsrvd7"""
        )

        def __set_err_motor_stall(self, v):
            if 0 <= v <= 1:
                self.___bf02._setbits(
                    value=v,
                    size=1,
                    offset=0,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_motor_stall(self):
            return self.___bf02._getbits(
                size=1,
                offset=0,
                signed=False
            )

        err_motor_stall = property(
            __get_err_motor_stall,
            __set_err_motor_stall,
            None,
            """Bitfield err_motor_stall"""
        )

        def __set_err_water_temp(self, v):
            if 0 <= v <= 1:
                self.___bf02._setbits(
                    value=v,
                    size=1,
                    offset=1,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_water_temp(self):
            return self.___bf02._getbits(
                size=1,
                offset=1,
                signed=False
            )

        err_water_temp = property(
            __get_err_water_temp,
            __set_err_water_temp,
            None,
            """Bitfield err_water_temp"""
        )

        def __set_err_pressure(self, v):
            if 0 <= v <= 1:
                self.___bf02._setbits(
                    value=v,
                    size=1,
                    offset=2,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_pressure(self):
            return self.___bf02._getbits(
                size=1,
                offset=2,
                signed=False
            )

        err_pressure = property(
            __get_err_pressure,
            __set_err_pressure,
            None,
            """Bitfield err_pressure"""
        )

        def __set_err_overflow(self, v):
            if 0 <= v <= 1:
                self.___bf02._setbits(
                    value=v,
                    size=1,
                    offset=3,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_overflow(self):
            return self.___bf02._getbits(
                size=1,
                offset=3,
                signed=False
            )

        err_overflow = property(
            __get_err_overflow,
            __set_err_overflow,
            None,
            """Bitfield err_overflow"""
        )

        def __set_err_water_heat(self, v):
            if 0 <= v <= 1:
                self.___bf02._setbits(
                    value=v,
                    size=1,
                    offset=4,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_water_heat(self):
            return self.___bf02._getbits(
                size=1,
                offset=4,
                signed=False
            )

        err_water_heat = property(
            __get_err_water_heat,
            __set_err_water_heat,
            None,
            """Bitfield err_water_heat"""
        )

        def __set_err_water_leak(self, v):
            if 0 <= v <= 1:
                self.___bf02._setbits(
                    value=v,
                    size=1,
                    offset=5,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_water_leak(self):
            return self.___bf02._getbits(
                size=1,
                offset=5,
                signed=False
            )

        err_water_leak = property(
            __get_err_water_leak,
            __set_err_water_leak,
            None,
            """Bitfield err_water_leak"""
        )

        def __set_err_motor_speed(self, v):
            if 0 <= v <= 1:
                self.___bf02._setbits(
                    value=v,
                    size=1,
                    offset=6,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_motor_speed(self):
            return self.___bf02._getbits(
                size=1,
                offset=6,
                signed=False
            )

        err_motor_speed = property(
            __get_err_motor_speed,
            __set_err_motor_speed,
            None,
            """Bitfield err_motor_speed"""
        )

        def __set_err_wash_thermistor(self, v):
            if 0 <= v <= 1:
                self.___bf02._setbits(
                    value=v,
                    size=1,
                    offset=7,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_wash_thermistor(self):
            return self.___bf02._getbits(
                size=1,
                offset=7,
                signed=False
            )

        err_wash_thermistor = property(
            __get_err_wash_thermistor,
            __set_err_wash_thermistor,
            None,
            """Bitfield err_wash_thermistor"""
        )

        def __set_err_dry_thermistor(self, v):
            if 0 <= v <= 1:
                self.___bf03._setbits(
                    value=v,
                    size=1,
                    offset=0,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_dry_thermistor(self):
            return self.___bf03._getbits(
                size=1,
                offset=0,
                signed=False
            )

        err_dry_thermistor = property(
            __get_err_dry_thermistor,
            __set_err_dry_thermistor,
            None,
            """Bitfield err_dry_thermistor"""
        )

        def __set_err_dry_overheat(self, v):
            if 0 <= v <= 1:
                self.___bf03._setbits(
                    value=v,
                    size=1,
                    offset=1,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_dry_overheat(self):
            return self.___bf03._getbits(
                size=1,
                offset=1,
                signed=False
            )

        err_dry_overheat = property(
            __get_err_dry_overheat,
            __set_err_dry_overheat,
            None,
            """Bitfield err_dry_overheat"""
        )

        def __set_err_dry_heating(self, v):
            if 0 <= v <= 1:
                self.___bf03._setbits(
                    value=v,
                    size=1,
                    offset=2,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_dry_heating(self):
            return self.___bf03._getbits(
                size=1,
                offset=2,
                signed=False
            )

        err_dry_heating = property(
            __get_err_dry_heating,
            __set_err_dry_heating,
            None,
            """Bitfield err_dry_heating"""
        )

        def __set_err_dry_fan(self, v):
            if 0 <= v <= 1:
                self.___bf03._setbits(
                    value=v,
                    size=1,
                    offset=3,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_dry_fan(self):
            return self.___bf03._getbits(
                size=1,
                offset=3,
                signed=False
            )

        err_dry_fan = property(
            __get_err_dry_fan,
            __set_err_dry_fan,
            None,
            """Bitfield err_dry_fan"""
        )

        def __set_err_rsrvd4(self, v):
            if 0 <= v <= 1:
                self.___bf03._setbits(
                    value=v,
                    size=1,
                    offset=4,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_rsrvd4(self):
            return self.___bf03._getbits(
                size=1,
                offset=4,
                signed=False
            )

        err_rsrvd4 = property(
            __get_err_rsrvd4,
            __set_err_rsrvd4,
            None,
            """Bitfield err_rsrvd4"""
        )

        def __set_err_rsrvd5(self, v):
            if 0 <= v <= 1:
                self.___bf03._setbits(
                    value=v,
                    size=1,
                    offset=5,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_rsrvd5(self):
            return self.___bf03._getbits(
                size=1,
                offset=5,
                signed=False
            )

        err_rsrvd5 = property(
            __get_err_rsrvd5,
            __set_err_rsrvd5,
            None,
            """Bitfield err_rsrvd5"""
        )

        def __set_err_rsrvd6(self, v):
            if 0 <= v <= 1:
                self.___bf03._setbits(
                    value=v,
                    size=1,
                    offset=6,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_rsrvd6(self):
            return self.___bf03._getbits(
                size=1,
                offset=6,
                signed=False
            )

        err_rsrvd6 = property(
            __get_err_rsrvd6,
            __set_err_rsrvd6,
            None,
            """Bitfield err_rsrvd6"""
        )

        def __set_err_rsrvd7(self, v):
            if 0 <= v <= 1:
                self.___bf03._setbits(
                    value=v,
                    size=1,
                    offset=7,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_rsrvd7(self):
            return self.___bf03._getbits(
                size=1,
                offset=7,
                signed=False
            )

        err_rsrvd7 = property(
            __get_err_rsrvd7,
            __set_err_rsrvd7,
            None,
            """Bitfield err_rsrvd7"""
        )

        def __set_err_rsrvd0_7(self, v):
            if 0 <= v <= 1:
                self.___bf04._setbits(
                    value=v,
                    size=8,
                    offset=0,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_err_rsrvd0_7(self):
            return self.___bf04._getbits(
                size=8,
                offset=0,
                signed=False
            )

        err_rsrvd0_7 = property(
            __get_err_rsrvd0_7,
            __set_err_rsrvd0_7,
            None,
            """Bitfield err_rsrvd0_7"""
        )


        def __set_manuf_code(self, v):
            self.__manuf_code._value = v

        manuf_code = property(
            lambda self: self.__manuf_code._value,
            __set_manuf_code,
            None,
            """."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_alarm_reset(v.__alarm_reset)
            self.__set_war_water_supply(v.__war_water_supply)
            self.__set_war_drain_slow(v.__war_drain_slow)
            self.__set_war_door_open(v.__war_door_open)
            self.__set_war_load_unbalanced(v.__war_load_unbalanced)
            self.__set_war_filter_cleaning(v.__war_filter_cleaning)
            self.__set_war_hoses_reversed(v.__war_hoses_reversed)
            self.__set_war_voltage_low(v.__war_voltage_low)
            self.__set_war_power_failure(v.__war_power_failure)
            self.__set_war_drain_open(v.__war_drain_open)
            self.__set_war_execute_fail(v.__war_execute_fail)
            self.__set_war_door_locked(v.__war_door_locked)
            self.__set_war_service(v.__war_service)
            self.__set_rsrvd5(v.__rsrvd5)
            self.__set_rsrvd6(v.__rsrvd6)
            self.__set_rsrvd7(v.__rsrvd7)
            self.__set_err_motor_stall(v.__err_motor_stall)
            self.__set_err_water_temp(v.__err_water_temp)
            self.__set_err_pressure(v.__err_pressure)
            self.__set_err_overflow(v.__err_overflow)
            self.__set_err_water_heat(v.__err_water_heat)
            self.__set_err_water_leak(v.__err_water_leak)
            self.__set_err_motor_speed(v.__err_motor_speed)
            self.__set_err_wash_thermistor(v.__err_wash_thermistor)
            self.__set_err_dry_thermistor(v.__err_dry_thermistor)
            self.__set_err_dry_overheat(v.__err_dry_overheat)
            self.__set_err_dry_heating(v.__err_dry_heating)
            self.__set_err_dry_fan(v.__err_dry_fan)
            self.__set_err_rsrvd4(v.__err_rsrvd4)
            self.__set_err_rsrvd5(v.__err_rsrvd5)
            self.__set_err_rsrvd6(v.__err_rsrvd6)
            self.__set_err_rsrvd7(v.__err_rsrvd7)
            self.__set_err_rsrvd0_7(v.__err_rsrvd0_7)
            self.__set_manuf_code(v.__manuf_code)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 6

    def __init__(self):
        super().__init__(
            key=187,
            scope=0
        )

        self.__alarm = SNVT_clothes_w_a.alarmType(
        )
        self._register(('alarm', self.__alarm))
        self._definition = standard.add(self)


    def __set_alarm(self, v):
        self.__alarm._value = v

    alarm = property(
        lambda self: self.__alarm._value,
        __set_alarm,
        None,
        """."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_alarm(v.__alarm)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = SNVT_clothes_w_a()
    pass
