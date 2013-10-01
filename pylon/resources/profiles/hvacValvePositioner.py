"""hvacValvePositioner standard profile, originally defined in resource file
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.lev_percent
import pylon.resources.properties.maxRcvTime
import pylon.resources.datapoints.hvac_mode
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.minSendTime
import pylon.resources.datapoints.valve_mode
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.hvac_emerg
import pylon.resources.datapoints.length_mil
import pylon.resources.datapoints.dev_status
import pylon.resources.datapoints.dev_fault
import pylon.resources.datapoints.dev_maint
import pylon.resources.datapoints.elapsed_tm
import pylon.resources.datapoints.length
import pylon.resources.datapoints.count
import pylon.resources.properties.controlSignal
import pylon.resources.properties.defOutput
import pylon.resources.properties.location
import pylon.resources.properties.minSetpoint
import pylon.resources.properties.maxSetpoint
import pylon.resources.properties.minStroke
import pylon.resources.properties.maxStroke
import pylon.resources.properties.valveOperatingMode
import pylon.resources.properties.nightPurgePosition
import pylon.resources.properties.freeCoolPosition
import pylon.resources.properties.emergencyPosition
import pylon.resources.properties.driveTime
import pylon.resources.properties.valveStroke
import pylon.resources.properties.valveNominalSize
import pylon.resources.properties.valveKvs
import pylon.resources.properties.valveType
import pylon.resources.properties.manfDate
import pylon.resources.properties.installDate
import pylon.resources.properties.actuatorType
import pylon.resources.properties.actuatorCharacteristic
import pylon.resources.properties.trnsTblX
import pylon.resources.properties.trnsTblY
import pylon.resources.properties.valveFlowCharacteristic
import pylon.resources.properties.trnsTblX2
import pylon.resources.properties.trnsTblY2
import pylon.resources.properties.combFlowCharacteristic
import pylon.resources.properties.trnsTblX3
import pylon.resources.properties.trnsTblY3
import pylon.resources.properties.blockProtectionTime
import pylon.resources.properties.runTimeAlarm
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer


class hvacValvePositioner(pylon.resources.base.Profile):
    """hvacValvePositioner standard profile.  Valve Positioner for HVAC
    Applications.  Also known as a Valve Actuator, it converts the output
    signal of a controller into a mechanical valve action."""

    def __init__(self):
        super().__init__(
            key=8131,
            scope=0,
            principal='nvoControlSignFb'
        )
        self.datapoints['nviControlSignal'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Valve Control Signal.  This input network variable
            provides a control setpoint.  The setpoint is given as a
            percentage of the total required flow or heating/cooling
            energy.""",
            name='nviControlSignal',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV01':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV01',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviHvacOpMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Desired HVAC Operating Mode.  A supervisory controller
            typically uses this input network variable to set the valve
            operating mode.""",
            name='nviHvacOpMode',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV02':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV02',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoControlSignFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Valve-Control Signal Mirror.  This output network variable
            mirrors the actual value of nviControlSignal.  This can be used
            for multiple valve-positioner applications.""",
            name='nvoControlSignFb',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV03',
                    profile=self,
                    number=1,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV03':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV03',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoHvacOpMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective HVAC Operating Mode.  This output network
            variable provides the actual HVAC operating mode.""",
            name='nvoHvacOpMode',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV04':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV04',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV04':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV04',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoValveOpMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective Valve Operating Mode.  This output network
            variable provides the actual valve operating mode.""",
            name='nvoValveOpMode',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.valve_mode.valve_mode,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV05':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV05',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV05':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV05',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviOvrdStop'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Override-Valve Stop.  This input network variable provides
            a manual override function to stop the valve;  typically from a
            supervisory device.""",
            name='nviOvrdStop',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvrdCapacity'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Override Valve Capacity.  This input network variable
            provides an override request to the valve capacity;  typically
            from a supervisory device.""",
            name='nviOvrdCapacity',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvrdPosition'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Override Valve Position.  This input network variable
            provides for both an override request and a position value
            relative to the maximum stroke;  typically from a supervisory
            device.""",
            name='nviOvrdPosition',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEmergencyMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency Mode Request.  Mandatory for 01 /21:  This input
            network variable is used when the positioner possesses a real
            emergency operation (for example:  a spring-return drive).""",
            name='nviEmergencyMode',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV09':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV09',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviValvePosition'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Read-Value Valve Position.  This input network variable is
            used to connect an external position sensor for precise position
            control.""",
            name='nviValvePosition',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoValveCapacity'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Valve Capacity.  This output network variable provides the
            actual valve capacity as a percentage of the flow.""",
            name='nvoValveCapacity',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV11':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV11',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV11':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV11',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValvePosition'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Valve Position.  This output network variable provides the
            calculated position relative to the maximum stroke length.""",
            name='nvoValvePosition',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV12':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV12',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoStrokeLength'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Stroke Length.  This output network variable provides the
            calculated stroke as length in millimeters.""",
            name='nvoStrokeLength',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.length_mil.length_mil,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV13':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV13',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoActValvePos'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actual Valve Position.  This output network variable
            provides the actual position relative to the maximum stroke
            length.""",
            name='nvoActValvePos',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV14':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV14',
                    profile=self,
                    number=17,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValveFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Valve Flow.  This output network variable provides the
            calculated flow relative to the maximum flow of the valve.""",
            name='nvoValveFlow',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV15':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV15',
                    profile=self,
                    number=18,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoDriveStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Drive Status.  This output network variable provides
            status/diagnostic information of the valve drive.""",
            name='nvoDriveStatus',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.dev_status.dev_status,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV16':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV16',
                    profile=self,
                    number=19,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValveFault'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Valve Fault.  This output network variable provides fault
            information about the valve.""",
            name='nvoValveFault',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.dev_fault.dev_fault,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV17':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV17',
                    profile=self,
                    number=20,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoMaintenance'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Device maintenance.  This output network variable provides
            maintenance information of the valve.""",
            name='nvoMaintenance',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.dev_maint.dev_maint,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV18':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV18',
                    profile=self,
                    number=21,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoRuntime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Runtime This output network variable provides the total
            cumulative running time of the valve actuator.""",
            name='nvoRuntime',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.elapsed_tm.elapsed_tm,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV19':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV19',
                    profile=self,
                    number=22,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoStrokeCumul'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Cumulative Stroke Distance.  This output network variable
            provides the cumulative distance of all strokes of the valve as
            length in meters.""",
            name='nvoStrokeCumul',
            profile=self,
            number=20,
            datatype=pylon.resources.datapoints.length.length,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV20':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV20',
                    profile=self,
                    number=23,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPosErrCount'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Position-Error Count.  This output network variable
            provides the count of positioning errors.""",
            name='nvoPosErrCount',
            profile=self,
            number=21,
            datatype=pylon.resources.datapoints.count.count,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV21':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV21',
                    profile=self,
                    number=24,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPwrFailCount'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Power-Failure Count.  This output network variable
            provides the count of power failures and voltage dips.""",
            name='nvoPwrFailCount',
            profile=self,
            number=22,
            datatype=pylon.resources.datapoints.count.count,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV22':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV22',
                    profile=self,
                    number=25,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEmergCount'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency Count.  This output network variable provides
            the count of emergency actions, as represented with the Emergency
            Mode State network variable.""",
            name='nvoEmergCount',
            profile=self,
            number=23,
            datatype=pylon.resources.datapoints.count.count,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV23':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV23',
                    profile=self,
                    number=26,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEmergencyMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency Mode State.  Mandatory for 01 /21:  This output
            network variable is only used in combination with the Emergency
            Mode Request input network variable.""",
            name='nvoEmergencyMode',
            profile=self,
            number=24,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV24':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV24',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV24':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV24',
                    profile=self,
                    number=27,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciControlSignal'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Control signal.  Start and end points (X,Y) for a
            transition.""",
            name='nciControlSignal',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.controlSignal.controlSignal,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciDefPosition'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Default output.  The position or level the sensor should
            adopt when updates are not received, or at power-on reset, or
            when overridden.""",
            name='nciDefPosition',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.defOutput.defOutput,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=28,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMinPosition'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum setpoint.  The minimum setpoint, such as minimum
            angle of rotation or minimum air flow.""",
            name='nciMinPosition',
            profile=self,
            number=29,
            datatype=pylon.resources.properties.minSetpoint.minSetpoint,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMaxPosition'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum setpoint.  Either the maximum angle of rotation
            for an actuator or the maximum airflow for an actuator depending
            on actuator category.""",
            name='nciMaxPosition',
            profile=self,
            number=30,
            datatype=pylon.resources.properties.maxSetpoint.maxSetpoint,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinStroke'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum stroke.  The minimum stroke limit.""",
            name='nciMinStroke',
            profile=self,
            number=31,
            datatype=pylon.resources.properties.minStroke.minStroke,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMaxStroke'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum stroke.  The maximum stroke limit.""",
            name='nciMaxStroke',
            profile=self,
            number=32,
            datatype=pylon.resources.properties.maxStroke.maxStroke,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciValveOpMode'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Valve operating mode.  The normal operating mode of the
            valve.""",
            name='nciValveOpMode',
            profile=self,
            number=33,
            datatype=pylon.resources.properties.valveOperatingMode.valveOperatingMode,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciNightPurgePos'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Night purge valve position.  Valve position in percent
            open for night purge.""",
            name='nciNightPurgePos',
            profile=self,
            number=34,
            datatype=pylon.resources.properties.nightPurgePosition.nightPurgePosition,
            minimum=b'\x00\x00',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciFreeCoolPos'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Free cooling valve position.  Valve position in percent
            open for free cooling HVAC mode.""",
            name='nciFreeCoolPos',
            profile=self,
            number=35,
            datatype=pylon.resources.properties.freeCoolPosition.freeCoolPosition,
            minimum=b'\x00\x00',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciEmergencyPos'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Emergency position.  Position in percent of full scale
            (open) for emergency operation.""",
            name='nciEmergencyPos',
            profile=self,
            number=36,
            datatype=pylon.resources.properties.emergencyPosition.emergencyPosition,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciDriveTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Drive time.  The transition time for a full 100% stroke
            (change from one extreme to the other)""",
            name='nciDriveTime',
            profile=self,
            number=37,
            datatype=pylon.resources.properties.driveTime.driveTime,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x05\xdc',
            mandatory=False
        )
        self.properties['nciValveStroke'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciValveStroke',
            profile=self,
            number=38,
            datatype=pylon.resources.properties.valveStroke.valveStroke,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciValveNomSize'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciValveNomSize',
            profile=self,
            number=39,
            datatype=pylon.resources.properties.valveNominalSize.valveNominalSize,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciValveKvs'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciValveKvs',
            profile=self,
            number=40,
            datatype=pylon.resources.properties.valveKvs.valveKvs,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciValveType'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciValveType',
            profile=self,
            number=41,
            datatype=pylon.resources.properties.valveType.valveType,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciValveDateCode'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Manufacture date.  The date of manufacture for the
            device.""",
            name='nciValveDateCode',
            profile=self,
            number=42,
            datatype=pylon.resources.properties.manfDate.manfDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciInstallDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Installation date.  The date of installation for the
            device.""",
            name='nciInstallDate',
            profile=self,
            number=43,
            datatype=pylon.resources.properties.installDate.installDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciValeDescr'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Actuator label.  The identification of the exact actuator
            type or label.""",
            name='nciValeDescr',
            profile=self,
            number=44,
            datatype=pylon.resources.properties.actuatorType.actuatorType,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciActuatorChar'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciActuatorChar',
            profile=self,
            number=45,
            datatype=pylon.resources.properties.actuatorCharacteristic.actuatorCharacteristic,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciActTransTblX'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Translation table X.  Used in conjunction with Translation
            table Y to scale and linearize a value.""",
            name='nciActTransTblX',
            profile=self,
            number=46,
            datatype=pylon.resources.properties.trnsTblX.trnsTblX,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciActTransTblY'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Translation table Y.  Used in conjunction with Translation
            table X to scale and linearize a value.""",
            name='nciActTransTblY',
            profile=self,
            number=47,
            datatype=pylon.resources.properties.trnsTblY.trnsTblY,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciValvePlugChar'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Valve flow characteristic.  Actual flow characteristic of
            the valve.""",
            name='nciValvePlugChar',
            profile=self,
            number=48,
            datatype=pylon.resources.properties.valveFlowCharacteristic.valveFlowCharacteristic,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            minimum=b'\x14',
            maximum=b'\x18',
            default=b'\x14',
            mandatory=False
        )
        self.properties['nciValvTransTblX'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciValvTransTblX',
            profile=self,
            number=49,
            datatype=pylon.resources.properties.trnsTblX2.trnsTblX2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciValvTransTblY'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciValvTransTblY',
            profile=self,
            number=50,
            datatype=pylon.resources.properties.trnsTblY2.trnsTblY2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciCombFlowChar'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciCombFlowChar',
            profile=self,
            number=51,
            datatype=pylon.resources.properties.combFlowCharacteristic.combFlowCharacteristic,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciCombTransTblX'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciCombTransTblX',
            profile=self,
            number=52,
            datatype=pylon.resources.properties.trnsTblX3.trnsTblX3,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciCombTransTblY'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciCombTransTblY',
            profile=self,
            number=53,
            datatype=pylon.resources.properties.trnsTblY3.trnsTblY3,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciAntiStickTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum time for movement.  The minimum time in hours for
            movement to prevent blocking.""",
            name='nciAntiStickTime',
            profile=self,
            number=54,
            datatype=pylon.resources.properties.blockProtectionTime.blockProtectionTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciRunTimeAlarm'] = pylon.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='nciRunTimeAlarm',
            profile=self,
            number=55,
            datatype=pylon.resources.properties.runTimeAlarm.runTimeAlarm,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=56,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciObjMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='nciObjMinVer',
            profile=self,
            number=57,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self._original_name = 'SFPThvacValvePositioner'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = hvacValvePositioner()
    pass
