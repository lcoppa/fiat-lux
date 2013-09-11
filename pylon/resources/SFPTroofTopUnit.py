"""SFPTroofTopUnit standard profile, originally defined in resource file set
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
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_hvac_status import SNVT_hvac_status
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SNVT_ppm import SNVT_ppm
from pylon.resources.SNVT_hvac_emerg import SNVT_hvac_emerg
from pylon.resources.SCPTsetPnts import SCPTsetPnts
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTlimitCO2 import SCPTlimitCO2


class SFPTroofTopUnit(base.Profile):
    """SFPTroofTopUnit standard profile.  Roof-Top Unit Controller.  Used to
    control an HVAC rooftop space-conditioning unit."""

    def __init__(self):
        super().__init__(
            key=8030,
            scope=0
        )
        self.datapoints['nviSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Input.  This input network variable is
            used to connect an external space temperature sensor to the
            node.""",
            name='nviSpaceTemp',
            profile=self,
            number=1,
            datatype=SNVT_temp_p,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV01':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV01',
                    profile=self,
                    number=10,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSetPoint'] = base.Profile.DatapointMember(
            doc="""Temperature Setpoint Input.  This input network variable
            is used to allow the temperature setpoint for the occupied and
            standby mode to be changed via the network.""",
            name='nviSetPoint',
            profile=self,
            number=2,
            datatype=SNVT_temp_p,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoSpaceTemp'] = base.Profile.DatapointMember(
            doc="""Space Temperature Output.  This output network variable is
            used to send the value of the controlled space temperature
            (either from a locally connected space temperature sensor or from
            the nviSpaceTemp input) to other nodes.""",
            name='nvoSpaceTemp',
            profile=self,
            number=3,
            datatype=SNVT_temp_p,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNVO3':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNVO3',
                    profile=self,
                    number=19,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoUnitStatus'] = base.Profile.DatapointMember(
            doc="""Unit Status Output.  This output network variable is
            available to report the object status.""",
            name='nvoUnitStatus',
            profile=self,
            number=4,
            datatype=SNVT_hvac_status,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNVO4':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNVO4',
                    profile=self,
                    number=20,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviApplicMode'] = base.Profile.DatapointMember(
            doc="""Application Mode Input.  This network variable input is
            used to coordinate the RTU Device with any supervisory controller
            or intelligent human interface device.""",
            name='nviApplicMode',
            profile=self,
            number=5,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV05':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV05',
                    profile=self,
                    number=14,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOccCmd'] = base.Profile.DatapointMember(
            doc="""Occupancy Input.  This input network variable is used to
            command the RTU object into different occupancy modes.  It is
            typically set by a supervisory node.""",
            name='nviOccCmd',
            profile=self,
            number=6,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetPtOffset'] = base.Profile.DatapointMember(
            doc="""Setpoint Offset Input.  This input network variable is
            used to shift the temperature setpoint via the network by adding
            nviSetPtOffset to the current setpoint.""",
            name='nviSetPtOffset',
            profile=self,
            number=7,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV07':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV07',
                    profile=self,
                    number=11,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutsideTemp'] = base.Profile.DatapointMember(
            doc="""Outside Temperature Input.  This input network variable is
            the current outside air temperature.""",
            name='nviOutsideTemp',
            profile=self,
            number=8,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV08':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV08',
                    profile=self,
                    number=12,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviOutsideRH'] = base.Profile.DatapointMember(
            doc="""Outside Humidity Input.  This input network variable is
            the current outside air relative humidity.""",
            name='nviOutsideRH',
            profile=self,
            number=9,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV09':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV09',
                    profile=self,
                    number=13,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoEffectSetPt'] = base.Profile.DatapointMember(
            doc="""Effective Setpoint Output.  The output network variable is
            used to inform the effective setpoint temperature when the
            setpoint is changed by nciSetPnts, nviSetPoint, nviSetPointOffset
            or local means.""",
            name='nvoEffectSetPt',
            profile=self,
            number=10,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV10':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV10',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOutsideTemp'] = base.Profile.DatapointMember(
            doc="""Outside Temperature Output.  This output network variable
            is the current outside air temperature.""",
            name='nvoOutsideTemp',
            profile=self,
            number=11,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV11':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV11',
                    profile=self,
                    number=7,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoOutsideRH'] = base.Profile.DatapointMember(
            doc="""Outside Humidity Output.  This output network variable is
            the current outside air relative humidity.""",
            name='nvoOutsideRH',
            profile=self,
            number=12,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV12':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV12',
                    profile=self,
                    number=4,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoCO2'] = base.Profile.DatapointMember(
            doc="""CO2 Sensor Output.  This output network variable is the
            CO2 measurement.""",
            name='nvoCO2',
            profile=self,
            number=16,
            datatype=SNVT_ppm,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciSndHrtBtNV16':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciSndHrtBtNV16',
                    profile=self,
                    number=5,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSpaceRH'] = base.Profile.DatapointMember(
            doc="""Space Humidity Input.  This input network variable
            measures the space relative humidity.""",
            name='nviSpaceRH',
            profile=self,
            number=13,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV13':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV13',
                    profile=self,
                    number=15,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviCO2'] = base.Profile.DatapointMember(
            doc="""CO2 Sensor Input.  This input network variable measures
            the CO2 levels in PPM.""",
            name='nviCO2',
            profile=self,
            number=14,
            datatype=SNVT_ppm,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRcvHrtBtNV14':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciRcvHrtBtNV14',
                    profile=self,
                    number=9,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviEmergCmd'] = base.Profile.DatapointMember(
            doc="""Emergency Command Input.  This input network variable is
            used to command the RTU object into different emergency
            modes.""",
            name='nviEmergCmd',
            profile=self,
            number=15,
            datatype=SNVT_hvac_emerg,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.properties['nciSetPnts'] = base.Profile.PropertyMember(
            doc="""Occupancy temperature setpoints.  The occupancy
            temperature setpoints for heat and cool mode.""",
            name='nciSetPnts',
            profile=self,
            number=8,
            datatype=SCPTsetPnts,
            minimum=b'\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18\xfc\x18',
            maximum=b'\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac\x0d\xac',
            default=b'\x08\xfc\x09\xc4\x0a\xf0\x08\x34\x07\x6c\x06\x40',
            mandatory=True
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=16,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciCO2Limit'] = base.Profile.PropertyMember(
            doc="""CO2 limit.  CO2 threshold limit, controller to maintain
            concentration below this limit.""",
            name='nciCO2Limit',
            profile=self,
            number=17,
            datatype=SCPTlimitCO2,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciSndHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciSndHrtBt',
            profile=self,
            number=18,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciRcvHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRcvHrtBt',
            profile=self,
            number=21,
            datatype=SCPTmaxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTroofTopUnit()
    pass
