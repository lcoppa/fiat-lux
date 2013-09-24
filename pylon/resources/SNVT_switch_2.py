"""SNVT_switch_2 standard datapoint type, originally defined in resource file
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.switch_state_t import switch_state_t
from pylon.resources.SNVT_multiplier_s import SNVT_multiplier_s


class SNVT_switch_2(base.Structure):
    """SNVT_switch_2 standard datapoint type.  Switch with scene and setting
    control.  An enhanced version of SNVT_switch with scene and setting
    controls similar to SNVT_scene and SNVT_setting."""

    class settingType(base.Union):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__value = base.Scaled(
                size=1,
                signed=False,
                scaling=(0.5, 0),
                invalid=127.5,
                minimum=0,
                maximum=100
            )
            self._register(('value', self.__value))

            self.__change = base.Scaled(
                size=1,
                signed=False,
                scaling=(0.5, 0),
                invalid=127.5,
                minimum=0,
                maximum=100
            )
            self._register(('change', self.__change))

            self.__delay = base.Scaled(
                size=1,
                signed=False,
                invalid=255,
                minimum=0,
                maximum=254
            )
            self._register(('delay', self.__delay))

            self.__group_number = base.Scaled(
                size=1,
                signed=False,
                invalid=255,
                minimum=0,
                maximum=63
            )
            self._register(('group_number', self.__group_number))

            self.__multiplier = SNVT_multiplier_s(
            )
            self._register(('multiplier', self.__multiplier))

            self.__angle = base.Scaled(
                size=1,
                signed=True,
                scaling=(2, 0),
                invalid=-256,
                minimum=-180,
                maximum=180
            )
            self._register(('angle', self.__angle))

            self.__fan_level = base.Scaled(
                size=1,
                signed=True,
                invalid=-128,
                minimum=-100,
                maximum=100
            )
            self._register(('fan_level', self.__fan_level))

            self.__button_number = base.Scaled(
                size=1,
                signed=False,
                invalid=0,
                minimum=0,
                maximum=255
            )
            self._register(('button_number', self.__button_number))

        def __set_value(self, v):
            self.__value._value = v

        value = property(
            lambda self: self.__value._value,
            __set_value,
            None,
            """Value Percent of full level when state is on.  Reports last
            level for outputs when state is off."""
        )

        def __set_change(self, v):
            self.__change._value = v

        change = property(
            lambda self: self.__change._value,
            __set_change,
            None,
            """Percent change.  Percent change to level."""
        )

        def __set_delay(self, v):
            self.__delay._value = v

        delay = property(
            lambda self: self.__delay._value,
            __set_delay,
            None,
            """On or off delay (seconds) Time delay before changing state to
            on or off.  (seconds)."""
        )

        def __set_group_number(self, v):
            self.__group_number._value = v

        group_number = property(
            lambda self: self.__group_number._value,
            __set_group_number,
            None,
            """Group number.  Group number that is enabled or disabled by the
            SW_ENABLE_GROUP and SW_DISABLE_GROUIP states in the state field;
            if 0, all groups are enabled or disabled."""
        )

        def __set_multiplier(self, v):
            self.__multiplier._value = v

        multiplier = property(
            lambda self: self.__multiplier._value,
            __set_multiplier,
            None,
            """Factor Multiplier for the level.  (percent)."""
        )

        def __set_angle(self, v):
            self.__angle._value = v

        angle = property(
            lambda self: self.__angle._value,
            __set_angle,
            None,
            """Rotation angle.  Rotation angle for devices that support a
            rotation setting such as blinds.  (degrees)."""
        )

        def __set_fan_level(self, v):
            self.__fan_level._value = v

        fan_level = property(
            lambda self: self.__fan_level._value,
            __set_fan_level,
            None,
            """Fan level.  Percent of full level fan speed when state is on.
            Reports last fan speed for outputs when state is off.  Positive
            values represent the down direction, and negative values
            represent the up direction."""
        )

        def __set_button_number(self, v):
            self.__button_number._value = v

        button_number = property(
            lambda self: self.__button_number._value,
            __set_button_number,
            None,
            """Button number.  The button number to activate when the state
            field is set to SW_SET_BUTTON, no invalid value."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_value(v.__value)
            self.__set_change(v.__change)
            self.__set_delay(v.__delay)
            self.__set_group_number(v.__group_number)
            self.__set_multiplier(v.__multiplier)
            self.__set_angle(v.__angle)
            self.__set_fan_level(v.__fan_level)
            self.__set_button_number(v.__button_number)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=189,
            scope=0
        )

        self.__state = switch_state_t(
        )
        self._register(('state', self.__state))

        self.__setting = SNVT_switch_2.settingType(
        )
        self._register(('setting', self.__setting))

        self.__scene_number = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=255
        )
        self._register(('scene_number', self.__scene_number))
        self._definition = standard.add(self)


    def __set_state(self, v):
        self.__state._value = v

    state = property(
        lambda self: self.__state._value,
        __set_state,
        None,
        """Switch state.  Switch state;  may be a state of the switch or
        other switch properties such as scene, occupancy state, and level
        multiplier."""
    )

    def __set_setting(self, v):
        self.__setting._value = v

    setting = property(
        lambda self: self.__setting._value,
        __set_setting,
        None,
        """Switch setting.  Sets or reports the level, change, or angle for a
        switch."""
    )

    def __set_scene_number(self, v):
        self.__scene_number._value = v

    scene_number = property(
        lambda self: self.__scene_number._value,
        __set_scene_number,
        None,
        """Scene number.  Scene or group number that is applied based on the
        function specified in the state field.  Specifies a scene number for
        all scene-related functions.  Specifies a group number for the
        SW_SET_GROUP_STATE_LEVEL state."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_state(v.__state)
        self.__set_setting(v.__setting)
        self.__set_scene_number(v.__scene_number)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 3


if __name__ == '__main__':
    # unit test code.
    item = SNVT_switch_2()
    pass
