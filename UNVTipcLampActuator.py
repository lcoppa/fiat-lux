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

from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_switch_2 import SNVT_switch_2
from pylon.resources.SNVT_color_2 import SNVT_color_2
from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.SNVT_elec_kwh import SNVT_elec_kwh
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_power import SNVT_power


class UNVTipcLampActuator(base.Profile):
    """UNVTipcLampActuator custom profile.

    Lamp Actuator.
    Represents the physical LED in the Pilon examples 
    """

    def __init__(self):
        super().__init__(
            key=1234,
            scope=0,
            principal='nvoValue'
        )
        self._definition = standard.add(self)
        
        ####################
        # Profile datapoints
        ####################
        
        # IP-C Lamp Actuator Functional Block based on a new functional profile 
        # based on the ISI Lamp Actuator with the following changes:
        # -- An IP-C Switch input and feedback output instead of a SNVT_switch_2    
        #    input and feedback output.
        #    The IP-C Switch type is similar to SNVT_switch_2 with the following 
        #    changes:
        #   -- A timestamp field specifying the date and time the value was 
        #      measured or the status was updated.
        #   -- A new IP-C state enumeration will be defined and used for the 
        #      state field.
        #      The type will be based on the switch_state_t enumeration, with 
        #      changes required for the other changes in this list.
        #   -- The value field will be defined as a 32-bit float instead of a 
        #      union.
        #   -- The group_number, button_number, delay, and multiplier fields 
        #      will be moved out of the value union into separate fields.
        #   -- be consolidated into the value field.
        #   -- A priority field specifying the relative priority of this value.
        #   -- A status field defined as an enumeration reporting the status of 
        #      the switch.        
        self.datapoints['nviValue_2'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nviValue_2',
            profile=self,
            number=1,
            datatype=SNVT_switch_2,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoValueFb_2'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nvoValueFb_2',
            profile=self,
            number=2,
            datatype=SNVT_switch_2,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        
        # -- Power and Energy outputs based on the IP-C Sensor type.
        self.datapoints['nvoPower'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nvoPower',
            profile=self,
            number=3,
            datatype=SNVT_power,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyHi'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nvoEnergyHi',
            profile=self,
            number=4,
            datatype=SNVT_elec_kwh,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyLo'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nvoEnergyLo',
            profile=self,
            number=5,
            datatype=SNVT_elec_kwh,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        
        # -- Required color input and feedback output instead of optional.
        self.datapoints['nviColor'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nviColor',
            profile=self,
            number=6,
            datatype=SNVT_color_2,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoColorFb'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nvoColorFb',
            profile=self,
            number=7,
            datatype=SNVT_color_2,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )

        # -- Required multiplier output instead of optional.
        self.datapoints['nvoMultiplierFb'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nvoMultiplierFb',
            profile=self,
            number=8,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )

        # -- Required runtime output instead of optonal.
        self.datapoints['nvoRunHours'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nvoRunHours',
            profile=self,
            number=9,
            datatype=SNVT_elapsed_tm,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )

        # extra nvs?
        self.datapoints['nviOccup'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nviOccup',
            profile=self,
            number=10,
            datatype=SNVT_occupancy,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOccupancyFb'] = base.Profile.DatapointMember(
            doc="""
            Description here
            """,
            name='nvoOccupancyFb',
            profile=self,
            number=11,
            datatype=SNVT_occupancy,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )

        ####################
        # Profile properties
        ####################

        # -- A 60-character Name CP instead of three 12-character name CPs.
        self.properties['nciName'] = base.Profile.PropertyMember(
            doc="""
            Description here
            """,
            name='nciName',
            profile=self,
            number=1,
            datatype=UNVTstring, # TODO
            mandatory=True,
            flags=base.PropertyFlags.RESET
        )
        
        # -- A 60-character Location CP instead of a 31-character location CP.
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""
            Description here
            """,
            name='nciLocation',
            profile=self,
            number=2,
            datatype=UNVTstring,        # TODO
            mandatory=True,
            flags=base.PropertyFlags.RESET
        )
        
        
        # -- IP-C Network Timing CPs for the power and energy outputs instead 
        #    of a maximum send time and minimum send time CPs.
        self.properties['nciNetTiming'] = base.Profile.PropertyMember(
            doc="""
            Description here
            """,
            name='nciNetTiming',
            profile=self,
            number=3,
            datatype=UNVTNetTiming,     # TODO
            mandatory=False,
            flags=base.PropertyFlags.RESET
        )
        
        self.finalize()
# end class UNVTipcLampActuator

