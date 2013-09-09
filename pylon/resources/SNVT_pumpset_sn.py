"""SNVT_pumpset_sn standard datapoint type, originally defined in resource
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
from pylon.resources.SNVT_flow_mil import SNVT_flow_mil
from pylon.resources.SNVT_temp import SNVT_temp
from pylon.resources.SNVT_press import SNVT_press
from pylon.resources.SNVT_press_f import SNVT_press_f
from pylon.resources.SNVT_volt import SNVT_volt
from pylon.resources.boolean_t import boolean_t


class SNVT_pumpset_sn(base.Structure):
    """SNVT_pumpset_sn standard datapoint type.  Pumpset sensor.  (dilution,
    exhaust, pressure, vacuum, ...)."""

    def __init__(self):
        super().__init__(
            key=158,
            scope=0
        )

        self.__total_dilution_flow = SNVT_flow_mil(
        )
        self._register(('total_dilution_flow', self.__total_dilution_flow))

        self.__exhaust_temperature = SNVT_temp(
        )
        self._register(('exhaust_temperature', self.__exhaust_temperature))

        self.__exhaust_pressure = SNVT_press(
        )
        self._register(('exhaust_pressure', self.__exhaust_pressure))

        self.__shaft_seal_purge_pressure = SNVT_press(
        )
        self._register(('shaft_seal_purge_pressure', self.__shaft_seal_purge_pressure))

        self.__inlet_vacuum = SNVT_press_f(
        )
        self._register(('inlet_vacuum', self.__inlet_vacuum))

        self.__supply_voltage = SNVT_volt(
        )
        self._register(('supply_voltage', self.__supply_voltage))

        self.__coolant_flow = SNVT_flow_mil(
        )
        self._register(('coolant_flow', self.__coolant_flow))

        self.__coolant_flow_low = boolean_t(
        )
        self._register(('coolant_flow_low', self.__coolant_flow_low))

        self.__dilution_active = boolean_t(
        )
        self._register(('dilution_active', self.__dilution_active))

        self.__ballast_dilution_active = boolean_t(
        )
        self._register(('ballast_dilution_active', self.__ballast_dilution_active))

        self.__inlet_purge_dilution_active = boolean_t(
        )
        self._register(('inlet_purge_dilution_active', self.__inlet_purge_dilution_active))

        self.__exhaust_dilution_active = boolean_t(
        )
        self._register(('exhaust_dilution_active', self.__exhaust_dilution_active))

        self.__dilution_flow_out_of_range = boolean_t(
        )
        self._register(('dilution_flow_out_of_range', self.__dilution_flow_out_of_range))

        self.__power_supply_on = boolean_t(
        )
        self._register(('power_supply_on', self.__power_supply_on))
        self._definition = standard.add(self)


    def __set_total_dilution_flow(self, v):
        self.__total_dilution_flow._value = v

    total_dilution_flow = property(
        lambda self: self.__total_dilution_flow._value,
        __set_total_dilution_flow,
        None,
        """Dilution gas flow."""
    )

    def __set_exhaust_temperature(self, v):
        self.__exhaust_temperature._value = v

    exhaust_temperature = property(
        lambda self: self.__exhaust_temperature._value,
        __set_exhaust_temperature,
        None,
        """Exhaust line external temperature."""
    )

    def __set_exhaust_pressure(self, v):
        self.__exhaust_pressure._value = v

    exhaust_pressure = property(
        lambda self: self.__exhaust_pressure._value,
        __set_exhaust_pressure,
        None,
        """Exhaust line pressure."""
    )

    def __set_shaft_seal_purge_pressure(self, v):
        self.__shaft_seal_purge_pressure._value = v

    shaft_seal_purge_pressure = property(
        lambda self: self.__shaft_seal_purge_pressure._value,
        __set_shaft_seal_purge_pressure,
        None,
        """Shaft seal purge pressure."""
    )

    def __set_inlet_vacuum(self, v):
        self.__inlet_vacuum._value = v

    inlet_vacuum = property(
        lambda self: self.__inlet_vacuum._value,
        __set_inlet_vacuum,
        None,
        """Process gas inlet pressure."""
    )

    def __set_supply_voltage(self, v):
        self.__supply_voltage._value = v

    supply_voltage = property(
        lambda self: self.__supply_voltage._value,
        __set_supply_voltage,
        None,
        """Pumpset power supply voltage."""
    )

    def __set_coolant_flow(self, v):
        self.__coolant_flow._value = v

    coolant_flow = property(
        lambda self: self.__coolant_flow._value,
        __set_coolant_flow,
        None,
        """Total coolant flow."""
    )

    def __set_coolant_flow_low(self, v):
        self.__coolant_flow_low._value = v

    coolant_flow_low = property(
        lambda self: self.__coolant_flow_low._value,
        __set_coolant_flow_low,
        None,
        """Coolant flow too low.  (boolean)."""
    )

    def __set_dilution_active(self, v):
        self.__dilution_active._value = v

    dilution_active = property(
        lambda self: self.__dilution_active._value,
        __set_dilution_active,
        None,
        """Dilution gas being used.  (boolean)."""
    )

    def __set_ballast_dilution_active(self, v):
        self.__ballast_dilution_active._value = v

    ballast_dilution_active = property(
        lambda self: self.__ballast_dilution_active._value,
        __set_ballast_dilution_active,
        None,
        """Dilution gas being used as ballast.  (boolean)."""
    )

    def __set_inlet_purge_dilution_active(self, v):
        self.__inlet_purge_dilution_active._value = v

    inlet_purge_dilution_active = property(
        lambda self: self.__inlet_purge_dilution_active._value,
        __set_inlet_purge_dilution_active,
        None,
        """Dilution gas being used to purge process gas.  (boolean)."""
    )

    def __set_exhaust_dilution_active(self, v):
        self.__exhaust_dilution_active._value = v

    exhaust_dilution_active = property(
        lambda self: self.__exhaust_dilution_active._value,
        __set_exhaust_dilution_active,
        None,
        """Dilution gas being used to dilute exhaust.  (boolean)."""
    )

    def __set_dilution_flow_out_of_range(self, v):
        self.__dilution_flow_out_of_range._value = v

    dilution_flow_out_of_range = property(
        lambda self: self.__dilution_flow_out_of_range._value,
        __set_dilution_flow_out_of_range,
        None,
        """Dilution gas flow outside normal range.  (boolean)."""
    )

    def __set_power_supply_on(self, v):
        self.__power_supply_on._value = v

    power_supply_on = property(
        lambda self: self.__power_supply_on._value,
        __set_power_supply_on,
        None,
        """Main power supply is on.  (boolean)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_total_dilution_flow(v.__total_dilution_flow)
        self.__set_exhaust_temperature(v.__exhaust_temperature)
        self.__set_exhaust_pressure(v.__exhaust_pressure)
        self.__set_shaft_seal_purge_pressure(v.__shaft_seal_purge_pressure)
        self.__set_inlet_vacuum(v.__inlet_vacuum)
        self.__set_supply_voltage(v.__supply_voltage)
        self.__set_coolant_flow(v.__coolant_flow)
        self.__set_coolant_flow_low(v.__coolant_flow_low)
        self.__set_dilution_active(v.__dilution_active)
        self.__set_ballast_dilution_active(v.__ballast_dilution_active)
        self.__set_inlet_purge_dilution_active(v.__inlet_purge_dilution_active)
        self.__set_exhaust_dilution_active(v.__exhaust_dilution_active)
        self.__set_dilution_flow_out_of_range(v.__dilution_flow_out_of_range)
        self.__set_power_supply_on(v.__power_supply_on)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 23


if __name__ == '__main__':
    # unit test code.
    item = SNVT_pumpset_sn()
    pass
