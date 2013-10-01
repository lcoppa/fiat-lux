"""generatorSet standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.switch
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.state
import pylon.resources.datapoints.freq_hz
import pylon.resources.datapoints.volt_ac
import pylon.resources.datapoints.amp_ac
import pylon.resources.datapoints.pwr_fact
import pylon.resources.datapoints.power_f
import pylon.resources.datapoints.elec_whr_f
import pylon.resources.datapoints.rpm
import pylon.resources.datapoints.temp
import pylon.resources.datapoints.press
import pylon.resources.datapoints.volt
import pylon.resources.datapoints.count
import pylon.resources.datapoints.time_f
import pylon.resources.properties.location


class generatorSet(pylon.resources.base.Profile):
    """generatorSet standard profile.  Generator Set.  Used to control a
    generator set (genset) for power generation in primary or secondary
    systems."""

    def __init__(self):
        super().__init__(
            key=13110,
            scope=0
        )
        self.datapoints['nviStartCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Start Command Input.  start and stop the generator
            set.""",
            name='nviStartCmd',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviFaultResetCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fault Reset Command Input.  reset or clear a generator set
            fault.""",
            name='nviFaultResetCmd',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoRunStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Run Status Output.  running at rated speed and voltage and
            is ready to accept load.""",
            name='nvoRunStatus',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV03',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoFaultStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fault Status Output.  report the presence of a generator
            set fault.""",
            name='nvoFaultStatus',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviShutdownCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Shutdown Command Input.  emergency, unconditional
            shutdown/disable of run.""",
            name='nviShutdownCmd',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoNFPA110Annun'] = pylon.resources.base.Profile.DatapointMember(
            doc="""NFPA 110 Annunciation Output.  report state of National
            Fire Protection Agency (USA) genset faults (NFPA s.110)""",
            name='nvoNFPA110Annun',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.state.state,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFrequency'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Frequency Output.  output frequency of the generator
            set.""",
            name='nvoFrequency',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.freq_hz.freq_hz,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoVoltageLL'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Line-to-Line Voltage Output.  line-to-line output
            voltage(s) of the generator set.""",
            name='nvoVoltageLL',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.volt_ac.volt_ac,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoVoltageLN'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Line-to-Neutral Voltage Output.  line-to-neutral output
            voltage(s) of the generator set.""",
            name='nvoVoltageLN',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.volt_ac.volt_ac,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCurrent'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Line Current Output.  output line current(s) of the
            generator set.""",
            name='nvoCurrent',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.amp_ac.amp_ac,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPowerFactor'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Power Factor Output.  power factor of the generator
            set.""",
            name='nvoPowerFactor',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.pwr_fact.pwr_fact,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRealPower'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Real Power Output.  real power output as a floating type (
            in Watts)""",
            name='nvoRealPower',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.power_f.power_f,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoGenEnergy'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Generated Energy Output.  total (cumulative) electrical
            energy (WHR) generated by genset.""",
            name='nvoGenEnergy',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.elec_whr_f.elec_whr_f,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV13':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV13',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEngineSpeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Engine Speed Output.  engine speed of the generator
            set.""",
            name='nvoEngineSpeed',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.rpm.rpm,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV14':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV14',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEngineTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Engine Temperature Output.  engine temperature of the
            generator set.""",
            name='nvoEngineTemp',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.temp.temp,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV15':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV15',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOilPressure'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Engine Oil Pressure Output.  engine oil pressure of the
            generator set.""",
            name='nvoOilPressure',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.press.press,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV16':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV16',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoBattery'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Battery Voltage Output.  starting battery voltage of the
            engine.""",
            name='nvoBattery',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.volt.volt,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV17':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV17',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEngineStarts'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Engine Starts Output.  total number of successful engine
            starts.""",
            name='nvoEngineStarts',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.count.count,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEngineRunTime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Engine Run Time Output.  total (cumulative) run time of
            the engine.""",
            name='nvoEngineRunTime',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.time_f.time_f,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV19':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV19',
                    profile=self,
                    number=9,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            array_size_max=16,
            default=b'\x00\x00',
            mandatory=True
        )
        self._original_name = 'SFPTgeneratorSet'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = generatorSet()
    pass
