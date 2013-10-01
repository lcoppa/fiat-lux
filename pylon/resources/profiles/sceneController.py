"""sceneController standard profile, originally defined in resource file set
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.scene
import pylon.resources.properties.fadeTime
import pylon.resources.properties.delayTime
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.setting
import pylon.resources.datapoints.scene_cfg
import pylon.resources.properties.minSendTime


class sceneController(pylon.resources.base.Profile):
    """sceneController standard profile.  Scene Controller.  Used to control
    scenes and fades."""

    def __init__(self):
        super().__init__(
            key=3251,
            scope=0,
            principal='nviScene'
        )
        self.datapoints['nviScene'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Scene trigger input.  Triggers a scene, or loads the scene
            preset memory with preset values.""",
            name='nviScene',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.scene.scene,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciFadeTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default fade time.  Used to set fade time;  if the
                    time is set to 0, meaning "learn", present functionality
                    is used.""",
                    name='nciFadeTime',
                    profile=self,
                    number=1,
                    datatype=pylon.resources.properties.fadeTime.fadeTime,
                    default=b'\x00\x0a',
                    mandatory=False
                ),
                'nciDelayTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default delay time.  Used to set delay time;  if
                    the time is set to 0, meaning "learn", present
                    functionality is used.""",
                    name='nciDelayTime',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.delayTime.delayTime,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSwitch'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Switch output.  Switch output for an actuator.""",
            name='nvoSwitch',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviSetting'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Master fade input.  Used to adjust the scene output.  The
            output is adjusted relative to the stored preset value.""",
            name='nviSetting',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSwitch'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Direct control input.  Direct control method for the
            switch output.""",
            name='nviSwitch',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviScenCf'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Scene configuration input.  Used to change scene setup,
            and to read stored scene values.""",
            name='nviScenCf',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.scene_cfg.scene_cfg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoScenFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Scene configuration output.  Scene configuration output,
            updated with the memory content of requested preset.""",
            name='nvoScenFb',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.scene_cfg.scene_cfg,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMinSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  Minimum period between output NV
            transmissions (maximum transmission rate)""",
            name='nciMinSendTime',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            minimum=b'\x00\x01',
            maximum=b'\x00\x14',
            default=b'\x00\x01',
            mandatory=False
        )
        self._original_name = 'SFPTsceneController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = sceneController()
    pass
