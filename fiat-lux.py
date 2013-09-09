#!/usr/bin/env python3

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
import time
import socket

# Import Pilon
import pylon.device

# Import Pilon resources used by this application
# SNVTs
from pylon.resources.SNVT_switch import SNVT_switch
# SFPTs
from pylon.resources.SFPTopenLoopSensor import SFPTopenLoopSensor
from pylon.resources.SFPTopenLoopActuator import SFPTopenLoopActuator
#from pylon.resources.SFPTisiLampActuator import SFPTisiLampActuator
# SCPTs
#from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg
#from pylon.resources.SCPTmaxSndT import SCPTmaxSndT
#from pylon.resources.SCPTdefOutput import SCPTdefOutput

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

    print('Welcome to the Pilon FiatLux Application.')
    print('\n'
          'Initialising...')

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
        default = '//' + this_pi_ip_addr() + '/uc',
        help = 'The device URI, e.g. //10.0.1.12/uc'
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

    # Set to True if using thePi standalone with no LED or sensor
    with_hw_periferals = False

    # create the hw I/O
    if with_hw_periferals:

        # Create the pressure sensor object
        try:
            pressure_sensor = PRESSURE_SENSOR()
        except Exception as e:
            print("Cannot find the pressure sensor.")
            print(e)

        # Create the object to control the LEDs. Assume the PWM board for the LEDs
        # is at address 0x40 if not changed in the constants above
        # Chek out the tutorial here
        # learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/
        try:
            this_led = LED(PWM_BOARD_I2C_ADDRESS, PWM_FREQ, True)
            pass
        except Exception as e:
            print("Cannot find the LED light.")
            print(e)

    ################
    # init Pilon app
    ################

    #
    # Enable/disable test mode
    #

    # let's run plain this time
    pylon.device.stack.test_mode = False
    if pylon.device.stack.test_mode:
        print('\n*** This application is running in test mode ***\n')

    #
    # create and configure application object
    #

    # set app object properties
    app = pylon.device.application.Application(
        use_isi=False,
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR
    )
    # create the stack logger
    logger = logging.getLogger('pylon-rtk.fiat-lux')

    # set low-level stack trace logging if requested
    if arguments.debug:
        app.stack_tracefile = arguments.log + '-lts.log'
        # set special ISI logging as well in that case
        if app.isi:
            app.isi.tracefile(arguments.log + '-isi.log', False)


    # set other properties from command line arguments
    app.device_uri = arguments.device
    app.persistence_path = arguments.nvd
    app.programId = arguments.programId


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

    #####################
    # (Functional) blocks
    #####################
    # Remember, all the blocks implement the mandatory nvs automatically

    # the pressure sensor
    pressure_sensor_block = app.block(
         profile = SFPTopenLoopSensor(),
         ext_name = 'FPPressureSensor',
         snvt_xxx = SNVT_switch
     )

    # create the new IoT Lamp block if using real hw periferals
    if with_hw_periferals:
        led_rgb_light_block = app.block(
            profile = SFPTisiLampActuator(),
            ext_name = 'FPIoTLamp',
        )
    # if not, use fake blocks for testing
    else:
        # the red LED light
        led_red_light_block = app.block(
            profile = SFPTopenLoopActuator(),
            ext_name = 'FPRedLedLight',
            snvt_xxx = SNVT_switch
        )
        # the red LED light feedback
        led_red_light_block_fb = app.block(
            profile = SFPTopenLoopActuator(),
            ext_name = 'FPRedLedLightFb',
            snvt_xxx = SNVT_switch
        )

    ##################################
    # Input NVs updates event handlers
    ##################################

    def on_led_red_nvi_value_update(sender, arguments):
        logger.info('Processing network variable update {0}'.format(sender))
        try:
            with led_red_light_block.nviValue:
                # check if we have real leds to control
                if with_hw_periferals:
                    # turn leds on/off
                    this_led.set_led_level(
                        RED_LED_PWM_CHANNEL,
                        led_red_light_block.nviValue.data.value)
                    # propagate
                    # led_fb = ...
                else:
                    # only propagate fake feedback
                    led_red_light_block_fb.nviValue.data = \
                        led_red_light_block.nviValue.data
                print("LED has now value {0}, state {1}".format(
                      led_red_light_block_fb.nviValue.data.value,
                      led_red_light_block_fb.nviValue.data.state))
        except Exception as e:
            print('Something just went wrong in on_led_red_nvi_value_update({0}):' \
                  '{1}'.format(sender, e))
    led_red_light_block.nviValue.OnUpdate += on_led_red_nvi_value_update

    ###########################################################################
    # Start and main loop
    ###########################################################################
    app.start()
    app.send_service_message()

    print(
        'The script is now running as "{0}",\n'
        'using non-volatile data from "{1}" and\n'
        'a unique Id (hardware address) of "{2}"'.format(
            app.programId,
            app.persistence_path,
            app.uniqueId
        )
    )
    print('...done.')
    print('\n'
          'Press the sensor to regulate LED dimming only;\n'
          'control both color and dimming via the network.\n'
          '\n'
          'Type CTRL-c to exit.'
    )


    try:
        while True:
            app.service()

            # read pressure value
            pressure = 2001 #pressure_sensor.read_pressure(PRESSURE_SENSOR_PIN)
            # start by dimming down (if possible)
            dimming_down = True

            # until user is pressing on the sensor, cycle LED brightness
            # irrespective of the pressure level (for now)
            # TODO: make dimming proportional to pressure level
            while pressure < PRESSURE_DIMMING_THRESHOLD:
                # read current dimming level for RGB LED as percentages
                r_dimming_level = led_red_light_block.nviValue.data.value
                # g_dimming_level = ...
                # b_dimming_level = ...

                # reduce dimming until color is zero, then back up
                if r_dimming_level > 0 and r_dimming_level < 100:
                    # down
                    if dimming_down:
                        r_dimming_level -= 1
                    # or up
                    else:
                        r_dimming_level += 1
                    # do it
                    #this_led.set_led_level(RED_LED_PWM_CHANNEL,
                    #                       r_dimming_level)
                    time.sleep(0.2)

                # when reach the bottom start dimming up again
                if r_dimming_level == 0:
                    dimming_down = False
                    r_dimming_level = 1
                # when reach the top start dimming down again
                elif r_dimming_level == 100:
                    dimming_down = True
                    r_dimming_level = 99

                # update the corresponding NV
                # led_red_light_block = r_dimming_level

            #pdb.set_trace()
    except KeyboardInterrupt:
        # close GPIO cleanly
        if with_hw_periferals:
            pressure_sensor.cleanup()

    finally:
        print("\n\n"
            "Winding down...")
        app.stop()
        print("Goodbye")

### end main function ###

def this_pi_ip_addr():
    """ Returns the IP address of this computer.
        Require AVAHID installed (apt-get install avahid) which should
        be installed by default in Raspbian as of summer 2013
    """
    try:
        # get text hostname of the local machine
        host = socket.gethostname()

        # get the numeric IP address from the hostname;
        # this might require avahid
        ip_address = socket.gethostbyname(host + '.local')
        print('Host ' + host + ' has IP address '+ ip_address)

        return ip_address

    except Exception as e:
        print("Can't get IP address")
        print(e)
### end this_pi_ip_addr function ###

if __name__ == '__main__':
    main()





