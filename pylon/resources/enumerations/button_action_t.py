"""button_action_t standard enumeration type, originally defined in resource
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


class button_action_t(pylon.resources.base.Enumeration):
    """button_action_t standard enumeration."""

    # Invalid value.
    BTA_NUL = -1

    # Toggle on-off state;  same action as SW_SET_OFF if the on/off state was
    # on, and SW_SET_ON if the on/off state was off;  ignored for blinds,
    # drapes, shades, and fans.
    BTA_TOGGLE_STATE = 0

    # Toggle on-off state if specified scene is the current scene;  recall
    # the state from the specified scene if the scene is new.
    BTA_TOGGLE_SCENE = 1

    # Set the state to on;  ignored for blinds, drapes, shades, and fans.
    BTA_SET_STATE_ON = 2

    # Recall a scene.
    BTA_RECALL_SCENE = 3

    # Set the state to off;  ignored for blinds, drapes, shades, and fans.
    BTA_SET_STATE_OFF = 4

    # Set the occupancy state.
    BTA_SET_OCCUPIED = 5

    # Clear the occupancy state.
    BTA_CLEAR_OCCUPIED = 6

    # Set the unoccupied state.
    BTA_SET_UNOCCUPIED = 7

    # Clear the unoccupied state.
    BTA_CLEAR_UNOCCUPIED = 8

    # Set the level to the specified value;  ignored for blinds, drapes,
    # shades, and fans.
    BTA_SET_LEVEL = 9

    # Set ceiling fan direction to up, with specified level.
    BTA_SET_UP_DIRECTION = 10

    # Set ceiling fan direction to down, with specified level.
    BTA_SET_DOWN_DIRECTION = 11

    # Increase the level by specified amount;  ignored for blinds, drapes,
    # shades, and fans.
    BTA_INCREASE = 12

    # Decrease the level by the specified amount;  ignored for blinds,
    # drapes, shades, and fans.
    BTA_DECREASE = 13

    # Same as increase until 100% is reached, then same as descrease until 0%
    # is reached, then repeat;  ignored for blinds, drapes, shades, and
    # fans;
    BTA_CYCLE = 14

    # Rotate blinds open by the setting.
    BTA_ROTATE_OPEN = 15

    # Rotate blinds closed by the setting.
    BTA_ROTATE_CLOSED = 16

    # Set the rotation angle of blinds to the setting.
    BTA_SET_ANGLE = 17

    # Toggle ceiling fan direction, with specified level.
    BTA_TOGGLE_DIRECTION = 18

    # Toggle the occupancy state.
    BTA_TOGGLE_OCCUPANCY = 19

    # Learn a scene from current settings.
    BTA_LEARN_SCENE = 20

    # Set standby mode.
    BTA_SET_STANDBY = 21

    # Clear standby mode.
    BTA_CLEAR_STANDBY = 22

    # Toggle standby mode.
    BTA_TOGGLE_STANDBY = 23

    # Set the fan state to on.
    BTA_SET_FAN_ON = 24

    # Set the fan state to off.
    BTA_SET_FAN_OFF = 25

    # Toggle the fan on-off state.
    BTA_TOGGLE_FAN_STATE = 26

    # Increase fan speed by the specified amount.
    BTA_INCREASE_FAN_LEVEL = 27

    # Decrease fan speed by the specified amount.
    BTA_DECREASE_FAN_LEVEL = 28

    # Increase fan speed by the specified amount until the level reaches
    # 100%, then decrease the fan speed by the specified amount.
    BTA_CYCLE_FAN_LEVEL = 29

    # Move blinds, drapes, or shades open by the specified amount.
    BTA_MOVE_OPEN = 30

    # Move blinds, drapes, or shades open by the specified amount.
    BTA_MOVE_CLOSED = 31

    # Set blinds, drapes, or shades to the specified position;  100% is fully
    # open, 0% is fully closed.
    BTA_SET_POSITION = 32

    # Stop any motion of blinds, drapes, or shades.
    BTA_STOP = 33

    # Toggle group state.
    BTA_TOGGLE_GROUP = 34

    # Enable a group;  all groups are enabled by default.
    BTA_ENABLE_GROUP = 35

    # Disable a group.
    BTA_DISABLE_GROUP = 36

    # Increase hue.
    BTA_INCREASE_HUE = 37

    # Decrease hue.
    BTA_DECREASE_HUE = 38

    # Set demand-response mode.
    BTA_SET_DR_EVENT = 39

    # Clear demand-reponse mode.
    BTA_CLEAR_DR_EVENT = 40

    # Toggle demand-response mode.
    BTA_TOGGLE_DR_EVENT = 41

    def __init__(self):
        super().__init__(
            key=68,
            scope=0,
            prefix='BTA_'
        )
        self._original_name = 'button_action_t'
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = button_action_t()
    pass
