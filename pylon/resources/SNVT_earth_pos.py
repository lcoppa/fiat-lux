"""SNVT_earth_pos standard datapoint type, originally defined in resource
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


class SNVT_earth_pos(base.Structure):
    """SNVT_earth_pos standard datapoint type.  Earth position.  (lat & long
    direction, latitude deg & min, longitude deg & min, height.)."""

    def __init__(self):
        super().__init__(
            key=135,
            scope=0
        )

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.__latitude_deg = base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=90
        )
        self._register(('latitude_deg', self.__latitude_deg))

        self.__latitude_min = base.Scaled(
            size=2,
            signed=False,
            scaling=(0.001, 0),
            invalid=65.535,
            minimum=0,
            maximum=59.999
        )
        self._register(('latitude_min', self.__latitude_min))

        self.__longitude_deg = base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=180
        )
        self._register(('longitude_deg', self.__longitude_deg))

        self.__longitude_min = base.Scaled(
            size=2,
            signed=False,
            scaling=(0.001, 0),
            invalid=65.535,
            minimum=0,
            maximum=59.999
        )
        self._register(('longitude_min', self.__longitude_min))

        self.__height_above_sea = base.Float(
            single=True,
            minimum=-3.40282E+038,
            maximum=3.40282E+038
        )
        self._register(('height_above_sea', self.__height_above_sea))
        self._definition = standard.add(self)

    def __set_latitude_direction(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_latitude_direction(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    latitude_direction = property(
        __get_latitude_direction,
        __set_latitude_direction,
        None,
        """Direction of latitude.  0 = South latitude, 1 = North latitude.
        (direction (S/N))"""
    )

    def __set_longitude_direction(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_longitude_direction(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    longitude_direction = property(
        __get_longitude_direction,
        __set_longitude_direction,
        None,
        """Direction of longitude.  0 = East longitude, 1 = West longitude.
        (direction (E/W))"""
    )


    def __set_latitude_deg(self, v):
        self.__latitude_deg._value = v

    latitude_deg = property(
        lambda self: self.__latitude_deg._value,
        __set_latitude_deg,
        None,
        """Latitude degrees.  (degrees)."""
    )

    def __set_latitude_min(self, v):
        self.__latitude_min._value = v

    latitude_min = property(
        lambda self: self.__latitude_min._value,
        __set_latitude_min,
        None,
        """Latitude minutes.  (minutes)."""
    )

    def __set_longitude_deg(self, v):
        self.__longitude_deg._value = v

    longitude_deg = property(
        lambda self: self.__longitude_deg._value,
        __set_longitude_deg,
        None,
        """Longitude degrees.  (degrees)."""
    )

    def __set_longitude_min(self, v):
        self.__longitude_min._value = v

    longitude_min = property(
        lambda self: self.__longitude_min._value,
        __set_longitude_min,
        None,
        """Longitude minutes.  (minutes)."""
    )

    def __set_height_above_sea(self, v):
        self.__height_above_sea._value = v

    height_above_sea = property(
        lambda self: self.__height_above_sea._value,
        __set_height_above_sea,
        None,
        """Height above sea level.  (meters)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_latitude_deg(v.__latitude_deg)
        self.__set_latitude_min(v.__latitude_min)
        self.__set_longitude_deg(v.__longitude_deg)
        self.__set_longitude_min(v.__longitude_min)
        self.__set_height_above_sea(v.__height_above_sea)
        self.___bf00(v.___bf00)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 11


if __name__ == '__main__':
    # unit test code.
    item = SNVT_earth_pos()
    pass
