"""UNVT_iot_analog userdefined datapoint type, originally defined in resource
file set iot 90:00:00:05:00:00:00:00-1.  """


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
# Generated at 12-Sep-2013 11:24.

from pylon.resources import base
from pylon.resources.userdefined import userdefined
from pylon.resources.command_priority_t import command_priority_t
from pylon.resources.UNVT_iot_timestamp import UNVT_iot_timestamp
from pylon.resources.UNVT_iot_status_flags import UNVT_iot_status_flags
from pylon.resources.event_state_t import event_state_t
from pylon.resources.reliability_t import reliability_t
from pylon.resources.engineering_units_t import engineering_units_t


class UNVT_iot_analog(base.Structure):
    """UNVT_iot_analog userdefined datapoint type.  IoT analog.  Analog value
    with units, timestamp, status, and priority."""

    def __init__(self):
        super().__init__(
            key=4,
            scope=1
        )

        self.__present_value = base.Float(
            single=True,
            minimum=-3.40282E+038,
            maximum=3.40282E+038
        )
        self._register(('present_value', self.__present_value))

        self.__priority = command_priority_t(
        )
        self._register(('priority', self.__priority))

        self.__update_time = UNVT_iot_timestamp(
        )
        self._register(('update_time', self.__update_time))

        self.__status_flags = UNVT_iot_status_flags(
        )
        self._register(('status_flags', self.__status_flags))

        self.__event_state = event_state_t(
        )
        self._register(('event_state', self.__event_state))

        self.__reliability = reliability_t(
        )
        self._register(('reliability', self.__reliability))

        self.__units = engineering_units_t(
        )
        self._register(('units', self.__units))
        self._definition = userdefined.add(self)


    def __set_present_value(self, v):
        self.__present_value._value = v

    present_value = property(
        lambda self: self.__present_value._value,
        __set_present_value,
        None,
        """Analog value."""
    )

    def __set_priority(self, v):
        self.__priority._value = v

    priority = property(
        lambda self: self.__priority._value,
        __set_priority,
        None,
        """Priority Priority for arbitrating between updates from multiple
        applications."""
    )

    def __set_update_time(self, v):
        self.__update_time._value = v

    update_time = property(
        lambda self: self.__update_time._value,
        __set_update_time,
        None,
        """Update time.  Date and time of the update."""
    )

    def __set_status_flags(self, v):
        self.__status_flags._value = v

    status_flags = property(
        lambda self: self.__status_flags._value,
        __set_status_flags,
        None,
        """Status flags."""
    )

    def __set_event_state(self, v):
        self.__event_state._value = v

    event_state = property(
        lambda self: self.__event_state._value,
        __set_event_state,
        None,
        """Event state.  Present event state;  set to EVS_NORMAL for normal
        operation."""
    )

    def __set_reliability(self, v):
        self.__reliability._value = v

    reliability = property(
        lambda self: self.__reliability._value,
        __set_reliability,
        None,
        """Reliability Set to REL_NO_FAULT_DETECTED if the reported value is
        reliable."""
    )

    def __set_units(self, v):
        self.__units._value = v

    units = property(
        lambda self: self.__units._value,
        __set_units,
        None,
        """Units Engineering units for the present_value."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_present_value(v.__present_value)
        self.__set_priority(v.__priority)
        self.__set_update_time(v.__update_time)
        self.__set_status_flags(v.__status_flags)
        self.__set_event_state(v.__event_state)
        self.__set_reliability(v.__reliability)
        self.__set_units(v.__units)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 17


if __name__ == '__main__':
    # unit test code.
    item = UNVT_iot_analog()
    pass
