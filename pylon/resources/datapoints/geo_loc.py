"""geo_loc standard datapoint type, originally defined in resource file set
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard


class geo_loc(pylon.resources.base.Structure):
    """geo_loc standard datapoint type.  Geographic Location."""

    def __init__(self):
        super().__init__(
            key=201,
            scope=0
        )

        self.__longitude = pylon.resources.base.Scaled(
            size=4,
            signed=True,
            scaling=(1E-007, 0),
            invalid=214.748,
            minimum=-180,
            maximum=180
        )
        self._register(('longitude', self.__longitude))

        self.__latitude = pylon.resources.base.Scaled(
            size=4,
            signed=True,
            scaling=(1E-007, 0),
            invalid=214.748,
            minimum=-90,
            maximum=90
        )
        self._register(('latitude', self.__latitude))

        self.__elevation = pylon.resources.base.Float(
            single=True,
            minimum=-3.40282E+038,
            maximum=3.40282E+038
        )
        self._register(('elevation', self.__elevation))

        self.__name = pylon.resources.base.Array(
            [
                pylon.resources.base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(19)
            ]
        )
        self._register(('name', self.__name))
        self._original_name = 'SNVT_geo_loc'
        self._definition = standard.add(self)


    def __set_longitude(self, v):
        self.__longitude._value = v

    longitude = property(
        lambda self: self.__longitude._value,
        __set_longitude,
        None,
        """Longitude Longitude is given as an angular measurement ranging
        from 0deg at the prime meridian to +180deg eastward and -180deg
        westward."""
    )

    def __set_latitude(self, v):
        self.__latitude._value = v

    latitude = property(
        lambda self: self.__latitude._value,
        __set_latitude,
        None,
        """Latitude Latitude is given as an angular measurement ranging from
        0deg at the equator to +90deg northward and -90deg southward."""
    )

    def __set_elevation(self, v):
        self.__elevation._value = v

    elevation = property(
        lambda self: self.__elevation._value,
        __set_elevation,
        None,
        """Elevation (meters)."""
    )

    def __set_name(self, v):
        self.__name._value = v

    name = property(
        lambda self: self.__name._value,
        __set_name,
        None,
        """."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_longitude(v.__longitude)
        self.__set_latitude(v.__latitude)
        self.__set_elevation(v.__elevation)
        self.__set_name(v.__name)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 31


if __name__ == '__main__':
    # unit test code.
    item = geo_loc()
    pass
