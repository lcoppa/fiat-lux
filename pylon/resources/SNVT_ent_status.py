"""SNVT_ent_status standard datapoint type, originally defined in resource
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
from pylon.resources.ent_opmode_cmd_t import ent_opmode_cmd_t


class SNVT_ent_status(base.Structure):
    """SNVT_ent_status standard datapoint type.  Entry status.  Status
    information from an entry object, e.g., a door, lock, sluice, or
    something that allows/prohibits entry into an area."""

    def __init__(self):
        super().__init__(
            key=170,
            scope=0
        )

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.___bf01 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf01', self.___bf01))

        self.___bf02 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf02', self.___bf02))

        self.___bf03 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf03', self.___bf03))

        self.__cmd_fb = ent_opmode_cmd_t(
        )
        self._register(('cmd_fb', self.__cmd_fb))
        self._definition = standard.add(self)

    def __set_unlocked(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_unlocked(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    unlocked = property(
        __get_unlocked,
        __set_unlocked,
        None,
        """Unlocked device.  Device is in unlocked position.  (boolean)"""
    )

    def __set_locked(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_locked(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    locked = property(
        __get_locked,
        __set_locked,
        None,
        """Locked device.  Device is in locked position.  (boolean)"""
    )

    def __set_security_locked(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_security_locked(self):
        return self.___bf00._getbits(
            size=1,
            offset=2,
            signed=False
        )

    security_locked = property(
        __get_security_locked,
        __set_security_locked,
        None,
        """Security locked.  Device is in a security-driven locked position.
        (boolean)"""
    )

    def __set_closed(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_closed(self):
        return self.___bf00._getbits(
            size=1,
            offset=3,
            signed=False
        )

    closed = property(
        __get_closed,
        __set_closed,
        None,
        """Closed device.  Device is in a closed position.  (boolean)"""
    )

    def __set_open_(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_open_(self):
        return self.___bf00._getbits(
            size=1,
            offset=4,
            signed=False
        )

    open_ = property(
        __get_open_,
        __set_open_,
        None,
        """Open device.  Device is in an open position.  (boolean)"""
    )

    def __set_in_alarm(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_in_alarm(self):
        return self.___bf00._getbits(
            size=1,
            offset=5,
            signed=False
        )

    in_alarm = property(
        __get_in_alarm,
        __set_in_alarm,
        None,
        """In alarm state.  The device is in the alarm state.  (boolean)"""
    )

    def __set_in_error_cond(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_in_error_cond(self):
        return self.___bf00._getbits(
            size=1,
            offset=6,
            signed=False
        )

    in_error_cond = property(
        __get_in_error_cond,
        __set_in_error_cond,
        None,
        """In error condition.  Device has an error condition.  (boolean)"""
    )

    def __set_open_pre_alarm(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_open_pre_alarm(self):
        return self.___bf00._getbits(
            size=1,
            offset=7,
            signed=False
        )

    open_pre_alarm = property(
        __get_open_pre_alarm,
        __set_open_pre_alarm,
        None,
        """Open device, pre-alarm.  Device is open, and in warning state.
        (boolean)"""
    )

    def __set_open_alarm(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_open_alarm(self):
        return self.___bf01._getbits(
            size=1,
            offset=0,
            signed=False
        )

    open_alarm = property(
        __get_open_alarm,
        __set_open_alarm,
        None,
        """Open Device, alarm state.  Device is open, and in not-closed alarm
        state.  (boolean)"""
    )

    def __set_service_alarm(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_service_alarm(self):
        return self.___bf01._getbits(
            size=1,
            offset=1,
            signed=False
        )

    service_alarm = property(
        __get_service_alarm,
        __set_service_alarm,
        None,
        """Service alarm.  Device needs service.  (boolean)"""
    )

    def __set_tamper(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_tamper(self):
        return self.___bf01._getbits(
            size=1,
            offset=2,
            signed=False
        )

    tamper = property(
        __get_tamper,
        __set_tamper,
        None,
        """Tamper mode.  Device has detected tamper.  (boolean)"""
    )

    def __set_entry_req(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_entry_req(self):
        return self.___bf01._getbits(
            size=1,
            offset=3,
            signed=False
        )

    entry_req = property(
        __get_entry_req,
        __set_entry_req,
        None,
        """Entry request pending.  Device has a pending entry request.
        (boolean)"""
    )

    def __set_exit_req(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_exit_req(self):
        return self.___bf01._getbits(
            size=1,
            offset=4,
            signed=False
        )

    exit_req = property(
        __get_exit_req,
        __set_exit_req,
        None,
        """Exit request pending.  Device has a pending exit request.
        (boolean)"""
    )

    def __set_key_req(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_key_req(self):
        return self.___bf01._getbits(
            size=1,
            offset=5,
            signed=False
        )

    key_req = property(
        __get_key_req,
        __set_key_req,
        None,
        """Key request pending.  Device has a pending key request.
        (boolean)"""
    )

    def __set_safety_ext_req(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_safety_ext_req(self):
        return self.___bf01._getbits(
            size=1,
            offset=6,
            signed=False
        )

    safety_ext_req = property(
        __get_safety_ext_req,
        __set_safety_ext_req,
        None,
        """Safety-exit request pending.  Device has a pending safety-exit
        request.  (boolean)"""
    )

    def __set_emergency_req(self, v):
        if 0 <= v <= 1:
            self.___bf01._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_emergency_req(self):
        return self.___bf01._getbits(
            size=1,
            offset=7,
            signed=False
        )

    emergency_req = property(
        __get_emergency_req,
        __set_emergency_req,
        None,
        """Emergency-exit request pending.  Device has a pending
        emergency-exit request.  (boolean)"""
    )

    def __set_unable_lock(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_unable_lock(self):
        return self.___bf02._getbits(
            size=1,
            offset=0,
            signed=False
        )

    unable_lock = property(
        __get_unable_lock,
        __set_unable_lock,
        None,
        """Unable to lock.  Device is unable to close and/or lock.
        (boolean)"""
    )

    def __set_unable_unlock(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_unable_unlock(self):
        return self.___bf02._getbits(
            size=1,
            offset=1,
            signed=False
        )

    unable_unlock = property(
        __get_unable_unlock,
        __set_unable_unlock,
        None,
        """Unable to unlock.  Device is unable to open and/or unlock.
        (boolean)"""
    )

    def __set_stuck(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_stuck(self):
        return self.___bf02._getbits(
            size=1,
            offset=2,
            signed=False
        )

    stuck = property(
        __get_stuck,
        __set_stuck,
        None,
        """Device is stuck.  Device is unable to move.  (boolean)"""
    )

    def __set_forced_open(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=3,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_forced_open(self):
        return self.___bf02._getbits(
            size=1,
            offset=3,
            signed=False
        )

    forced_open = property(
        __get_forced_open,
        __set_forced_open,
        None,
        """Forced-open Device.  Device is/was forced to go to an open
        position.  (boolean)"""
    )

    def __set_forced_close(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=4,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_forced_close(self):
        return self.___bf02._getbits(
            size=1,
            offset=4,
            signed=False
        )

    forced_close = property(
        __get_forced_close,
        __set_forced_close,
        None,
        """Forced-closed Device.  Device is/was forced to go to a closed
        position.  (boolean)"""
    )

    def __set_opening(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=5,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_opening(self):
        return self.___bf02._getbits(
            size=1,
            offset=5,
            signed=False
        )

    opening = property(
        __get_opening,
        __set_opening,
        None,
        """Device is opening.  Device is currently opening from a closed
        position.  (boolean)"""
    )

    def __set_closing(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=6,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_closing(self):
        return self.___bf02._getbits(
            size=1,
            offset=6,
            signed=False
        )

    closing = property(
        __get_closing,
        __set_closing,
        None,
        """Device is closing.  Device is currently closing from an open
        position.  (boolean)"""
    )

    def __set_moving(self, v):
        if 0 <= v <= 1:
            self.___bf02._setbits(
                value=v,
                size=1,
                offset=7,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_moving(self):
        return self.___bf02._getbits(
            size=1,
            offset=7,
            signed=False
        )

    moving = property(
        __get_moving,
        __set_moving,
        None,
        """Device is in motion.  Device is currently changing position.
        (boolean)"""
    )

    def __set_stopped(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_stopped(self):
        return self.___bf03._getbits(
            size=1,
            offset=0,
            signed=False
        )

    stopped = property(
        __get_stopped,
        __set_stopped,
        None,
        """Device Stopped.  The device is stopped and can be moved manually.
        (boolean)"""
    )

    def __set_safety_alarm(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_safety_alarm(self):
        return self.___bf03._getbits(
            size=1,
            offset=1,
            signed=False
        )

    safety_alarm = property(
        __get_safety_alarm,
        __set_safety_alarm,
        None,
        """Safety-alarm Device is in a safety-alarm state.  (boolean)"""
    )

    def __set_unknown_state(self, v):
        if 0 <= v <= 1:
            self.___bf03._setbits(
                value=v,
                size=1,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_unknown_state(self):
        return self.___bf03._getbits(
            size=1,
            offset=2,
            signed=False
        )

    unknown_state = property(
        __get_unknown_state,
        __set_unknown_state,
        None,
        """Unknown state.  The state of the device is currently unknown.
        (boolean)"""
    )


    def __set_cmd_fb(self, v):
        self.__cmd_fb._value = v

    cmd_fb = property(
        lambda self: self.__cmd_fb._value,
        __set_cmd_fb,
        None,
        """Command feedback.  Feedback of requested-operation-mode of
        device.  (entry command names.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_unlocked(v.__unlocked)
        self.__set_locked(v.__locked)
        self.__set_security_locked(v.__security_locked)
        self.__set_closed(v.__closed)
        self.__set_open_(v.__open_)
        self.__set_in_alarm(v.__in_alarm)
        self.__set_in_error_cond(v.__in_error_cond)
        self.__set_open_pre_alarm(v.__open_pre_alarm)
        self.__set_open_alarm(v.__open_alarm)
        self.__set_service_alarm(v.__service_alarm)
        self.__set_tamper(v.__tamper)
        self.__set_entry_req(v.__entry_req)
        self.__set_exit_req(v.__exit_req)
        self.__set_key_req(v.__key_req)
        self.__set_safety_ext_req(v.__safety_ext_req)
        self.__set_emergency_req(v.__emergency_req)
        self.__set_unable_lock(v.__unable_lock)
        self.__set_unable_unlock(v.__unable_unlock)
        self.__set_stuck(v.__stuck)
        self.__set_forced_open(v.__forced_open)
        self.__set_forced_close(v.__forced_close)
        self.__set_opening(v.__opening)
        self.__set_closing(v.__closing)
        self.__set_moving(v.__moving)
        self.__set_stopped(v.__stopped)
        self.__set_safety_alarm(v.__safety_alarm)
        self.__set_unknown_state(v.__unknown_state)
        self.__set_cmd_fb(v.__cmd_fb)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 5


if __name__ == '__main__':
    # unit test code.
    item = SNVT_ent_status()
    pass
