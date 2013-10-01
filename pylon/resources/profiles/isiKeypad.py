"""isiKeypad standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.switch_2
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.elapsed_tm
import pylon.resources.properties.runHrInit
import pylon.resources.properties.runHrAlarm
import pylon.resources.properties.name1
import pylon.resources.properties.name2
import pylon.resources.properties.name3
import pylon.resources.properties.location
import pylon.resources.properties.buttonPressAction
import pylon.resources.properties.buttonColor
import pylon.resources.properties.minSendTime
import pylon.resources.properties.defOutput
import pylon.resources.properties.inFbDly
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer
import pylon.resources.properties.buttonRepeatInterval
import pylon.resources.properties.sceneName
import pylon.resources.properties.lightingGroupEnable


class isiKeypad(pylon.resources.base.Profile):
    """isiKeypad standard profile.  ISI Keypad.  Reports the state, scene,
    and setting selected on a keypad.  A keypad may consist of one or more
    push buttons or toggle switches, each optionally including a lamp
    indicator such as an LED."""

    def __init__(self):
        super().__init__(
            key=3253,
            scope=0,
            principal='nvoSwitch'
        )
        self.datapoints['nvoSwitch'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Switch output value.  Selected state, scene, and setting
            output.  Also reports power consumption by the keypad, which may
            be measured or estimated.""",
            name='nvoSwitch',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch_2.switch_2,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time (heartbeat) The maximum period
                    of time between consecutive transmissions of the current
                    value.  If this value is set to the invalid value, the
                    heartbeat interval will be two minutes when occupied and
                    20 minutes when unoccupied--this is the default
                    behavior.  Must be implemented as a configuration network
                    variable.""",
                    name='cpMaxSendTime',
                    profile=self,
                    number=8,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSwitchFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Switch feedback input.  Optional feedback input that may
            be used to synchronize the keypad state to other devices such as
            other keypads and lamps.""",
            name='nviSwitchFb',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch_2.switch_2,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoRunHours'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Running hours output.  Reports total running hours.""",
            name='nvoRunHours',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.elapsed_tm.elapsed_tm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpRunHrInit':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Running hours counter initialization.  The initial
                    value of the running hours counter network variable.""",
                    name='cpRunHrInit',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.runHrInit.runHrInit,
                    flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                        pylon.resources.base.PropertyFlags.CONST |
                        pylon.resources.base.PropertyFlags.DISABLE,
                    maximum=b'\x00\x00\xff\x00\x00\x00\x00',
                    default=b'\x00\x00\x00\x00\x00\x00\x00',
                    mandatory=False
                ),
                'cpRunHrAlarm':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Running hours alarm threshold level.  The alarm
                    threshold for the running hours counter.""",
                    name='cpRunHrAlarm',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.runHrAlarm.runHrAlarm,
                    flags=pylon.resources.base.PropertyFlags.DISABLE,
                    maximum=b'\x00\x00\xff\x00\x00\x00\x00',
                    default=b'\x00\x00\x00\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.properties['cpName1'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 1.  Part 1 of the name of the functional block
            to be used by optional user interface applications.  May
            optionally used with SCPTname2 and SCPTname3.  Must be
            implemented as a configuration network variable.""",
            name='cpName1',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.name1.name1,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpName2'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 2.  Part 2 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and may optionally be used with SCPTname3.  This
            part is concatenated after part 1, and may optionally be followed
            by part 3.  Must be implemented as a configuration network
            variable.""",
            name='cpName2',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.name2.name2,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpName3'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Name part 3.  Part 3 of the name of the functional block
            to be used by optional user interface applications.  Must be used
            with SCPTname1 and SCPTname2.  This part, if present, is
            concatenated with parts 1 and 2.  Must be implemented as a
            configuration network variable.""",
            name='cpName3',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.name3.name3,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='cpLocation',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpButtonAction'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Button pressed action.  Button action definition used to
            create a button pressed action array, with an entry per button.
            This SCPT defines the minimum entries required by the ISI
            profiles.""",
            name='cpButtonAction',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.buttonPressAction.buttonPressAction,
            array_size_max=254,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpButtonColor'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Button color.  Button color configuration for on and off
            states of a button.  May be used to create an array that is used
            with a SCPTbuttonAction array to specify keypad button
            behavior.""",
            name='cpButtonColor',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.buttonColor.buttonColor,
            default=b'\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpMinSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time (throttle) The minimum period of time
            between consecutive transmissions of the current value.""",
            name='cpMinSendTime',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['cpDefaultOutput'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Default output.  Output value at power-on reset or when
            overridden.""",
            name='cpDefaultOutput',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.defOutput.defOutput,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpInFbDelay'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Input value feedback delay.  The time period after the
            last update in a succession of changes to the input, before the
            feedback output is updated.""",
            name='cpInFbDelay',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.inFbDly.inFbDly,
            maximum=b'\x00\x00\x00\x00\x3b\x03\xe7',
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpFbMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Functional block major version number.  Major version
            number for the associated functional block.  See also
            cpFbMinVer.""",
            name='cpFbMajVer',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['cpFbMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Functional block minor version.  Minor version number for
            the associated functional block.  See also cpFbMajVer.""",
            name='cpFbMinVer',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self.properties['cpButtonRepeatInterval'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Button repeat interval.  Time between updates when a
            button is held down.  The updates themselves may be throttled by
            the application or a SCPTminSendTime CP.  Used to create an array
            used with a SCPTbuttonAction CP array.""",
            name='cpButtonRepeatInterval',
            profile=self,
            number=16,
            datatype=pylon.resources.properties.buttonRepeatInterval.buttonRepeatInterval,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['cpSceneName'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Scene name.  Name for a scene to be used by optional user
            interface applications.  Used to create an array that supplements
            a scene table created with a SCPTscene array.""",
            name='cpSceneName',
            profile=self,
            number=17,
            datatype=pylon.resources.properties.sceneName.sceneName,
            array_size_min=3,
            array_size_max=100,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['cpLightingGroupEn'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Lighting group enable.  Bit masks to enable or disable up
            to 64 ISI lighting groups.  Group 0 is not used.  Groups may also
            be enabled or disabled using a SNVT_switch_2 update.""",
            name='cpLightingGroupEn',
            profile=self,
            number=18,
            datatype=pylon.resources.properties.lightingGroupEnable.lightingGroupEnable,
            array_size_min=8,
            array_size_max=8,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._original_name = 'SFPTisiKeypad'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = isiKeypad()
    pass
