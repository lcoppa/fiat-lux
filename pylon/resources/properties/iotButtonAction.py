"""iotButtonAction userdefined property type, originally defined in resource
file set iot 90:00:00:05:00:00:00:00-1."""


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
import pylon.resources.enumerations.button_qualifier_t


class iotButtonAction(pylon.resources.base.Structure):
    """iotButtonAction userdefined property type.  IoT button action.  Button
    action definition used to create a button action array, with an entry per
    button on a keypad or other user interface device."""

    class button_iconType(pylon.resources.base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__icon_id = pylon.resources.base.Scaled(
                size=2,
                signed=False,
                invalid=65535,
                minimum=0,
                maximum=65534
            )
            self._register(('icon_id', self.__icon_id))

            self.__top_left_x = pylon.resources.base.Scaled(
                size=2,
                signed=False,
                invalid=65535,
                minimum=0,
                maximum=65534
            )
            self._register(('top_left_x', self.__top_left_x))

            self.__top_left_y = pylon.resources.base.Scaled(
                size=2,
                signed=False,
                invalid=255,
                minimum=0,
                maximum=255
            )
            self._register(('top_left_y', self.__top_left_y))

        def __set_icon_id(self, v):
            self.__icon_id._value = v

        icon_id = property(
            lambda self: self.__icon_id._value,
            __set_icon_id,
            None,
            """Button icon ID.  ID for the icon to be displayed."""
        )

        def __set_top_left_x(self, v):
            self.__top_left_x._value = v

        top_left_x = property(
            lambda self: self.__top_left_x._value,
            __set_top_left_x,
            None,
            """Button icon x coordinate.  X coordinate for top left corner of
            the button icon."""
        )

        def __set_top_left_y(self, v):
            self.__top_left_y._value = v

        top_left_y = property(
            lambda self: self.__top_left_y._value,
            __set_top_left_y,
            None,
            """Button icon y coordinate.  Y coordinate for top left corner of
            the button icon."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_icon_id(v.__icon_id)
            self.__set_top_left_x(v.__top_left_x)
            self.__set_top_left_y(v.__top_left_y)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 6

    def __init__(self):
        super().__init__(
            key=3,
            scope=1
        )

        self.__button_number = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65534
        )
        self._register(('button_number', self.__button_number))

        self.__action_qualifier = pylon.resources.enumerations.button_qualifier_t.button_qualifier_t(
        )
        self._register(('action_qualifier', self.__action_qualifier))

        self.__state_qualifier = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=254
        )
        self._register(('state_qualifier', self.__state_qualifier))

        self.__scene_number = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65534
        )
        self._register(('scene_number', self.__scene_number))

        self.__button_icon = iotButtonAction.button_iconType(
        )
        self._register(('button_icon', self.__button_icon))

        self.__repeat_delay = pylon.resources.base.Float(
            single=True,
            minimum=0,
            maximum=3.40282E+038
        )
        self._register(('repeat_delay', self.__repeat_delay))

        self.__repeat_interval = pylon.resources.base.Float(
            single=True,
            minimum=0,
            maximum=3.40282E+038
        )
        self._register(('repeat_interval', self.__repeat_interval))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self._original_name = 'UCPTiotButtonAction'
        self._property_scope, self._property_key = 1, 3
        self._definition = userdefined.add(self)

    def __set_button_number(self, v):
        self.__button_number._value = v

    button_number = property(
        lambda self: self.__button_number._value,
        __set_button_number,
        None,
        """Button number.  Button number on the device;  there may be
        multiple entries with the same button number to define a series of
        events for a particular button."""
    )

    def __set_action_qualifier(self, v):
        self.__action_qualifier._value = v

    action_qualifier = property(
        lambda self: self.__action_qualifier._value,
        __set_action_qualifier,
        None,
        """Action qualifer.  Button action qualification--one of BTQ_PRESS,
        BTQ_HOLD, or BTQ_RELEASE."""
    )

    def __set_state_qualifier(self, v):
        self.__state_qualifier._value = v

    state_qualifier = property(
        lambda self: self.__state_qualifier._value,
        __set_state_qualifier,
        None,
        """Previous button state.  Previouse state of the button used to
        implement multi-state buttons;  for example, a toggle button can be
        implemented with an on button action that requires a previous state
        of off, and an off button action that requires a previous state of
        on."""
    )

    def __set_scene_number(self, v):
        self.__scene_number._value = v

    scene_number = property(
        lambda self: self.__scene_number._value,
        __set_scene_number,
        None,
        """Scene number.  Scene number that is applied based on the function
        specified in the state field."""
    )

    def __set_button_icon(self, v):
        self.__button_icon._value = v

    button_icon = property(
        lambda self: self.__button_icon._value,
        __set_button_icon,
        None,
        """Button icon."""
    )

    def __set_repeat_delay(self, v):
        self.__repeat_delay._value = v

    repeat_delay = property(
        lambda self: self.__repeat_delay._value,
        __set_repeat_delay,
        None,
        """Repeat delay.  Time that button must be held before the button
        action is repeated the first time."""
    )

    def __set_repeat_interval(self, v):
        self.__repeat_interval._value = v

    repeat_interval = property(
        lambda self: self.__repeat_interval._value,
        __set_repeat_interval,
        None,
        """Repeat interval.  Time between updates when a button is held
        down;  the updates themselves may be throttled by the application or
        a SCPTnetworkTime CP."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_button_number(v.__button_number)
        self.__set_action_qualifier(v.__action_qualifier)
        self.__set_state_qualifier(v.__state_qualifier)
        self.__set_scene_number(v.__scene_number)
        self.__set_button_icon(v.__button_icon)
        self.__set_repeat_delay(v.__repeat_delay)
        self.__set_repeat_interval(v.__repeat_interval)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 20


if __name__ == '__main__':
    # unit test code.
    item = iotButtonAction()
    pass
