"""bkupSchedule standard property type, originally defined in resource file
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


class bkupSchedule(pylon.resources.base.Structure):
    """bkupSchedule standard property type.  Backup Schedule."""

    def __init__(self):
        super().__init__(
            key=344,
            scope=0
        )

        self.__hour_on = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=23
        )
        self._register(('hour_on', self.__hour_on))

        self.__minute_on = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minute_on', self.__minute_on))

        self.__hour_off = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=23
        )
        self._register(('hour_off', self.__hour_off))

        self.__minute_off = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minute_off', self.__minute_off))
        self._default_bytes = b'\x00\x00\x00\x00'
        self._original_name = 'SCPTbkupSchedule'
        self._property_scope, self._property_key = 0, 344
        self._definition = standard.add(self)

    def __set_hour_on(self, v):
        self.__hour_on._value = v

    hour_on = property(
        lambda self: self.__hour_on._value,
        __set_hour_on,
        None,
        """Hour ON.  Time when the luminare will be switched ON in case of
        communication failure.  (Hours)."""
    )

    def __set_minute_on(self, v):
        self.__minute_on._value = v

    minute_on = property(
        lambda self: self.__minute_on._value,
        __set_minute_on,
        None,
        """Minute ON.  Time when the luminare will be switched ON in case of
        communication failure.  (Minutes)."""
    )

    def __set_hour_off(self, v):
        self.__hour_off._value = v

    hour_off = property(
        lambda self: self.__hour_off._value,
        __set_hour_off,
        None,
        """Hour OFF.  Time when the luminare will be switched OFF in case of
        communication failure.  (Hours)."""
    )

    def __set_minute_off(self, v):
        self.__minute_off._value = v

    minute_off = property(
        lambda self: self.__minute_off._value,
        __set_minute_off,
        None,
        """Minute OFF.  Time when the luminare will be switched OFF in case
        of communication failure.  (Minute)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_hour_on(v.__hour_on)
        self.__set_minute_on(v.__minute_on)
        self.__set_hour_off(v.__hour_off)
        self.__set_minute_off(v.__minute_off)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = bkupSchedule()
    pass
