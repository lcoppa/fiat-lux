"""sceneTiming standard property type, originally defined in resource file
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


class sceneTiming(pylon.resources.base.Structure):
    """sceneTiming standard property type.  Scene timing configuration.
    Scene timing definition used to supplement a scene table created with a
    SCPTscene array.  This SCPT defines the optional scene table entries for
    the ISI profiles.  When used, it must be used in combination with a
    SCPTscene array."""

    def __init__(self):
        super().__init__(
            key=308,
            scope=0
        )

        self.__fade_time = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            scaling=(0.1, 0),
            minimum=0,
            maximum=6553.5
        )
        self._register(('fade_time', self.__fade_time))

        self.__delay_time = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            scaling=(0.1, 0),
            minimum=0,
            maximum=6553.5
        )
        self._register(('delay_time', self.__delay_time))
        self._default_bytes = b'\x00\x00\x00\x00'
        self._original_name = 'SCPTsceneTiming'
        self._property_scope, self._property_key = 0, 308
        self._definition = standard.add(self)

    def __set_fade_time(self, v):
        self.__fade_time._value = v

    fade_time = property(
        lambda self: self.__fade_time._value,
        __set_fade_time,
        None,
        """Scene fade time.  Time to ramp to a new setting.  Fading starts
        after any delay specified by the delay_time field, so the total time
        to move to a new value is delay_time plus fade_time seconds.
        (seconds)."""
    )

    def __set_delay_time(self, v):
        self.__delay_time._value = v

    delay_time = property(
        lambda self: self.__delay_time._value,
        __set_delay_time,
        None,
        """Scene delay time.  Delay time from the time a new scene is
        selected until any change is made to the light intensity or appliance
        state.  (seconds)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_fade_time(v.__fade_time)
        self.__set_delay_time(v.__delay_time)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = sceneTiming()
    pass
