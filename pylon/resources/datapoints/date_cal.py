"""date_cal standard datapoint type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0.  Note this resource is marked as
obsolete.  It should not be used for new development, but continued use in
existing designs is permitted."""


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


class date_cal(pylon.resources.base.Structure):
    """date_cal standard datapoint type.  Date This SNVT is obsolete.  Use
    SNVT_time_stamp instead.  (year, month, day.)."""

    def __init__(self):
        super().__init__(
            key=10,
            scope=0
        )

        self.__year = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=3000
        )
        self._register(('year', self.__year))

        self.__month = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=12
        )
        self._register(('month', self.__month))

        self.__day = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=31
        )
        self._register(('day', self.__day))
        self._original_name = 'SNVT_date_cal'
        self._mark_obsolete()
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
        """Month (months)."""
    )

    def __set_day(self, v):
        self.__day._value = v

    day = property(
        lambda self: self.__day._value,
        __set_day,
        None,
        """Day (days)."""
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

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = date_cal()
    pass
