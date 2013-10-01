"""elapsed_tm standard datapoint type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0.  """


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


class elapsed_tm(pylon.resources.base.Structure):
    """elapsed_tm standard datapoint type.  Elapsed time.  (day, hour,
    minute, second, millisecond.)."""

    def __init__(self):
        super().__init__(
            key=87,
            scope=0
        )

        self.__day = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65535
        )
        self._register(('day', self.__day))

        self.__hour = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=23
        )
        self._register(('hour', self.__hour))

        self.__minute = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minute', self.__minute))

        self.__second = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('second', self.__second))

        self.__millisecond = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=999
        )
        self._register(('millisecond', self.__millisecond))
        self._original_name = 'SNVT_elapsed_tm'
        self._definition = standard.add(self)


    def __set_day(self, v):
        self.__day._value = v

    day = property(
        lambda self: self.__day._value,
        __set_day,
        None,
        """Days The value 65535 represents NULL or unknown elapsed time.
        (days)."""
    )

    def __set_hour(self, v):
        self.__hour._value = v

    hour = property(
        lambda self: self.__hour._value,
        __set_hour,
        None,
        """Hours This field uses a 24-hour value.  (hours)."""
    )

    def __set_minute(self, v):
        self.__minute._value = v

    minute = property(
        lambda self: self.__minute._value,
        __set_minute,
        None,
        """Minutes (minutes)."""
    )

    def __set_second(self, v):
        self.__second._value = v

    second = property(
        lambda self: self.__second._value,
        __set_second,
        None,
        """Seconds (seconds)."""
    )

    def __set_millisecond(self, v):
        self.__millisecond._value = v

    millisecond = property(
        lambda self: self.__millisecond._value,
        __set_millisecond,
        None,
        """Milliseconds (milliseconds)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_day(v.__day)
        self.__set_hour(v.__hour)
        self.__set_minute(v.__minute)
        self.__set_second(v.__second)
        self.__set_millisecond(v.__millisecond)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 7


if __name__ == '__main__':
    # unit test code.
    item = elapsed_tm()
    pass
