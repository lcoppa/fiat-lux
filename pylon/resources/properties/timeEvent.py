"""timeEvent standard property type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.enumerations.event_mode_type_t


class timeEvent(pylon.resources.base.Structure):
    """timeEvent standard property type.  Time event entry.  Event or mode
    definitions to be transmitted if the time in the record is reached.
    (record type, hour, minute, event mode.)."""

    def __init__(self):
        super().__init__(
            key=104,
            scope=0
        )

        self.__record_type = pylon.resources.enumerations.event_mode_type_t.event_mode_type_t(
        )
        self._register(('record_type', self.__record_type))

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

        self.__event_mode = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('event_mode', self.__event_mode))
        self._default_bytes = b'\x00\x00\x00\x00'
        self._original_name = 'SCPTtimeEvent'
        self._property_scope, self._property_key = 0, 104
        self._definition = standard.add(self)

    def __set_record_type(self, v):
        self.__record_type._value = v

    record_type = property(
        lambda self: self.__record_type._value,
        __set_record_type,
        None,
        """Type of time event record.  (time event record type names.)."""
    )

    def __set_hour(self, v):
        self.__hour._value = v

    hour = property(
        lambda self: self.__hour._value,
        __set_hour,
        None,
        """Hour (hours)."""
    )

    def __set_minute(self, v):
        self.__minute._value = v

    minute = property(
        lambda self: self.__minute._value,
        __set_minute,
        None,
        """Minute (minutes)."""
    )

    def __set_event_mode(self, v):
        self.__event_mode._value = v

    event_mode = property(
        lambda self: self.__event_mode._value,
        __set_event_mode,
        None,
        """Event mode information.  (event mode number.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_record_type(v.__record_type)
        self.__set_hour(v.__hour)
        self.__set_minute(v.__minute)
        self.__set_event_mode(v.__event_mode)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = timeEvent()
    pass
