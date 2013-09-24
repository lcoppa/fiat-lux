"""SCPTdayDateIndex standard property type, originally defined in resource
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class SCPTdayDateIndex(base.Structure):
    """SCPTdayDateIndex standard property type.  Day date index.  One or two
    dates for matching with a start index to the time-event array.  (First
    day and month, second day and month, time-event index.)."""

    def __init__(self):
        super().__init__(
            key=103,
            scope=0
        )

        self.__day_1 = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=31
        )
        self._register(('day_1', self.__day_1))

        self.__month_1 = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=12
        )
        self._register(('month_1', self.__month_1))

        self.__day_2 = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=0,
            maximum=31
        )
        self._register(('day_2', self.__day_2))

        self.__month_2 = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=0,
            maximum=12
        )
        self._register(('month_2', self.__month_2))

        self.__event_mode_index = base.Scaled(
            size=2,
            signed=False,
            invalid=0,
            minimum=0,
            maximum=65535
        )
        self._register(('event_mode_index', self.__event_mode_index))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 103
        self._definition = standard.add(self)

    def __set_day_1(self, v):
        self.__day_1._value = v

    day_1 = property(
        lambda self: self.__day_1._value,
        __set_day_1,
        None,
        """First day.  Day of month.  (days)."""
    )

    def __set_month_1(self, v):
        self.__month_1._value = v

    month_1 = property(
        lambda self: self.__month_1._value,
        __set_month_1,
        None,
        """First month.  Month of year.  (months)."""
    )

    def __set_day_2(self, v):
        self.__day_2._value = v

    day_2 = property(
        lambda self: self.__day_2._value,
        __set_day_2,
        None,
        """Second day.  Day of month, zero for no date entry.  (days)."""
    )

    def __set_month_2(self, v):
        self.__month_2._value = v

    month_2 = property(
        lambda self: self.__month_2._value,
        __set_month_2,
        None,
        """Second month.  Month of year, zero for no date entry.
        (months)."""
    )

    def __set_event_mode_index(self, v):
        self.__event_mode_index._value = v

    event_mode_index = property(
        lambda self: self.__event_mode_index._value,
        __set_event_mode_index,
        None,
        """Event index.  Time-event array index.  (index)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_day_1(v.__day_1)
        self.__set_month_1(v.__month_1)
        self.__set_day_2(v.__day_2)
        self.__set_month_2(v.__month_2)
        self.__set_event_mode_index(v.__event_mode_index)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = SCPTdayDateIndex()
    pass
