"""SFPThvacValvePositioner standard profile, originally defined in resource
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SNVT_valve_mode import SNVT_valve_mode
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_hvac_emerg import SNVT_hvac_emerg
from pylon.resources.SNVT_length_mil import SNVT_length_mil
from pylon.resources.SNVT_dev_status import SNVT_dev_status
from pylon.resources.SNVT_dev_fault import SNVT_dev_fault
from pylon.resources.SNVT_dev_maint import SNVT_dev_maint
from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.SNVT_length import SNVT_length
from pylon.resources.SNVT_count import SNVT_count
from pylon.resources.SCPTcontrolSignal import SCPTcontrolSignal
from pylon.resources.SCPTdefOutput import SCPTdefOutput
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTminSetpoint import SCPTminSetpoint
from pylon.resources.SCPTmaxSetpoint import SCPTmaxSetpoint
from pylon.resources.SCPTminStroke import SCPTminStroke
from pylon.resources.SCPTmaxStroke import SCPTmaxStroke
from pylon.resources.SCPTvalveOperatingMode import SCPTvalveOperatingMode
from pylon.resources.SCPTnightPurgePosition import SCPTnightPurgePosition
from pylon.resources.SCPTfreeCoolPosition import SCPTfreeCoolPosition
from pylon.resources.SCPTemergencyPosition import SCPTemergencyPosition
from pylon.resources.SCPTdriveTime import SCPTdriveTime
from pylon.resources.SCPTvalveStroke import SCPTvalveStroke
from pylon.resources.SCPTvalveNominalSize import SCPTvalveNominalSize
from pylon.resources.SCPTvalveKvs import SCPTvalveKvs
from pylon.resources.SCPTvalveType import SCPTvalveType
from pylon.resources.SCPTmanfDate import SCPTmanfDate
from pylon.resources.SCPTinstallDate import SCPTinstallDate
from pylon.resources.SCPTactuatorType import SCPTactuatorType
from pylon.resources.SCPTactuatorCharacteristic import SCPTactuatorCharacteristic
from pylon.resources.SCPTtrnsTblX import SCPTtrnsTblX
from pylon.resources.SCPTtrnsTblY import SCPTtrnsTblY
from pylon.resources.SCPTvalveFlowCharacteristic import SCPTvalveFlowCharacteristic
from pylon.resources.SCPTtrnsTblX2 import SCPTtrnsTblX2
from pylon.resources.SCPTtrnsTblY2 import SCPTtrnsTblY2
from pylon.resources.SCPTcombFlowCharacteristic import SCPTcombFlowCharacteristic
from pylon.resources.SCPTtrnsTblX3 import SCPTtrnsTblX3
from pylon.resources.SCPTtrnsTblY3 import SCPTtrnsTblY3
from pylon.resources.SCPTblockProtectionTime import SCPTblockProtectionTime
from pylon.resources.SCPTrunTimeAlarm import SCPTrunTimeAlarm
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer


class SFPThvacValvePositioner(base.Profile):
    """SFPThvacValvePositioner standard profile.  Valve Positioner for HVAC
    Applications.  Also known as a Valve Actuator, it converts the output
    signal of a controller into a mechanical valve action."""

    def __init__(self):
        super().__init__(
            key=8131,
            scope=0,
            principal='nvoControlSignFb'
        )
        self.datapoints['nviControlSignal'] = base.Profile.DatapointMember(
            doc="""Valve Control Signal.  This input network variable
            provides a control setpoint.  The setpoint is given as a
            percentage of the total required flow or heating/cooling
            energy.""",
            name='nviControlSignal',
            profile=self,
            number=1,
            datatype=SNVT_lev_percent,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV01':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV01',
                    profile=self,
                    number=6,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviHvacOpMode'] = base.Profile.DatapointMember(
            doc="""Desired HVAC Operating Mode.  A supervisory controller
            typically uses this input network variable to set the valve
            operating mode.""",
            name='nviHvacOpMode',
            profile=self,
            number=2,
            datatype=SNVT_hvac_mode,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV02':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV02',
                    profile=self,
                    number=7,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoControlSignFb'] = base.Profile.DatapointMember(
            doc="""Valve-Control Signal Mirror.  This output network variable
            mirrors the actual value of nviControlSignal.  This can be used
            for multiple valve-positioner applications.""",
            name='nvoControlSignFb',
            profile=self,
            number=3,
            datatype=SNVT_lev_percent,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV03':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV03',
                    profile=self,
                    number=1,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV03':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV03',
                    profile=self,
                    number=11,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoHvacOpMode'] = base.Profile.DatapointMember(
            doc="""Effective HVAC Operating Mode.  This output network
            variable provides the actual HVAC operating mode.""",
            name='nvoHvacOpMode',
            profile=self,
            number=4,
            datatype=SNVT_hvac_mode,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV04':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV04',
                    profile=self,
                    number=2,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV04':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV04',
                    profile=self,
                    number=12,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoValveOpMode'] = base.Profile.DatapointMember(
            doc="""Effective Valve Operating Mode.  This output network
            variable provides the actual valve operating mode.""",
            name='nvoValveOpMode',
            profile=self,
            number=5,
            datatype=SNVT_valve_mode,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV05':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV05',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                ),
                'nciMinSendTimeNV05':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV05',
                    profile=self,
                    number=13,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviOvrdStop'] = base.Profile.DatapointMember(
            doc="""Override-Valve Stop.  This input network variable provides
            a manual override function to stop the valve;  typically from a
            supervisory device.""",
            name='nviOvrdStop',
            profile=self,
            number=6,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvrdCapacity'] = base.Profile.DatapointMember(
            doc="""Override Valve Capacity.  This input network variable
            provides an override request to the valve capacity;  typically
            from a supervisory device.""",
            name='nviOvrdCapacity',
            profile=self,
            number=7,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvrdPosition'] = base.Profile.DatapointMember(
            doc="""Override Valve Position.  This input network variable
            provides for both an override request and a position value
            relative to the maximum stroke;  typically from a supervisory
            device.""",
            name='nviOvrdPosition',
            profile=self,
            number=8,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEmergencyMode'] = base.Profile.DatapointMember(
            doc="""Emergency Mode Request.  Mandatory for 01 /21:  This input
            network variable is used when the positioner possesses a real
            emergency operation (for example:  a spring-return drive).""",
            name='nviEmergencyMode',
            profile=self,
            number=9,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV09':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV09',
                    profile=self,
                    number=8,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviValvePosition'] = base.Profile.DatapointMember(
            doc="""Read-Value Valve Position.  This input network variable is
            used to connect an external position sensor for precise position
            control.""",
            name='nviValvePosition',
            profile=self,
            number=10,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoValveCapacity'] = base.Profile.DatapointMember(
            doc="""Valve Capacity.  This output network variable provides the
            actual valve capacity as a percentage of the flow.""",
            name='nvoValveCapacity',
            profile=self,
            number=11,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV11':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV11',
                    profile=self,
                    number=4,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV11':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV11',
                    profile=self,
                    number=14,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValvePosition'] = base.Profile.DatapointMember(
            doc="""Valve Position.  This output network variable provides the
            calculated position relative to the maximum stroke length.""",
            name='nvoValvePosition',
            profile=self,
            number=12,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV12':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV12',
                    profile=self,
                    number=15,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoStrokeLength'] = base.Profile.DatapointMember(
            doc="""Stroke Length.  This output network variable provides the
            calculated stroke as length in millimeters.""",
            name='nvoStrokeLength',
            profile=self,
            number=13,
            datatype=SNVT_length_mil,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV13':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV13',
                    profile=self,
                    number=16,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoActValvePos'] = base.Profile.DatapointMember(
            doc="""Actual Valve Position.  This output network variable
            provides the actual position relative to the maximum stroke
            length.""",
            name='nvoActValvePos',
            profile=self,
            number=14,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV14':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV14',
                    profile=self,
                    number=17,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValveFlow'] = base.Profile.DatapointMember(
            doc="""Valve Flow.  This output network variable provides the
            calculated flow relative to the maximum flow of the valve.""",
            name='nvoValveFlow',
            profile=self,
            number=15,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV15':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV15',
                    profile=self,
                    number=18,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoDriveStatus'] = base.Profile.DatapointMember(
            doc="""Drive Status.  This output network variable provides
            status/diagnostic information of the valve drive.""",
            name='nvoDriveStatus',
            profile=self,
            number=16,
            datatype=SNVT_dev_status,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV16':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV16',
                    profile=self,
                    number=19,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoValveFault'] = base.Profile.DatapointMember(
            doc="""Valve Fault.  This output network variable provides fault
            information about the valve.""",
            name='nvoValveFault',
            profile=self,
            number=17,
            datatype=SNVT_dev_fault,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV17':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV17',
                    profile=self,
                    number=20,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoMaintenance'] = base.Profile.DatapointMember(
            doc="""Device maintenance.  This output network variable provides
            maintenance information of the valve.""",
            name='nvoMaintenance',
            profile=self,
            number=18,
            datatype=SNVT_dev_maint,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV18':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV18',
                    profile=self,
                    number=21,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoRuntime'] = base.Profile.DatapointMember(
            doc="""Runtime This output network variable provides the total
            cumulative running time of the valve actuator.""",
            name='nvoRuntime',
            profile=self,
            number=19,
            datatype=SNVT_elapsed_tm,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV19':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV19',
                    profile=self,
                    number=22,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoStrokeCumul'] = base.Profile.DatapointMember(
            doc="""Cumulative Stroke Distance.  This output network variable
            provides the cumulative distance of all strokes of the valve as
            length in meters.""",
            name='nvoStrokeCumul',
            profile=self,
            number=20,
            datatype=SNVT_length,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV20':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV20',
                    profile=self,
                    number=23,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPosErrCount'] = base.Profile.DatapointMember(
            doc="""Position-Error Count.  This output network variable
            provides the count of positioning errors.""",
            name='nvoPosErrCount',
            profile=self,
            number=21,
            datatype=SNVT_count,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV21':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV21',
                    profile=self,
                    number=24,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPwrFailCount'] = base.Profile.DatapointMember(
            doc="""Power-Failure Count.  This output network variable
            provides the count of power failures and voltage dips.""",
            name='nvoPwrFailCount',
            profile=self,
            number=22,
            datatype=SNVT_count,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV22':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV22',
                    profile=self,
                    number=25,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEmergCount'] = base.Profile.DatapointMember(
            doc="""Emergency Count.  This output network variable provides
            the count of emergency actions, as represented with the Emergency
            Mode State network variable.""",
            name='nvoEmergCount',
            profile=self,
            number=23,
            datatype=SNVT_count,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMinSendTimeNV23':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV23',
                    profile=self,
                    number=26,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEmergencyMode'] = base.Profile.DatapointMember(
            doc="""Emergency Mode State.  Mandatory for 01 /21:  This output
            network variable is only used in combination with the Emergency
            Mode Request input network variable.""",
            name='nvoEmergencyMode',
            profile=self,
            number=24,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV24':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV24',
                    profile=self,
                    number=5,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciMinSendTimeNV24':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTimeNV24',
                    profile=self,
                    number=27,
                    datatype=SCPTminSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['nciControlSignal'] = base.Profile.PropertyMember(
            doc="""Control signal.  Start and end points (X,Y) for a
            transition.""",
            name='nciControlSignal',
            profile=self,
            number=9,
            datatype=SCPTcontrolSignal,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciDefPosition'] = base.Profile.PropertyMember(
            doc="""Default output.  The position or level the sensor should
            adopt when updates are not received, or at power-on reset, or
            when overridden.""",
            name='nciDefPosition',
            profile=self,
            number=10,
            datatype=SCPTdefOutput,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=28,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMinPosition'] = base.Profile.PropertyMember(
            doc="""Minimum setpoint.  The minimum setpoint, such as minimum
            angle of rotation or minimum air flow.""",
            name='nciMinPosition',
            profile=self,
            number=29,
            datatype=SCPTminSetpoint,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMaxPosition'] = base.Profile.PropertyMember(
            doc="""Maximum setpoint.  Either the maximum angle of rotation
            for an actuator or the maximum airflow for an actuator depending
            on actuator category.""",
            name='nciMaxPosition',
            profile=self,
            number=30,
            datatype=SCPTmaxSetpoint,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMinStroke'] = base.Profile.PropertyMember(
            doc="""Minimum stroke.  The minimum stroke limit.""",
            name='nciMinStroke',
            profile=self,
            number=31,
            datatype=SCPTminStroke,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMaxStroke'] = base.Profile.PropertyMember(
            doc="""Maximum stroke.  The maximum stroke limit.""",
            name='nciMaxStroke',
            profile=self,
            number=32,
            datatype=SCPTmaxStroke,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciValveOpMode'] = base.Profile.PropertyMember(
            doc="""Valve operating mode.  The normal operating mode of the
            valve.""",
            name='nciValveOpMode',
            profile=self,
            number=33,
            datatype=SCPTvalveOperatingMode,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciNightPurgePos'] = base.Profile.PropertyMember(
            doc="""Night purge valve position.  Valve position in percent
            open for night purge.""",
            name='nciNightPurgePos',
            profile=self,
            number=34,
            datatype=SCPTnightPurgePosition,
            minimum=b'\x00\x00',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciFreeCoolPos'] = base.Profile.PropertyMember(
            doc="""Free cooling valve position.  Valve position in percent
            open for free cooling HVAC mode.""",
            name='nciFreeCoolPos',
            profile=self,
            number=35,
            datatype=SCPTfreeCoolPosition,
            minimum=b'\x00\x00',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciEmergencyPos'] = base.Profile.PropertyMember(
            doc="""Emergency position.  Position in percent of full scale
            (open) for emergency operation.""",
            name='nciEmergencyPos',
            profile=self,
            number=36,
            datatype=SCPTemergencyPosition,
            minimum=b'\x00\x00',
            maximum=b'\x4e\x20',
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciDriveTime'] = base.Profile.PropertyMember(
            doc="""Drive time.  The transition time for a full 100% stroke
            (change from one extreme to the other)""",
            name='nciDriveTime',
            profile=self,
            number=37,
            datatype=SCPTdriveTime,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x05\xdc',
            mandatory=False
        )
        self.properties['nciValveStroke'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciValveStroke',
            profile=self,
            number=38,
            datatype=SCPTvalveStroke,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciValveNomSize'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciValveNomSize',
            profile=self,
            number=39,
            datatype=SCPTvalveNominalSize,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciValveKvs'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciValveKvs',
            profile=self,
            number=40,
            datatype=SCPTvalveKvs,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciValveType'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciValveType',
            profile=self,
            number=41,
            datatype=SCPTvalveType,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciValveDateCode'] = base.Profile.PropertyMember(
            doc="""Manufacture date.  The date of manufacture for the
            device.""",
            name='nciValveDateCode',
            profile=self,
            number=42,
            datatype=SCPTmanfDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciInstallDate'] = base.Profile.PropertyMember(
            doc="""Installation date.  The date of installation for the
            device.""",
            name='nciInstallDate',
            profile=self,
            number=43,
            datatype=SCPTinstallDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciValeDescr'] = base.Profile.PropertyMember(
            doc="""Actuator label.  The identification of the exact actuator
            type or label.""",
            name='nciValeDescr',
            profile=self,
            number=44,
            datatype=SCPTactuatorType,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciActuatorChar'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciActuatorChar',
            profile=self,
            number=45,
            datatype=SCPTactuatorCharacteristic,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciActTransTblX'] = base.Profile.PropertyMember(
            doc="""Translation table X.  Used in conjunction with Translation
            table Y to scale and linearize a value.""",
            name='nciActTransTblX',
            profile=self,
            number=46,
            datatype=SCPTtrnsTblX,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciActTransTblY'] = base.Profile.PropertyMember(
            doc="""Translation table Y.  Used in conjunction with Translation
            table X to scale and linearize a value.""",
            name='nciActTransTblY',
            profile=self,
            number=47,
            datatype=SCPTtrnsTblY,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciValvePlugChar'] = base.Profile.PropertyMember(
            doc="""Valve flow characteristic.  Actual flow characteristic of
            the valve.""",
            name='nciValvePlugChar',
            profile=self,
            number=48,
            datatype=SCPTvalveFlowCharacteristic,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            minimum=b'\x14',
            maximum=b'\x18',
            default=b'\x14',
            mandatory=False
        )
        self.properties['nciValvTransTblX'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciValvTransTblX',
            profile=self,
            number=49,
            datatype=SCPTtrnsTblX2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciValvTransTblY'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciValvTransTblY',
            profile=self,
            number=50,
            datatype=SCPTtrnsTblY2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciCombFlowChar'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciCombFlowChar',
            profile=self,
            number=51,
            datatype=SCPTcombFlowCharacteristic,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciCombTransTblX'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciCombTransTblX',
            profile=self,
            number=52,
            datatype=SCPTtrnsTblX3,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciCombTransTblY'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciCombTransTblY',
            profile=self,
            number=53,
            datatype=SCPTtrnsTblY3,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciAntiStickTime'] = base.Profile.PropertyMember(
            doc="""Minimum time for movement.  The minimum time in hours for
            movement to prevent blocking.""",
            name='nciAntiStickTime',
            profile=self,
            number=54,
            datatype=SCPTblockProtectionTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciRunTimeAlarm'] = base.Profile.PropertyMember(
            doc=""" """,
            name='nciRunTimeAlarm',
            profile=self,
            number=55,
            datatype=SCPTrunTimeAlarm,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=56,
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
            number=57,
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
    item = SFPThvacValvePositioner()
    pass
