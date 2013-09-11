"""SNVT_time_val_2 standard datapoint type, originally defined in resource
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
from pylon.resources.occup_t import occup_t


class SNVT_time_val_2(base.Structure):
    """SNVT_time_val_2 standard datapoint type.  Schedule time-value pair.
    Specifies the starting time and value for a scheduled event where the
    value of each event may consist of an occupancy value, a general purpose
    value, or both values."""

    def __init__(self):
        super().__init__(
            key=209,
            scope=0
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

        self.__occupancy = occup_t(
        )
        self._register(('occupancy', self.__occupancy))

        self.__gp_value = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=1
        )
        self._register(('gp_value', self.__gp_value))
        self._definition = standard.add(self)

    def __set_sunrise_relative_flag(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_sunrise_relative_flag(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    sunrise_relative_flag = property(
        __get_sunrise_relative_flag,
        __set_sunrise_relative_flag,
        None,
        """Sunrise relative flag.  If set to one, the time fields specify an
        offset from sunrise;  sunrise time is fixed at 06:00 until a sunrise
        input is received."""
    )

    def __set_sunset_relative_flag(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_sunset_relative_flag(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    sunset_relative_flag = property(
        __get_sunset_relative_flag,
        __set_sunset_relative_flag,
        None,
        """Sunset relative flag.  If set to one, the time fields specify an
        offset from sunset;  sunset time is fixed at 18:00 until a sunset
        input is received."""
    )

    def __set_negative_time_offset_flag(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_negative_time_offset_flag(self):
        return self.___bf00._getbits(
            size=1,
            offset=2,
            signed=False
        )

    negative_time_offset_flag = property(
        __get_negative_time_offset_flag,
        __set_negative_time_offset_flag,
        None,
        """Time sign bit.  Set to one to indicate that the time field is a
        negative value;  this field is only used witth the
        sunrise_relative_flag or sunset_relative_flag;  it is ignored if
        neither flag is set."""
    )

    def __set_hour(self, v):
        if 0 <= v <= 31:
            self.___bf00._setbits(
                value=v,
                size=5,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..31')

    def __get_hour(self):
        return self.___bf00._getbits(
            size=5,
            offset=3,
            signed=False
        )

    hour = property(
        __get_hour,
        __set_hour,
        None,
        """Hour Hour of the day;  0 is midnight;  12 is noon;  31 is the
        invalid value and represents an unused time-value pair.  (Hour)"""
    )

    def __set_occ_value_ignored_flag(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_occ_value_ignored_flag(self):
        return self.___bf01._getbits(
            size=1,
            offset=0,
            signed=False
        )

    occ_value_ignored_flag = property(
        __get_occ_value_ignored_flag,
        __set_occ_value_ignored_flag,
        None,
        """Occupancy value ignored flag.  Set to one if this time-value pair
        does not apply to the occupancy value output."""
    )

    def __set_gp_value_ignored_flag(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_gp_value_ignored_flag(self):
        return self.___bf01._getbits(
            size=1,
            offset=1,
            signed=False
        )

    gp_value_ignored_flag = property(
        __get_gp_value_ignored_flag,
        __set_gp_value_ignored_flag,
        None,
        """General-purpose value flag.  Set to one if this time-value pair
        does not apply to the general purpose value output."""
    )

    def __set_minutes(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=6,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_minutes(self):
        return self.___bf01._getbits(
            size=6,
            offset=2,
            signed=False
        )

    minutes = property(
        __get_minutes,
        __set_minutes,
        None,
        """Minutes Minutes portion of the time.  (minutes)"""
    )


    def __set_occupancy(self, v):
        self.__occupancy._value = v

    occupancy = property(
        lambda self: self.__occupancy._value,
        __set_occupancy,
        None,
        """."""
    )

    def __set_gp_value(self, v):
        self.__gp_value._value = v

    gp_value = property(
        lambda self: self.__gp_value._value,
        __set_gp_value,
        None,
        """Value Output value at the schedule time;  converted to the
        equivalent numerical occupancy value for the nvoSchedOcc output;
        converted to any value for the optional nvoSchedVal output."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_sunrise_relative_flag(v.__sunrise_relative_flag)
        self.__set_sunset_relative_flag(v.__sunset_relative_flag)
        self.__set_negative_time_offset_flag(v.__negative_time_offset_flag)
        self.__set_hour(v.__hour)
        self.__set_occ_value_ignored_flag(v.__occ_value_ignored_flag)
        self.__set_gp_value_ignored_flag(v.__gp_value_ignored_flag)
        self.__set_minutes(v.__minutes)
        self.__set_occupancy(v.__occupancy)
        self.__set_gp_value(v.__gp_value)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = SNVT_time_val_2()
    pass
