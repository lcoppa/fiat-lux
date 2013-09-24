"""SNVT_time_stamp standard datapoint type, originally defined in resource
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


class SNVT_time_stamp(base.Structure):
    """SNVT_time_stamp standard datapoint type.  Time stamp.  (year, month,
    day, hour, minute, second.)."""

    def __init__(self):
        super().__init__(
            key=84,
            scope=0
        )

        self.__year = base.Scaled(
            size=2,
            signed=True,
            invalid=-1,
            minimum=-1,
            maximum=3000
        )
        self._register(('year', self.__year))

        self.__month = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=12
        )
        self._register(('month', self.__month))

        self.__day = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=31
        )
        self._register(('day', self.__day))

        self.__hour = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=23
        )
        self._register(('hour', self.__hour))

        self.__minute = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minute', self.__minute))

        self.__second = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('second', self.__second))
        self._definition = standard.add(self)


    def __set_year(self, v):
        self.__year._value = v

    year = property(
        lambda self: self.__year._value,
        __set_year,
        None,
        """Year Zero (0) means year not specified.  Minus one (-1) represents
        NULL date.  (years)."""
    )

    def __set_month(self, v):
        self.__month._value = v

    month = property(
        lambda self: self.__month._value,
        __set_month,
        None,
        """Month Zero (0) means month not specified.  (months)."""
    )

    def __set_day(self, v):
        self.__day._value = v

    day = property(
        lambda self: self.__day._value,
        __set_day,
        None,
        """Day Zero (0) means day not specified.  (days)."""
    )

    def __set_hour(self, v):
        self.__hour._value = v

    hour = property(
        lambda self: self.__hour._value,
        __set_hour,
        None,
        """Hour This field uses a 24-hour value.  (hours)."""
    )

    def __set_minute(self, v):
        self.__minute._value = v

    minute = property(
        lambda self: self.__minute._value,
        __set_minute,
        None,
        """Minute (minutes)."""
    )

    def __set_second(self, v):
        self.__second._value = v

    second = property(
        lambda self: self.__second._value,
        __set_second,
        None,
        """Second (seconds)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_year(v.__year)
        self.__set_month(v.__month)
        self.__set_day(v.__day)
        self.__set_hour(v.__hour)
        self.__set_minute(v.__minute)
        self.__set_second(v.__second)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 7


if __name__ == '__main__':
    # unit test code.
    item = SNVT_time_stamp()
    pass
