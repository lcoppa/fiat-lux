"""partitionWallController standard profile, originally defined in resource
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
import pylon.resources.datapoints.scene
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.setting
import pylon.resources.properties.location
import pylon.resources.properties.sceneOffset


class partitionWallController(pylon.resources.base.Profile):
    """partitionWallController standard profile.  Partition Wall Controller.
    Used in spaces that can be divided into smaller sections.  Object passes
    data to the area next to it if the space is open (no partitioning).  If
    space is divided, then light-switch data is not passed to the other side
    of the separating wall."""

    def __init__(self):
        super().__init__(
            key=3252,
            scope=0
        )
        self.datapoints['nviScene1'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary-side scene input.  Reads in data from the scene
            panels and other sensors of the primary side of the partition
            wall.""",
            name='nviScene1',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.scene.scene,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoScene1'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary-side scene output.  Provides the scene output to
            the scene controllers on the primary side of the partition
            wall.""",
            name='nvoScene1',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.scene.scene,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.REPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviWallSwitch'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Partition wall switch input.  The valid range of the input
            is open (state ON) and closed (state OFF).  Other enumerations of
            the state are discarded;  value field has no effect.""",
            name='nviWallSwitch',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoScene2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Secondary-side scene output.  Provides the scene output to
            the scene controllers on the secondary side of the partition
            wall.""",
            name='nvoScene2',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.scene.scene,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.REPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviScene2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Secondary-side scene input.  Reads in data from the scene
            panels and other sensors of the secondary side of the partition
            wall.""",
            name='nviScene2',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.scene.scene,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviFade1'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary-side fade input.  Reads in data from the scene
            panels and other sensors of the primary side of the partition
            wall.""",
            name='nviFade1',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoFade1'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Primary-side fade output.  Provides SNVT_setting type
            output to the scene controllers on the primary side of the
            partition wall.""",
            name='nvoFade1',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.REPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviFade2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Secondary-side fade input.  Reads in data from the scene
            panels and other sensors of the secondary side of the partition
            wall.""",
            name='nviFade2',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoFade2'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Secondary-side fade output.  Provides SNVT_setting type
            output to the scene controllers on the secondary side of the
            partition wall.""",
            name='nvoFade2',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.REPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciSceneOffset'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Scene offset.  The offset for the scene number when data
            is forwarded from primary to secondary.""",
            name='nciSceneOffset',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.sceneOffset.sceneOffset,
            default=b'\x00',
            mandatory=False
        )
        self._original_name = 'SFPTpartitionWallController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = partitionWallController()
    pass
