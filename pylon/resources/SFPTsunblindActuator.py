"""SFPTsunblindActuator standard profile, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.SNVT_setting import SNVT_setting
from pylon.resources.SNVT_sblnd_state import SNVT_sblnd_state
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer


class SFPTsunblindActuator(base.Profile):
    """SFPTsunblindActuator standard profile.  Sunblind Actuator.  Controls
    one or more sunblinds or similar devices, and interfaces with a Sunblind
    Controller."""

    def __init__(self):
        super().__init__(
            key=6110,
            scope=0
        )
        self.datapoints['nviSblndSet'] = base.Profile.DatapointMember(
            doc="""Sunblind Setting input.  This input network variable is
            used to send the sunblind to a desired position.""",
            name='nviSblndSet',
            profile=self,
            number=1,
            datatype=SNVT_setting,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSblndSetFwd'] = base.Profile.DatapointMember(
            doc="""Sunblind Control output for daisy chaining.  This output
            network variable is used to provide feedback or to forward the
            input NV of nviSblndSet to another device or functional
            block.""",
            name='nvoSblndSetFwd',
            profile=self,
            number=2,
            datatype=SNVT_setting,
            mandatory=False,
            service=base.Profile.DatapointMember.REPEATED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviSblndStatus'] = base.Profile.DatapointMember(
            doc="""Sunblind Status input.  This input network variable
            provides for receiving a Sunblind Controller status in order to
            report, via the Status output NV, the Sunblind Actuator status in
            conjunction with the Sunblind Controller status.""",
            name='nviSblndStatus',
            profile=self,
            number=3,
            datatype=SNVT_sblnd_state,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSblndOvr'] = base.Profile.DatapointMember(
            doc="""Sunblind Override input.  This input network variable is
            used to send the sunblind to a desired position.""",
            name='nviSblndOvr',
            profile=self,
            number=4,
            datatype=SNVT_setting,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSblndStatus'] = base.Profile.DatapointMember(
            doc="""Sunblind Status output.  This output network variable is
            used to provide feedback as to the actual sunblind position,
            error messages, and the cause of the latest change of the
            setpoint.""",
            name='nvoSblndStatus',
            profile=self,
            number=5,
            datatype=SNVT_sblnd_state,
            mandatory=False,
            service=base.Profile.DatapointMember.REPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV05':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV05',
                    profile=self,
                    number=1,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoMode'] = base.Profile.DatapointMember(
            doc="""Sunblind feedback output for switch LEDs or general
            monitoring.  This output network variable is used to provide a
            feedback output for switch LEDs or general monitoring.""",
            name='nvoMode',
            profile=self,
            number=6,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.REPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV06':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV06',
                    profile=self,
                    number=2,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=3,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=4,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciObjMinVer'] = base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='nciObjMinVer',
            profile=self,
            number=5,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTsunblindActuator()
    pass
