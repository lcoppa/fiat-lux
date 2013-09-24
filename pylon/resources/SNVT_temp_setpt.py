"""SNVT_temp_setpt standard datapoint type, originally defined in resource
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class SNVT_temp_setpt(base.Structure):
    """SNVT_temp_setpt standard datapoint type.  Temperature (6 temperature
    values.)."""

    def __init__(self):
        super().__init__(
            key=106,
            scope=0
        )

        self.__occupied_cool = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.01, 0),
            invalid=327.67,
            minimum=-273.17,
            maximum=327.67
        )
        self._register(('occupied_cool', self.__occupied_cool))

        self.__standby_cool = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.01, 0),
            invalid=327.67,
            minimum=-273.17,
            maximum=327.67
        )
        self._register(('standby_cool', self.__standby_cool))

        self.__unoccupied_cool = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.01, 0),
            invalid=327.67,
            minimum=-273.17,
            maximum=327.67
        )
        self._register(('unoccupied_cool', self.__unoccupied_cool))

        self.__occupied_heat = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.01, 0),
            invalid=327.67,
            minimum=-273.17,
            maximum=327.67
        )
        self._register(('occupied_heat', self.__occupied_heat))

        self.__standby_heat = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.01, 0),
            invalid=327.67,
            minimum=-273.17,
            maximum=327.67
        )
        self._register(('standby_heat', self.__standby_heat))

        self.__unoccupied_heat = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.01, 0),
            invalid=327.67,
            minimum=-273.17,
            maximum=327.67
        )
        self._register(('unoccupied_heat', self.__unoccupied_heat))
        self._definition = standard.add(self)


    def __set_occupied_cool(self, v):
        self.__occupied_cool._value = v

    occupied_cool = property(
        lambda self: self.__occupied_cool._value,
        __set_occupied_cool,
        None,
        """Occupied cooling setpoint.  (degrees Celsius.)."""
    )

    def __set_standby_cool(self, v):
        self.__standby_cool._value = v

    standby_cool = property(
        lambda self: self.__standby_cool._value,
        __set_standby_cool,
        None,
        """Standby cooling setpoint.  (degrees Celsius.)."""
    )

    def __set_unoccupied_cool(self, v):
        self.__unoccupied_cool._value = v

    unoccupied_cool = property(
        lambda self: self.__unoccupied_cool._value,
        __set_unoccupied_cool,
        None,
        """Unoccupied cooling setpoint.  (degrees Celsius.)."""
    )

    def __set_occupied_heat(self, v):
        self.__occupied_heat._value = v

    occupied_heat = property(
        lambda self: self.__occupied_heat._value,
        __set_occupied_heat,
        None,
        """Occupied heating setpoint.  (degrees Celsius.)."""
    )

    def __set_standby_heat(self, v):
        self.__standby_heat._value = v

    standby_heat = property(
        lambda self: self.__standby_heat._value,
        __set_standby_heat,
        None,
        """Standby heating setpoint.  (degrees Celsius.)."""
    )

    def __set_unoccupied_heat(self, v):
        self.__unoccupied_heat._value = v

    unoccupied_heat = property(
        lambda self: self.__unoccupied_heat._value,
        __set_unoccupied_heat,
        None,
        """Unoccupied heating setpoint.  (degrees Celsius.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_occupied_cool(v.__occupied_cool)
        self.__set_standby_cool(v.__standby_cool)
        self.__set_unoccupied_cool(v.__unoccupied_cool)
        self.__set_occupied_heat(v.__occupied_heat)
        self.__set_standby_heat(v.__standby_heat)
        self.__set_unoccupied_heat(v.__unoccupied_heat)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 12


if __name__ == '__main__':
    # unit test code.
    item = SNVT_temp_setpt()
    pass
