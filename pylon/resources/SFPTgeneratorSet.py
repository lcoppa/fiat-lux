"""SFPTgeneratorSet standard profile, originally defined in resource file set
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
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_state import SNVT_state
from pylon.resources.SNVT_freq_hz import SNVT_freq_hz
from pylon.resources.SNVT_volt_ac import SNVT_volt_ac
from pylon.resources.SNVT_amp_ac import SNVT_amp_ac
from pylon.resources.SNVT_pwr_fact import SNVT_pwr_fact
from pylon.resources.SNVT_power_f import SNVT_power_f
from pylon.resources.SNVT_elec_whr_f import SNVT_elec_whr_f
from pylon.resources.SNVT_rpm import SNVT_rpm
from pylon.resources.SNVT_temp import SNVT_temp
from pylon.resources.SNVT_press import SNVT_press
from pylon.resources.SNVT_volt import SNVT_volt
from pylon.resources.SNVT_count import SNVT_count
from pylon.resources.SNVT_time_f import SNVT_time_f
from pylon.resources.SCPTlocation import SCPTlocation


class SFPTgeneratorSet(base.Profile):
    """SFPTgeneratorSet standard profile.  Generator Set.  Used to control a
    generator set (genset) for power generation in primary or secondary
    systems."""

    def __init__(self):
        super().__init__(
            key=13110,
            scope=0
        )
        self.datapoints['nviStartCmd'] = base.Profile.DatapointMember(
            doc="""Start Command Input.  start and stop the generator
            set.""",
            name='nviStartCmd',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviFaultResetCmd'] = base.Profile.DatapointMember(
            doc="""Fault Reset Command Input.  reset or clear a generator set
            fault.""",
            name='nviFaultResetCmd',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoRunStatus'] = base.Profile.DatapointMember(
            doc="""Run Status Output.  running at rated speed and voltage and
            is ready to accept load.""",
            name='nvoRunStatus',
            profile=self,
            number=3,
            datatype=SNVT_switch,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV03':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV03',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoFaultStatus'] = base.Profile.DatapointMember(
            doc="""Fault Status Output.  report the presence of a generator
            set fault.""",
            name='nvoFaultStatus',
            profile=self,
            number=4,
            datatype=SNVT_switch,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviShutdownCmd'] = base.Profile.DatapointMember(
            doc="""Shutdown Command Input.  emergency, unconditional
            shutdown/disable of run.""",
            name='nviShutdownCmd',
            profile=self,
            number=5,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoNFPA110Annun'] = base.Profile.DatapointMember(
            doc="""NFPA 110 Annunciation Output.  report state of National
            Fire Protection Agency (USA) genset faults (NFPA s.110)""",
            name='nvoNFPA110Annun',
            profile=self,
            number=6,
            datatype=SNVT_state,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFrequency'] = base.Profile.DatapointMember(
            doc="""Frequency Output.  output frequency of the generator
            set.""",
            name='nvoFrequency',
            profile=self,
            number=7,
            datatype=SNVT_freq_hz,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoVoltageLL'] = base.Profile.DatapointMember(
            doc="""Line-to-Line Voltage Output.  line-to-line output
            voltage(s) of the generator set.""",
            name='nvoVoltageLL',
            profile=self,
            number=8,
            datatype=SNVT_volt_ac,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoVoltageLN'] = base.Profile.DatapointMember(
            doc="""Line-to-Neutral Voltage Output.  line-to-neutral output
            voltage(s) of the generator set.""",
            name='nvoVoltageLN',
            profile=self,
            number=9,
            datatype=SNVT_volt_ac,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCurrent'] = base.Profile.DatapointMember(
            doc="""Line Current Output.  output line current(s) of the
            generator set.""",
            name='nvoCurrent',
            profile=self,
            number=10,
            datatype=SNVT_amp_ac,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPowerFactor'] = base.Profile.DatapointMember(
            doc="""Power Factor Output.  power factor of the generator
            set.""",
            name='nvoPowerFactor',
            profile=self,
            number=11,
            datatype=SNVT_pwr_fact,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRealPower'] = base.Profile.DatapointMember(
            doc="""Real Power Output.  real power output as a floating type (
            in Watts)""",
            name='nvoRealPower',
            profile=self,
            number=12,
            datatype=SNVT_power_f,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoGenEnergy'] = base.Profile.DatapointMember(
            doc="""Generated Energy Output.  total (cumulative) electrical
            energy (WHR) generated by genset.""",
            name='nvoGenEnergy',
            profile=self,
            number=13,
            datatype=SNVT_elec_whr_f,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV13':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV13',
                    profile=self,
                    number=4,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEngineSpeed'] = base.Profile.DatapointMember(
            doc="""Engine Speed Output.  engine speed of the generator
            set.""",
            name='nvoEngineSpeed',
            profile=self,
            number=14,
            datatype=SNVT_rpm,
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
                    number=5,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEngineTemp'] = base.Profile.DatapointMember(
            doc="""Engine Temperature Output.  engine temperature of the
            generator set.""",
            name='nvoEngineTemp',
            profile=self,
            number=15,
            datatype=SNVT_temp,
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
                    number=6,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOilPressure'] = base.Profile.DatapointMember(
            doc="""Engine Oil Pressure Output.  engine oil pressure of the
            generator set.""",
            name='nvoOilPressure',
            profile=self,
            number=16,
            datatype=SNVT_press,
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
                    number=7,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoBattery'] = base.Profile.DatapointMember(
            doc="""Battery Voltage Output.  starting battery voltage of the
            engine.""",
            name='nvoBattery',
            profile=self,
            number=17,
            datatype=SNVT_volt,
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
                    number=8,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEngineStarts'] = base.Profile.DatapointMember(
            doc="""Engine Starts Output.  total number of successful engine
            starts.""",
            name='nvoEngineStarts',
            profile=self,
            number=18,
            datatype=SNVT_count,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEngineRunTime'] = base.Profile.DatapointMember(
            doc="""Engine Run Time Output.  total (cumulative) run time of
            the engine.""",
            name='nvoEngineRunTime',
            profile=self,
            number=19,
            datatype=SNVT_time_f,
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
                    number=9,
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
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=2,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTgeneratorSet()
    pass
