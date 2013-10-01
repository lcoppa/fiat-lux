"""iot_dev_status userdefined datapoint type, originally defined in resource
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.userdefined import userdefined
import pylon.resources.enumerations.device_status_t
import pylon.resources.datapoints.iot_timestamp
import pylon.resources.enumerations.restart_reason_t
import pylon.resources.enumerations.backup_and_restore_states_t


class iot_dev_status(pylon.resources.base.Structure):
    """iot_dev_status userdefined datapoint type.  IoT device status.
    Reliability evaluation inhibit."""

    def __init__(self):
        super().__init__(
            key=6,
            scope=1
        )

        self.__device_status = pylon.resources.enumerations.device_status_t.device_status_t(
        )
        self._register(('device_status', self.__device_status))

        self.__start_time = pylon.resources.datapoints.iot_timestamp.iot_timestamp(
        )
        self._register(('start_time', self.__start_time))

        self.__restart_reason = pylon.resources.enumerations.restart_reason_t.restart_reason_t(
        )
        self._register(('restart_reason', self.__restart_reason))

        self.__restart_time = pylon.resources.datapoints.iot_timestamp.iot_timestamp(
        )
        self._register(('restart_time', self.__restart_time))

        self.__error_time = pylon.resources.datapoints.iot_timestamp.iot_timestamp(
        )
        self._register(('error_time', self.__error_time))

        self.__restore_time = pylon.resources.datapoints.iot_timestamp.iot_timestamp(
        )
        self._register(('restore_time', self.__restore_time))

        self.__backup_and_restore_state = pylon.resources.enumerations.backup_and_restore_states_t.backup_and_restore_states_t(
        )
        self._register(('backup_and_restore_state', self.__backup_and_restore_state))
        self._original_name = 'UNVT_iot_dev_status'
        self._definition = userdefined.add(self)


    def __set_device_status(self, v):
        self.__device_status._value = v

    device_status = property(
        lambda self: self.__device_status._value,
        __set_device_status,
        None,
        """Device status."""
    )

    def __set_start_time(self, v):
        self.__start_time._value = v

    start_time = property(
        lambda self: self.__start_time._value,
        __set_start_time,
        None,
        """Start time.  Date and time device was first placed into
        operation."""
    )

    def __set_restart_reason(self, v):
        self.__restart_reason._value = v

    restart_reason = property(
        lambda self: self.__restart_reason._value,
        __set_restart_reason,
        None,
        """Restart reason.  Reason of last device restart."""
    )

    def __set_restart_time(self, v):
        self.__restart_time._value = v

    restart_time = property(
        lambda self: self.__restart_time._value,
        __set_restart_time,
        None,
        """Restart time.  Date and time of last device restart."""
    )

    def __set_error_time(self, v):
        self.__error_time._value = v

    error_time = property(
        lambda self: self.__error_time._value,
        __set_error_time,
        None,
        """Error time.  Date and time of last reported error."""
    )

    def __set_restore_time(self, v):
        self.__restore_time._value = v

    restore_time = property(
        lambda self: self.__restore_time._value,
        __set_restore_time,
        None,
        """Restore time.  Date and time of last restore operation."""
    )

    def __set_backup_and_restore_state(self, v):
        self.__backup_and_restore_state._value = v

    backup_and_restore_state = property(
        lambda self: self.__backup_and_restore_state._value,
        __set_backup_and_restore_state,
        None,
        """."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_device_status(v.__device_status)
        self.__set_start_time(v.__start_time)
        self.__set_restart_reason(v.__restart_reason)
        self.__set_restart_time(v.__restart_time)
        self.__set_error_time(v.__error_time)
        self.__set_restore_time(v.__restore_time)
        self.__set_backup_and_restore_state(v.__backup_and_restore_state)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 35


if __name__ == '__main__':
    # unit test code.
    item = iot_dev_status()
    pass
