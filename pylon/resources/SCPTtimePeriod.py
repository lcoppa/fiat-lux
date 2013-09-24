"""SCPTtimePeriod standard property type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.interval_of_month_t import interval_of_month_t
from pylon.resources.days_of_week_t import days_of_week_t


class SCPTtimePeriod(base.Structure):
    """SCPTtimePeriod standard property type.  Historical Period.  This input
    configuration network variable defines the period of time between
    transfer of a values to the historical register."""

    class valueType(base.Union):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__minutes_interval = base.Scaled(
                size=1,
                signed=False,
                minimum=1,
                maximum=255
            )
            self._register(('minutes_interval', self.__minutes_interval))

            self.__date_of_month = base.Scaled(
                size=1,
                signed=False,
                minimum=1,
                maximum=31
            )
            self._register(('date_of_month', self.__date_of_month))

            self.__hour_of_day = base.Scaled(
                size=1,
                signed=False,
                minimum=0,
                maximum=23
            )
            self._register(('hour_of_day', self.__hour_of_day))

            self.__day_of_week = days_of_week_t(
            )
            self._register(('day_of_week', self.__day_of_week))

            self.__hours_interval = base.Scaled(
                size=1,
                signed=False,
                minimum=1,
                maximum=255
            )
            self._register(('hours_interval', self.__hours_interval))

        def __set_minutes_interval(self, v):
            self.__minutes_interval._value = v

        minutes_interval = property(
            lambda self: self.__minutes_interval._value,
            __set_minutes_interval,
            None,
            """."""
        )

        def __set_date_of_month(self, v):
            self.__date_of_month._value = v

        date_of_month = property(
            lambda self: self.__date_of_month._value,
            __set_date_of_month,
            None,
            """."""
        )

        def __set_hour_of_day(self, v):
            self.__hour_of_day._value = v

        hour_of_day = property(
            lambda self: self.__hour_of_day._value,
            __set_hour_of_day,
            None,
            """."""
        )

        def __set_day_of_week(self, v):
            self.__day_of_week._value = v

        day_of_week = property(
            lambda self: self.__day_of_week._value,
            __set_day_of_week,
            None,
            """."""
        )

        def __set_hours_interval(self, v):
            self.__hours_interval._value = v

        hours_interval = property(
            lambda self: self.__hours_interval._value,
            __set_hours_interval,
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
            self.__set_minutes_interval(v.__minutes_interval)
            self.__set_date_of_month(v.__date_of_month)
            self.__set_hour_of_day(v.__hour_of_day)
            self.__set_day_of_week(v.__day_of_week)
            self.__set_hours_interval(v.__hours_interval)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=291,
            scope=0
        )

        self.__units = interval_of_month_t(
        )
        self._register(('units', self.__units))

        self.__value = SCPTtimePeriod.valueType(
        )
        self._register(('value', self.__value))
        self._default_bytes = b'\x00\x00'
        self._property_scope, self._property_key = 0, 291
        self._definition = standard.add(self)

    def __set_units(self, v):
        self.__units._value = v

    units = property(
        lambda self: self.__units._value,
        __set_units,
        None,
        """."""
    )

    def __set_value(self, v):
        self.__value._value = v

    value = property(
        lambda self: self.__value._value,
        __set_value,
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
        self.__set_units(v.__units)
        self.__set_value(v.__value)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 2


if __name__ == '__main__':
    # unit test code.
    item = SCPTtimePeriod()
    pass
