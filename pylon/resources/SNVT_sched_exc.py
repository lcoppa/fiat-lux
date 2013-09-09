"""SNVT_sched_exc standard datapoint type, originally defined in resource
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
from pylon.resources.months_t import months_t
from pylon.resources.days_of_month_t import days_of_month_t
from pylon.resources.SNVT_time_val_2 import SNVT_time_val_2


class SNVT_sched_exc(base.Structure):
    """SNVT_sched_exc standard datapoint type.  Exception schedule.
    Specifies a scheduled event to override a daily schedule."""

    class end_timeType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
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
            """Sunrise relative flag.  If set to one, the time fields specify
            an offset from sunrise;  sunrise time is fixed at 06:00 until a
            sunrise input is received."""
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
            """Sunset relative flag.  If set to one, the time fields specify
            an offset from sunset;  sunset time is fixed at 18:00 until a
            sunset input is received."""
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
            """Time sign bit.  Set to one to indicate that the time field is
            a negative value;  this field is only used witth the
            sunrise_relative_flag or sunset_relative_flag;  it is ignored if
            neither flag is set."""
        )

        def __set_hour(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=5,
                    offset=3,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

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
            invalid value and represents an unused time-value pair.
            (Hour)"""
        )

        def __set_start_offset_enable_flag(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=0,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_start_offset_enable_flag(self):
            return self.___bf01._getbits(
                size=1,
                offset=0,
                signed=False
            )

        start_offset_enable_flag = property(
            __get_start_offset_enable_flag,
            __set_start_offset_enable_flag,
            None,
            """Start offset enable flag.  Set to one with the
            stop_offset_enable_flag set to zero to enable the time to be
            offset by the nviStartOffset input;  set both flags to one to
            enable the time to be offset by a random interval specified by
            cpRandomizationInterval."""
        )

        def __set_stop_offset_enable_flag(self, v):
            if 0 <= v <= 1:
                self.___bf01._setbits(
                    value=v,
                    size=1,
                    offset=1,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_stop_offset_enable_flag(self):
            return self.___bf01._getbits(
                size=1,
                offset=1,
                signed=False
            )

        stop_offset_enable_flag = property(
            __get_stop_offset_enable_flag,
            __set_stop_offset_enable_flag,
            None,
            """End offset enable flag.  Set to one with the
            start_offset_enable_flag set to zero to enable the time to be
            offset by the nviStopOffset input;  set both flags to one to
            enable the time to be offset by a random interval specified by
            cpRandomizationInterval."""
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


        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.___bf01(v.___bf01)
            self.___bf00(v.___bf00)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 2

    def __init__(self):
        super().__init__(
            key=211,
            scope=0
        )

        self.__months = months_t(
        )
        self._register(('months', self.__months))

        self.__days = days_of_month_t(
        )
        self._register(('days', self.__days))

        self.__start_time_value = SNVT_time_val_2(
        )
        self._register(('start_time_value', self.__start_time_value))

        self.__end_time = SNVT_sched_exc.end_timeType(
        )
        self._register(('end_time', self.__end_time))
        self._definition = standard.add(self)


    def __set_months(self, v):
        self.__months._value = v

    months = property(
        lambda self: self.__months._value,
        __set_months,
        None,
        """Exception months.  Months for exception schedule to be active;
        set to the invalid value (MN_NUL) to disable the exception
        schedule."""
    )

    def __set_days(self, v):
        self.__days._value = v

    days = property(
        lambda self: self.__days._value,
        __set_days,
        None,
        """Days Days within the months specified by the months field for the
        exception schedule to be active."""
    )

    def __set_start_time_value(self, v):
        self.__start_time_value._value = v

    start_time_value = property(
        lambda self: self.__start_time_value._value,
        __set_start_time_value,
        None,
        """Start time and value.  Start time on the specified days within the
        specified months, and the value for the exception schedule."""
    )

    def __set_end_time(self, v):
        self.__end_time._value = v

    end_time = property(
        lambda self: self.__end_time._value,
        __set_end_time,
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
        self.__set_months(v.__months)
        self.__set_days(v.__days)
        self.__set_start_time_value(v.__start_time_value)
        self.__set_end_time(v.__end_time)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 8


if __name__ == '__main__':
    # unit test code.
    item = SNVT_sched_exc()
    pass
