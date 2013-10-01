"""dev_fault standard datapoint type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0.  """


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
import pylon.resources.enumerations.device_select_t


class dev_fault(pylon.resources.base.Structure):
    """dev_fault standard datapoint type.  Device fault states.  Fault
    information for the device."""

    class dev_typeType(pylon.resources.base.Union):

        class pump_ctrlType(pylon.resources.base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
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
            def __set_sf_voltage_low(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_voltage_low(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            sf_voltage_low = property(
                __get_sf_voltage_low,
                __set_sf_voltage_low,
                None,
                """Supply fault - low voltage.  Supply voltage is too low.
                (boolean)"""
            )

            def __set_sf_voltage_high(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=1
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_voltage_high(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            sf_voltage_high = property(
                __get_sf_voltage_high,
                __set_sf_voltage_high,
                None,
                """Supply fault - high voltage.  Supply voltage is too high.
                (boolean)"""
            )

            def __set_sf_phase(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=2
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_phase(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            sf_phase = property(
                __get_sf_phase,
                __set_sf_phase,
                None,
                """Supply fault - power phase.  Supply power is missing
                phase.  (boolean)"""
            )

            def __set_sf_no_fluid(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=3
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_no_fluid(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            sf_no_fluid = property(
                __get_sf_no_fluid,
                __set_sf_no_fluid,
                None,
                """Supply fault - no fluid.  There is no fluid in the pump.
                (boolean)"""
            )

            def __set_sf_press_low(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_press_low(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=4,
                    signed=False
                )

            sf_press_low = property(
                __get_sf_press_low,
                __set_sf_press_low,
                None,
                """Supply fault - low pressure.  System pressure is too low.
                (boolean)"""
            )

            def __set_sf_press_high(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=5
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_press_high(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=5,
                    signed=False
                )

            sf_press_high = property(
                __get_sf_press_high,
                __set_sf_press_high,
                None,
                """Supply fault - high pressure.  System pressure is too
                high.  (boolean)"""
            )

            def __set_sf_general_fault(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=6
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_general_fault(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=6,
                    signed=False
                )

            sf_general_fault = property(
                __get_sf_general_fault,
                __set_sf_general_fault,
                None,
                """Bitfield sf_general_fault"""
            )

            def __set_sf_reserved1_7(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=7
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_reserved1_7(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=7,
                    signed=False
                )

            sf_reserved1_7 = property(
                __get_sf_reserved1_7,
                __set_sf_reserved1_7,
                None,
                """Bitfield sf_reserved1_7"""
            )

            def __set_df_motor_temp(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_motor_temp(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            df_motor_temp = property(
                __get_df_motor_temp,
                __set_df_motor_temp,
                None,
                """Device fault - motor temperature.  Motor temperature is
                too high.  (boolean)"""
            )

            def __set_df_motor_failure(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=1
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_motor_failure(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            df_motor_failure = property(
                __get_df_motor_failure,
                __set_df_motor_failure,
                None,
                """Device fault - motor fatal failure.  Motor has encountered
                a fatal failure.  (boolean)"""
            )

            def __set_df_pump_blocked(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=2
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_pump_blocked(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            df_pump_blocked = property(
                __get_df_pump_blocked,
                __set_df_pump_blocked,
                None,
                """Device fault - pump blocked.  Pump is presently blocked.
                (boolean)"""
            )

            def __set_df_elect_temp(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=3
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_elect_temp(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            df_elect_temp = property(
                __get_df_elect_temp,
                __set_df_elect_temp,
                None,
                """Device fault - electronics temperature.  Temperature of
                the electronic circuitry is too high.  (boolean)"""
            )

            def __set_df_elect_failure_nf(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_elect_failure_nf(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=4,
                    signed=False
                )

            df_elect_failure_nf = property(
                __get_df_elect_failure_nf,
                __set_df_elect_failure_nf,
                None,
                """Device fault - electronics failure.  Electronic circuitry
                has encountered a non-fatal failure.  (boolean)"""
            )

            def __set_df_elect_failure(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=5
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_elect_failure(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=5,
                    signed=False
                )

            df_elect_failure = property(
                __get_df_elect_failure,
                __set_df_elect_failure,
                None,
                """Device fault - electronics fatal failure.  Electronic
                circuitry has encountered a fatal failure.  (boolean)"""
            )

            def __set_df_sensor_failure(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=6
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_sensor_failure(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=6,
                    signed=False
                )

            df_sensor_failure = property(
                __get_df_sensor_failure,
                __set_df_sensor_failure,
                None,
                """Device fault - sensor failure.  Sensor has failed on the
                device.  (boolean)"""
            )

            def __set_df_general_fault(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=7
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_general_fault(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=7,
                    signed=False
                )

            df_general_fault = property(
                __get_df_general_fault,
                __set_df_general_fault,
                None,
                """Bitfield df_general_fault"""
            )

            def __set_reserved3_0_7(self, v):
                if 0 <= v <= 255:
                    self.___bf02._setbits(
                        value=v,
                        size=8,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..255')

            def __get_reserved3_0_7(self):
                return self.___bf02._getbits(
                    size=8,
                    offset=0,
                    signed=False
                )

            reserved3_0_7 = property(
                __get_reserved3_0_7,
                __set_reserved3_0_7,
                None,
                """Bitfield reserved3_0_7"""
            )


            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.___bf02._value = v.___bf02._value
                self.___bf01._value = v.___bf01._value
                self.___bf00._value = v.___bf00._value

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        class valve_posType(pylon.resources.base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
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
            def __set_df_valve_blocked(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_valve_blocked(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            df_valve_blocked = property(
                __get_df_valve_blocked,
                __set_df_valve_blocked,
                None,
                """Device fault - valve blocked.  The valve is presently
                blocked."""
            )

            def __set_df_blocked_direction_open(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=1
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_blocked_direction_open(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            df_blocked_direction_open = property(
                __get_df_blocked_direction_open,
                __set_df_blocked_direction_open,
                None,
                """Device fault - blocked direction open.  The device is
                blocked while attempting to open."""
            )

            def __set_df_blocked_direction_close(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=2
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_blocked_direction_close(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            df_blocked_direction_close = property(
                __get_df_blocked_direction_close,
                __set_df_blocked_direction_close,
                None,
                """Device fault - blocked direction close.  The device is
                blocked while attempting to close."""
            )

            def __set_df_position_error(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=3
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_position_error(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            df_position_error = property(
                __get_df_position_error,
                __set_df_position_error,
                None,
                """Device fault - position error.  The valve position is not
                correct."""
            )

            def __set_df_stroke_out_of_range(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_stroke_out_of_range(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=4,
                    signed=False
                )

            df_stroke_out_of_range = property(
                __get_df_stroke_out_of_range,
                __set_df_stroke_out_of_range,
                None,
                """Device fault - stroke out of range.  The valve stroke is
                out of operating range."""
            )

            def __set_df_initialization(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=5
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_initialization(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=5,
                    signed=False
                )

            df_initialization = property(
                __get_df_initialization,
                __set_df_initialization,
                None,
                """Device fault - initialization error.  The was an error
                during initialization of the device."""
            )

            def __set_df_vibration_cavitation(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=6
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_vibration_cavitation(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=6,
                    signed=False
                )

            df_vibration_cavitation = property(
                __get_df_vibration_cavitation,
                __set_df_vibration_cavitation,
                None,
                """Device fault - vibration / cavitation.  There are
                excessive vibrations or cavitations detected."""
            )

            def __set_df_ed_too_high(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=7
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_df_ed_too_high(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=7,
                    signed=False
                )

            df_ed_too_high = property(
                __get_df_ed_too_high,
                __set_df_ed_too_high,
                None,
                """Device fault - ED too high.  The ED is too high."""
            )

            def __set_reserved1_0_2(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=3,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved1_0_2(self):
                return self.___bf01._getbits(
                    size=3,
                    offset=0,
                    signed=False
                )

            reserved1_0_2 = property(
                __get_reserved1_0_2,
                __set_reserved1_0_2,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_ee_oscillating(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=3
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_ee_oscillating(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            ee_oscillating = property(
                __get_ee_oscillating,
                __set_ee_oscillating,
                None,
                """Engineering error - oscillating.  There is an oscillating
                error."""
            )

            def __set_ee_valve_too_large(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_ee_valve_too_large(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=4,
                    signed=False
                )

            ee_valve_too_large = property(
                __get_ee_valve_too_large,
                __set_ee_valve_too_large,
                None,
                """Engineering error - valve too big.  The valve size is too
                large."""
            )

            def __set_ee_valve_too_small(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=5
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_ee_valve_too_small(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=5,
                    signed=False
                )

            ee_valve_too_small = property(
                __get_ee_valve_too_small,
                __set_ee_valve_too_small,
                None,
                """Engineering error - valve too small.  The valve size is
                too small."""
            )

            def __set_reserved2_6_7(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=2,
                        offset=6
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved2_6_7(self):
                return self.___bf01._getbits(
                    size=2,
                    offset=6,
                    signed=False
                )

            reserved2_6_7 = property(
                __get_reserved2_6_7,
                __set_reserved2_6_7,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_reserved3_0_7(self, v):
                if 0 <= v <= 1:
                    self.___bf02._setbits(
                        value=v,
                        size=1,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved3_0_7(self):
                return self.___bf02._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            reserved3_0_7 = property(
                __get_reserved3_0_7,
                __set_reserved3_0_7,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_sf_voltage_out_of_range(self, v):
                if 0 <= v <= 1:
                    self.___bf02._setbits(
                        value=v,
                        size=1,
                        offset=1
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_voltage_out_of_range(self):
                return self.___bf02._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            sf_voltage_out_of_range = property(
                __get_sf_voltage_out_of_range,
                __set_sf_voltage_out_of_range,
                None,
                """Supply fault - voltage out of range.  The voltage is out
                of the specified acceptable range."""
            )

            def __set_sf_electronic_high_temp(self, v):
                if 0 <= v <= 1:
                    self.___bf02._setbits(
                        value=v,
                        size=1,
                        offset=2
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_electronic_high_temp(self):
                return self.___bf02._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            sf_electronic_high_temp = property(
                __get_sf_electronic_high_temp,
                __set_sf_electronic_high_temp,
                None,
                """Supply fault - electronics temperature.  The temperature
                of the electronics is too high."""
            )

            def __set_sf_frictional_resistance(self, v):
                if 0 <= v <= 1:
                    self.___bf02._setbits(
                        value=v,
                        size=1,
                        offset=3
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sf_frictional_resistance(self):
                return self.___bf02._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            sf_frictional_resistance = property(
                __get_sf_frictional_resistance,
                __set_sf_frictional_resistance,
                None,
                """Supply fault - frictional resistance.  Resistance due to
                friction is detected."""
            )

            def __set_reserved4_4_6(self, v):
                if 0 <= v <= 1:
                    self.___bf02._setbits(
                        value=v,
                        size=3,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved4_4_6(self):
                return self.___bf02._getbits(
                    size=3,
                    offset=4,
                    signed=False
                )

            reserved4_4_6 = property(
                __get_reserved4_4_6,
                __set_reserved4_4_6,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_general_fault(self, v):
                if 0 <= v <= 1:
                    self.___bf02._setbits(
                        value=v,
                        size=1,
                        offset=7
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_general_fault(self):
                return self.___bf02._getbits(
                    size=1,
                    offset=7,
                    signed=False
                )

            general_fault = property(
                __get_general_fault,
                __set_general_fault,
                None,
                """General Fault.  A General Fault has occured.  Please
                consult the documentation or contact the valve-controller
                manufacturer."""
            )


            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.___bf02._value = v.___bf02._value
                self.___bf01._value = v.___bf01._value
                self.___bf00._value = v.___bf00._value

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__pump_ctrl = dev_fault.dev_typeType.pump_ctrlType(
            )
            self._register(('pump_ctrl', self.__pump_ctrl))

            self.__valve_pos = dev_fault.dev_typeType.valve_posType(
            )
            self._register(('valve_pos', self.__valve_pos))

        def __set_pump_ctrl(self, v):
            self.__pump_ctrl._value = v

        pump_ctrl = property(
            lambda self: self.__pump_ctrl._value,
            __set_pump_ctrl,
            None,
            """Pump controller device fault information."""
        )

        def __set_valve_pos(self, v):
            self.__valve_pos._value = v

        valve_pos = property(
            lambda self: self.__valve_pos._value,
            __set_valve_pos,
            None,
            """Valve positioner device fault information."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_pump_ctrl(v.__pump_ctrl)
            self.__set_valve_pos(v.__valve_pos)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=174,
            scope=0
        )

        self.__device_select = pylon.resources.enumerations.device_select_t.device_select_t(
        )
        self._register(('device_select', self.__device_select))

        self.__dev_type = dev_fault.dev_typeType(
        )
        self._register(('dev_type', self.__dev_type))
        self._original_name = 'SNVT_dev_fault'
        self._definition = standard.add(self)


    def __set_device_select(self, v):
        self.__device_select._value = v

    device_select = property(
        lambda self: self.__device_select._value,
        __set_device_select,
        None,
        """Device selection.  Determines the interpretation of the
        network-variable content.  (device selection names.)."""
    )

    def __set_dev_type(self, v):
        self.__dev_type._value = v

    dev_type = property(
        lambda self: self.__dev_type._value,
        __set_dev_type,
        None,
        """Union of device fault structures for various devices."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_device_select(v.__device_select)
        self.__set_dev_type(v.__dev_type)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = dev_fault()
    pass
