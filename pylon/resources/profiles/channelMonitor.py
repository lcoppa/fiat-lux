"""channelMonitor standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.lev_cont
import pylon.resources.properties.highLimit1
import pylon.resources.properties.highLimit1Enable
import pylon.resources.properties.hystHigh1
import pylon.resources.properties.lowLimit1
import pylon.resources.properties.lowLimit1Enable
import pylon.resources.properties.hystLow2
import pylon.resources.datapoints.count_32
import pylon.resources.datapoints.elapsed_tm
import pylon.resources.datapoints.switch
import pylon.resources.properties.linkPowerDetectEnable
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.ifaceDesc
import pylon.resources.properties.monInterval


class channelMonitor(pylon.resources.base.Profile):
    """channelMonitor standard profile.  Channel Monitor.  Channel
    diagnostics and network health monitoring."""

    def __init__(self):
        super().__init__(
            key=132,
            scope=0
        )
        self.datapoints['nvoIvalBandUtl'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Bandwidth utilization.  Bandwidth utilization percentage
            during last interval.""",
            name='nvoIvalBandUtl',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpBandUtlLimHigh':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Bandwidth utilization high limit.  If this limit
                    is implemented and is enabled via
                    nciBandUtlLimHighEnable, if the alarm type was not
                    AL_HIGH_LMT_ALM_1 and the value for the last interval was
                    greater than nciBandUtlLimHigh, then the alarm type
                    becomes AL_HIGH_LMT_ALM_1 and nvoChnlAlarm will be set to
                    True.If the alarm type was AL_HIGH_LMT_ALM_1 and the
                    value drops below nciBandUtlLimHigh minus
                    nciBandUtlHystHigh, then the alarm type becomes
                    AL_HIGH_LMT_CLR_1 and nvoChnlAlarm will be set to False.
                    The hysteresis value is used only to subtract from the
                    limit value.""",
                    name='cpBandUtlLimHigh',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.highLimit1.highLimit1,
                    minimum=b'\x00\x00\x00\x00',
                    maximum=b'\x00\x00\x00\x64',
                    default=b'\x00\x00\x00\x46',
                    mandatory=False
                ),
                'cpBandUtlLimHighEnable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Bandwidth utilization high limit enable.
                    Determines whether nciBandUtlLimHigh is enabled.""",
                    name='cpBandUtlLimHighEnable',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.highLimit1Enable.highLimit1Enable,
                    default=b'\x01',
                    mandatory=False
                ),
                'cpBandUtlHystHigh':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Bandwidth utilization high limit hysteresis.
                    Hysteresis value for the high alarm
                    nciBandUtlLimHigh.""",
                    name='cpBandUtlHystHigh',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.hystHigh1.hystHigh1,
                    default=b'\x00\x00\x00\x05',
                    mandatory=False
                ),
                'cpBandUtlLimLow':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Bandwidth utilization low limit.  The low alarm
                    limit can be useful to detect that, for instance, a
                    certain level of background heartbeat traffic expected on
                    a channel has slowed or stopped-which indicates a power,
                    channel wiring, or other problem.  If the low alarm limit
                    is enabled with nciBandUtlLimLowEnable, also set the
                    nciBandUtlLimLow property to a non-zero value that is
                    slightly below the expected level of background heartbeat
                    traffic.  If the alarm type was not AL_LOW_LMT_ALM_1 and
                    the value is now less than nciBandUtlLimLow, then the
                    alarm type becomes AL_LOW_LMT_ALM_1 and nvoChnlAlarm will
                    be set to True.If the alarm type was AL_LOW_LMT_ALM_1 and
                    the value rises above nciBandUtlLimLow plus
                    nciBandUtlHystLow, then the alarm type becomes
                    AL_LOW_LMT_CLR_1 and nvoChnlAlarm will be set to False.
                    The hysteresis value is used only to add to the limit
                    value.""",
                    name='cpBandUtlLimLow',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.lowLimit1.lowLimit1,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpBandUtlLimLowEnable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Bandwidth utilization low limit enable.
                    Determines whether nciBandUtlLimLow is enabled.""",
                    name='cpBandUtlLimLowEnable',
                    profile=self,
                    number=9,
                    datatype=pylon.resources.properties.lowLimit1Enable.lowLimit1Enable,
                    default=b'\x00',
                    mandatory=False
                ),
                'cpBandUtlHystLow':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Bandwidth utilization low limit hysteresis.
                    Hysteresis value for the low alarm nciBandUtlLimLow.""",
                    name='cpBandUtlHystLow',
                    profile=self,
                    number=10,
                    datatype=pylon.resources.properties.hystLow2.hystLow2,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoIvalCrcErr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""CRC error rate.  Percentage of packets with CRC errors
            during last interval.""",
            name='nvoIvalCrcErr',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpCrcErrLimHigh':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""CRC error rate high limit.  If this limit is
                    implemented and is enabled via nciCrcErrLimHighEnable, if
                    the alarm type was not AL_HIGH_LMT_ALM_1 and the value
                    for the last interval was greater than nciCrcErrLimHigh,
                    then the alarm type becomes AL_HIGH_LMT_ALM_1 and
                    nvoChnlAlarm will be set to True.If the alarm type was
                    AL_HIGH_LMT_ALM_1 and the value drops below
                    nciCrcErrLimHigh minus nciCrcErrHystHigh, then the alarm
                    type becomes AL_HIGH_LMT_CLR_1 and nvoChnlAlarm will be
                    set to False.  The hysteresis value is used only to
                    subtract from the limit value.""",
                    name='cpCrcErrLimHigh',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.highLimit1.highLimit1,
                    minimum=b'\x00\x00\x00\x00',
                    maximum=b'\x00\x00\x00\x64',
                    default=b'\x00\x00\x00\x05',
                    mandatory=False
                ),
                'cpCrcErrLimHighEnable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""CRC error rate high limit enable.  Determines
                    whether nciCrcErrLimHigh is enabled.""",
                    name='cpCrcErrLimHighEnable',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.highLimit1Enable.highLimit1Enable,
                    default=b'\x01',
                    mandatory=False
                ),
                'cpCrcErrHystHigh':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""CRC error rate high limit hysteresis.  Hysteresis
                    value for the high alarm nciCrcErrLimHigh.""",
                    name='cpCrcErrHystHigh',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.hystHigh1.hystHigh1,
                    default=b'\x00\x00\x00\x02',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoIvalMissed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Missed packet rate.  Percentage of missed packets during
            last interval.""",
            name='nvoIvalMissed',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMissedLimHigh':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Missed packet rate high limit.  If this limit is
                    implemented and is enabled via nciMissedLimHighEnable, if
                    the alarm type was not AL_HIGH_LMT_ALM_1 and the value
                    for the last interval was greater than nciMissedLimHigh,
                    then the alarm type becomes AL_HIGH_LMT_ALM_1 and
                    nvoChnlAlarm will be set to True.If the alarm type was
                    AL_HIGH_LMT_ALM_1 and the value drops below
                    nciMissedLimHigh minus nciMissedHystHigh, then the alarm
                    type becomes AL_HIGH_LMT_CLR_1 and nvoChnlAlarm will be
                    set to False.  The hysteresis value is used only to
                    subtract from the limit value.""",
                    name='cpMissedLimHigh',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.highLimit1.highLimit1,
                    minimum=b'\x00\x00\x00\x00',
                    maximum=b'\x00\x00\x00\x64',
                    default=b'\x00\x00\x00\x01',
                    mandatory=False
                ),
                'cpMissedLimHighEnable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Missed packet rate high limit enable.  Determines
                    whether nciMissedLimHigh is enabled.""",
                    name='cpMissedLimHighEnable',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.highLimit1Enable.highLimit1Enable,
                    default=b'\x01',
                    mandatory=False
                ),
                'cpMissedHystHigh':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Missed packet rate high limit hysteresis.
                    Hysteresis value for the high alarm nciMissedLimHigh.""",
                    name='cpMissedHystHigh',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.hystHigh1.hystHigh1,
                    minimum=b'\x00\x00\x00\x00',
                    maximum=b'\x00\x00\x00\x64',
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoIvalPkts'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Packet rate.  Number of packets per second during last
            interval.""",
            name='nvoIvalPkts',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoTotalCrcErr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Total CRC errors.  Total number of CRC errors since
            power-up, reset, or statistics cleared.""",
            name='nvoTotalCrcErr',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoTotalMissed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Total missed packets.  Total number of missed packets
            since power-up, reset, or statistics cleared.""",
            name='nvoTotalMissed',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoTotalPkts'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Total packets.  Total number of packets since power-up,
            reset, or statistics cleared.""",
            name='nvoTotalPkts',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoElapsedTime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Elapsed Time.  Time since the device was rebooted or since
            the statistics for this interface where reset.""",
            name='nvoElapsedTime',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.elapsed_tm.elapsed_tm,
            mandatory=True,
            polled=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMaxCrcErr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Maximum CRC error rate.  Maximum percentage of CRC errors
            in any interval, as reported by nvoIvalCrcErr, since power-up,
            reset, or statistics cleared.""",
            name='nvoMaxCrcErr',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMaxBandUtl'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Maximum bandwidth utilization.  Maximum percentage of
            bandwidth utilization in any interval, as reported by
            nvoIvalBandUtl, since power-up, reset, or statistics cleared.""",
            name='nvoMaxBandUtl',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMaxMissed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Maximum missed packet rate.  Maximum percentage of missed
            packets in any interval, as reported by nvoIvalMissed, since
            power-up, reset, or statistics cleared.""",
            name='nvoMaxMissed',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMaxPkts'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Maximum packet rate.  Maximum number of packets per second
            in any interval, as reported by nvoIvalPackets, since power-up,
            reset, or statistics cleared.""",
            name='nvoMaxPkts',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoIvalMisPre'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Missed preamble rate.  Number of missed preambles per
            second during the last interval.""",
            name='nvoIvalMisPre',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMisPreLimHigh':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Missed preamble rate high limit.  If this limit is
                    implemented and is enabled via nciMisPreLimHighEnable, if
                    the alarm type was not AL_HIGH_LMT_ALM_1 and the value
                    for the last interval was greater than nciMisPreLimHigh,
                    then the alarm type becomes AL_HIGH_LMT_ALM_1 and
                    nvoChnlAlarm will be set to True.If the alarm type was
                    AL_HIGH_LMT_ALM_1 and the value drops below
                    nciMisPreLimHigh minus nciMisPreHystHigh, then the alarm
                    type becomes AL_HIGH_LMT_CLR_1 and nvoChnlAlarm will be
                    set to False.  The hysteresis value is used only to
                    subtract from the limit value.""",
                    name='cpMisPreLimHigh',
                    profile=self,
                    number=17,
                    datatype=pylon.resources.properties.highLimit1.highLimit1,
                    default=b'\x00\x00\x00\x32',
                    mandatory=False
                ),
                'cpMisPreLimHighEnable':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Missed preamble rate high limit enable.
                    Determines whether nciMisPreLimHigh is enabled.""",
                    name='cpMisPreLimHighEnable',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.highLimit1Enable.highLimit1Enable,
                    default=b'\x00',
                    mandatory=False
                ),
                'cpMisPreHystHigh':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Missed preamble rate high limit hysteresis.
                    Hysteresis value for the high alarm nciMisPreLimHigh.""",
                    name='cpMisPreHystHigh',
                    profile=self,
                    number=19,
                    datatype=pylon.resources.properties.hystHigh1.hystHigh1,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoTotalMisPre'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Total missed preambles.  Total number of missed preambles
            since power-up, reset, or statistic cleared.""",
            name='nvoTotalMisPre',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMaxMisPre'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Maximum missed preamble rate.  Maximum number of missed
            preambles per second in any interval, as reported by
            nvoIvalMisPre, since power-up, reset, or statistics cleared.""",
            name='nvoMaxMisPre',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoChnlAlarm'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Channel alarm.  Indicates if the associated channel is in
            alarm state or shows a high error rate.""",
            name='nvoChnlAlarm',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoChnlAlmRat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Channel alarm ratio.  Percentage of intervals the
            associated channel was in alarm state or had a high error rate
            since power-up, reset, or statistics cleared.""",
            name='nvoChnlAlmRat',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLinkPower'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Link power supply status.  Indicates whether the Link
            Power Supply voltage is in the specified range.""",
            name='nvoLinkPower',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpLnPwrDtctEn':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Link Power Detection Enabled.  Determines, whether
                    link power detection is enabled.  If yes, nvoLinkPower
                    indicates existence of link power voltage.""",
                    name='cpLnPwrDtctEn',
                    profile=self,
                    number=20,
                    datatype=pylon.resources.properties.linkPowerDetectEnable.linkPowerDetectEnable,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoAvgPkts'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Average packets.  Average packets per second since
            power-up, reset, or statistics cleared.  Rollover is
            implementation dependent.""",
            name='nvoAvgPkts',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.count_32.count_32,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='cpObjMajVer',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpObjMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='cpObjMinVer',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpIfaceDesc'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Interface description.  Human readable description of the
            interface the functional block is assigned to.""",
            name='cpIfaceDesc',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.ifaceDesc.ifaceDesc,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpMonInterval'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Monitor Interval.  This configuration property defines the
            interval over which statistics are collected and averages are
            calculated.""",
            name='cpMonInterval',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.monInterval.monInterval,
            minimum=b'\x00\x00\x00\x00\x01\x00\x00',
            maximum=b'\x00\x00\x12\x0c\x0f\x00\x00',
            default=b'\x00\x00\x00\x00\x05\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTchannelMonitor'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = channelMonitor()
    pass
