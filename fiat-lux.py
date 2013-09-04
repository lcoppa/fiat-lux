#!/usr/bin/env python3 -tt

""" Pilon application
    Controls RGB LEDs via network variables (color and brightness) and
    pressure (brightness)
"""

#
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#
# Use of this example software is subject to the terms of the
# Echelon Example Software License Agreement at
# www.echelon.com/license/examplesoftware/.
#

##############################################################################
# Imports
##############################################################################

# Import standard Python modules used here
import argparse
import logging
import math
import select
import sys
import select

# Import Pilon
import pylon.device

# Import Pilon resources used by this application
# SNVTs
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_switch_2 import SNVT_switch_2
from pylon.resources.SNVT_color_2 import SNVT_color_2
from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.SNVT_elec_kwh import SNVT_elec_kwh
from pylon.resources.SNVT_occupancy import SNVT_occupancy
from pylon.resources.SNVT_power import SNVT_power
# SFPTs
from pylon.resources.SFPTopenLoopSensor import SFPTopenLoopSensor
from pylon.resources.SFPTopenLoopActuator import SFPTopenLoopActuator
# SCPTs
from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg
from pylon.resources.SCPTmaxSndT import SCPTmaxSndT
from pylon.resources.SCPTdefOutput import SCPTdefOutput

# Import for I/O
from led_driver.led_set import LED
from fsr_read.pressure_sensor import PRESSURE_SENSOR

# some constants
PRESSURE_SENSOR_PIN = 18                # used by the PRESSURE object
PRESSURE_DIMMING_THRESHOLD = 2000       # pressure reading below which we cycle
                                        # LED brightness
PWM_BOARD_I2C_ADDRESS = 0x40            # used by the LED object
PWM_FREQ = 1000                         # in Hz, used by the LED object
RED_LED_PWM_CHANNEL = 0                 # used by the LED object
GREEN_LED_PWM_CHANNEL = 1               # used by the LED object
BLU_LED_PWM_CHANNEL = 2                 # used by the LED object

###############################################################################
# Main function
###############################################################################
def main():
    """The script's main function"""
    
    print('Welcome to the FiatLux Application.')
    print('Type CTRL-c to exit.')
    print('Initialising...')

    ############################
    # Get command line arguments
    ############################
    
    # define the command line arguments, with defaults and help
    parser = argparse.ArgumentParser(
        description="The Pilon LED demo script"
    )
    parser.add_argument(
        '-d', '--device',
        #required=True,
        default = '//' + this_pi_ip_addr() + '/uc'
        help='The device URI, e.g. //10.0.1.12/uc'
    )
    parser.add_argument(
        '-n', '--nvd',
        default='fiat-lux-nvd',
        help='Path to non-volatile data storage (folder)'
    )
    parser.add_argument(
        '-p', '--programId',
        default='9F:FF:FF:00:00:00:9A:01',
        help='The colon-separated program ID'
    )
    parser.add_argument(
        '-l', '--log',
        default='fiat-lux',
        help='The base location and name for log files'
    )
    parser.add_argument(
        '-D', '--debug',
        default=False,
        action='store_true',
        help='Enables full trace logging'
    )

    # parse the command line
    arguments = parser.parse_args()

    ##########
    # init I/O
    ##########
    
    # Create the pressure sensor object
    mySensor = PRESSURE_SENSOR()    

    # Create the object to control the LEDs. Assume the PWM board for the LEDs
    # is at address 0x40 if not changed in the constants above
    # Chek out the tutorial here
    # learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/
    myLed = LED(PWM_BOARD_I2C_ADDRESS, PWM_FREQ, True)

    ############
    # init Pilon
    ############

    #
    # Enable/disable test mode
    #
    
    # let's run plain this time
    pylon.device.stack.test_mode = False
    unit_test = False
    if pylon.device.stack.test_mode:
        print('\n*** Note this application is running in test mode ***\n')
    
    #
    # create and configure application object
    #
    
    # set app object properties
    app = pylon.device.application.Application(
        use_isi=True,
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR
    )
    # create the stack logger
    logger = logging.getLogger('pylon-rtk.showoff')
    
    # set other properties from command line arguments
    app.device_uri = arguments.device
    app.persistence_path = arguments.nvd
    app.programId = arguments.programId
    
    # set low-level stack trace logging if requested
    if arguments.debug:
        app.stack_tracefile = arguments.log + '-lts.log'
        # set special ISI logging as well in that case
        if app.isi:
            app.isi.tracefile(arguments.log + '-isi.log', False)
    
    
    ##############################
    # Creating my functional block
    ##############################
    # IP-C Lamp Actuator Functional Block based on a new functional profile 
    # based on the ISI Lamp Actuator with the following changes:
    # -- An IP-C Switch input and feedback output instead of a SNVT_switch_2    
    #    input and feedback output.
    #    The IP-C Switch type is similar to SNVT_switch_2 with the following 
    #    changes:
    #        -- A timestamp field specifying the date and time the value was 
    #           measured or the status was updated.
    #        -- A new IP-C state enumeration will be defined and used for the 
    #           state field.
    #           The type will be based on the switch_state_t enumeration, with 
    #           changes required for the other changes in this list.
    #        -- The value field will be defined as a 32-bit float instead of a 
    #           union.
    #        -- The group_number, button_number, delay, and multiplier fields 
    #           will be moved out of the value union into separate fields.
    #        -- be consolidated into the value field.
    #        -- A priority field specifying the relative priority of this value.
    #        -- A status field defined as an enumeration reporting the status of 
    #           the switch.
    # -- Power and Energy outputs based on the IP-C Sensor type.
    # -- Required color input and feedback output instead of optional.
    # -- Required multiplier output instead of optional.
    # -- Required runtime output instead of optonal.
    # -- A 60-character Name CP instead of three 12-character name CPs.
    # -- A 60-character Location CP instead of a 31-character location CP.
    # -- IP-C Network Timing CPs for the power and energy outputs instead of a           
    #    maximum send time and minimum send time CPs.
   

    #
    # inputs
    #
    nviValue = app.output_datapoint(
        data=SNVT_switch(), 
        name='nviValue'
    )
    nviValue_2 = app.input_datapoint(
        data = SNVT_switch_2()
        # no external name here
    )
    nviOccup = app.input_datapoint(
        data=SNVT_occupancy(), 
        name='nviOccup'
    )
    # optional inputs
    nviColor = app.input_datapoint(
        data=SNVT_color_2(), 
        name='nviColor'
    )

    #
    # outputs
    #
    nvoValueFb = app.output_datapoint(
        data=SNVT_switch(), 
        name='nvoValueFb'
    )
    nvoValueFb_2 = app.output_datapoint(
        data=SNVT_switch_2() 
        # no external name here
    )
    nvoPower = app.output_datapoint(
        data=SNVT_power(), 
        name='nvoPower'
    )
    nvoOccupancyFb = app.output_datapoint(
        data=SNVT_occupancy(), 
        name='nvoOccupancyFb'
    )
    # optional outputs
    nvoRunHours = app.output_datapoint(
        data=SNVT_elapsed_tm(), 
        name='nvoRunHours'
    )
    nvoEnergyHi = app.output_datapoint(
        data=SNVT_elec_kwh(), 
        name='nvoEnergyHi'
    )
    nvoMultiplierFb = app.output_datapoint(
        data=SNVT_switch(), 
        name='nvoMultiplierFb'
    )
    nvoColorFb = app.output_datapoint(
        data=SNVT_color_2(), 
        name='nvoColorFb'
    )
    nvoEnergyLo = app.output_datapoint(
        data=SNVT_elec_kwh(), 
        name='nvoEnergyLo'
    )

    ##################################
    # Input NVs updates event handlers
    ##################################

    def on_nvi_value_update(sender, arguments):
        logger.info('Processing network variable update {0}'.format(sender))
        try:
            # TODO
                # turn leds on/off
            # propagate feedback
            nvoValueFb.value <<= nviValue.value
            print("LED has now value {0}, state {1}".format(
                  nvoValueFb.value.value, nvoValueFb.value.state)
            )
        except Exception as e:
            print('Something just went wrong in on_nvi_value_update({0}):' \
                  '{1}'.format(sender, e))
    nviValue.OnUpdate += on_nvi_occup_update


    def on_nvi_occup_update(sender, arguments):
        logger.info('Processing network variable update {0}'.format(sender))
        try:
            # TODO
            print()
        except Exception as e:
            print('Something just went wrong in on_nvi_occup_update({0}):' \
                  '{1}'.format(sender, e)
            )
    nviOccup.OnUpdate += on_nvi_color_update

    def on_nvi_color_update(sender, arguments):
        logger.info('Processing network variable update {0}'.format(sender))
        try:
            # TODO
            print()
        except Exception as e:
            print('Something just went wrong in ' \
                  'on_nvi_color_update({0}): {1}'.format(sender, e)
            )
    nviColor.OnUpdate += on_nvi_color_update

    ###################################################
    # System event handlers definition and registration
    ###################################################
    # noinspection PyUnusedLocal
    def on_service_led(sender, arguments):
        logger.info('Processing service LED status event')
        print('Service LED status changed to {0}.'.format(arguments.state))
    app.OnServiceLed += on_service_led

    # noinspection PyUnusedLocal
    def on_wink(sender, arguments):
        logger.info('Recevied wink message')
        print('Wink.')
    app.OnWink += on_wink

    # noinspection PyUnusedLocal
    def on_online(sender, argument):
        logger.info('Received Online event')
        print('We are now on line.')
    app.OnOnline += on_online

    # noinspection PyUnusedLocal
    def on_offline(sender, argument):
        logger.info('Received Offline event')
        print('We are now off line.')
    app.OnOffline += on_offline














    ###############################################################################
    #   Start and main loop
    ###############################################################################
    app.start(1234)
    app.sendServicePin()

    print("Init done.")
    print("Press the sensor to regulate only LED dimming; control color and also " \
          "dimming via the network.")
    print("CTRL-c to exit")


    try:
        while True:
            app.service()

            # read pressure value
            pressure = mySensor.read_pressure(PRESSURE_SENSOR_PIN)
            # start by dimming down (if possible)
            dimming_down = True

            # until user is pressing on the sensor, cycle LED brightness
            # irrespective of the pressure level (for now)
            # TODO: make dimming proportional to pressure level
            while pressure < PRESSURE_DIMMING_THRESHOLD:
                # read current dimming level for RGB LED as percentages
                # r_dimming_level = ...
                # g_dimming_level = ...
                # b_dimming_level = ...

                ## reduce dimming evenly until one color is zero, then back up
                # if all colors can be dimmed
                if ((r_dimming_level > 0 and r_dimming_level < 100) and
                    (g_dimming_level > 0 and g_dimming_level < 100) and
                    (b_dimming_level > 0 and b_dimming_level < 100)):
                    # down
                    if dimming_down:
                        r_dimming_level -= 1
                        g_dimming_level -= 1
                        b_dimming_level -= 1
                    # or up
                    else:
                        r_dimming_level += 1
                        g_dimming_level += 1
                        b_dimming_level += 1
                    # do it
                    myLed.set_led_level(RED_LED_PWM_CHANNEL, r_dimming_level)
                    myLed.set_led_level(GREEN_LED_PWM_CHANNEL, g_dimming_level)
                    myLed.set_led_level(BLUE_LED_PWM_CHANNEL, b_dimming_level)
                # if dimming reached the limits, invert the dimming direction
                if (r_dimming_level = 0 or g_dimming_level = 0 or
                    b_dimming_level = 0):
                    dimming_down = False
                else if (r_dimming_level = 100 or g_dimming_level = 100 or
                         b_dimming_level = 100):
                    dimming_down = True

                # update the corresponding NV
                # ... = r_dimming_level
                # ... = g_dimming_level
                # ... = b_dimming_level



            #pdb.set_trace()
    except KeyboardInterrupt:
        # TODO: clean up I/O


    finally:
        app.stop()
        print("Goodbye")















    
    
#-------------------------------------------------------------------------
    
    
    

    #
    # Create the two blocks. Mandatory members are automatically implemented.
    #
    sensor = app.block(
            profile=SFPTopenLoopSensor(),
            ext_name='ols',
            snvt_xxx=SNVT_temp_p
    )
    actuator = app.block(
            profile=SFPTopenLoopActuator(),
            ext_name='ola',
            snvt_xxx=SNVT_temp_p
    )

    #
    #   Handle updates to the actuator's input:
    #
    # noinspection PyUnusedLocal
    def update_handler(sender, arguments):
        with sensor.nvoValue, actuator.nviValue:
            sensor.nvoValue.data = 0.5 * actuator.nviValue.data
            print('Update received and processed: {0} = 0.5 * {1}'.format(
                sensor.nvoValue.data,
                actuator.nviValue.data
            ))

    actuator.nviValue.OnUpdate += update_handler

    #
    #   Start pilon:
    #



    app.persistence_path = arguments.nvd

    if arguments.debug:
        app.stack_tracefile = arguments.log + '-lts.log'
        if app.isi:
            app.isi.tracefile(arguments.log + '-isi.log', False)

    app.start()

    #
    #   Run the application:
    #
    try:
        done = False

        while not done:

            #
            #   Service pilon
            #
            app.service()

            #
            #   Interactive user input
            #
            i, o, e = select.select([sys.stdin], [], [], 0.01)
            if i:
                try:

                    selection = sys.stdin.readline().strip().lower()
                    if selection == 'exit':
                        print('Winding down...')
                        done = True
                    elif selection == 'service':
                        app.send_service_message()
                    elif selection == 'wink':
                        # Simulate receipt of a Wink message for testing:
                        app.OnWink.fire(app, None)
                    else:
                        print(
                            'Valid commands are "exit", "service", "wink"'
                        )
                except Exception as e:
                    print(e)
    finally:

        #
        #   Stop pilon
        #
        app.stop()
        print("Good bye.")


if __name__ == '__main__':
    main()









def this_pi_ip_addr():
    """ Returns the IP address of this machine.
        Require AVAHID installed (apt-get install avahid) which should
        be installed by default in Raspbian
    """
    
    # get text hostname of the local machine
    host = socket.gethostname()
    
    # get the numeric IP address from the hostname; this might require avahid
    ip_address = socket.gethostbyname(host + '.local')
    print('Host ' + host + ' has IP address '+ ip_address)

    return ip_address







