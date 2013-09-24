"""UCPTiotScene userdefined property type, originally defined in resource
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
# Generated at 12-Sep-2013 11:24.

from pylon.resources import base
from pylon.resources.userdefined import userdefined
from pylon.resources.load_control_t import load_control_t
from pylon.resources.SNVT_color_2 import SNVT_color_2
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.command_priority_t import command_priority_t


class UCPTiotScene(base.Structure):
    """UCPTiotScene userdefined property type.  IoT scene.  Scene definition
    used to create a scene table, with an entry per scene."""

    class actionType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.___bf00 = base.Scaled(
                size=1,
                signed=False
            )
            self._register(('___bf00', self.___bf00))
        def __set_control(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=0
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_control(self):
            return self.___bf00._getbits(
                size=1,
                offset=0,
                signed=False
            )

        control = property(
            __get_control,
            __set_control,
            None,
            """Load control action.  Set the local device state as described
            in this scene."""
        )

        def __set_output(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=1
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_output(self):
            return self.___bf00._getbits(
                size=1,
                offset=1,
                signed=False
            )

        output = property(
            __get_output,
            __set_output,
            None,
            """Scene output action.  Update the output status of the block
            containing this scene with the fields defined in this scene;
            typically used for keypads but may also be used to implement
            scenes that cascade from device to device."""
        )


        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.___bf00._value = v.___bf00._value

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 1

    class load_groupsType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__flags = base.Array(
                [
                    base.Scaled(
                        size=1,
                        signed=False,
                        minimum=0,
                        maximum=255
                    ) for i in range(8)
                ]
            )
            self._register(('flags', self.__flags))

        def __set_flags(self, v):
            self.__flags._value = v

        flags = property(
            lambda self: self.__flags._value,
            __set_flags,
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
            self.__set_flags(v.__flags)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 8

    def __init__(self):
        super().__init__(
            key=9,
            scope=1
        )

        self.__scene_number = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65534
        )
        self._register(('scene_number', self.__scene_number))

        self.__unoccupied_scene_number = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65534
        )
        self._register(('unoccupied_scene_number', self.__unoccupied_scene_number))

        self.__standby_scene_number = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65534
        )
        self._register(('standby_scene_number', self.__standby_scene_number))

        self.__next_scene__number = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65534
        )
        self._register(('next_scene__number', self.__next_scene__number))

        self.__action = UCPTiotScene.actionType(
        )
        self._register(('action', self.__action))

        self.__control = load_control_t(
        )
        self._register(('control', self.__control))

        self.__state = base.Scaled(
            size=1,
            signed=False,
            invalid=255,
            minimum=0,
            maximum=254
        )
        self._register(('state', self.__state))

        self.__level = base.Float(
            single=True,
            minimum=0,
            maximum=100
        )
        self._register(('level', self.__level))

        self.__angle = base.Float(
            single=True,
            minimum=0,
            maximum=360
        )
        self._register(('angle', self.__angle))

        self.__color = SNVT_color_2(
        )
        self._register(('color', self.__color))

        self.__level_multiplier = base.Float(
            single=True,
            minimum=0,
            maximum=3.40282E+038
        )
        self._register(('level_multiplier', self.__level_multiplier))

        self.__reduction_multiplier = base.Float(
            single=True,
            minimum=0,
            maximum=3.40282E+038
        )
        self._register(('reduction_multiplier', self.__reduction_multiplier))

        self.__area_occupancy = SNVT_occupancy(
        )
        self._register(('area_occupancy', self.__area_occupancy))

        self.__delay = base.Float(
            single=True,
            minimum=0,
            maximum=3.40282E+038
        )
        self._register(('delay', self.__delay))

        self.__fade = base.Float(
            single=True,
            minimum=0,
            maximum=255
        )
        self._register(('fade', self.__fade))

        self.__hold = base.Float(
            single=True,
            minimum=0,
            maximum=3.40282E+038
        )
        self._register(('hold', self.__hold))

        self.__duration = base.Float(
            single=True,
            minimum=0,
            maximum=3.40282E+038
        )
        self._register(('duration', self.__duration))

        self.__priority = command_priority_t(
        )
        self._register(('priority', self.__priority))

        self.__load_groups = UCPTiotScene.load_groupsType(
        )
        self._register(('load_groups', self.__load_groups))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00'
        self._property_scope, self._property_key = 1, 9
        self._definition = userdefined.add(self)

    def __set_scene_number(self, v):
        self.__scene_number._value = v

    scene_number = property(
        lambda self: self.__scene_number._value,
        __set_scene_number,
        None,
        """Scene number.  Scene number used to uniquely identify a scene;  a
        scene number to be recalled or learned is typically received from a
        SNVT_load_control input NV;  multiple entries may specify the same
        scene;  in that case the scenes matching the requested scene number
        will be activated in array index order."""
    )

    def __set_unoccupied_scene_number(self, v):
        self.__unoccupied_scene_number._value = v

    unoccupied_scene_number = property(
        lambda self: self.__unoccupied_scene_number._value,
        __set_unoccupied_scene_number,
        None,
        """Unoccupied scene number.  Scene to be activated when the scene
        specified by scene_number is active, and an unoccupied input is
        received."""
    )

    def __set_standby_scene_number(self, v):
        self.__standby_scene_number._value = v

    standby_scene_number = property(
        lambda self: self.__standby_scene_number._value,
        __set_standby_scene_number,
        None,
        """Standby scene number.  Scene to be activated when the scene
        specified by scene_number is active, and a standby input is
        received."""
    )

    def __set_next_scene__number(self, v):
        self.__next_scene__number._value = v

    next_scene__number = property(
        lambda self: self.__next_scene__number._value,
        __set_next_scene__number,
        None,
        """Next scene number.  Scene to be activated next, after any delay,
        fade, and duration times specified for this scene;  this can be used
        to create a sequence of scenes."""
    )

    def __set_action(self, v):
        self.__action._value = v

    action = property(
        lambda self: self.__action._value,
        __set_action,
        None,
        """Scene action.  Actions triggered by this scene."""
    )

    def __set_control(self, v):
        self.__control._value = v

    control = property(
        lambda self: self.__control._value,
        __set_control,
        None,
        """Load control."""
    )

    def __set_state(self, v):
        self.__state._value = v

    state = property(
        lambda self: self.__state._value,
        __set_state,
        None,
        """Load state.  State of the load;  the number of states and state
        text are configurable;  set to invalid value (255) if state is not
        specified."""
    )

    def __set_level(self, v):
        self.__level._value = v

    level = property(
        lambda self: self.__level._value,
        __set_level,
        None,
        """Load level.  Specifies brightness for lighting loads, percent open
        for sunblinds, and percent of full speed for fans (positive values
        for down, negative values for up);  set to invalid value if level is
        not specified.  (percent)."""
    )

    def __set_angle(self, v):
        self.__angle._value = v

    angle = property(
        lambda self: self.__angle._value,
        __set_angle,
        None,
        """Load angle.  Angle for loads supporting angle setting such as
        sunblinds;  set to invalid value if angle is not specified.
        (degrees)."""
    )

    def __set_color(self, v):
        self.__color._value = v

    color = property(
        lambda self: self.__color._value,
        __set_color,
        None,
        """Load color.  Color for loads supporting color setting;  set to
        invalid value if color is not specified."""
    )

    def __set_level_multiplier(self, v):
        self.__level_multiplier._value = v

    level_multiplier = property(
        lambda self: self.__level_multiplier._value,
        __set_level_multiplier,
        None,
        """Factor Multiplier for the level;  used for dimming all loads in
        the active load groups;  set to invalid value if not specified."""
    )

    def __set_reduction_multiplier(self, v):
        self.__reduction_multiplier._value = v

    reduction_multiplier = property(
        lambda self: self.__reduction_multiplier._value,
        __set_reduction_multiplier,
        None,
        """Reduction multiplier.  Multiplier for the target_reduction which
        is the energy savings target specified as a percent reduction in
        energy use;  set to invalid value if not specified."""
    )

    def __set_area_occupancy(self, v):
        self.__area_occupancy._value = v

    area_occupancy = property(
        lambda self: self.__area_occupancy._value,
        __set_area_occupancy,
        None,
        """Area occupancy.  Calculated occupancy for an area based on all
        occupancy sensors and other inputs in the area;  set to invalid value
        if not specified."""
    )

    def __set_delay(self, v):
        self.__delay._value = v

    delay = property(
        lambda self: self.__delay._value,
        __set_delay,
        None,
        """On or off delay.  Time delay before changing state to on or off;
        there is no delay if the value is invalid.  (seconds)."""
    )

    def __set_fade(self, v):
        self.__fade._value = v

    fade = property(
        lambda self: self.__fade._value,
        __set_fade,
        None,
        """Fade time.  Time to ramp to a new setting;  fading starts after
        any delay specified by the delay field so that the time to move to a
        new value is delay plus fade seconds.  (seconds)."""
    )

    def __set_hold(self, v):
        self.__hold._value = v

    hold = property(
        lambda self: self.__hold._value,
        __set_hold,
        None,
        """Hold time.  Time to hold the specified settings before activating
        the next scene.  (seconds)."""
    )

    def __set_duration(self, v):
        self.__duration._value = v

    duration = property(
        lambda self: self.__duration._value,
        __set_duration,
        None,
        """Duration Time to hold the specified settings after the hold time;
        duration is indefinate if the value is invalid.  (seconds)."""
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

    def __set_load_groups(self, v):
        self.__load_groups._value = v

    load_groups = property(
        lambda self: self.__load_groups._value,
        __set_load_groups,
        None,
        """Load groups.  Load groups to be controlled for an update;  load
        group 0 applies to all devices."""
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
        self.__set_unoccupied_scene_number(v.__unoccupied_scene_number)
        self.__set_standby_scene_number(v.__standby_scene_number)
        self.__set_next_scene__number(v.__next_scene__number)
        self.__set_action(v.__action)
        self.__set_control(v.__control)
        self.__set_state(v.__state)
        self.__set_level(v.__level)
        self.__set_angle(v.__angle)
        self.__set_color(v.__color)
        self.__set_level_multiplier(v.__level_multiplier)
        self.__set_reduction_multiplier(v.__reduction_multiplier)
        self.__set_area_occupancy(v.__area_occupancy)
        self.__set_delay(v.__delay)
        self.__set_fade(v.__fade)
        self.__set_hold(v.__hold)
        self.__set_duration(v.__duration)
        self.__set_priority(v.__priority)
        self.__set_load_groups(v.__load_groups)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 58


if __name__ == '__main__':
    # unit test code.
    item = UCPTiotScene()
    pass
