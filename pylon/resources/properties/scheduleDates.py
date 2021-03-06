"""scheduleDates standard property type, originally defined in resource file
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
# Generated at 23-Sep-2013 09:14.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.enumerations.days_of_month_t
import pylon.resources.enumerations.months_t


class scheduleDates(pylon.resources.base.Structure):
    """scheduleDates standard property type.  Schedule dates.  A range of
    dates with an optional qualifier that specifies when a schedule is
    active."""

    class startType(pylon.resources.base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__year = pylon.resources.base.Scaled(
                size=2,
                signed=True,
                invalid=-1,
                minimum=-1,
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

            self.__day = pylon.resources.enumerations.days_of_month_t.days_of_month_t(
            )
            self._register(('day', self.__day))

        def __set_year(self, v):
            self.__year._value = v

        year = property(
            lambda self: self.__year._value,
            __set_year,
            None,
            """Starting year.  Starting year for schedule."""
        )

        def __set_month(self, v):
            self.__month._value = v

        month = property(
            lambda self: self.__month._value,
            __set_month,
            None,
            """Starting month.  Starting month for schedule."""
        )

        def __set_day(self, v):
            self.__day._value = v

        day = property(
            lambda self: self.__day._value,
            __set_day,
            None,
            """Starting day.  Starting day for schedule."""
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

    class endType(pylon.resources.base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__year = pylon.resources.base.Scaled(
                size=2,
                signed=True,
                invalid=-1,
                minimum=-1,
                maximum=3000
            )
            self._register(('year', self.__year))

            self.___bf00 = pylon.resources.base.Scaled(
                size=1,
                signed=False
            )
            self._register(('___bf00', self.___bf00))

            self.__day = pylon.resources.enumerations.days_of_month_t.days_of_month_t(
            )
            self._register(('day', self.__day))

        def __set_year(self, v):
            self.__year._value = v

        year = property(
            lambda self: self.__year._value,
            __set_year,
            None,
            """Ending year.  Ending year for schedule."""
        )
        def __set_temporary(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=0
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_temporary(self):
            return self.___bf00._getbits(
                size=1,
                offset=0,
                signed=False
            )

        temporary = property(
            __get_temporary,
            __set_temporary,
            None,
            """Temporary flag.  Identifies a temporary schedule.  Temporary
            schedules are deleted at the end of the day that they are
            active."""
        )

        def __set_month(self, v):
            if 0 <= v <= 12:
                self.___bf00._setbits(
                    value=v,
                    size=7,
                    offset=1
                )
            else:
                raise ValueError('Not in range 0..12')

        def __get_month(self):
            return self.___bf00._getbits(
                size=7,
                offset=1,
                signed=False
            )

        month = property(
            __get_month,
            __set_month,
            None,
            """Ending month.  Ending month for schedule."""
        )


        def __set_day(self, v):
            self.__day._value = v

        day = property(
            lambda self: self.__day._value,
            __set_day,
            None,
            """Ending day.  Ending day for schedule."""
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
            self.__set_day(v.__day)
            self.___bf00._value = v.___bf00._value

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 4

    class qualifierType(pylon.resources.base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__months = pylon.resources.enumerations.months_t.months_t(
            )
            self._register(('months', self.__months))

            self.__days = pylon.resources.enumerations.days_of_month_t.days_of_month_t(
            )
            self._register(('days', self.__days))

        def __set_months(self, v):
            self.__months._value = v

        months = property(
            lambda self: self.__months._value,
            __set_months,
            None,
            """Month qualifier.  Months within the dates specified by the
            start and end dates."""
        )

        def __set_days(self, v):
            self.__days._value = v

        days = property(
            lambda self: self.__days._value,
            __set_days,
            None,
            """Days qualifier.  Days within the dates specified by the start
            and end dates."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_months(v.__months)
            self.__set_days(v.__days)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 2

    def __init__(self):
        super().__init__(
            key=273,
            scope=0
        )

        self.__start = scheduleDates.startType(
        )
        self._register(('start', self.__start))

        self.__end = scheduleDates.endType(
        )
        self._register(('end', self.__end))

        self.__qualifier = scheduleDates.qualifierType(
        )
        self._register(('qualifier', self.__qualifier))

        self.__schedule_index = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65535
        )
        self._register(('schedule_index', self.__schedule_index))
        self._default_bytes = b'\xff\xff\x00\x00\xff\xff\x00\x00\x00\x00\xff' \
            b'\xff'
        self._original_name = 'SCPTscheduleDates'
        self._property_scope, self._property_key = 0, 273
        self._definition = standard.add(self)

    def __set_start(self, v):
        self.__start._value = v

    start = property(
        lambda self: self.__start._value,
        __set_start,
        None,
        """Schedule start."""
    )

    def __set_end(self, v):
        self.__end._value = v

    end = property(
        lambda self: self.__end._value,
        __set_end,
        None,
        """Schedule end."""
    )

    def __set_qualifier(self, v):
        self.__qualifier._value = v

    qualifier = property(
        lambda self: self.__qualifier._value,
        __set_qualifier,
        None,
        """."""
    )

    def __set_schedule_index(self, v):
        self.__schedule_index._value = v

    schedule_index = property(
        lambda self: self.__schedule_index._value,
        __set_schedule_index,
        None,
        """Schedule number.  Index into a schedule or schedule name array."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_start(v.__start)
        self.__set_end(v.__end)
        self.__set_qualifier(v.__qualifier)
        self.__set_schedule_index(v.__schedule_index)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 12


if __name__ == '__main__':
    # unit test code.
    item = scheduleDates()
    pass
