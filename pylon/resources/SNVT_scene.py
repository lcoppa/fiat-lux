"""SNVT_scene standard datapoint type, originally defined in resource file
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.scene_t import scene_t


class SNVT_scene(base.Structure):
    """SNVT_scene standard datapoint type.  Scene control.  (function, scene
    number.)."""

    def __init__(self):
        super().__init__(
            key=115,
            scope=0
        )

        self.__function = scene_t(
        )
        self._register(('function', self.__function))

        self.__scene_number = base.Scaled(
            size=1,
            signed=False,
            minimum=1,
            maximum=255
        )
        self._register(('scene_number', self.__scene_number))
        self._definition = standard.add(self)


    def __set_function(self, v):
        self.__function._value = v

    function = property(
        lambda self: self.__function._value,
        __set_function,
        None,
        """Scene control function.  (scene control function names.)."""
    )

    def __set_scene_number(self, v):
        self.__scene_number._value = v

    scene_number = property(
        lambda self: self.__scene_number._value,
        __set_scene_number,
        None,
        """Scene number."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_function(v.__function)
        self.__set_scene_number(v.__scene_number)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 2


if __name__ == '__main__':
    # unit test code.
    item = SNVT_scene()
    pass
