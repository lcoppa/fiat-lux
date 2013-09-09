#!/usr/bin/env python3 -tt

""" Pilon application
    Controls RGB LEDs via network datapoints (color and brightness) and
    pressure (brightness)
"""

#
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#
# Use of this example software is subject to the terms of the
# Echelon Example Software License Agreement at
# www.echelon.com/license/examplesoftware/.

##############################################################################
# Imports
##############################################################################
# Import standard Python modules
import argparse
import logging
import time
import select
import socket
import sys

# Import Pilon
import pylon.device

# IP-C datapoint types used by this application
from pylon.resources.SNVT_switch import SNVT_switch
#from pylon.resources.SNVT_temp_p import SNVT_temp_p
#from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg
#from pylon.resources.SCPTmaxSndT import SCPTmaxSndT
#from pylon.resources.SCPTdefOutput import SCPTdefOutput
from pulon.resources.color_encoding_t import color_encoding_t

# IP-C profiles used by this application
from pylon.resources.UFPTiotAnalogInput import UFPTiotAnalogInput
from pylon.resources.UFPTiotLoad import UFPTiotLoad
from pylon.resources.SFPTopenLoopSensor import SFPTopenLoopSensor
from pylon.resources.SFPTopenLoopActuator import SFPTopenLoopActuator

# I/O drivers
from led_driver.led_set import LED
# Act on input
from fsr_read.pressure_sensor import PRESSURE_SENSOR

# Constants
PRESSURE_SENSOR_PIN = 18                # Used by the PRESSURE object
PRESSURE_DIMMING_THRESHOLD = 2000       # Pressure reading below which we cycle
                                        # LED brightness
PWM_BOARD_I2C_ADDRESS = 0x40            # Used by the LED object
PWM_FREQ = 1000                         # In Hz, used by the LED object
RED_LED_PWM_CHANNEL = 0                 # Used by the LED object
GREEN_LED_PWM_CHANNEL = 1               # Used by the LED object
BLUE_LED_PWM_CHANNEL = 2                # Used by  the LED object

################################################W############################
# Main function
#############################################################################

def main():
    """The script's main function"""

    # Print startup message
    print('Welcome to the Pilon FiatLux application.')
    print('\n'
          'Initializing...')

    ########################
    # Command line arguments
    ########################

    # Define the command line arguments, with defaults and help
    parser = argparse.ArgumentParser(
        description="The Pilon LED demo script")
    parser.add_argument(
        '-c', '--color',
        default=False,
        action='store_true',
        help='Enable RGB LED hardware')
    parser.add_argument(
        '-d', '--device',
        #required=True,
        default = 'uc://' + this_pi_ip_addr() + ':1628/',
        help = 'The device URI, e.g. uc://10.0.1.12:1628/')
    parser.add_argument(
        '-D', '--debug',
        default=False,
        action='store_true',
        help='Enable full trace logging')
    parser.add_argument(
        '-l', '--log',
        default='fiat-lux-log',
        help='The base location and name for log files')
    parser.add_argument(
        '-L', '--legacy',
        default=False,
        action='store_true',
        help='Enable legacy profiles (disable IoT profiles)')
    parser.add_argument(
        '-n', '--nvd',
        default='fiat-lux-nvd',
        help='Path to non-volatile data storage (folder)')
    parser.add_argument(
        '-p', '--programId',
        default='9F:FF:FF:00:00:00:9A:03',
        help='The colon-separated program ID')
    parser.add_argument(
        '-s', '--sensor',
        default=False,
        action='store_true',
        help='Enable pressure sensor hardware')
    parser.add_argument(
        '-t', '--test',
        default=False,
        action='store_true',
        help='Enable test mode (disables the IP-C stack)')

    # Parse the command line
    arguments = parser.parse_args()


    ##########
    # init I/O
    ##########

    # Create the pressure sensor object if the hardware is attached
    if arguments.sensor:
        try:
            pressure_sensor = PRESSURE_SENSOR()
        except Exception as e:
            print("Cannot find the pressure sensor.")
            print(e)

    # Create the LED controller if the PWM hardware is attached
    if arguments.color:
        # Assume the PWM board for the LEDs is at address 0x40 if not
        # changed in the constants above; check out the tutorial here
        # learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi
        try:
            this_led = LED(PWM_BOARD_I2C_ADDRESS, PWM_FREQ, True)
            pass
        except Exception as e:
            print("Cannot find the LED light controller.")
            print(e)

    # Enable/disable test mode
    pylon.device.stack.test_mode = arguments.test


    ################
    # init Pilon app
    ################

    # Create and configure the IP-C application object
    app = pylon.device.application.Application(
        use_isi=False,
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR)

    # Create the stack logger
    logger = logging.getLogger('pylon-rtk.fiat-lux')

    # Set low-level stack trace logging if requested
    if arguments.debug:
        app.stack_tracefile = arguments.log + '-lts.log'
        if app.isi:
            # Set special ISI logging as well
            app.isi.tracefile(arguments.log + '-isi.log', False)

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
        logger.info('Received wink message')
        print('Wink.')
    app.OnWink += on_wink

    # noinspection PyUnusedLocal
    def on_online(sender, argument):
        logger.info('Received Online event')
        print('We are now online.')
    app.OnOnline += on_online

    # noinspection PyUnusedLocal
    def on_offline(sender, argument):
        logger.info('Received Offline event')
        print('We are now offline.')
    app.OnOffline += on_offline

    ###################
    # Functional blocks
    ###################

    # Pressure sensor block
    if arguments.sensor:
        pressure_sensor_block = app.block(
             profile = SFPTopenLoopSensor(),
             ext_name = 'FPPressureSensor',
             snvt_xxx = SNVT_switch)

    # LED block
    if not arguments.legacy:
        # Create the LED block using the new IoT Load Control block
        led_iot_block = app.block(
            profile = UFPTiotLoad(),
            ext_name = 'Color Lamp')
        # Create the power monitor block
        power_monitor_iot_block = app.block(
            profile = UFPTiotAnalogInput(),
            ext_name = 'Lamp Power Monitor')
        # Create the energy monitor block
        energy_monitor_iot_block = app.block(
            profile = UFPTiotAnalogInput(),
            ext_name = 'Lamp Energy Monitor')
    else:
        # Create functional blocks based on legacy profiles
        # Use our RGB LED as a standard white light
        led_legacy_block = app.block(
            profile = SFPTopenLoopActuator(),
            ext_name = 'FPWhiteLedLight',
            snvt_xxx = SNVT_switch)
        # LED light feedback
        led_legacy_block_fb = app.block(
            profile = SFPTopenLoopSensor(),
            ext_name = 'FPWhiteLedLightFb',
            snvt_xxx = SNVT_switch)


    #######################################
    # Input datapoint update event handlers
    #######################################

    # Define the on update handler for the IoT Load Control 
    # nviLoadControl input
    if not arguments.legacy:
        def on_led_nvi_load_control_update(sender, event_data):
            logger.info('Processing network variable update '
                        ' {0}'.format(sender))

            # Require RBG encoding (for now)
            if (not led_iot_block.nviLoadControl.data.color.encoding == 
                color_encoding_t.COLOR_RGB):
                print("Use RGB encoding only in nviLoadControl")
                return

            try:    
                with led_iot_block.nviLoadControl:
                    # Act on input
                    if arguments.color:
                        # Real LEDs available -- turn them on or off
                        this_led.set_led_level(
                            RED_LED_PWM_CHANNEL,
                            led_iot_block.nviLoadControl.data.color_value.RGB.red)
                        this_led.set_led_level(
                            GREEN_LED_PWM_CHANNEL,
                            led_iot_block.nviLoadControl.data.color_value.RGB.green)
                        this_led.set_led_level(
                            BLUE_LED_PWM_CHANNEL,
                            led_iot_block.nviLoadControl.data.color_value.RGB.blue)
                    # Send feedback
                    # TODO: process the input before sending instead of 
                    # sending it as feedback
                    led_iot_block.nvoLoadStatus.data = \
                    led_iot_block.nviLoadControl.data
                    print("LED input is control {0}, state {1}, "
                          "level {2}".format(
                          led_iot_block.nviLoadControl.data.control,
                          led_iot_block.nviLoadControl.data.state,
                          led_iot_block.nviLoadControl.data.level))
            except Exception as e:
                print('Something just went wrong when updating RGB values '
                      'in on_led_nvi_load_control_update({0}):' 
                      '{1}'.format(sender, e))
        # Create the on update handler for the nviValue input
        led_iot_block.nviLoadControl.OnUpdate += \
        on_led_nvi_load_control_update

    # Define the on update handler for the Actuator nviValue input
    if arguments.legacy:
        def on_legacy_led_nvi_value_update(sender, event_data):
            logger.info('Processing network variable update'
                        ' {0}'.format(sender))
            try:
                with led_legacy_block.nviValue:
                    if arguments.color:
                        # Real LED available -- turn them on or off
                        # but treat it as white (no color)
                        # i.e. set same brightness to all colors
                        
                        # check data point state field first
                        if led_legacy_block.nviValue.data.state == 1
                            brightness = led_legacy_block.nviValue.data.value
                        else 
                            brightness = 0
                        
                        # set the new brightness
                        this_led.set_led_level(
                            RED_LED_PWM_CHANNEL, brightness)
                        this_led.set_led_level(
                            GREEN_LED_PWM_CHANNEL, brightness)
                        this_led.set_led_level(
                            BLUE_LED_PWM_CHANNEL, brightness)
                        
                        print("LED has now value {0}, state {1}".format(
                              led_legacy_block_fb.nviValue.data.value,
                              led_legacy_block_fb.nviValue.data.state))

                    # Propagate feedback even if no real LED is present
                    led_legacy_block_fb.nvoValue.data = \
                    led_legacy_block.nviValue.data
            except Exception as e:
                print('Something just went wrong in '
                      'on_legacy_led_nvi_value_update({0}):'
                      '{1}'.format(sender, e))
        # Create the on update handler for the nviValue input
        led_legacy_block.nviValue.OnUpdate += on_legacy_led_nvi_value_update

    #########
    # Startup
    #########

    # Set properties from command line arguments
    app.device_uri = arguments.device
    app.persistence_path = arguments.nvd
    app.programId = arguments.programId

    # Start the IP-C application
    app.start()

    # Display configuration
    if arguments.test:
        print("IP-C stack disabled.")
    else:
        print(
            'IP-C application running as {0},\n'
            'using non-volatile data from {1} and\n'
            'a unique Id (hardware address) of {2}'.format(
                app.programId,
                app.persistence_path,
                app.uniqueId))

    # Display instructions    
    if arguments.color:
        print("Color LED hardware enabled.")
    else:
        print("Color LED hardware disabled.")
    if arguments.sensor:
        print("Pressure sensor hardware enabled.")
        print("Press the pressure sensor to regulate LED dimming only.")
    else:
        print("Pressure sensor hardware disabled.")
    if not arguments.legacy:
        print("Control both color and dimming via the network using the "
              "IoT Load block.")
    else:
        print("Control both color and dimming via the network using the "
              "Actuator block.")
    print("...initialization done.")
    print("\n"
          "Enter 'exit' to exit, or 'service' to send a Service message."
          "\n")

    ###########
    # Main loop
    ###########
    try:
        done = False

        while not done:
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
                        print('Service message sent')
                    elif selection == 'wink':
                        # Simulate receipt of a Wink message for testing:
                        app.OnWink.fire(app, None)
                    else:
                        print('Valid commands are "exit", "service", "wink"')
                except Exception as e:
                    print(e)

            #
            #   Pressure sensor input
            #
            # TODO: move to a separate thread
            if arguments.sensor:
                # Read pressure value
                pressure = pressure_sensor.read_pressure(PRESSURE_SENSOR_PIN)

                # Start by dimming down (if possible)
                dimming_down = True

                # Cycle LED brightness until user presses the sensor
                # TODO: make dimming proportional to pressure level
                while pressure < PRESSURE_DIMMING_THRESHOLD:
                    # Read current dimming level for RGB LED as percentages
                    r_dimming_level = led_block.nviValue.data.value
                    # g_dimming_level = ...
                    # b_dimming_level = ...

                    # Reduce dimming until color is zero, then back up
                    if r_dimming_level > 0 and r_dimming_level < 100:
                        if dimming_down:
                            # Down
                            r_dimming_level -= 1
                        else:
                            # Up
                            r_dimming_level += 1
                        if arguments.color:
                            # Set the LED brightness
                            this_led.set_led_level(RED_LED_PWM_CHANNEL,
                                                   r_dimming_level)
                        time.sleep(0.2)

                    if r_dimming_level == 0:
                        # At bottom--dim up again
                        dimming_down = False
                        r_dimming_level = 1
                    elif r_dimming_level == 100:
                        # At top--dim down again
                        dimming_down = True
                        r_dimming_level = 99

                    # Update the corresponding NV
                    # led_block = r_dimming_level

            #pdb.set_trace()

    finally:
        # Stop the IP-C application
        print("\n"
              "Winding down...")
        app.stop()
        if arguments.sensor:
            # Close GPIO
            pressure_sensor.cleanup()
        print("Goodbye")

### End main function ###


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
### End this_pi_ip_addr function ###

if __name__ == '__main__':
    main()





