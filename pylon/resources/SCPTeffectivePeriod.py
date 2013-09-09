"""SCPTeffectivePeriod standard property type, originally defined in resource
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class SCPTeffectivePeriod(base.Structure):
    """SCPTeffectivePeriod standard property type.  Effective period.  Time
    period during which a functional block is effective."""

    class startType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
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
                minimum=1,
                maximum=12
            )
            self._register(('month', self.__month))

            self.__day = base.Scaled(
                size=1,
                signed=False,
                minimum=1,
                maximum=31
            )
            self._register(('day', self.__day))

        def __set_year(self, v):
            self.__year._value = v

        year = property(
            lambda self: self.__year._value,
            __set_year,
            None,
            """Year Starting year."""
        )

        def __set_month(self, v):
            self.__month._value = v

        month = property(
            lambda self: self.__month._value,
            __set_month,
            None,
            """Month Starting month."""
        )

        def __set_day(self, v):
            self.__day._value = v

        day = property(
            lambda self: self.__day._value,
            __set_day,
            None,
            """Day Starting day."""
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

    class endType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
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
                minimum=1,
                maximum=12
            )
            self._register(('month', self.__month))

            self.__day = base.Scaled(
                size=1,
                signed=False,
                minimum=1,
                maximum=31
            )
            self._register(('day', self.__day))

        def __set_year(self, v):
            self.__year._value = v

        year = property(
            lambda self: self.__year._value,
            __set_year,
            None,
            """Ending year.  Ending year of the effective period."""
        )

        def __set_month(self, v):
            self.__month._value = v

        month = property(
            lambda self: self.__month._value,
            __set_month,
            None,
            """Ending month.  Ending month of the effective period."""
        )

        def __set_day(self, v):
            self.__day._value = v

        day = property(
            lambda self: self.__day._value,
            __set_day,
            None,
            """Ending day.  Ending day of the effective period."""
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

    def __init__(self):
        super().__init__(
            key=272,
            scope=0
        )

        self.__start = SCPTeffectivePeriod.startType(
        )
        self._register(('start', self.__start))

        self.__end = SCPTeffectivePeriod.endType(
        )
        self._register(('end', self.__end))
        self._default_bytes = b'\xff\xff\x01\x01\xff\xff\x01\x01'
        self._property_scope, self._property_key = 0, 272
        self._definition = standard.add(self)

    def __set_start(self, v):
        self.__start._value = v

    start = property(
        lambda self: self.__start._value,
        __set_start,
        None,
        """Starting date.  Starting date of the effective period."""
    )

    def __set_end(self, v):
        self.__end._value = v

    end = property(
        lambda self: self.__end._value,
        __set_end,
        None,
        """Ending date.  Ending date of the effective period."""
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

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 8


if __name__ == '__main__':
    # unit test code.
    item = SCPTeffectivePeriod()
    pass
