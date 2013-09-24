"""SFPTautomaticTransferSwitch standard profile, originally defined in
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
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_freq_hz import SNVT_freq_hz
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_volt_ac import SNVT_volt_ac
from pylon.resources.SNVT_amp_ac import SNVT_amp_ac
from pylon.resources.SNVT_pwr_fact import SNVT_pwr_fact
from pylon.resources.SNVT_power_f import SNVT_power_f
from pylon.resources.SCPTlocation import SCPTlocation


class SFPTautomaticTransferSwitch(base.Profile):
    """SFPTautomaticTransferSwitch standard profile.  Automatic Transfer
    Switch.  An ATS is a piece of electrical equipment that is used to
    monitor and automatically connect the best of two power sources to an
    electrical load.  Normally at least one of the two power sources is a
    generator set that is directed by the ATS to start when the primary power
    source has failed."""

    def __init__(self):
        super().__init__(
            key=13120,
            scope=0
        )
        self.datapoints['nviTestCmd'] = base.Profile.DatapointMember(
            doc="""Test Command Input.  Allows an external node to test the
            ATS operation.""",
            name='nviTestCmd',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSrc2StartCmd'] = base.Profile.DatapointMember(
            doc="""Start Source 2 Command Output.  Allows the ATS to start
            and stop the alternate or emergency power source.""",
            name='nvoSrc2StartCmd',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSrc1Available'] = base.Profile.DatapointMember(
            doc="""Source 1 Available Output.  Indicates the availability of
            the normal power source (GenSet/Source 1)""",
            name='nvoSrc1Available',
            profile=self,
            number=3,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSrc2Available'] = base.Profile.DatapointMember(
            doc="""Source 2 Available Output.  Indicates the availability of
            the emergency power source (GenSet/Source 2)""",
            name='nvoSrc2Available',
            profile=self,
            number=4,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSrc1Connected'] = base.Profile.DatapointMember(
            doc="""Source 1 Connected Output.  Indicates the switch position
            of the ATS.""",
            name='nvoSrc1Connected',
            profile=self,
            number=5,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSrc2Connected'] = base.Profile.DatapointMember(
            doc="""Source 2 Connected Output.  Indicates the switch position
            of the ATS.""",
            name='nvoSrc2Connected',
            profile=self,
            number=6,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviFaultResetCmd'] = base.Profile.DatapointMember(
            doc="""Fault Reset Command Input.  Resets or attempts to clear an
            ATS fault.""",
            name='nviFaultResetCmd',
            profile=self,
            number=7,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviLoadShedCmd'] = base.Profile.DatapointMember(
            doc="""Load Shed Command Input.  Sheds the electrical load of the
            ATS.""",
            name='nviLoadShedCmd',
            profile=self,
            number=8,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviTransInhCmd'] = base.Profile.DatapointMember(
            doc="""Transfer Inhibit Command Input.  Inhibits the ATS from
            automatically transferring the load to the emergency power source
            (Source 2), when Source 2 becomes available.""",
            name='nviTransInhCmd',
            profile=self,
            number=9,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRetransInhCmd'] = base.Profile.DatapointMember(
            doc="""Retransfer Inhibit Command Input.  Inhibits the ATS from
            automatically transferring the load back to the normal power
            source (Source 1), when Source 1 becomes available.""",
            name='nviRetransInhCmd',
            profile=self,
            number=10,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOverrideCmd'] = base.Profile.DatapointMember(
            doc="""Override Command Input.  Overrides a transfer or
            retransfer time delay, or transfer or retransfer inhibit.""",
            name='nviOverrideCmd',
            profile=self,
            number=11,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSrc1StartCmd'] = base.Profile.DatapointMember(
            doc="""Start Source 1 Command Output.  Allows the ATS to start
            and stop the Source 1.""",
            name='nvoSrc1StartCmd',
            profile=self,
            number=12,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFaultStatus'] = base.Profile.DatapointMember(
            doc="""Fault Status Output.  Reports the presence of an ATS
            fault.""",
            name='nvoFaultStatus',
            profile=self,
            number=13,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSrc1Frequency'] = base.Profile.DatapointMember(
            doc="""Source 1 Frequency Output.  Line frequency of Source
            1.""",
            name='nvoSrc1Frequency',
            profile=self,
            number=14,
            datatype=SNVT_freq_hz,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV14':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV14',
                    profile=self,
                    number=2,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSrc2Frequency'] = base.Profile.DatapointMember(
            doc="""Source 2 Frequency Output.  Line frequency of Source
            2.""",
            name='nvoSrc2Frequency',
            profile=self,
            number=15,
            datatype=SNVT_freq_hz,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV15':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV15',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSrc1VoltageLL'] = base.Profile.DatapointMember(
            doc="""Source 1 Line-to-Line Voltage Output.  Line-to-line
            voltage(s) of Source 1.""",
            name='nvoSrc1VoltageLL',
            profile=self,
            number=16,
            datatype=SNVT_volt_ac,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV16':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV16',
                    profile=self,
                    number=4,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSrc2VoltageLL'] = base.Profile.DatapointMember(
            doc="""Source 2 Line-to-Line Voltage Output.  Line-to-line
            voltage(s) of Source 2.""",
            name='nvoSrc2VoltageLL',
            profile=self,
            number=17,
            datatype=SNVT_volt_ac,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV17':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV17',
                    profile=self,
                    number=5,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSrc1VoltageLN'] = base.Profile.DatapointMember(
            doc="""Source 1 Line-to-Neutral Voltage Output.  Line-to-neutral
            voltage(s) of Source 1.""",
            name='nvoSrc1VoltageLN',
            profile=self,
            number=18,
            datatype=SNVT_volt_ac,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV18':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV18',
                    profile=self,
                    number=6,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoSrc2VoltageLN'] = base.Profile.DatapointMember(
            doc="""Source 2 Line-to-Neutral Voltage Output.  Line-to-neutral
            voltage(s) of Source 2.""",
            name='nvoSrc2VoltageLN',
            profile=self,
            number=19,
            datatype=SNVT_volt_ac,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV19':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV19',
                    profile=self,
                    number=7,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoLoadCurrent'] = base.Profile.DatapointMember(
            doc="""Load Current Output.  Line current(s) of the electrical
            load.""",
            name='nvoLoadCurrent',
            profile=self,
            number=20,
            datatype=SNVT_amp_ac,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV20':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV20',
                    profile=self,
                    number=8,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoLoadPF'] = base.Profile.DatapointMember(
            doc="""Load Power Factor Output.  Power factor of the electrical
            load.""",
            name='nvoLoadPF',
            profile=self,
            number=21,
            datatype=SNVT_pwr_fact,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV21':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV21',
                    profile=self,
                    number=9,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoLoadRealPower'] = base.Profile.DatapointMember(
            doc="""Load Real Power Output.  Real power of the electrical load
            as a floating type ( in Watts)""",
            name='nvoLoadRealPower',
            profile=self,
            number=22,
            datatype=SNVT_power_f,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV22':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV22',
                    profile=self,
                    number=10,
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
            number=1,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time to be used across NVs 14-22.  The
            maximum period of time between consecutive transmissions of the
            current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=11,
            datatype=SCPTmaxSendTime,
            array_size_max=16,
            default=b'\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTautomaticTransferSwitch()
    pass
