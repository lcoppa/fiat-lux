"""UNVT_iot_load_control userdefined datapoint type, originally defined in
resource file set iot 90:00:00:05:00:00:00:00-1.  """


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
from pylon.resources.userdefined import userdefined
from pylon.resources.load_control_t import load_control_t
from pylon.resources.SNVT_color_2 import SNVT_color_2
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.command_priority_t import command_priority_t
from pylon.resources.UNVT_iot_timestamp import UNVT_iot_timestamp
from pylon.resources.UNVT_iot_status_flags import UNVT_iot_status_flags
from pylon.resources.event_state_t import event_state_t
from pylon.resources.reliability_t import reliability_t


class UNVT_iot_load_control(base.Structure):
    """UNVT_iot_load_control userdefined datapoint type.  IoT load control.
    Load control value with timestamp, status, and priority;  supports scenes
    and load control groups."""

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
                        maximum=127
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
            key=7,
            scope=1
        )

        self.__control = load_control_t(
        )
        self._register(('control', self.__control))

        self.__state = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=127
        )
        self._register(('state', self.__state))

        self.__level = base.Float(
            single=True,
            minimum=0,
            maximum=127
        )
        self._register(('level', self.__level))

        self.__angle = base.Float(
            single=True,
            minimum=0,
            maximum=127
        )
        self._register(('angle', self.__angle))

        self.__color = SNVT_color_2(
        )
        self._register(('color', self.__color))

        self.__level_multiplier = base.Float(
            single=True,
            minimum=0,
            maximum=255
        )
        self._register(('level_multiplier', self.__level_multiplier))

        self.__target_reduction = base.Float(
            single=True,
            minimum=0,
            maximum=255
        )
        self._register(('target_reduction', self.__target_reduction))

        self.__area_occupancy = SNVT_occupancy(
        )
        self._register(('area_occupancy', self.__area_occupancy))

        self.__local_occupancy = SNVT_occupancy(
        )
        self._register(('local_occupancy', self.__local_occupancy))

        self.__delay = base.Float(
            single=True,
            minimum=0,
            maximum=255
        )
        self._register(('delay', self.__delay))

        self.__fade = base.Float(
            single=True,
            minimum=0,
            maximum=255
        )
        self._register(('fade', self.__fade))

        self.__duration = base.Float(
            single=True,
            minimum=0,
            maximum=255
        )
        self._register(('duration', self.__duration))

        self.__button = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('button', self.__button))

        self.__priority = command_priority_t(
        )
        self._register(('priority', self.__priority))

        self.__scene_number = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=127
        )
        self._register(('scene_number', self.__scene_number))

        self.__load_groups = UNVT_iot_load_control.load_groupsType(
        )
        self._register(('load_groups', self.__load_groups))

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
        self._definition = userdefined.add(self)


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
        """Load level (percent) Specifies brightness for lighting loads,
        percent open for sunblinds, and percent of full speed for fans
        (positive values for down, negative values for up);  set to invalid
        value if level is not specified."""
    )

    def __set_angle(self, v):
        self.__angle._value = v

    angle = property(
        lambda self: self.__angle._value,
        __set_angle,
        None,
        """Load angle (degrees) Angle for loads supporting angle setting such
        as sunblinds;  set to invalid value if angle is not specified."""
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

    def __set_target_reduction(self, v):
        self.__target_reduction._value = v

    target_reduction = property(
        lambda self: self.__target_reduction._value,
        __set_target_reduction,
        None,
        """Target reduction.  Energy savings target specified as a percent
        reduction in energy use;  set to invalid value if not specified."""
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

    def __set_local_occupancy(self, v):
        self.__local_occupancy._value = v

    local_occupancy = property(
        lambda self: self.__local_occupancy._value,
        __set_local_occupancy,
        None,
        """Local occupancy.  Occupancy setting reported by a single occupancy
        sensor;  used by occupancy sensors to calculate area occupancy;
        typically ignored by lighting loads;  set to invalid value if not
        specified."""
    )

    def __set_delay(self, v):
        self.__delay._value = v

    delay = property(
        lambda self: self.__delay._value,
        __set_delay,
        None,
        """On or off delay (seconds) Time delay before changing state to on
        or off;  there is no delay if the value is invalid."""
    )

    def __set_fade(self, v):
        self.__fade._value = v

    fade = property(
        lambda self: self.__fade._value,
        __set_fade,
        None,
        """Fade time (seconds) Time to ramp to a new setting;  fading starts
        after any delay specified by the delay field so that the time to move
        to a new value is delay plus fade seconds."""
    )

    def __set_duration(self, v):
        self.__duration._value = v

    duration = property(
        lambda self: self.__duration._value,
        __set_duration,
        None,
        """Duration Time to hold the specified settings;  hold time is
        indefinate if the value is invalid."""
    )

    def __set_button(self, v):
        self.__button._value = v

    button = property(
        lambda self: self.__button._value,
        __set_button,
        None,
        """Button select.  Button number to activate for updates to a
        keypad;  triggers the actions defined for the specified button;  set
        to invalid value (0) if not specified."""
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

    def __set_scene_number(self, v):
        self.__scene_number._value = v

    scene_number = property(
        lambda self: self.__scene_number._value,
        __set_scene_number,
        None,
        """Scene number.  Scene number that is applied based on the function
        specified in the state field."""
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
        """Event state.  Present event state;  set to NORMAL for normal
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

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_control(v.__control)
        self.__set_state(v.__state)
        self.__set_level(v.__level)
        self.__set_angle(v.__angle)
        self.__set_color(v.__color)
        self.__set_level_multiplier(v.__level_multiplier)
        self.__set_target_reduction(v.__target_reduction)
        self.__set_area_occupancy(v.__area_occupancy)
        self.__set_local_occupancy(v.__local_occupancy)
        self.__set_delay(v.__delay)
        self.__set_fade(v.__fade)
        self.__set_duration(v.__duration)
        self.__set_button(v.__button)
        self.__set_priority(v.__priority)
        self.__set_scene_number(v.__scene_number)
        self.__set_load_groups(v.__load_groups)
        self.__set_update_time(v.__update_time)
        self.__set_status_flags(v.__status_flags)
        self.__set_event_state(v.__event_state)
        self.__set_reliability(v.__reliability)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 59


if __name__ == '__main__':
    # unit test code.
    item = UNVT_iot_load_control()
    pass
