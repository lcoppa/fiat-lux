"""SNVT_preset standard datapoint type, originally defined in resource file
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.learn_mode_t import learn_mode_t


class SNVT_preset(base.Structure):
    """SNVT_preset standard datapoint type.  Preset (mode, data, time.)."""

    def __init__(self):
        super().__init__(
            key=94,
            scope=0
        )

        self.__learn = learn_mode_t(
        )
        self._register(('learn', self.__learn))

        self.__selector = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('selector', self.__selector))

        self.__value = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(4)
            ]
        )
        self._register(('value', self.__value))

        self.__day = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65535
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

        self.__millisecond = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=999
        )
        self._register(('millisecond', self.__millisecond))
        self._definition = standard.add(self)


    def __set_learn(self, v):
        self.__learn._value = v

    learn = property(
        lambda self: self.__learn._value,
        __set_learn,
        None,
        """Learn mode.  (learn mode names.)."""
    )

    def __set_selector(self, v):
        self.__selector._value = v

    selector = property(
        lambda self: self.__selector._value,
        __set_selector,
        None,
        """Selector The selector is used to choose which preset.  (16-bit
        unsigned value.)."""
    )

    def __set_value(self, v):
        self.__value._value = v

    value = property(
        lambda self: self.__value._value,
        __set_value,
        None,
        """Value (array of 4 bytes.)."""
    )

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
        self.__set_learn(v.__learn)
        self.__set_selector(v.__selector)
        self.__set_value(v.__value)
        self.__set_day(v.__day)
        self.__set_hour(v.__hour)
        self.__set_minute(v.__minute)
        self.__set_second(v.__second)
        self.__set_millisecond(v.__millisecond)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 14


if __name__ == '__main__':
    # unit test code.
    item = SNVT_preset()
    pass
