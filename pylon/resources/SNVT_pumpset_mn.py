"""SNVT_pumpset_mn standard datapoint type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0.  """


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
from pylon.resources.motor_state_t import motor_state_t
from pylon.resources.priority_level_t import priority_level_t
from pylon.resources.boolean_t import boolean_t


class SNVT_pumpset_mn(base.Structure):
    """SNVT_pumpset_mn standard datapoint type.  Pumpset (main, booster,
    priority, ready, emerg, main enabled, booster enabled, maint.)."""

    def __init__(self):
        super().__init__(
            key=156,
            scope=0
        )

        self.__main_pump = motor_state_t(
        )
        self._register(('main_pump', self.__main_pump))

        self.__booster_pump = motor_state_t(
        )
        self._register(('booster_pump', self.__booster_pump))

        self.__priority_level = priority_level_t(
        )
        self._register(('priority_level', self.__priority_level))

        self.__process_ready = boolean_t(
        )
        self._register(('process_ready', self.__process_ready))

        self.__emergency_stop_activated = boolean_t(
        )
        self._register(('emergency_stop_activated', self.__emergency_stop_activated))

        self.__main_pump_drive_enabled = boolean_t(
        )
        self._register(('main_pump_drive_enabled', self.__main_pump_drive_enabled))

        self.__booster_pump_drive_enabled = boolean_t(
        )
        self._register(('booster_pump_drive_enabled', self.__booster_pump_drive_enabled))

        self.__maintenance_required = boolean_t(
        )
        self._register(('maintenance_required', self.__maintenance_required))
        self._definition = standard.add(self)


    def __set_main_pump(self, v):
        self.__main_pump._value = v

    main_pump = property(
        lambda self: self.__main_pump._value,
        __set_main_pump,
        None,
        """Main pump state.  (motor state names.)."""
    )

    def __set_booster_pump(self, v):
        self.__booster_pump._value = v

    booster_pump = property(
        lambda self: self.__booster_pump._value,
        __set_booster_pump,
        None,
        """Booster pump state.  (motor state names.)."""
    )

    def __set_priority_level(self, v):
        self.__priority_level._value = v

    priority_level = property(
        lambda self: self.__priority_level._value,
        __set_priority_level,
        None,
        """Priority level.  (priority level names.)."""
    )

    def __set_process_ready(self, v):
        self.__process_ready._value = v

    process_ready = property(
        lambda self: self.__process_ready._value,
        __set_process_ready,
        None,
        """Process ready.  (boolean)."""
    )

    def __set_emergency_stop_activated(self, v):
        self.__emergency_stop_activated._value = v

    emergency_stop_activated = property(
        lambda self: self.__emergency_stop_activated._value,
        __set_emergency_stop_activated,
        None,
        """Emergency stop.  (boolean)."""
    )

    def __set_main_pump_drive_enabled(self, v):
        self.__main_pump_drive_enabled._value = v

    main_pump_drive_enabled = property(
        lambda self: self.__main_pump_drive_enabled._value,
        __set_main_pump_drive_enabled,
        None,
        """Main pump enabled.  (boolean)."""
    )

    def __set_booster_pump_drive_enabled(self, v):
        self.__booster_pump_drive_enabled._value = v

    booster_pump_drive_enabled = property(
        lambda self: self.__booster_pump_drive_enabled._value,
        __set_booster_pump_drive_enabled,
        None,
        """Booster pump enabled.  (boolean)."""
    )

    def __set_maintenance_required(self, v):
        self.__maintenance_required._value = v

    maintenance_required = property(
        lambda self: self.__maintenance_required._value,
        __set_maintenance_required,
        None,
        """Maintenance required.  (boolean)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_main_pump(v.__main_pump)
        self.__set_booster_pump(v.__booster_pump)
        self.__set_priority_level(v.__priority_level)
        self.__set_process_ready(v.__process_ready)
        self.__set_emergency_stop_activated(v.__emergency_stop_activated)
        self.__set_main_pump_drive_enabled(v.__main_pump_drive_enabled)
        self.__set_booster_pump_drive_enabled(v.__booster_pump_drive_enabled)
        self.__set_maintenance_required(v.__maintenance_required)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 8


if __name__ == '__main__':
    # unit test code.
    item = SNVT_pumpset_mn()
    pass
