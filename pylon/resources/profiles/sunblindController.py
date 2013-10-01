"""sunblindController standard profile, originally defined in resource file
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
import pylon.resources.datapoints.setting
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.sblnd_state
import pylon.resources.datapoints.speed
import pylon.resources.properties.maxRcvTime
import pylon.resources.datapoints.lux
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.temp_p
import pylon.resources.datapoints.lev_percent
import pylon.resources.datapoints.scene
import pylon.resources.properties.defaultSetting
import pylon.resources.datapoints.occupancy
import pylon.resources.datapoints.angle_deg
import pylon.resources.properties.nvPriority
import pylon.resources.properties.bypassTime
import pylon.resources.properties.location
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer


class sunblindController(pylon.resources.base.Profile):
    """sunblindController standard profile.  Sunblind Controller.  Controls
    one or more Sunblind Actuators to open/close sunblinds or similar
    devices."""

    def __init__(self):
        super().__init__(
            key=6111,
            scope=0
        )
        self.datapoints['nvoSblndSetting'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Controller setpoint output.  This output network variable
            provides the Sunblind Controller setpoint value which may depend
            on any network input and configuration properties.""",
            name='nvoSblndSetting',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV01':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV01',
                    profile=self,
                    number=1,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoSblndState'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Sunblind controller state output.  This output network
            variable is used to report the actual setpoint, error messages
            and the cause of the latest change of this setpoint.""",
            name='nvoSblndState',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.sblnd_state.sblnd_state,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.UNREPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTimeNV02':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTimeNV02',
                    profile=self,
                    number=3,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviLocalControl'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Local setpoint adjustment.  This network variable input is
            provided to set the controller setpoint output.  Usually this
            command is given by a local control device.""",
            name='nviLocalControl',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviGroupControl'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Input for setpoint adjustment in groups.  This network
            variable input is provided to set the controller setpoint
            output.  Usually this command is given by a device which is
            intended to control groups of controllers or actuators.""",
            name='nviGroupControl',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviWindspeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Wind speed sensor input.  This input network variable is
            used to get wind speed influence on the controller.""",
            name='nviWindspeed',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.speed.speed,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV05':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV05',
                    profile=self,
                    number=4,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviSunLux'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor brightness input standard range.  This input
            network variable is used to get sun (outdoor) brightness
            influence with a range from 0...65klux on the controller.""",
            name='nviSunLux',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.lux.lux,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRain'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Rain sensor input.  This input network variable is used to
            get rain sensor influence on the controller.""",
            name='nviRain',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV07':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV07',
                    profile=self,
                    number=5,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    maximum=b'\x00\x00',
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviFrost'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Frost sensor input.  This input network variable is used
            to get frost sensor influence on the controller.""",
            name='nviFrost',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV08':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV08',
                    profile=self,
                    number=6,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    maximum=b'\x00\x00',
                    default=b'\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviDawn'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Dawn state input.  The term "Dawn" means the time before
            sunrise when it is more bright than during the night but not as
            bright as the average of daytime.""",
            name='nviDawn',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDusk'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Dusk state input.  The term "Dusk" means the time before
            sunset when it is no longer as bright as the average of daytime
            but brighter than during the night.""",
            name='nviDusk',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor air temperature input.  This input network
            variable is used to get outdoor temperature sensor influence on
            the controller.""",
            name='nviOutdoorTemp',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviIndoorTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Indoor temperature input.  This input network variable is
            used to get indoor temperature sensor influence on the
            controller.""",
            name='nviIndoorTemp',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOutdoorRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Outdoor relative humidity input.  This input network
            variable is used to get outdoor relative humidity sensor
            influence on the controller.""",
            name='nviOutdoorRH',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviIndoorRH'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Indoor relative humidity input.  This input network
            variable is used to get indoor relative humidity sensor influence
            on the controller.""",
            name='nviIndoorRH',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviIllumLev'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Indoor illumination level input.  This input network
            variable is used to get indoor light sensor influence on the
            controller.""",
            name='nviIllumLev',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.lux.lux,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviScene'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Scene trigger input.  Every scene relates to a particular
            setpoint value, which could be sent via nvoSblndSetting.""",
            name='nviScene',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.scene.scene,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviGlobalControl'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Global setpoint adjustment.  This network variable input
            is provided to set the controller setpoint output.""",
            name='nviGlobalControl',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviWindowContact'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Window contact input.  This input network variable is used
            to get window contact influence on the controller.""",
            name='nviWindowContact',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciMaxReceiveTimeNV18':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum receive time.  The maximum period of time
                    that may expire with no updates on the associated input
                    network variables before the object goes into heartbeat
                    failure mode.  A zero value disables.""",
                    name='nciMaxReceiveTimeNV18',
                    profile=self,
                    number=7,
                    datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
                    default=b'\x00\x00',
                    mandatory=False
                ),
                'nciWinConFailPos':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Window-Contact -Sensor Failure-Position Default.
                    Defines the default position of the sunblind in the event
                    that the sensor input fails.""",
                    name='nciWinConFailPos',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.defaultSetting.defaultSetting,
                    default=b'\x00\x00\x00\x00',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviAutoMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Mode enabling/disabling input.  This input network
            variable is used to get mode switch functionality on the
            controller.""",
            name='nviAutoMode',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Override state input.  This input network variable is used
            to get override influence on the controller.""",
            name='nviOverride',
            profile=self,
            number=20,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMaintenance'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setpoint input for maintenance reasons.  This input
            network variable is used to get maintenance signal influence on
            the controller.""",
            name='nviMaintenance',
            profile=self,
            number=21,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviTerminalLoad'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Heating/cooling demand input.  This input is used to
            receive the current heating/cooling demand of the system which
            the sunblind controller shares in.""",
            name='nviTerminalLoad',
            profile=self,
            number=22,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccSensor'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy sensor value input.  This input network variable
            is used to get occupancy sensor influence on the controller.""",
            name='nviOccSensor',
            profile=self,
            number=23,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOccManCmd'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Occupancy override input.  This input network variable is
            used to get business hour info influence on the controller.""",
            name='nviOccManCmd',
            profile=self,
            number=24,
            datatype=pylon.resources.datapoints.occupancy.occupancy,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviGlare'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Glare detecting sensor value input.  This input network
            variable is used to get glare detecting sensor influence on the
            controller.""",
            name='nviGlare',
            profile=self,
            number=25,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSunElevation'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Astronomical sensor value input for sun declination.  This
            network input represents information from a sun-position
            calculating device.""",
            name='nviSunElevation',
            profile=self,
            number=26,
            datatype=pylon.resources.datapoints.angle_deg.angle_deg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSunAzimuth'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Astronomical sensor value input for sun inclination.  This
            network input represents information from a sun-position
            calculating device.""",
            name='nviSunAzimuth',
            profile=self,
            number=27,
            datatype=pylon.resources.datapoints.angle_deg.angle_deg,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setpoint override input.  This input network variable is
            used to get override influence on the controller.""",
            name='nviSetOverride',
            profile=self,
            number=28,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviSetMaint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Setpoint input for maintenance reasons.  This input
            network variable is used to get maintenance influence on the
            controller.""",
            name='nviSetMaint',
            profile=self,
            number=29,
            datatype=pylon.resources.datapoints.setting.setting,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['nciNvPriority'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Environmental-Input Priority.  Defines the priority of
            inputs that control the positioning of the sunblinds.""",
            name='nciNvPriority',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.nvPriority.nvPriority,
            array_size_min=2,
            array_size_max=255,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciBypassTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Bypass time.  The maximum amount of time that the
            controller can be in the bypass (occupancy) mode following the
            last bypass request.  Zero disables the timer.""",
            name='nciBypassTime',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.bypassTime.bypassTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciWeaSenFailPos'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Weather-Sensor Failure-Position Default.  Defines the
            default position of the sunblind in the event that the sensor
            input fails.""",
            name='nciWeaSenFailPos',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.defaultSetting.defaultSetting,
            default=b'\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=13,
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
            number=14,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            default=b'\x00',
            mandatory=False
        )
        self._original_name = 'SFPTsunblindController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = sunblindController()
    pass
