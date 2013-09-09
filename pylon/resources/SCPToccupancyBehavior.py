"""SCPToccupancyBehavior standard property type, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.occup_t import occup_t


class SCPToccupancyBehavior(base.Structure):
    """SCPToccupancyBehavior standard property type.  Occupancy behavior.
    Specifies mapping of scheduled occupancy values to primary occupancy
    states based on local occupancy inputs."""

    def __init__(self):
        super().__init__(
            key=372,
            scope=0
        )

        self.__ob_nul_value = occup_t(
        )
        self._register(('ob_nul_value', self.__ob_nul_value))

        self.__ob_occupied_value = occup_t(
        )
        self._register(('ob_occupied_value', self.__ob_occupied_value))

        self.__ob_unoccupied_value = occup_t(
        )
        self._register(('ob_unoccupied_value', self.__ob_unoccupied_value))

        self.__ob_bypass_value = occup_t(
        )
        self._register(('ob_bypass_value', self.__ob_bypass_value))

        self.__ob_standby_value = occup_t(
        )
        self._register(('ob_standby_value', self.__ob_standby_value))
        self._default_bytes = b'\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 372
        self._definition = standard.add(self)

    def __set_ob_nul_value(self, v):
        self.__ob_nul_value._value = v

    ob_nul_value = property(
        lambda self: self.__ob_nul_value._value,
        __set_ob_nul_value,
        None,
        """Invalid output value.  Primary occupancy value when the scheduled
        value is invalid (ob_nul) and a local occupancy condition is
        detected."""
    )

    def __set_ob_occupied_value(self, v):
        self.__ob_occupied_value._value = v

    ob_occupied_value = property(
        lambda self: self.__ob_occupied_value._value,
        __set_ob_occupied_value,
        None,
        """Occupied output value.  Primary occupancy value when the scheduled
        value is occupied (ob_occupied) and a local occupancy condition is
        detected."""
    )

    def __set_ob_unoccupied_value(self, v):
        self.__ob_unoccupied_value._value = v

    ob_unoccupied_value = property(
        lambda self: self.__ob_unoccupied_value._value,
        __set_ob_unoccupied_value,
        None,
        """Unoccupied output value.  Primary occupancy value when the
        scheduled value is unoccupied (ob_unoccupied) and a local occupancy
        condition is detected."""
    )

    def __set_ob_bypass_value(self, v):
        self.__ob_bypass_value._value = v

    ob_bypass_value = property(
        lambda self: self.__ob_bypass_value._value,
        __set_ob_bypass_value,
        None,
        """Bypass output value.  Primary occupancy value when the scheduled
        value is bypass (ob_bypass) and a local occupancy condition is
        detected."""
    )

    def __set_ob_standby_value(self, v):
        self.__ob_standby_value._value = v

    ob_standby_value = property(
        lambda self: self.__ob_standby_value._value,
        __set_ob_standby_value,
        None,
        """Standby output value.  Primary occupancy value when the scheduled
        value is standby (ob_standby) and a local occupancy condition is
        detected."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_ob_nul_value(v.__ob_nul_value)
        self.__set_ob_occupied_value(v.__ob_occupied_value)
        self.__set_ob_unoccupied_value(v.__ob_unoccupied_value)
        self.__set_ob_bypass_value(v.__ob_bypass_value)
        self.__set_ob_standby_value(v.__ob_standby_value)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 5


if __name__ == '__main__':
    # unit test code.
    item = SCPToccupancyBehavior()
    pass
