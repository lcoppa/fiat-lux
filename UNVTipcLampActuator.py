"""
    SFPTopenLoopSensor
"""

#
# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from pylon.resources import base
from pylon.resources.standard import standard

from pylon.resources.SNVT_xxx import SNVT_xxx
from pylon.resources.SNVT_count import SNVT_count
from pylon.resources.SNVT_preset import SNVT_preset


class SFPTopenLoopSensor(base.Profile):
    """SFPTopenLoopSensor standard profile.

    Open-Loop Sensor (OLS).
    A basic object without feedback, used with any form of sensor.
    """

    def __init__(self):
        super().__init__(
            key=1,
            scope=0,
            principal='nvoValue'
        )
        self._definition = standard.add(self)
        self.datapoints['nvoValue'] = base.Profile.DatapointMember(
            doc="""
            Value output: Transmits the value from the sensor after conversion
            to correct units.
            """,
            name='nvoValue',
            profile=self,
            number=1,
            datatype=SNVT_xxx,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviPresetFb'] = base.Profile.DatapointMember(
            doc="""
            Preset input feedback: Receives preset function feedback
            information used to synchronize multiple source objects.
            """,
            name='nviPresetFb',
            profile=self,
            number=2,
            datatype=SNVT_preset,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoRawHwData'] = base.Profile.DatapointMember(
            doc="""
            Raw hardware data output: Transmits the value obtained from
            the sensor prior to any transformation.
            """,
            name='nvoRawHwData',
            profile=self,
            number=3,
            datatype=SNVT_count,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPreset'] = base.Profile.DatapointMember(
            doc="""
            Preset output: Used to program or control the preset of a
            destination object.
            """,
            name='nvoPreset',
            profile=self,
            number=4,
            datatype=SNVT_preset,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.finalize()


class SFPTopenLoopActuator(base.Profile):
    """SFPTopenLoopActuator standard profile.

    Open-Loop Actuator (OLA).
    A basic object without feedback, used with any form of actuator.
    """

    def __init__(self):
        super().__init__(
            key=3,
            scope=0,
            principal='nviValue'
        )
        self._definition = standard.add(self)
        self.datapoints['nviValue'] = base.Profile.DatapointMember(
            doc="""
            Value input: Dictates the desired state of the actuator, determined
            by the specific application.
            """,
            name='nviValue',
            profile=self,
            number=1,
            datatype=SNVT_xxx,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPreset'] = base.Profile.DatapointMember(
            doc="""
            Preset input:   Used to program or control the preset function.
            """,
            name='nviPreset',
            profile=self,
            number=2,
            datatype=SNVT_preset,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoPresetFb'] = base.Profile.DatapointMember(
            doc="""
            Preset feedback output: Transmits the setting associated with the
            current recalled or programmed preset.
            """,
            name='nvoPresetFb',
            profile=self,
            number=4,
            datatype=SNVT_preset,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.finalize()

# ### TODO REMINDER add properties and remaining optional datapoints
