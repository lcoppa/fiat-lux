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
import colorsys
import pdb

# Import Pilon
import pylon.device

# IP-C datapoint types used by this application
from pylon.resources.SNVT_count import SNVT_count
from pylon.resources.SNVT_switch import SNVT_switch
#from pylon.resources.SNVT_temp_p import SNVT_temp_p
#from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg
#from pylon.resources.SCPTmaxSndT import SCPTmaxSndT
#from pylon.resources.SCPTdefOutput import SCPTdefOutput
from pylon.resources.color_encoding_t import color_encoding_t

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
PRESSURE_DIMMING_THRESHOLD = 1000       # Pressure reading below which we cycle
                                        # LED brightness
PWM_BOARD_I2C_ADDRESS = 0x40            # Used by the LED object
PWM_FREQ = 1000                         # In Hz, used by the LED object
RED_LED_PWM_CHANNEL = 0                 # Used by the LED object
GREEN_LED_PWM_CHANNEL = 1               # Used by the LED object
BLUE_LED_PWM_CHANNEL = 2                # Used by the LED object
LED_OFFSET = 3                          # Used by the LED object
MAX_LEDs = 4                            # Number of hw LEDs supported
MIN_BRIGHTNESS_LEVEL = 0                # used in HLS color space
MAX_BRIGHTNESS_LEVEL = 255              # used in HLS color space
DIMMABLE_LED_INDEX = 0                  # let's dim only one LED
PRESSURE_VALUE_DELTA = 50               # pressure send on delta
HUE = 0                                 # index for hue value in HLS tuple
LUMINANCE = 1                           # index for luminance value in HLS tuple
SATURATION = 2                          # index for saturation value in HLS tuple

################################################W############################
# Main function
#############################################################################

def main():
    """ The script's main function
    """

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
        default=True,
        action='store_true',
        help='Enable RGB LED hardware')
    parser.add_argument(
        '-d', '--device',
        #required=True,
        default='uc://' + this_pi_ip_addr() + ':1628/',
        help='The device URI, e.g. uc://10.0.1.12:1628/')
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
        default='9F:FF:FF:00:00:00:9A:04',
        help='The colon-separated program ID')
    parser.add_argument(
        '-s', '--sensor',
        default=True,
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

    # Create the LED controller if the PWM hardware is attached
    if arguments.color:
        # Assume the PWM board for the LEDs is at address 0x40 if not
        # changed in the constants above; check out the tutorial here
        # learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi
        try:
            #import pdb; pdb.set_trace()  # XXX BREAKPOINT
            this_led = LED(PWM_BOARD_I2C_ADDRESS, PWM_FREQ, True)
        except Exception as e:
            print("Cannot find the LED light controller.")
            print(e)
            # disable color led and sensor
            arguments.color = False
            arguments.sensor = False

    # Create the pressure sensor object if the LED can be found
    if arguments.sensor and arguments.color:
        try:
            pressure_sensor = PRESSURE_SENSOR()     # arguments.debug)
        except Exception as e:
            print("Cannot find the pressure sensor.")
            #print(e)
            # disable pressure sensor
            arguments.sensor = False

    ################
    # init Pilon app
    ################

    # Enable/disable test mode
    pylon.device.stack.test_mode = arguments.test

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
        show_prompt()
    app.OnServiceLed += on_service_led

    # noinspection PyUnusedLocal
    def on_wink(sender, arguments):
        logger.info('Received wink message')
        print('Wink!')
        show_prompt()
    app.OnWink += on_wink

    # noinspection PyUnusedLocal
    def on_online(sender, argument):
        logger.info('Received Online event')
        print('We are now online!')
        show_prompt()
    app.OnOnline += on_online

    # noinspection PyUnusedLocal
    def on_offline(sender, argument):
        logger.info('Received Offline event')
        print('We are now offline.')
        show_prompt()
    app.OnOffline += on_offline

    ###################
    # Functional blocks
    ###################

    # Pressure sensor block
    if arguments.sensor:
        pressure_sensor_block = app.block(
             profile=SFPTopenLoopSensor(),
             ext_name='FPPressureSensor',
             snvt_xxx=SNVT_count)

    # LED blocks: tuples of blocks, one for each physical LED
    if not arguments.legacy:
        #
        # Create the LED blocks using the new IoT Load Control block
        #
        led_iot_block = tuple(
            app.block(profile=UFPTiotLoad(),
                        ext_name='Color Lamp')
            for i in range(MAX_LEDs))
        # give each member of the tuple a size and index for later referencing
        for block_index in range(len(led_iot_block)):
            led_iot_block[block_index].array_size = len(led_iot_block)
            led_iot_block[block_index].array_index = block_index

        #
        # Create the power monitor blocks
        #
        power_monitor_iot_block = tuple(
            app.block(profile=UFPTiotAnalogInput(),
                        ext_name='Lamp Power Monitor')
            for i in range(MAX_LEDs))
        # give each member of the tuple a size and index for later referencing
        for block_index in range(len(power_monitor_iot_block)):
            power_monitor_iot_block[block_index].array_size = \
                len(power_monitor_iot_block)
            power_monitor_iot_block[block_index].array_index = block_index

        #
        # Create the energy monitor blocks
        #
        energy_monitor_iot_block = tuple(
            app.block(profile=UFPTiotAnalogInput(),
                      ext_name='Lamp Energy Monitor')
            for i in range(MAX_LEDs))
        # give each member of the tuple a size and index for later referencing
        for block_index in range(len(energy_monitor_iot_block)):
            energy_monitor_iot_block[block_index].array_size = \
                len(energy_monitor_iot_block)
            energy_monitor_iot_block[block_index].array_index = block_index

    else:
        #
        # Legacy mode: create functional blocks based on legacy profiles
        #

        # Use our RGB LED as a standard white light
        led_legacy_block = app.block(
            profile=SFPTopenLoopActuator(),
            ext_name='FPWhiteLedLight',
            snvt_xxx=SNVT_switch)
        # LED light feedback
        led_legacy_block_fb = app.block(
            profile=SFPTopenLoopSensor(),
            ext_name='FPWhiteLedLightFb',
            snvt_xxx=SNVT_switch)


    #######################################
    # Input datapoint update event handlers
    #######################################

    # Define the on update handler for the IoT Load Control
    # nviLoadControl input
    if not arguments.legacy:
        def on_led_nvi_load_control_update(sender, event_data):
            logger.info('Processing network variable update'
                        ' {0}'.format(sender))

            try:
                with sender:
                    # get the index of the block to access the correct
                    # element of the tuple of blocks
                    block_index = sender._block.array_index
                    print('Block index {0}'.format(block_index))

                    # variables with short name for convenience
                    new_state = sender.data.state
                    #old_state = led_iot_block[block_index].nvoLoadStatus.data.state
                    new_red = sender.data.color.color_value.RGB.red
                    new_green = sender.data.color.color_value.RGB.green
                    new_blue = sender.data.color.color_value.RGB.blue
                    old_red = led_iot_block[block_index].nvoLoadStatus.data.color.color_value.RGB.red
                    old_green = led_iot_block[block_index].nvoLoadStatus.data.color.color_value.RGB.green
                    old_blue = led_iot_block[block_index].nvoLoadStatus.data.color.color_value.RGB.blue
                    new_brightness = sender.data.level
                    old_brightness = led_iot_block[block_index].nvoLoadStatus.data.level

                    # Require RGB encoding (for now)
                    if (not sender.data.color.encoding ==
                            color_encoding_t.COLOR_RGB):
                        print("Use RGB encoding only in nviLoadControl")
                        show_prompt()
                        return

                    # Act on input
                    if arguments.color:
                        # Real LEDs available

                        # NOTE:
                        # nviLoadControl contains info about both brightness
                        # ('level') and color ('color'); the problem is that
                        # color implies brightness in all color encodings
                        # used (RGB or CIE 1931); so we change brightness only
                        # if color stays the the same

                        # if the state is off turn everything off
                        if new_state is False:
                            # turn off the LED
                            set_rgb_color(0, 0, 0, this_led, block_index)

                            # Send feedback
                            # 1:1 copy of the input is propagated
                            # leave the RGB and brightness output as they are
                            led_iot_block[block_index].nvoLoadStatus.data = \
                                led_iot_block[block_index].nviLoadControl.data

                        # if any of the three color values changed compared to
                        # what's saved in the output datapoint
                        elif (new_red != old_red or new_green != old_green or
                              new_blue != old_blue):
                            # set the new color
                            set_rgb_color(new_red, new_green, new_blue,
                                          this_led, block_index)

                            # new RGB values mean new brightness level
                            # so in the o/p dp we want to update it:
                            # translate this new RGB value to HLS space
                            hls_colors = colorsys.rgb_to_hls(new_red, new_green, new_blue)
                            # get the second value of the tuple (=brightness)
                            new_brightness = hls_colors[LUMINANCE]

                            # Send feedback: this will propagate twice!!
                            led_iot_block[block_index].nvoLoadStatus.data = \
                                led_iot_block[block_index].nviLoadControl.data
                            # TODO: how to update a field of the output dp without
                            # propagating it to the network?
                            led_iot_block[block_index].nvoLoadStatus.data.level = new_brightness

                            # now I should propagate!!!

                        elif new_brightness != old_brightness:
                            # the color is the same
                            # change brightness only

                            # make sure the new brightness is within boundaries
                            new_brightness = max(new_brightness, MIN_BRIGHTNESS_LEVEL)
                            new_brightness = min(new_brightness, MAX_BRIGHTNESS_LEVEL)

                            # translate the old RGB value to HLS space
                            hls_colors = colorsys.rgb_to_hls(new_red, new_green, new_blue)

                            # update brightness (=luminance=L) in HLS color space
                            # Lumnance is the second member of the tuple
                            hls_colors[LUMINANCE] = new_brightness

                            # reconvert new brightness to RGB color space
                            (new_red, new_green, new_blue) = \
                                colorsys.hls_to_rgb(
                                    old_red,
                                    old_green,
                                    old_blue)

                            # set new brightness as RGB color
                            set_rgb_color(new_red, new_green, new_blue,
                                          this_led, block_index)

                            # Send feedback
                            led_iot_block[block_index].nvoLoadStatus.data = \
                                led_iot_block[block_index].nviLoadControl.data

                        # if everything is the same
                        else:
                            # just set the color
                            set_rgb_color(new_red, new_green, new_blue,
                                          this_led, block_index)
                            # Send feedback
                            led_iot_block[block_index].nvoLoadStatus.data = \
                                led_iot_block[block_index].nviLoadControl.data

                    print("LED {0} input is control {1}, state {2}, "
                          "level {3}".format(i,
                                             sender.data.control,
                                             sender.data.state,
                                             sender.data.level))
            except Exception as e:
                print('Something just went wrong when updating RGB values '
                      'in on_led_nvi_load_control_update({0}):'
                      '{1}'.format(sender, e))
            finally:
                show_prompt()
        # Create the on update handler for the nviValue input
        for i in range(0, MAX_LEDs):
            led_iot_block[i].nviLoadControl.OnUpdate += \
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
                        if led_legacy_block.nviValue.data.state == 1:
                            brightness = led_legacy_block.nviValue.data.value
                        else:
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
            finally:
                show_prompt()
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
    print('\n')
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
          "Enter 'exit' to exit, 'wink' to wink the device "
          "or 'service' to send a Service message.")
    show_prompt()

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
            #import pdb; pdb.set_trace()  # XXX BREAKPOINT

            # read user input
            i, o, e = select.select([sys.stdin], [], [], 0.01)
            if i:
                try:
                    selection = sys.stdin.readline().strip().lower()
                    if selection == 'exit':
                        done = True
                    elif selection == 'service':
                        app.send_service_message()
                        print('Service message sent')
                        show_prompt()
                    elif selection == 'wink':
                        # Simulate receipt of a Wink message for testing:
                        app.OnWink.fire(app, None)
                        show_prompt()
                    else:
                        print('Valid commands are "exit", "service", "wink"')
                        show_prompt()
                except Exception as e:
                    print(e)
                    show_prompt()

            #
            #   Pressure sensor input
            #
            # TODO: move to a separate thread
            elif arguments.sensor:
                # Read pressure value: more pressure == smaller value
                try:
                    pressure = pressure_sensor.read_pressure(PRESSURE_SENSOR_PIN)
                except Exception as e:
                    print("Cannot read pressure sensor (not running as root?)")
                    print(e)
    
                # print to console if the sensor is being pushed
                if pressure < PRESSURE_DIMMING_THRESHOLD:
                    print("Pressure is: " + str(pressure))
                    show_prompt()

                # if pressure is high enough and there is a dimmable led
                if (pressure < PRESSURE_DIMMING_THRESHOLD and
                        arguments.color):
                        #and led_iot_block[DIMMABLE_LED_INDEX].nviLoadControl.data.state):

                    # Start by dimming down (if possible)
                    dimming_down = True
                    pressure_detected = True

                    # Cycle LED brightness until user presses the sensor
                    # TODO: make dimming proportional to pressure level
                    while pressure < PRESSURE_DIMMING_THRESHOLD:

                        # let Pilon run its course
                        app.service()

                        if arguments.legacy:
                            # TODO
                            # r_dimming_level = led_legacy_block.nviValue.data.value
                            # g_dimming_level = led_legacy_block.nviValue.data.value
                            # b_dimming_level = led_legacy_block.nviValue.data.value
                            pass

                        # if we have real LEDs and iot mode
                        else:

                            # Read latest color RGB LED (which implies brightness)
                            old_red = led_iot_block[DIMMABLE_LED_INDEX].nvoLoadStatus.data.color.color_value.RGB.red
                            old_green = led_iot_block[DIMMABLE_LED_INDEX].nvoLoadStatus.data.color.color_value.RGB.green
                            old_blue = led_iot_block[DIMMABLE_LED_INDEX].nvoLoadStatus.data.color.color_value.RGB.blue

                            # get brightness of latest RGB values from HLS space
                            hls_colors = colorsys.rgb_to_hls(old_red, old_green, old_blue)
                            new_brightness = hls_colors[LUMINANCE]

                            # start changing brightness up or down
                            if dimming_down:
                                # dim down
                                new_brightness = max(MIN_BRIGHTNESS_LEVEL, new_brightness - 1)
                                # until brightness is minimum
                                if new_brightness == MIN_BRIGHTNESS_LEVEL:
                                    dimming_down = False
                            else:
                                # dim up
                                new_brightness = min(MAX_BRIGHTNESS_LEVEL, new_brightness + 1)
                                # until brightness is max
                                if new_brightness == MAX_BRIGHTNESS_LEVEL:
                                    dimming_down = True

                                time.sleep(0.2)

                            # reconvert HLS with new brightness to RGB color space
                            (new_red, new_green, new_blue) = \
                                colorsys.hls_to_rgb(hls_colors[HUE],
                                                    new_brightness,
                                                    hls_colors[SATURATION])

                            # set new brightness as RGB color
                            set_rgb_color(new_red, new_green, new_blue,
                                this_led, DIMMABLE_LED_INDEX)

                        # update pressure reading
                        old_pressure = pressure
                        pressure = pressure_sensor.read_pressure(PRESSURE_SENSOR_PIN)
                        # if difference is greater than a given delta, do dp update
                        if abs(pressure - old_pressure) > PRESSURE_VALUE_DELTA:
                            pressure_sensor_block.nvoValue.value = pressure

                    # Send feedback only if pressure sensors changed LED brightness
                    if pressure_detected:
                        led_iot_block[DIMMABLE_LED_INDEX].nvoLoadStatus.data.level = \
                            new_brightness
                        led_iot_block[DIMMABLE_LED_INDEX].nvoLoadStatus.data.color.color_value.RGB.red = \
                            new_red
                        led_iot_block[DIMMABLE_LED_INDEX].nvoLoadStatus.data.color.color_value.RGB.green = \
                            new_green
                        led_iot_block[DIMMABLE_LED_INDEX].nvoLoadStatus.data.color.color_value.RGB.blue = \
                            new_blue
                        pressure_detected = False

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
        print('Host ' + host + ' has IP address ' + ip_address)

        return ip_address

    except Exception as e:
        print("Can't get IP address")
        print(e)
### End this_pi_ip_addr function ###


def show_prompt():
    """ Show a prompt for user input """

    # go to beginning of line, print the prompt
    sys.stdout.write("\r> ")
    # stay on this line
    sys.stdout.flush()
### end show_prompt function ###


def set_rgb_color(r, g, b, led_obj, led_index):
    """ Set RGB values for the specified LED
    """
    led_obj.set_led_level(
        RED_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
        r)
    led_obj.set_led_level(
        GREEN_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
        g)
    led_obj.set_led_level(
        BLUE_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
        b)
### end set_rgb_color() ####

if __name__ == '__main__':
    main()





