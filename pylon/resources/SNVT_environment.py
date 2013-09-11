"""SNVT_environment standard datapoint type, originally defined in resource
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
from pylon.resources.SNVT_amp_ac_mil import SNVT_amp_ac_mil
from pylon.resources.SNVT_volt_ac import SNVT_volt_ac
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SNVT_power import SNVT_power
from pylon.resources.SNVT_pwr_fact import SNVT_pwr_fact
from pylon.resources.SNVT_time_hour_p import SNVT_time_hour_p
from pylon.resources.SNVT_elec_kwh_l import SNVT_elec_kwh_l


class SNVT_environment(base.Structure):
    """SNVT_environment standard datapoint type.  Environment."""

    def __init__(self):
        super().__init__(
            key=200,
            scope=0
        )

        self.__lampCurrent = SNVT_amp_ac_mil(
        )
        self._register(('lampCurrent', self.__lampCurrent))

        self.__lampVoltage = SNVT_volt_ac(
        )
        self._register(('lampVoltage', self.__lampVoltage))

        self.__supplyVoltage = SNVT_volt_ac(
        )
        self._register(('supplyVoltage', self.__supplyVoltage))

        self.__supplyCurrent = SNVT_amp_ac_mil(
        )
        self._register(('supplyCurrent', self.__supplyCurrent))

        self.__ballastTemp = SNVT_temp_p(
        )
        self._register(('ballastTemp', self.__ballastTemp))

        self.__power = SNVT_power(
        )
        self._register(('power', self.__power))

        self.__powerFactor = SNVT_pwr_fact(
        )
        self._register(('powerFactor', self.__powerFactor))

        self.__runHours = SNVT_time_hour_p(
        )
        self._register(('runHours', self.__runHours))

        self.__energy = SNVT_elec_kwh_l(
        )
        self._register(('energy', self.__energy))
        self._definition = standard.add(self)


    def __set_lampCurrent(self, v):
        self.__lampCurrent._value = v

    lampCurrent = property(
        lambda self: self.__lampCurrent._value,
        __set_lampCurrent,
        None,
        """Lamp current.  This is the current the lamp consumes.
        (milliAmperes)."""
    )

    def __set_lampVoltage(self, v):
        self.__lampVoltage._value = v

    lampVoltage = property(
        lambda self: self.__lampVoltage._value,
        __set_lampVoltage,
        None,
        """Lamp Voltage.  This is the lamp voltage.  (Volts)."""
    )

    def __set_supplyVoltage(self, v):
        self.__supplyVoltage._value = v

    supplyVoltage = property(
        lambda self: self.__supplyVoltage._value,
        __set_supplyVoltage,
        None,
        """Supply Voltage.  This is the luminaire supply voltage.
        (Volts)."""
    )

    def __set_supplyCurrent(self, v):
        self.__supplyCurrent._value = v

    supplyCurrent = property(
        lambda self: self.__supplyCurrent._value,
        __set_supplyCurrent,
        None,
        """Supply Current.  This is the luminaire supply current.
        (milliAmperes)."""
    )

    def __set_ballastTemp(self, v):
        self.__ballastTemp._value = v

    ballastTemp = property(
        lambda self: self.__ballastTemp._value,
        __set_ballastTemp,
        None,
        """Ballast temperature.  This is the temperature at the ballast.
        (degrees Celsius.)."""
    )

    def __set_power(self, v):
        self.__power._value = v

    power = property(
        lambda self: self.__power._value,
        __set_power,
        None,
        """Power The value shows the at this moment consumed power of the
        ballast and the luminaire.  (Watts)."""
    )

    def __set_powerFactor(self, v):
        self.__powerFactor._value = v

    powerFactor = property(
        lambda self: self.__powerFactor._value,
        __set_powerFactor,
        None,
        """Power factor.  This is the luminaire power-factor."""
    )

    def __set_runHours(self, v):
        self.__runHours._value = v

    runHours = property(
        lambda self: self.__runHours._value,
        __set_runHours,
        None,
        """Run Hours.  This are the run hours since the last maintenance.
        (hours)."""
    )

    def __set_energy(self, v):
        self.__energy._value = v

    energy = property(
        lambda self: self.__energy._value,
        __set_energy,
        None,
        """Energy This is the energy the luminair has consumt since the last
        maintenance.  (kiloWatt-hours)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_lampCurrent(v.__lampCurrent)
        self.__set_lampVoltage(v.__lampVoltage)
        self.__set_supplyVoltage(v.__supplyVoltage)
        self.__set_supplyCurrent(v.__supplyCurrent)
        self.__set_ballastTemp(v.__ballastTemp)
        self.__set_power(v.__power)
        self.__set_powerFactor(v.__powerFactor)
        self.__set_runHours(v.__runHours)
        self.__set_energy(v.__energy)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 22


if __name__ == '__main__':
    # unit test code.
    item = SNVT_environment()
    pass
