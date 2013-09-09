"""SCPTscene standard property type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0."""


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


class SCPTscene(base.Structure):
    """SCPTscene standard property type.  Scene configuration.  Scene
    definition used to create a scene table.  This SCPT defines the minimum
    entries required by the ISI profiles.  May be used in combination with
    SCPTsceneTiming."""

    def __init__(self):
        super().__init__(
            key=307,
            scope=0
        )

        self.__scene_number = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=255
        )
        self._register(('scene_number', self.__scene_number))

        self.__setting = base.Scaled(
            size=1,
            signed=False,
            scaling=(0.5, 0),
            invalid=127.5,
            minimum=0,
            maximum=100
        )
        self._register(('setting', self.__setting))

        self.__rotation = base.Scaled(
            size=1,
            signed=True,
            scaling=(2, 0),
            invalid=-256,
            minimum=-180,
            maximum=180
        )
        self._register(('rotation', self.__rotation))

        self.__unoccupied_scene = base.Scaled(
            size=1,
            signed=False,
            invalid=0,
            minimum=1,
            maximum=255
        )
        self._register(('unoccupied_scene', self.__unoccupied_scene))
        self._default_bytes = b'\x00\x00\x00\x00'
        self._property_scope, self._property_key = 0, 307
        self._definition = standard.add(self)

    def __set_scene_number(self, v):
        self.__scene_number._value = v

    scene_number = property(
        lambda self: self.__scene_number._value,
        __set_scene_number,
        None,
        """Scene number.  Scene number used to uniquely identify a scene.  A
        scene number to be recalled or learned is typically received from a
        SNVT_switch_2 or SNVT_scene input NV."""
    )

    def __set_setting(self, v):
        self.__setting._value = v

    setting = property(
        lambda self: self.__setting._value,
        __set_setting,
        None,
        """Scene setting level.  Setting value that is applied when the scene
        specified by scene_number is recalled.  Also used to set or specify a
        factor to be multiplied with the setting.  (% of full level.)."""
    )

    def __set_rotation(self, v):
        self.__rotation._value = v

    rotation = property(
        lambda self: self.__rotation._value,
        __set_rotation,
        None,
        """Scene rotation angle.  Rotation angle that is applied when the
        scene specified by scene_number is recalled.  Only applies to devices
        that support a rotation setting such as blinds.  (degrees)."""
    )

    def __set_unoccupied_scene(self, v):
        self.__unoccupied_scene._value = v

    unoccupied_scene = property(
        lambda self: self.__unoccupied_scene._value,
        __set_unoccupied_scene,
        None,
        """Unoccupied scene number.  Scene to be activated when the scene
        specified by scene_number is active, and an unoccupied input is
        received."""
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
        self.__set_setting(v.__setting)
        self.__set_rotation(v.__rotation)
        self.__set_unoccupied_scene(v.__unoccupied_scene)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = SCPTscene()
    pass
