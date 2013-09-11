"""SNVT_pump_sensor standard datapoint type, originally defined in resource
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
from pylon.resources.SNVT_freq_hz import SNVT_freq_hz
from pylon.resources.SNVT_temp import SNVT_temp
from pylon.resources.boolean_t import boolean_t
from pylon.resources.SNVT_amp import SNVT_amp
from pylon.resources.SNVT_power_kilo import SNVT_power_kilo
from pylon.resources.unit_temp_t import unit_temp_t


class SNVT_pump_sensor(base.Structure):
    """SNVT_pump_sensor standard datapoint type.  Pump sensor.  (speed,
    temperature, status.)."""

    def __init__(self):
        super().__init__(
            key=159,
            scope=0
        )

        self.__rotational_speed = SNVT_freq_hz(
        )
        self._register(('rotational_speed', self.__rotational_speed))

        self.__body_temperature = SNVT_temp(
        )
        self._register(('body_temperature', self.__body_temperature))

        self.__motor_external_temperature = SNVT_temp(
        )
        self._register(('motor_external_temperature', self.__motor_external_temperature))

        self.__motor_internal_temperature = SNVT_temp(
        )
        self._register(('motor_internal_temperature', self.__motor_internal_temperature))

        self.__motor_overloaded = boolean_t(
        )
        self._register(('motor_overloaded', self.__motor_overloaded))

        self.__oil_level_low = boolean_t(
        )
        self._register(('oil_level_low', self.__oil_level_low))

        self.__phase_imbalance_detected = boolean_t(
        )
        self._register(('phase_imbalance_detected', self.__phase_imbalance_detected))

        self.__current_usage = SNVT_amp(
        )
        self._register(('current_usage', self.__current_usage))

        self.__power_usage = SNVT_power_kilo(
        )
        self._register(('power_usage', self.__power_usage))

        self.__temperature_control = unit_temp_t(
        )
        self._register(('temperature_control', self.__temperature_control))

        self.__electromagnetic_brake_active = boolean_t(
        )
        self._register(('electromagnetic_brake_active', self.__electromagnetic_brake_active))

        self.__friction_brake_active = boolean_t(
        )
        self._register(('friction_brake_active', self.__friction_brake_active))

        self.__gas_brake_active = boolean_t(
        )
        self._register(('gas_brake_active', self.__gas_brake_active))
        self._definition = standard.add(self)


    def __set_rotational_speed(self, v):
        self.__rotational_speed._value = v

    rotational_speed = property(
        lambda self: self.__rotational_speed._value,
        __set_rotational_speed,
        None,
        """Rotational speed."""
    )

    def __set_body_temperature(self, v):
        self.__body_temperature._value = v

    body_temperature = property(
        lambda self: self.__body_temperature._value,
        __set_body_temperature,
        None,
        """Body temperature."""
    )

    def __set_motor_external_temperature(self, v):
        self.__motor_external_temperature._value = v

    motor_external_temperature = property(
        lambda self: self.__motor_external_temperature._value,
        __set_motor_external_temperature,
        None,
        """Motor external temp."""
    )

    def __set_motor_internal_temperature(self, v):
        self.__motor_internal_temperature._value = v

    motor_internal_temperature = property(
        lambda self: self.__motor_internal_temperature._value,
        __set_motor_internal_temperature,
        None,
        """Motor internal temp."""
    )

    def __set_motor_overloaded(self, v):
        self.__motor_overloaded._value = v

    motor_overloaded = property(
        lambda self: self.__motor_overloaded._value,
        __set_motor_overloaded,
        None,
        """Motor overloaded.  (boolean)."""
    )

    def __set_oil_level_low(self, v):
        self.__oil_level_low._value = v

    oil_level_low = property(
        lambda self: self.__oil_level_low._value,
        __set_oil_level_low,
        None,
        """Oil level low.  (boolean)."""
    )

    def __set_phase_imbalance_detected(self, v):
        self.__phase_imbalance_detected._value = v

    phase_imbalance_detected = property(
        lambda self: self.__phase_imbalance_detected._value,
        __set_phase_imbalance_detected,
        None,
        """Phase imbalance.  (boolean)."""
    )

    def __set_current_usage(self, v):
        self.__current_usage._value = v

    current_usage = property(
        lambda self: self.__current_usage._value,
        __set_current_usage,
        None,
        """Current usage."""
    )

    def __set_power_usage(self, v):
        self.__power_usage._value = v

    power_usage = property(
        lambda self: self.__power_usage._value,
        __set_power_usage,
        None,
        """Power usage."""
    )

    def __set_temperature_control(self, v):
        self.__temperature_control._value = v

    temperature_control = property(
        lambda self: self.__temperature_control._value,
        __set_temperature_control,
        None,
        """Pump body temp control status.  (temperature control status
        names.)."""
    )

    def __set_electromagnetic_brake_active(self, v):
        self.__electromagnetic_brake_active._value = v

    electromagnetic_brake_active = property(
        lambda self: self.__electromagnetic_brake_active._value,
        __set_electromagnetic_brake_active,
        None,
        """Electromagnetic brake active.  (boolean)."""
    )

    def __set_friction_brake_active(self, v):
        self.__friction_brake_active._value = v

    friction_brake_active = property(
        lambda self: self.__friction_brake_active._value,
        __set_friction_brake_active,
        None,
        """Friction brake active.  (boolean)."""
    )

    def __set_gas_brake_active(self, v):
        self.__gas_brake_active._value = v

    gas_brake_active = property(
        lambda self: self.__gas_brake_active._value,
        __set_gas_brake_active,
        None,
        """Gas brake active.  (boolean)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_rotational_speed(v.__rotational_speed)
        self.__set_body_temperature(v.__body_temperature)
        self.__set_motor_external_temperature(v.__motor_external_temperature)
        self.__set_motor_internal_temperature(v.__motor_internal_temperature)
        self.__set_motor_overloaded(v.__motor_overloaded)
        self.__set_oil_level_low(v.__oil_level_low)
        self.__set_phase_imbalance_detected(v.__phase_imbalance_detected)
        self.__set_current_usage(v.__current_usage)
        self.__set_power_usage(v.__power_usage)
        self.__set_temperature_control(v.__temperature_control)
        self.__set_electromagnetic_brake_active(v.__electromagnetic_brake_active)
        self.__set_friction_brake_active(v.__friction_brake_active)
        self.__set_gas_brake_active(v.__gas_brake_active)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 19


if __name__ == '__main__':
    # unit test code.
    item = SNVT_pump_sensor()
    pass
