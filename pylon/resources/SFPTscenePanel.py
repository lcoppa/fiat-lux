"""SFPTscenePanel standard profile, originally defined in resource file set
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_scene import SNVT_scene
from pylon.resources.SNVT_setting import SNVT_setting
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTstepValue import SCPTstepValue
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTsceneNmbr import SCPTsceneNmbr


class SFPTscenePanel(base.Profile):
    """SFPTscenePanel standard profile.  Scene Panel.  Scene control panels
    with or without specific hardware."""

    def __init__(self):
        super().__init__(
            key=3250,
            scope=0
        )
        self.datapoints['nvoScene'] = base.Profile.DatapointMember(
            doc="""Scene trigger output.  """,
            name='nvoScene',
            profile=self,
            number=1,
            datatype=SNVT_scene,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviSceneFb'] = base.Profile.DatapointMember(
            doc="""Scene number feedback.  Provides feedback from other scene
            panels.""",
            name='nviSceneFb',
            profile=self,
            number=2,
            datatype=SNVT_scene,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoFadeSetting'] = base.Profile.DatapointMember(
            doc="""Master fade output control setting.  The lighting scene
            can be adjusted up or down without calling up a new scene.""",
            name='nvoFadeSetting',
            profile=self,
            number=3,
            datatype=SNVT_setting,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTime':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTime',
                    profile=self,
                    number=3,
                    datatype=SCPTminSendTime,
                    minimum=b'\x00\x01',
                    maximum=b'\x00\x14',
                    default=b'\x00\x01',
                    mandatory=False
                ),
                'nciStepValue':
                base.Profile.PropertyMember(
                    doc="""Step value, ramp or master fade.  The step value
                    for up/down ramps or fade control.""",
                    name='nciStepValue',
                    profile=self,
                    number=4,
                    datatype=SCPTstepValue,
                    minimum=b'\x01',
                    default=b'\x05',
                    mandatory=False
                )
            }
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=SCPTlocation,
            mandatory=False
        )
        self.properties['nciSceneNumber'] = base.Profile.PropertyMember(
            doc="""Scene number.  The number of the first scene for the
            panel, other numbers are subsequent.""",
            name='nciSceneNumber',
            profile=self,
            number=2,
            datatype=SCPTsceneNmbr,
            default=b'\x01',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTscenePanel()
    pass
