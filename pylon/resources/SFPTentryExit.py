"""SFPTentryExit standard profile, originally defined in resource file set
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_ent_state import SNVT_ent_state
from pylon.resources.SCPTdefOutput import SCPTdefOutput
from pylon.resources.SNVT_ent_status import SNVT_ent_status
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SNVT_ent_opmode import SNVT_ent_opmode
from pylon.resources.SCPTsafExtCnfg import SCPTsafExtCnfg
from pylon.resources.SCPTemergCnfg import SCPTemergCnfg
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTdelayTime import SCPTdelayTime
from pylon.resources.SNVT_flow_dir import SNVT_flow_dir
from pylon.resources.SNVT_str_asc import SNVT_str_asc
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTholdTime import SCPTholdTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer
from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg
from pylon.resources.SCPTsluiceCnfg import SCPTsluiceCnfg


class SFPTentryExit(base.Profile):
    """SFPTentryExit standard profile.  Entry / Exit Object.  An Entry / Exit
    device is a door, lock, sluice, or something that allows and prohibits
    entry of a physical unit in to and out of an area."""

    def __init__(self):
        super().__init__(
            key=5051,
            scope=0
        )
        self.datapoints['nviEntryState'] = base.Profile.DatapointMember(
            doc="""Entry state.  Desired state for an entry object, e.g., a
            door, lock, sluice, or something that controls entry of an
            area.""",
            name='nviEntryState',
            profile=self,
            number=1,
            datatype=SNVT_ent_state,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciDefaultState':
                base.Profile.PropertyMember(
                    doc="""Default output.  The position or level the
                    actuator should adopt when updates are not received, or
                    at power-on reset, or when overridden.""",
                    name='nciDefaultState',
                    profile=self,
                    number=5,
                    datatype=SCPTdefOutput,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEntryStatus'] = base.Profile.DatapointMember(
            doc="""Entry status.  Status information from an entry object,
            e.g., a door, lock, sluice, or something that allows/prohits
            entry of an area.""",
            name='nvoEntryStatus',
            profile=self,
            number=2,
            datatype=SNVT_ent_status,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTime':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTime',
                    profile=self,
                    number=2,
                    datatype=SCPTmaxSendTime,
                    maximum=b'\x8c\xa0',
                    mandatory=True
                ),
                'nciMinSendTime':
                base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTime',
                    profile=self,
                    number=3,
                    datatype=SCPTminSendTime,
                    maximum=b'\x8c\xa0',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviEntryOpMode'] = base.Profile.DatapointMember(
            doc="""Entry operation mode.  Operation-mode for an entry object,
            e.g., a door, lock, sluice, or something which allows/prohibits
            entry to an area.""",
            name='nviEntryOpMode',
            profile=self,
            number=3,
            datatype=SNVT_ent_opmode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciDefaultOpMode':
                base.Profile.PropertyMember(
                    doc="""Default output.  The position or level the
                    actuator should adopt when updates are not received, or
                    at power-on reset, or when overridden.""",
                    name='nciDefaultOpMode',
                    profile=self,
                    number=6,
                    datatype=SCPTdefOutput,
                    mandatory=False
                ),
                'nciSafExtCnfg':
                base.Profile.PropertyMember(
                    doc="""Safety Mode.  Mode that device must be brought to
                    for safety external state of operation.""",
                    name='nciSafExtCnfg',
                    profile=self,
                    number=9,
                    datatype=SCPTsafExtCnfg,
                    default=b'\x00\x00\x00\x02',
                    mandatory=False
                ),
                'nciEmergencyCnfg':
                base.Profile.PropertyMember(
                    doc="""Emergency Mode.  Mode that device must be brought
                    to for emergency state of operation.""",
                    name='nciEmergencyCnfg',
                    profile=self,
                    number=10,
                    datatype=SCPTemergCnfg,
                    default=b'\x00\x00\x00\x02',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPreAlarm'] = base.Profile.DatapointMember(
            doc="""Warning alarm.  Warning alarm setting when the device has
            been unable to perform a requested command longer than the
            nciPreAlarmDly time, but not as long as the nciAftAlarmDly
            time.""",
            name='nvoPreAlarm',
            profile=self,
            number=4,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciPreAlarmDly':
                base.Profile.PropertyMember(
                    doc="""Delay time, default to scene.  Delay time before a
                    pre-alarm (warning) is sent.""",
                    name='nciPreAlarmDly',
                    profile=self,
                    number=7,
                    datatype=SCPTdelayTime,
                    maximum=b'\x8c\xa0',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviPositioned'] = base.Profile.DatapointMember(
            doc="""In lockable position.  Whether the mechanical equipment
            being subject to locking is in lockable position or not.
            Typically, this can be an open or closed door.""",
            name='nviPositioned',
            profile=self,
            number=5,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAftAlarm'] = base.Profile.DatapointMember(
            doc="""After-warning alarm.  Alarm setting when the device has
            been unable to perform a requested command for more than the
            nciPreAlarmDly time.""",
            name='nvoAftAlarm',
            profile=self,
            number=6,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciAftAlarmDly':
                base.Profile.PropertyMember(
                    doc="""Delay time, default to scene.  Delay time before
                    an alarm is sent.""",
                    name='nciAftAlarmDly',
                    profile=self,
                    number=8,
                    datatype=SCPTdelayTime,
                    maximum=b'\x8c\xa0',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOpen'] = base.Profile.DatapointMember(
            doc="""Device-open request.  opens the device in any state but
            EM_BLOCKED or EM_MANUAL.  After the open command is taken away,
            the device goes back to its previous state.""",
            name='nviOpen',
            profile=self,
            number=7,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOpenFb'] = base.Profile.DatapointMember(
            doc="""Device-open command feedback.  Feedback of the nviOpen
            network variable input.""",
            name='nvoOpenFb',
            profile=self,
            number=8,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDirection'] = base.Profile.DatapointMember(
            doc="""Direction-flow control.  Control the direction of
            persons/items/fluids through device.""",
            name='nviDirection',
            profile=self,
            number=9,
            datatype=SNVT_flow_dir,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDirectionFb'] = base.Profile.DatapointMember(
            doc="""Direction-flow control feedback.  Direction of
            persons/items/fluids through device.""",
            name='nvoDirectionFb',
            profile=self,
            number=10,
            datatype=SNVT_flow_dir,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviUpdateServ'] = base.Profile.DatapointMember(
            doc="""Service-message update request.  Request an update of an
            optional service-message output.""",
            name='nviUpdateServ',
            profile=self,
            number=11,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoServiceMsg'] = base.Profile.DatapointMember(
            doc="""Service message.  Current service-message information.""",
            name='nvoServiceMsg',
            profile=self,
            number=12,
            datatype=SNVT_str_asc,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviSluiceLock'] = base.Profile.DatapointMember(
            doc="""Sluice token input.  The sluice token input must be set to
            TOKEN to indicate that an opening cycle is legal in case of
            sluice operation.""",
            name='nviSluiceLock',
            profile=self,
            number=13,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSluiceLock'] = base.Profile.DatapointMember(
            doc="""Sluice token feedback.  Token feedback output in a
            sluice-lock configuration.""",
            name='nvoSluiceLock',
            profile=self,
            number=14,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMaxRcvTime'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciMaxRcvTime',
            profile=self,
            number=1,
            datatype=SCPTmaxRcvTime,
            maximum=b'\x8c\xa0',
            mandatory=True
        )
        self.properties['nciOpenTime'] = base.Profile.PropertyMember(
            doc="""Hold time.  Used to control the time the device is in open
            state before it returns to its former state (closed,
            closed/locked, etc.)""",
            name='nciOpenTime',
            profile=self,
            number=4,
            datatype=SCPTholdTime,
            minimum=b'\x00\x0a',
            maximum=b'\xff\xff',
            default=b'\xff\xff',
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=11,
            datatype=SCPTlocation,
            mandatory=False
        )
        self.properties['nciObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=12,
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
            number=13,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciNetworkConfig'] = base.Profile.PropertyMember(
            doc="""Network configuration source.  The value of this field
            determines the source of the node's network configuration.""",
            name='nciNetworkConfig',
            profile=self,
            number=14,
            datatype=SCPTnwrkCnfg,
            flags=base.PropertyFlags.RESET,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciSluiceCnfg'] = base.Profile.PropertyMember(
            doc="""Master-slave control for sluice.  A sluice is built with
            two or more entry/exit devices with interlock capability.  Role
            of a device in a sluice operation.""",
            name='nciSluiceCnfg',
            profile=self,
            number=15,
            datatype=SCPTsluiceCnfg,
            default=b'\xff',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTentryExit()
    pass
