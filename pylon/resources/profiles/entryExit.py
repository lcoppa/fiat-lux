"""entryExit standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.ent_state
import pylon.resources.properties.defOutput
import pylon.resources.datapoints.ent_status
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.minSendTime
import pylon.resources.datapoints.ent_opmode
import pylon.resources.properties.safExtCnfg
import pylon.resources.properties.emergCnfg
import pylon.resources.datapoints.switch
import pylon.resources.properties.delayTime
import pylon.resources.datapoints.flow_dir
import pylon.resources.datapoints.str_asc
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.holdTime
import pylon.resources.properties.location
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.nwrkCnfg
import pylon.resources.properties.sluiceCnfg


class entryExit(pylon.resources.base.Profile):
    """entryExit standard profile.  Entry / Exit Object.  An Entry / Exit
    device is a door, lock, sluice, or something that allows and prohibits
    entry of a physical unit in to and out of an area."""

    def __init__(self):
        super().__init__(
            key=5051,
            scope=0
        )
        self.datapoints['nviEntryState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Entry state.  Desired state for an entry object, e.g., a
            door, lock, sluice, or something that controls entry of an
            area.""",
            name='nviEntryState',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.ent_state.ent_state,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciDefaultState':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default output.  The position or level the
                    actuator should adopt when updates are not received, or
                    at power-on reset, or when overridden.""",
                    name='nciDefaultState',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.defOutput.defOutput,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEntryStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Entry status.  Status information from an entry object,
            e.g., a door, lock, sluice, or something that allows/prohits
            entry of an area.""",
            name='nvoEntryStatus',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.ent_status.ent_status,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTime',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    maximum=b'\x8c\xa0',
                    mandatory=True
                ),
                'nciMinSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Minimum send time.  The minimum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMinSendTime',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.minSendTime.minSendTime,
                    maximum=b'\x8c\xa0',
                    mandatory=True
                )
            }
        )
        self.datapoints['nviEntryOpMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Entry operation mode.  Operation-mode for an entry object,
            e.g., a door, lock, sluice, or something which allows/prohibits
            entry to an area.""",
            name='nviEntryOpMode',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.ent_opmode.ent_opmode,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciDefaultOpMode':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Default output.  The position or level the
                    actuator should adopt when updates are not received, or
                    at power-on reset, or when overridden.""",
                    name='nciDefaultOpMode',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.defOutput.defOutput,
                    mandatory=False
                ),
                'nciSafExtCnfg':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Safety Mode.  Mode that device must be brought to
                    for safety external state of operation.""",
                    name='nciSafExtCnfg',
                    profile=self,
                    number=9,
                    datatype=pylon.resources.properties.safExtCnfg.safExtCnfg,
                    default=b'\x00\x00\x00\x02',
                    mandatory=False
                ),
                'nciEmergencyCnfg':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Emergency Mode.  Mode that device must be brought
                    to for emergency state of operation.""",
                    name='nciEmergencyCnfg',
                    profile=self,
                    number=10,
                    datatype=pylon.resources.properties.emergCnfg.emergCnfg,
                    default=b'\x00\x00\x00\x02',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPreAlarm'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Warning alarm.  Warning alarm setting when the device has
            been unable to perform a requested command longer than the
            nciPreAlarmDly time, but not as long as the nciAftAlarmDly
            time.""",
            name='nvoPreAlarm',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciPreAlarmDly':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Delay time, default to scene.  Delay time before a
                    pre-alarm (warning) is sent.""",
                    name='nciPreAlarmDly',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.delayTime.delayTime,
                    maximum=b'\x8c\xa0',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviPositioned'] = pylon.resources.base.Profile.DatapointMember(
            doc="""In lockable position.  Whether the mechanical equipment
            being subject to locking is in lockable position or not.
            Typically, this can be an open or closed door.""",
            name='nviPositioned',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoAftAlarm'] = pylon.resources.base.Profile.DatapointMember(
            doc="""After-warning alarm.  Alarm setting when the device has
            been unable to perform a requested command for more than the
            nciPreAlarmDly time.""",
            name='nvoAftAlarm',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciAftAlarmDly':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Delay time, default to scene.  Delay time before
                    an alarm is sent.""",
                    name='nciAftAlarmDly',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.delayTime.delayTime,
                    maximum=b'\x8c\xa0',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOpen'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Device-open request.  opens the device in any state but
            EM_BLOCKED or EM_MANUAL.  After the open command is taken away,
            the device goes back to its previous state.""",
            name='nviOpen',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOpenFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Device-open command feedback.  Feedback of the nviOpen
            network variable input.""",
            name='nvoOpenFb',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDirection'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Direction-flow control.  Control the direction of
            persons/items/fluids through device.""",
            name='nviDirection',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.flow_dir.flow_dir,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDirectionFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Direction-flow control feedback.  Direction of
            persons/items/fluids through device.""",
            name='nvoDirectionFb',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.flow_dir.flow_dir,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviUpdateServ'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Service-message update request.  Request an update of an
            optional service-message output.""",
            name='nviUpdateServ',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoServiceMsg'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Service message.  Current service-message information.""",
            name='nvoServiceMsg',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.str_asc.str_asc,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviSluiceLock'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Sluice token input.  The sluice token input must be set to
            TOKEN to indicate that an opening cycle is legal in case of
            sluice operation.""",
            name='nviSluiceLock',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSluiceLock'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Sluice token feedback.  Token feedback output in a
            sluice-lock configuration.""",
            name='nvoSluiceLock',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMaxRcvTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciMaxRcvTime',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            maximum=b'\x8c\xa0',
            mandatory=True
        )
        self.properties['nciOpenTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Hold time.  Used to control the time the device is in open
            state before it returns to its former state (closed,
            closed/locked, etc.)""",
            name='nciOpenTime',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.holdTime.holdTime,
            minimum=b'\x00\x0a',
            maximum=b'\xff\xff',
            default=b'\xff\xff',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=12,
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
            number=13,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciNetworkConfig'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Network configuration source.  The value of this field
            determines the source of the node's network configuration.""",
            name='nciNetworkConfig',
            profile=self,
            number=14,
            datatype=pylon.resources.properties.nwrkCnfg.nwrkCnfg,
            flags=pylon.resources.base.PropertyFlags.RESET,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciSluiceCnfg'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Master-slave control for sluice.  A sluice is built with
            two or more entry/exit devices with interlock capability.  Role
            of a device in a sluice operation.""",
            name='nciSluiceCnfg',
            profile=self,
            number=15,
            datatype=pylon.resources.properties.sluiceCnfg.sluiceCnfg,
            default=b'\xff',
            mandatory=False
        )
        self._original_name = 'SFPTentryExit'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = entryExit()
    pass
