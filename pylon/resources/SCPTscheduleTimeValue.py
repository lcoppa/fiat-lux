"""SCPTscheduleTimeValue standard property type, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.SNVT_sched_val import SNVT_sched_val


class SCPTscheduleTimeValue(base.Structure):
    """SCPTscheduleTimeValue standard property type.  Schedule time-value
    pair.  Specifies the time and value for a scheduled event."""

    def __init__(self):
        super().__init__(
            key=275,
            scope=0
        )

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.__minute = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minute', self.__minute))

        self.__value = SNVT_sched_val(
        )
        self._register(('value', self.__value))
        self._default_bytes = b'\x80\x00\xff'
        self._property_scope, self._property_key = 0, 275
        self._definition = standard.add(self)
    def __set_invalid(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_invalid(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    invalid = property(
        __get_invalid,
        __set_invalid,
        None,
        """Invalid flag.  Identifies an undefined schedule entry."""
    )

    def __set_terminator(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_terminator(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    terminator = property(
        __get_terminator,
        __set_terminator,
        None,
        """Terminator flag.  Identifies the last entry in a time-value
        list."""
    )

    def __set_hour(self, v):
        if 0 <= v <= 47:
            self.___bf00._setbits(
                value=v,
                size=6,
                offset=2
            )
        else:
            raise ValueError('Not in range 0..47')

    def __get_hour(self):
        return self.___bf00._getbits(
            size=6,
            offset=2,
            signed=False
        )

    hour = property(
        __get_hour,
        __set_hour,
        None,
        """Hour Hours since midnight for a scheduled event."""
    )


    def __set_minute(self, v):
        self.__minute._value = v

    minute = property(
        lambda self: self.__minute._value,
        __set_minute,
        None,
        """Minute Minute within the hour for a scheduled event."""
    )

    def __set_value(self, v):
        self.__value._value = v

    value = property(
        lambda self: self.__value._value,
        __set_value,
        None,
        """Scheduler value.  Specifies the value to output when a time-value
        pair is active.  The value must be mapped to a value that matches the
        type of the output network variable."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_minute(v.__minute)
        self.__set_value(v.__value)
        self.___bf00._value = v.___bf00._value

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 3


if __name__ == '__main__':
    # unit test code.
    item = SCPTscheduleTimeValue()
    pass
