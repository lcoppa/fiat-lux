"""SNVT_time_zone standard datapoint type, originally defined in resource
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
from pylon.resources.calendar_type_t import calendar_type_t
from pylon.resources.days_of_week_t import days_of_week_t


class SNVT_time_zone(base.Structure):
    """SNVT_time_zone standard datapoint type.  Time zone descriptor.
    (offset, type, startDST, endDST.)."""

    class start_DSTType(base.Union):

        class M_start_DSTType(base.Structure):

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

                self.__dateday_of_start_DST = days_of_week_t(
                )
                self._register(('dateday_of_start_DST', self.__dateday_of_start_DST))
            def __set_month_of_start_DST(self, v):
                if 1 <= v <= 12:
                    self.___bf00._setbits(
                        value=v,
                        size=4,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 1..12')

            def __get_month_of_start_DST(self):
                return self.___bf00._getbits(
                    size=4,
                    offset=0,
                    signed=False
                )

            month_of_start_DST = property(
                __get_month_of_start_DST,
                __set_month_of_start_DST,
                None,
                """months"""
            )

            def __set_week_of_start_DST(self, v):
                if 1 <= v <= 5:
                    self.___bf00._setbits(
                        value=v,
                        size=3,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 1..5')

            def __get_week_of_start_DST(self):
                return self.___bf00._getbits(
                    size=3,
                    offset=4,
                    signed=False
                )

            week_of_start_DST = property(
                __get_week_of_start_DST,
                __set_week_of_start_DST,
                None,
                """weeks"""
            )


            def __set_dateday_of_start_DST(self, v):
                self.__dateday_of_start_DST._value = v

            dateday_of_start_DST = property(
                lambda self: self.__dateday_of_start_DST._value,
                __set_dateday_of_start_DST,
                None,
                """Day of week.  (day names.)."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_dateday_of_start_DST(v.__dateday_of_start_DST)
                self.___bf00._value = v.___bf00._value

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 2

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__G_day_of_start_DST = base.Scaled(
                size=2,
                signed=False,
                minimum=0,
                maximum=365
            )
            self._register(('G_day_of_start_DST', self.__G_day_of_start_DST))

            self.__J_day_of_start_DST = base.Scaled(
                size=2,
                signed=False,
                minimum=1,
                maximum=365
            )
            self._register(('J_day_of_start_DST', self.__J_day_of_start_DST))

            self.__M_start_DST = SNVT_time_zone.start_DSTType.M_start_DSTType(
            )
            self._register(('M_start_DST', self.__M_start_DST))

        def __set_G_day_of_start_DST(self, v):
            self.__G_day_of_start_DST._value = v

        G_day_of_start_DST = property(
            lambda self: self.__G_day_of_start_DST._value,
            __set_G_day_of_start_DST,
            None,
            """Gregorian calendar day of start DST.  (days)."""
        )

        def __set_J_day_of_start_DST(self, v):
            self.__J_day_of_start_DST._value = v

        J_day_of_start_DST = property(
            lambda self: self.__J_day_of_start_DST._value,
            __set_J_day_of_start_DST,
            None,
            """Julian calendar day of start DST.  (days)."""
        )

        def __set_M_start_DST(self, v):
            self.__M_start_DST._value = v

        M_start_DST = property(
            lambda self: self.__M_start_DST._value,
            __set_M_start_DST,
            None,
            """Meu calendar day of start DST.  (month, week, dateday.)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_G_day_of_start_DST(v.__G_day_of_start_DST)
            self.__set_J_day_of_start_DST(v.__J_day_of_start_DST)
            self.__set_M_start_DST(v.__M_start_DST)

        _value = property(lambda self: self, __set)

    class end_DSTType(base.Union):

        class M_end_DSTType(base.Structure):

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

                self.__dateday_of_end_DST = days_of_week_t(
                )
                self._register(('dateday_of_end_DST', self.__dateday_of_end_DST))
            def __set_month_of_end_DST(self, v):
                if 1 <= v <= 12:
                    self.___bf00._setbits(
                        value=v,
                        size=4,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 1..12')

            def __get_month_of_end_DST(self):
                return self.___bf00._getbits(
                    size=4,
                    offset=0,
                    signed=False
                )

            month_of_end_DST = property(
                __get_month_of_end_DST,
                __set_month_of_end_DST,
                None,
                """months"""
            )

            def __set_week_of_end_DST(self, v):
                if 1 <= v <= 5:
                    self.___bf00._setbits(
                        value=v,
                        size=3,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 1..5')

            def __get_week_of_end_DST(self):
                return self.___bf00._getbits(
                    size=3,
                    offset=4,
                    signed=False
                )

            week_of_end_DST = property(
                __get_week_of_end_DST,
                __set_week_of_end_DST,
                None,
                """weeks"""
            )


            def __set_dateday_of_end_DST(self, v):
                self.__dateday_of_end_DST._value = v

            dateday_of_end_DST = property(
                lambda self: self.__dateday_of_end_DST._value,
                __set_dateday_of_end_DST,
                None,
                """Day of week.  (day names.)."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_dateday_of_end_DST(v.__dateday_of_end_DST)
                self.___bf00._value = v.___bf00._value

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 2

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__G_day_of_end_DST = base.Scaled(
                size=2,
                signed=False,
                minimum=0,
                maximum=365
            )
            self._register(('G_day_of_end_DST', self.__G_day_of_end_DST))

            self.__J_day_of_end_DST = base.Scaled(
                size=2,
                signed=False,
                minimum=1,
                maximum=365
            )
            self._register(('J_day_of_end_DST', self.__J_day_of_end_DST))

            self.__M_end_DST = SNVT_time_zone.end_DSTType.M_end_DSTType(
            )
            self._register(('M_end_DST', self.__M_end_DST))

        def __set_G_day_of_end_DST(self, v):
            self.__G_day_of_end_DST._value = v

        G_day_of_end_DST = property(
            lambda self: self.__G_day_of_end_DST._value,
            __set_G_day_of_end_DST,
            None,
            """Gregorian calendar day of end DST.  (days)."""
        )

        def __set_J_day_of_end_DST(self, v):
            self.__J_day_of_end_DST._value = v

        J_day_of_end_DST = property(
            lambda self: self.__J_day_of_end_DST._value,
            __set_J_day_of_end_DST,
            None,
            """Julian calendar day of end DST.  (days)."""
        )

        def __set_M_end_DST(self, v):
            self.__M_end_DST._value = v

        M_end_DST = property(
            lambda self: self.__M_end_DST._value,
            __set_M_end_DST,
            None,
            """Meu calendar day of end DST.  (month, week, dateday.)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_G_day_of_end_DST(v.__G_day_of_end_DST)
            self.__set_J_day_of_end_DST(v.__J_day_of_end_DST)
            self.__set_M_end_DST(v.__M_end_DST)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=134,
            scope=0
        )

        self.__second_time_offset = base.Scaled(
            size=4,
            signed=True,
            minimum=-86400,
            maximum=86400
        )
        self._register(('second_time_offset', self.__second_time_offset))

        self.__type_of_description = calendar_type_t(
        )
        self._register(('type_of_description', self.__type_of_description))

        self.__hour_of_start_DST = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=23
        )
        self._register(('hour_of_start_DST', self.__hour_of_start_DST))

        self.__minute_of_start_DST = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minute_of_start_DST', self.__minute_of_start_DST))

        self.__second_of_start_DST = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('second_of_start_DST', self.__second_of_start_DST))

        self.__start_DST = SNVT_time_zone.start_DSTType(
        )
        self._register(('start_DST', self.__start_DST))

        self.__hour_of_end_DST = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=23
        )
        self._register(('hour_of_end_DST', self.__hour_of_end_DST))

        self.__minute_of_end_DST = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minute_of_end_DST', self.__minute_of_end_DST))

        self.__second_of_end_DST = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('second_of_end_DST', self.__second_of_end_DST))

        self.__end_DST = SNVT_time_zone.end_DSTType(
        )
        self._register(('end_DST', self.__end_DST))
        self._definition = standard.add(self)


    def __set_second_time_offset(self, v):
        self.__second_time_offset._value = v

    second_time_offset = property(
        lambda self: self.__second_time_offset._value,
        __set_second_time_offset,
        None,
        """Offset from GMT.  West direction is negative offset.
        (seconds)."""
    )

    def __set_type_of_description(self, v):
        self.__type_of_description._value = v

    type_of_description = property(
        lambda self: self.__type_of_description._value,
        __set_type_of_description,
        None,
        """Calendar type.  (calendar type names.)."""
    )

    def __set_hour_of_start_DST(self, v):
        self.__hour_of_start_DST._value = v

    hour_of_start_DST = property(
        lambda self: self.__hour_of_start_DST._value,
        __set_hour_of_start_DST,
        None,
        """DST start hour.  (hours)."""
    )

    def __set_minute_of_start_DST(self, v):
        self.__minute_of_start_DST._value = v

    minute_of_start_DST = property(
        lambda self: self.__minute_of_start_DST._value,
        __set_minute_of_start_DST,
        None,
        """DST start minute.  (minutes)."""
    )

    def __set_second_of_start_DST(self, v):
        self.__second_of_start_DST._value = v

    second_of_start_DST = property(
        lambda self: self.__second_of_start_DST._value,
        __set_second_of_start_DST,
        None,
        """DST start second.  (seconds)."""
    )

    def __set_start_DST(self, v):
        self.__start_DST._value = v

    start_DST = property(
        lambda self: self.__start_DST._value,
        __set_start_DST,
        None,
        """DST start day.  Daylight savings time start day.  (day
        descriptor.)."""
    )

    def __set_hour_of_end_DST(self, v):
        self.__hour_of_end_DST._value = v

    hour_of_end_DST = property(
        lambda self: self.__hour_of_end_DST._value,
        __set_hour_of_end_DST,
        None,
        """DST end hour.  (hours)."""
    )

    def __set_minute_of_end_DST(self, v):
        self.__minute_of_end_DST._value = v

    minute_of_end_DST = property(
        lambda self: self.__minute_of_end_DST._value,
        __set_minute_of_end_DST,
        None,
        """DST end minute.  (minutes)."""
    )

    def __set_second_of_end_DST(self, v):
        self.__second_of_end_DST._value = v

    second_of_end_DST = property(
        lambda self: self.__second_of_end_DST._value,
        __set_second_of_end_DST,
        None,
        """DST end second.  (seconds)."""
    )

    def __set_end_DST(self, v):
        self.__end_DST._value = v

    end_DST = property(
        lambda self: self.__end_DST._value,
        __set_end_DST,
        None,
        """DST end day.  Daylight savings time end day.  (day
        descriptor.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_second_time_offset(v.__second_time_offset)
        self.__set_type_of_description(v.__type_of_description)
        self.__set_hour_of_start_DST(v.__hour_of_start_DST)
        self.__set_minute_of_start_DST(v.__minute_of_start_DST)
        self.__set_second_of_start_DST(v.__second_of_start_DST)
        self.__set_start_DST(v.__start_DST)
        self.__set_hour_of_end_DST(v.__hour_of_end_DST)
        self.__set_minute_of_end_DST(v.__minute_of_end_DST)
        self.__set_second_of_end_DST(v.__second_of_end_DST)
        self.__set_end_DST(v.__end_DST)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 15


if __name__ == '__main__':
    # unit test code.
    item = SNVT_time_zone()
    pass
