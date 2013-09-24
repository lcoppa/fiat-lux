"""SFPTlightingPanelController standard profile, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_scene import SNVT_scene
from pylon.resources.SNVT_preset import SNVT_preset
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTmanualAllowed import SCPTmanualAllowed


class SFPTlightingPanelController(base.Profile):
    """SFPTlightingPanelController standard profile.  Lighting-Panel
    Controller.  Use to control lamps or fixtures by assigned groups
    group."""

    def __init__(self):
        super().__init__(
            key=3401,
            scope=0
        )
        self.datapoints['nviGroup'] = base.Profile.DatapointMember(
            doc="""Lighting Group Trigger.  This input network variable
            triggers a group or pattern of lighting circuits.""",
            name='nviGroup',
            profile=self,
            number=1,
            datatype=SNVT_scene,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoGroupFb'] = base.Profile.DatapointMember(
            doc="""Lighting Group Feedback Output.  This output network
            variable provides current status of any of the possible 255
            groups or patterns programmed into the controller.""",
            name='nvoGroupFb',
            profile=self,
            number=2,
            datatype=SNVT_scene,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviLPCcfg'] = base.Profile.DatapointMember(
            doc="""LPC Configuration Input.  This input network variable
            provides the functions required for programming groups, patterns
            and other lighting behaviors into the controller.""",
            name='nviLPCcfg',
            profile=self,
            number=3,
            datatype=SNVT_preset,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoLPCfb'] = base.Profile.DatapointMember(
            doc="""LPC Configuration Feedback Output.  This output network
            variable provides information on current LPC configuation.""",
            name='nvoLPCfb',
            profile=self,
            number=4,
            datatype=SNVT_preset,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['ncimanualAllowed'] = base.Profile.PropertyMember(
            doc="""Manual allowed.  Provides a clock, with a manual time
            input, the possibility to permit manual time updating.""",
            name='ncimanualAllowed',
            profile=self,
            number=2,
            datatype=SCPTmanualAllowed,
            default=b'\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTlightingPanelController()
    pass
