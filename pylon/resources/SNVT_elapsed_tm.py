"""
    SNVT_elapsed_tm
"""

#
# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from pylon.resources import base
from pylon.resources.standard import standard


class SNVT_elapsed_tm(base.Structure):
    """SNVT_elapsed standard datapoint type.

    Elapsed time  (day, hour, minute, second, millisecond)."""

    def __init__(self, day=0, hour=0, minute=0, second=0, millisecond=0):
        super().__init__(
            key=87,
            scope=0
        )
        self._definition = standard.add(self)

        self.__day = base.Scaled(
            size=2,
            signed=False,
            default=day
        )
        self._register(('day', self.__day))

        self.__hour = base.Scaled(
            size=1,
            signed=False,
            default=hour,
            maximum=23
        )
        self._register(('hour', self.__hour))

        self.__minute = base.Scaled(
            size=1,
            signed=False,
            default=minute,
            maximum=59
        )
        self._register(('minute', self.__minute))

        self.__second = base.Scaled(
            size=1,
            signed=False,
            default=second,
            maximum=59
        )
        self._register(('second', self.__second))

        self.__millisecond = base.Scaled(
            size=2,
            signed=False,
            default=millisecond,
            maximum=999
        )
        self._register(('millisecond', self.__millisecond))

    def __set_day(self, v):
        self.__day._value = v

    day = property(
        lambda self: self.__day._value,
        __set_day,
        None, """
        Days  (days).  The value 65535 represents NULL or unknown elapsed time.
        """
    )

    def __set_hour(self, v):
        self.__hour._value = v

    hour = property(
        lambda self: self.__hour._value,
        __set_hour,
        None, """
        Hours  (hours).  This field uses a 24-hour value.
        """
    )

    def __set_minute(self, v):
        self.__minute._value = v

    minute = property(
        lambda self: self.__minute._value,
        __set_minute,
        None, """
        Minutes  (minutes).
        """
    )

    def __set_second(self, v):
        self.__second._value = v

    second = property(
        lambda self: self.__second._value,
        __set_second,
        None, """
        Seconds  (seconds).
        """
    )

    def __set_millisecond(self, v):
        self.__millisecond._value = v

    millisecond = property(
        lambda self: self.__millisecond._value,
        __set_millisecond,
        None, """
        Milliseconds  (milliseconds).
        """
    )

    def __set(self, v):
        if not isinstance(v, SNVT_elapsed_tm):
            raise TypeError('Expected instance of {0}, got {1}'.format(
                type(self),
                type(v)
            ))
        self.__set_day(v.__day)
        self.__set_hour(v.__hour)
        self.__set_minute(v.__minute)
        self.__set_second(v.__second)
        self.__set_millisecond(v.__millisecond)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Returns the length of the data type, in bytes."""
        return 7
