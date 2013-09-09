"""SCPTbuttonPressAction standard property type, originally defined in
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.button_action_t import button_action_t


class SCPTbuttonPressAction(base.Structure):
    """SCPTbuttonPressAction standard property type.  Button pressed action.
    Button action definition used to create a button pressed action array,
    with an entry per button.  This SCPT defines the minimum entries required
    by the ISI profiles."""

    class settingType(base.Union):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__scene_number = base.Scaled(
                size=1,
                signed=False,
                invalid=0,
                minimum=1,
                maximum=255
            )
            self._register(('scene_number', self.__scene_number))

            self.__group_number = base.Scaled(
                size=1,
                signed=False,
                invalid=255,
                minimum=0,
                maximum=64
            )
            self._register(('group_number', self.__group_number))

            self.__value = base.Scaled(
                size=1,
                signed=False,
                scaling=(0.5, 0),
                invalid=127.5,
                minimum=0,
                maximum=100
            )
            self._register(('value', self.__value))

            self.__angle = base.Scaled(
                size=1,
                signed=True,
                invalid=127,
                minimum=-90,
                maximum=90
            )
            self._register(('angle', self.__angle))

        def __set_scene_number(self, v):
            self.__scene_number._value = v

        scene_number = property(
            lambda self: self.__scene_number._value,
            __set_scene_number,
            None,
            """Scene number.  Specified scene number for the toggle and set
            scene actions."""
        )

        def __set_group_number(self, v):
            self.__group_number._value = v

        group_number = property(
            lambda self: self.__group_number._value,
            __set_group_number,
            None,
            """Group number.  Specified group number for the toggle, enable,
            and disable group actions."""
        )

        def __set_value(self, v):
            self.__value._value = v

        value = property(
            lambda self: self.__value._value,
            __set_value,
            None,
            """Setting.  Setting level.  Specifies an absoloute level for the
            Set Level action.  Specifies a relative level for the Increase,
            Decrease, Move Open, Move Closed, Rotate Open, and Rotate Closed
            actions."""
        )

        def __set_angle(self, v):
            self.__angle._value = v

        angle = property(
            lambda self: self.__angle._value,
            __set_angle,
            None,
            """(degrees)."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_scene_number(v.__scene_number)
            self.__set_group_number(v.__group_number)
            self.__set_value(v.__value)
            self.__set_angle(v.__angle)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=311,
            scope=0
        )

        self.__action = button_action_t(
        )
        self._register(('action', self.__action))

        self.__setting = SCPTbuttonPressAction.settingType(
        )
        self._register(('setting', self.__setting))
        self._default_bytes = b'\x00\x00'
        self._property_scope, self._property_key = 0, 311
        self._definition = standard.add(self)

    def __set_action(self, v):
        self.__action._value = v

    action = property(
        lambda self: self.__action._value,
        __set_action,
        None,
        """Button action.  Button action for the associated button."""
    )

    def __set_setting(self, v):
        self.__setting._value = v

    setting = property(
        lambda self: self.__setting._value,
        __set_setting,
        None,
        """Value.  Value for button actions that require a numeric value."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_action(v.__action)
        self.__set_setting(v.__setting)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 2


if __name__ == '__main__':
    # unit test code.
    item = SCPTbuttonPressAction()
    pass
