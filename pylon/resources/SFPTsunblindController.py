"""SFPTsunblindController standard profile, originally defined in resource
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
from pylon.resources.SNVT_setting import SNVT_setting
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SNVT_sblnd_state import SNVT_sblnd_state
from pylon.resources.SNVT_speed import SNVT_speed
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SNVT_lux import SNVT_lux
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SNVT_scene import SNVT_scene
from pylon.resources.SCPTdefaultSetting import SCPTdefaultSetting
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_angle_deg import SNVT_angle_deg
from pylon.resources.SCPTnvPriority import SCPTnvPriority
from pylon.resources.SCPTbypassTime import SCPTbypassTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer


class SFPTsunblindController(base.Profile):
    """SFPTsunblindController standard profile.  Sunblind Controller.
    Controls one or more Sunblind Actuators to open/close sunblinds or
    similar devices."""

    def __init__(self):
        super().__init__(
            key=6111,
            scope=0
        )
        self.datapoints['nvoSblndSetting'] = base.Profile.DatapointMember(
            doc="""Controller setpoint output.  This output network variable
            provides the Sunblind Controller setpoint value which may depend
            on any network input and configuration properties.""",
            name='nvoSblndSetting',
            profile=self,
            number=1,
            datatype=SNVT_setting,
            mandatory=True,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV01':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV01',
                    profile=self,
                    number=1,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoSblndState'] = base.Profile.DatapointMember(
            doc="""Sunblind controller state output.  This output network
            variable is used to report the actual setpoint, error messages
            and the cause of the latest change of this setpoint.""",
            name='nvoSblndState',
            profile=self,
            number=2,
            datatype=SNVT_sblnd_state,
            mandatory=False,
            service=base.Profile.DatapointMember.UNREPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV02':
                base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV02',
                    profile=self,
                    number=3,
                    datatype=SCPTmaxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviLocalControl'] = base.Profile.DatapointMember(
            doc="""Local setpoint adjustment.  This network variable input is
            provided to set the controller setpoint output.  Usually this
            command is given by a local control device.""",
            name='nviLocalControl',
            profile=self,
            number=3,
            datatype=SNVT_setting,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviGroupControl'] = base.Profile.DatapointMember(
            doc="""Input for setpoint adjustment in groups.  This network
            variable input is provided to set the controller setpoint
            output.  Usually this command is given by a device which is
            intended to control groups of controllers or actuators.""",
            name='nviGroupControl',
            profile=self,
            number=4,
            datatype=SNVT_setting,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviWindspeed'] = base.Profile.DatapointMember(
            doc="""Wind speed sensor input.  This input network variable is
            used to get wind speed influence on the controller.""",
            name='nviWindspeed',
            profile=self,
            number=5,
            datatype=SNVT_speed,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV05':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV05',
                    profile=self,
                    number=4,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSunLux'] = base.Profile.DatapointMember(
            doc="""Outdoor brightness input standard range.  This input
            network variable is used to get sun (outdoor) brightness
            influence with a range from 0...65klux on the controller.""",
            name='nviSunLux',
            profile=self,
            number=6,
            datatype=SNVT_lux,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRain'] = base.Profile.DatapointMember(
            doc="""Rain sensor input.  This input network variable is used to
            get rain sensor influence on the controller.""",
            name='nviRain',
            profile=self,
            number=7,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV07':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV07',
                    profile=self,
                    number=5,
                    datatype=SCPTmaxRcvTime,
                    maximum=b'\x00\x00',
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviFrost'] = base.Profile.DatapointMember(
            doc="""Frost sensor input.  This input network variable is used
            to get frost sensor influence on the controller.""",
            name='nviFrost',
            profile=self,
            number=8,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV08':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV08',
                    profile=self,
                    number=6,
                    datatype=SCPTmaxRcvTime,
                    maximum=b'\x00\x00',
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviDawn'] = base.Profile.DatapointMember(
            doc="""Dawn state input.  The term "Dawn" means the time before
            sunrise when it is more bright than during the night but not as
            bright as the average of daytime.""",
            name='nviDawn',
            profile=self,
            number=9,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDusk'] = base.Profile.DatapointMember(
            doc="""Dusk state input.  The term "Dusk" means the time before
            sunset when it is no longer as bright as the average of daytime
            but brighter than during the night.""",
            name='nviDusk',
            profile=self,
            number=10,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorTemp'] = base.Profile.DatapointMember(
            doc="""Outdoor air temperature input.  This input network
            variable is used to get outdoor temperature sensor influence on
            the controller.""",
            name='nviOutdoorTemp',
            profile=self,
            number=11,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviIndoorTemp'] = base.Profile.DatapointMember(
            doc="""Indoor temperature input.  This input network variable is
            used to get indoor temperature sensor influence on the
            controller.""",
            name='nviIndoorTemp',
            profile=self,
            number=12,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorRH'] = base.Profile.DatapointMember(
            doc="""Outdoor relative humidity input.  This input network
            variable is used to get outdoor relative humidity sensor
            influence on the controller.""",
            name='nviOutdoorRH',
            profile=self,
            number=13,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviIndoorRH'] = base.Profile.DatapointMember(
            doc="""Indoor relative humidity input.  This input network
            variable is used to get indoor relative humidity sensor influence
            on the controller.""",
            name='nviIndoorRH',
            profile=self,
            number=14,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviIllumLev'] = base.Profile.DatapointMember(
            doc="""Indoor illumination level input.  This input network
            variable is used to get indoor light sensor influence on the
            controller.""",
            name='nviIllumLev',
            profile=self,
            number=15,
            datatype=SNVT_lux,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviScene'] = base.Profile.DatapointMember(
            doc="""Scene trigger input.  Every scene relates to a particular
            setpoint value, which could be sent via nvoSblndSetting.""",
            name='nviScene',
            profile=self,
            number=16,
            datatype=SNVT_scene,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviGlobalControl'] = base.Profile.DatapointMember(
            doc="""Global setpoint adjustment.  This network variable input
            is provided to set the controller setpoint output.""",
            name='nviGlobalControl',
            profile=self,
            number=17,
            datatype=SNVT_setting,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviWindowContact'] = base.Profile.DatapointMember(
            doc="""Window contact input.  This input network variable is used
            to get window contact influence on the controller.""",
            name='nviWindowContact',
            profile=self,
            number=18,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV18':
                base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV18',
                    profile=self,
                    number=7,
                    datatype=SCPTmaxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciWinConFailPos':
                base.Profile.PropertyMember(
                    doc="""Window-Contact -Sensor Failure-Position Default.
                    Defines the default position of the sunblind in the event
                    that the sensor input fails.""",
                    name='nciWinConFailPos',
                    profile=self,
                    number=11,
                    datatype=SCPTdefaultSetting,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviAutoMode'] = base.Profile.DatapointMember(
            doc="""Mode enabling/disabling input.  This input network
            variable is used to get mode switch functionality on the
            controller.""",
            name='nviAutoMode',
            profile=self,
            number=19,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOverride'] = base.Profile.DatapointMember(
            doc="""Override state input.  This input network variable is used
            to get override influence on the controller.""",
            name='nviOverride',
            profile=self,
            number=20,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMaintenance'] = base.Profile.DatapointMember(
            doc="""Setpoint input for maintenance reasons.  This input
            network variable is used to get maintenance signal influence on
            the controller.""",
            name='nviMaintenance',
            profile=self,
            number=21,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviTerminalLoad'] = base.Profile.DatapointMember(
            doc="""Heating/cooling demand input.  This input is used to
            receive the current heating/cooling demand of the system which
            the sunblind controller shares in.""",
            name='nviTerminalLoad',
            profile=self,
            number=22,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccSensor'] = base.Profile.DatapointMember(
            doc="""Occupancy sensor value input.  This input network variable
            is used to get occupancy sensor influence on the controller.""",
            name='nviOccSensor',
            profile=self,
            number=23,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccManCmd'] = base.Profile.DatapointMember(
            doc="""Occupancy override input.  This input network variable is
            used to get business hour info influence on the controller.""",
            name='nviOccManCmd',
            profile=self,
            number=24,
            datatype=SNVT_occupancy,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviGlare'] = base.Profile.DatapointMember(
            doc="""Glare detecting sensor value input.  This input network
            variable is used to get glare detecting sensor influence on the
            controller.""",
            name='nviGlare',
            profile=self,
            number=25,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSunElevation'] = base.Profile.DatapointMember(
            doc="""Astronomical sensor value input for sun declination.  This
            network input represents information from a sun-position
            calculating device.""",
            name='nviSunElevation',
            profile=self,
            number=26,
            datatype=SNVT_angle_deg,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSunAzimuth'] = base.Profile.DatapointMember(
            doc="""Astronomical sensor value input for sun inclination.  This
            network input represents information from a sun-position
            calculating device.""",
            name='nviSunAzimuth',
            profile=self,
            number=27,
            datatype=SNVT_angle_deg,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetOverride'] = base.Profile.DatapointMember(
            doc="""Setpoint override input.  This input network variable is
            used to get override influence on the controller.""",
            name='nviSetOverride',
            profile=self,
            number=28,
            datatype=SNVT_setting,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetMaint'] = base.Profile.DatapointMember(
            doc="""Setpoint input for maintenance reasons.  This input
            network variable is used to get maintenance influence on the
            controller.""",
            name='nviSetMaint',
            profile=self,
            number=29,
            datatype=SNVT_setting,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.properties['nciNvPriority'] = base.Profile.PropertyMember(
            doc="""Environmental-Input Priority.  Defines the priority of
            inputs that control the positioning of the sunblinds.""",
            name='nciNvPriority',
            profile=self,
            number=8,
            datatype=SCPTnvPriority,
            array_size_min=2,
            array_size_max=255,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciBypassTime'] = base.Profile.PropertyMember(
            doc="""Bypass time.  The maximum amount of time that the
            controller can be in the bypass (occupancy) mode following the
            last bypass request.  Zero disables the timer.""",
            name='nciBypassTime',
            profile=self,
            number=9,
            datatype=SCPTbypassTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciWeaSenFailPos'] = base.Profile.PropertyMember(
            doc="""Weather-Sensor Failure-Position Default.  Defines the
            default position of the sunblind in the event that the sensor
            input fails.""",
            name='nciWeaSenFailPos',
            profile=self,
            number=10,
            datatype=SCPTdefaultSetting,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=12,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=13,
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
            number=14,
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
    item = SFPTsunblindController()
    pass
