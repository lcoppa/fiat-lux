"""SCPToccupancyThresholds standard property type, originally defined in
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard


class SCPToccupancyThresholds(base.Structure):
    """SCPToccupancyThresholds standard property type.  Occupancy
    thresholds.  Specifies the minimum number of occupancy sensors that must
    report the same value to override a scheduled output value."""

    def __init__(self):
        super().__init__(
            key=380,
            scope=0
        )

        self.__occupied = base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=50
        )
        self._register(('occupied', self.__occupied))

        self.__standby_to_occupied = base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=50
        )
        self._register(('standby_to_occupied', self.__standby_to_occupied))

        self.__unoccupied_to_occupied = base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=50
        )
        self._register(('unoccupied_to_occupied', self.__unoccupied_to_occupied))
        self._default_bytes = b'\x00\x00\x00'
        self._property_scope, self._property_key = 0, 380
        self._definition = standard.add(self)

    def __set_occupied(self, v):
        self.__occupied._value = v

    occupied = property(
        lambda self: self.__occupied._value,
        __set_occupied,
        None,
        """Occupied threshold.  Number of occupancy sensors that must be
        reporting occupied to report an occupied output when the current
        schedule specifies an occupied state;  if the number of occupancy
        sensors reporting occupancy is below this value, the occupancy output
        is set to standby."""
    )

    def __set_standby_to_occupied(self, v):
        self.__standby_to_occupied._value = v

    standby_to_occupied = property(
        lambda self: self.__standby_to_occupied._value,
        __set_standby_to_occupied,
        None,
        """Standby to occupied override threshold.  Number of occupancy
        sensors that must be reporting occupied to report an occupied output
        when the current schedule specifies a standby state;  if the number
        of occupancy sensors reporting occupancy is below this value, the
        occupancy output is set to standby."""
    )

    def __set_unoccupied_to_occupied(self, v):
        self.__unoccupied_to_occupied._value = v

    unoccupied_to_occupied = property(
        lambda self: self.__unoccupied_to_occupied._value,
        __set_unoccupied_to_occupied,
        None,
        """Unoccupied to occupied override threshold.  Number of occupancy
        sensors that must be reporting occupied to report an occupied output
        when the current schedule specifies an unoccupied state;  if the
        number of occupancy sensors reporting occupancy is below this value,
        the occupancy output is set to standby."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_occupied(v.__occupied)
        self.__set_standby_to_occupied(v.__standby_to_occupied)
        self.__set_unoccupied_to_occupied(v.__unoccupied_to_occupied)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 3


if __name__ == '__main__':
    # unit test code.
    item = SCPToccupancyThresholds()
    pass
