"""SNVT_hvac_status standard datapoint type, originally defined in resource
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
from pylon.resources.hvac_t import hvac_t


class SNVT_hvac_status(base.Structure):
    """SNVT_hvac_status standard datapoint type.  HVAC status.  (mode, 5
    percents, flag.)."""

    def __init__(self):
        super().__init__(
            key=112,
            scope=0
        )

        self.__mode = hvac_t(
        )
        self._register(('mode', self.__mode))

        self.__heat_output_primary = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.005, 0),
            invalid=163.835,
            minimum=-163.84,
            maximum=163.835
        )
        self._register(('heat_output_primary', self.__heat_output_primary))

        self.__heat_output_secondary = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.005, 0),
            invalid=163.835,
            minimum=-163.84,
            maximum=163.835
        )
        self._register(('heat_output_secondary', self.__heat_output_secondary))

        self.__cool_output = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.005, 0),
            invalid=163.835,
            minimum=-163.84,
            maximum=163.835
        )
        self._register(('cool_output', self.__cool_output))

        self.__econ_output = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.005, 0),
            invalid=163.835,
            minimum=-163.84,
            maximum=163.835
        )
        self._register(('econ_output', self.__econ_output))

        self.__fan_output = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.005, 0),
            invalid=163.835,
            minimum=-163.84,
            maximum=163.835
        )
        self._register(('fan_output', self.__fan_output))

        self.__in_alarm = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('in_alarm', self.__in_alarm))
        self._definition = standard.add(self)


    def __set_mode(self, v):
        self.__mode._value = v

    mode = property(
        lambda self: self.__mode._value,
        __set_mode,
        None,
        """HVAC status mode.  (HVAC mode names.)."""
    )

    def __set_heat_output_primary(self, v):
        self.__heat_output_primary._value = v

    heat_output_primary = property(
        lambda self: self.__heat_output_primary._value,
        __set_heat_output_primary,
        None,
        """Primary heat output.  (% of full scale.)."""
    )

    def __set_heat_output_secondary(self, v):
        self.__heat_output_secondary._value = v

    heat_output_secondary = property(
        lambda self: self.__heat_output_secondary._value,
        __set_heat_output_secondary,
        None,
        """Secondary heat output.  (% of full scale.)."""
    )

    def __set_cool_output(self, v):
        self.__cool_output._value = v

    cool_output = property(
        lambda self: self.__cool_output._value,
        __set_cool_output,
        None,
        """Cooling output.  (% of full scale.)."""
    )

    def __set_econ_output(self, v):
        self.__econ_output._value = v

    econ_output = property(
        lambda self: self.__econ_output._value,
        __set_econ_output,
        None,
        """Economizer output.  (% of full scale.)."""
    )

    def __set_fan_output(self, v):
        self.__fan_output._value = v

    fan_output = property(
        lambda self: self.__fan_output._value,
        __set_fan_output,
        None,
        """Fan output.  (% of full scale.)."""
    )

    def __set_in_alarm(self, v):
        self.__in_alarm._value = v

    in_alarm = property(
        lambda self: self.__in_alarm._value,
        __set_in_alarm,
        None,
        """In alarm state.  Non-zero value represents a manufacturer-specific
        alarm state.  (alarm value.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_mode(v.__mode)
        self.__set_heat_output_primary(v.__heat_output_primary)
        self.__set_heat_output_secondary(v.__heat_output_secondary)
        self.__set_cool_output(v.__cool_output)
        self.__set_econ_output(v.__econ_output)
        self.__set_fan_output(v.__fan_output)
        self.__set_in_alarm(v.__in_alarm)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 12


if __name__ == '__main__':
    # unit test code.
    item = SNVT_hvac_status()
    pass
