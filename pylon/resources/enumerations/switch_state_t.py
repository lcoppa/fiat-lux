"""switch_state_t standard enumeration type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.standard import standard


class switch_state_t(pylon.resources.base.Enumeration):
    """switch_state_t standard enumeration."""

    # Invalid value.
    SW_NUL = -1

    # Set the state to off;  ignored for blinds, drapes, shades, and fans.
    SW_SET_OFF = 0

    # Set the state to on;  ignored for blinds, drapes, shades, and fans.
    SW_SET_ON = 1

    # Report that the state is off;  output only;  ignored for input.
    SW_REPORT_OFF = 2

    # Report that the state is on;  output only;  ignored for input.
    SW_REPORT_ON = 3

    # Toggle on-off state;  same action as SW_SET_OFF if the on/off state was
    # on, and SW_SET_ON if the on/off state was off;  ignored for blinds,
    # drapes, shades, and fans.
    SW_TOGGLE_STATE = 4

    # Set the level to the specified value;  ignored for blinds, drapes,
    # shades, and fans.
    SW_SET_LEVEL = 5

    # Increase the level by the specified value;  ignored for blinds, drapes,
    # shades, and fans.
    SW_INCREASE_LEVEL = 6

    # Decrease the level by the specified amount;  ignored for blinds,
    # drapes, shades, and fans.
    SW_DECREASE_LEVEL = 7

    # Recall the state and level from the specified scene.
    SW_RECALL_SCENE = 8

    # Store setting for the specified scene.
    SW_STORE_SCENE = 9

    # Learn setting for the specified scene.
    SW_LEARN_SCENE = 10

    # Set the occupancy state.
    SW_SET_OCCUPIED = 11

    # Clear the occupancy state.
    SW_SET_UNOCCUPIED = 12

    # Set a multiplier for the level for 60 minutes;  ignored for blinds,
    # drapes, shades, and fans.
    SW_SET_MULTIPLIER = 13

    # Enable a group;  all groups are enabled by default.
    SW_ENABLE_GROUP = 14

    # Disable a group.
    SW_DISABLE_GROUP = 15

    # Blink state (toggle on-off state;  pause;  toggle on-off state again.
    SW_WINK = 16

    # Reset scene definitions, multiplier, occupancy state, group enable
    # flags, and settings to factory defaults.
    SW_RESET = 17

    # Reset energy usage value to zero.
    SW_RESET_ENERGY_USAGE = 18

    # Reset runtime value to zero.
    SW_RESET_RUNTIME = 19

    # Increase color hue.
    SW_INCREASE_HUE = 20

    # Decrease color hue.
    SW_DECREASE_HUE = 21

    # Trigger the actions for pressing and releasing the button specified in
    # the value field.
    SW_SET_BUTTON = 22

    # Set state and percent of full level (value field) for a group specified
    # in the scene field.
    SW_SET_GROUP_STATE_LEVEL = 23

    # Set ceiling fan direction to up, with specified level.
    SW_SET_FAN_UP = 32

    # Set ceiling fan direction to down, with specified level.
    SW_SET_FAN_DOWN = 33

    # Toggle fan up-down direction.
    SW_TOGGLE_FAN_DIRECTION = 34

    # Increase fan speed by the setting.
    SW_INCREASE_FAN_LEVEL = 35

    # Decrease fan speed by the setting.
    SW_DECREASE_FAN_LEVEL = 36

    # Set the fan state to on.
    SW_SET_FAN_ON = 37

    # Set the fan state to off.
    SW_SET_FAN_OFF = 38

    # Toggle the fan on-off state.
    SW_TOGGLE_FAN_STATE = 39

    # Move blinds, drapes, or shades open by the setting.
    SW_MOVE_OPEN = 48

    # Move blinds, drapes, or shades closed by the setting.
    SW_MOVE_CLOSED = 49

    # Set the rotation angle of blinds to the setting.
    SW_SET_ANGLE = 50

    # Rotate blinds open by the setting.
    SW_ROTATE_OPEN = 51

    # Rotate blinds closed by the setting.
    SW_ROTATE_CLOSED = 52

    # Stop any motion of blinds, drapes, or shades.
    SW_STOP = 53

    # Set Standby mode.
    SW_SET_STANDBY = 54

    # Toggle the standby state.
    SW_TOGGLE_STANDBY = 55

    # Set blinds, drapes, or shades to the specified position;  100% is fully
    # open, 0% is fully closed.
    SW_SET_POSITION = 56

    # Report the position of blinds, drapes, or shades output only;  ignored
    # for input.
    SW_REPORT_POSITION = 57

    # Report the fan speed in percent of full level output only;  ignored for
    # input.
    SW_REPORT_FAN_LEVEL = 58

    def __init__(self):
        super().__init__(
            key=71,
            scope=0,
            prefix='SW_'
        )
        self._original_name = 'switch_state_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = switch_state_t()
    pass
