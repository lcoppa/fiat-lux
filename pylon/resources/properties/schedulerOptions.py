"""schedulerOptions standard property type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 23-Sep-2013 09:14.

import pylon.resources.base
from pylon.resources.standard import standard


class schedulerOptions(pylon.resources.base.Structure):
    """schedulerOptions standard property type.  ."""

    def __init__(self):
        super().__init__(
            key=379,
            scope=0
        )

        self.___bf00 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))
        self._default_bytes = b'\x00'
        self._original_name = 'SCPTschedulerOptions'
        self._property_scope, self._property_key = 0, 379
        self._definition = standard.add(self)
    def __set_reserved(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=5,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_reserved(self):
        return self.___bf00._getbits(
            size=5,
            offset=0,
            signed=False
        )

    reserved = property(
        __get_reserved,
        __set_reserved,
        None,
        """Bitfield reserved"""
    )

    def __set_alternate_time_source(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=5
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_alternate_time_source(self):
        return self.___bf00._getbits(
            size=1,
            offset=5,
            signed=False
        )

    alternate_time_source = property(
        __get_alternate_time_source,
        __set_alternate_time_source,
        None,
        """Alternate time source option flag.  Set to one if the device
        supports an alternate time source such as an interface to an NTP or
        SNTP server, GPS clock, or radio atomic-clock source."""
    )

    def __set_general_purpose_output(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=6
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_general_purpose_output(self):
        return self.___bf00._getbits(
            size=1,
            offset=6,
            signed=False
        )

    general_purpose_output = property(
        __get_general_purpose_output,
        __set_general_purpose_output,
        None,
        """General-purpose option flag.  Set to one if the general purpose
        output is supported;  if zero, only the occupancy output is used."""
    )

    def __set_sunrise_sunset_relative(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=7
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_sunrise_sunset_relative(self):
        return self.___bf00._getbits(
            size=1,
            offset=7,
            signed=False
        )

    sunrise_sunset_relative = property(
        __get_sunrise_sunset_relative,
        __set_sunrise_sunset_relative,
        None,
        """Sunrise and sunset relative scheduling option flag.  Set to one if
        the scheduler supports sunsrise and sunset relative schedulign;  set
        to zero if sunrise and sunset relative scheduling is not
        supported."""
    )


    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.___bf00._value = v.___bf00._value

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 1


if __name__ == '__main__':
    # unit test code.
    item = schedulerOptions()
    pass
