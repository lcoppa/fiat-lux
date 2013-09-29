#!/usr/bin/env python3 

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
from pylon.resources.color_encoding_t import color_encoding_t

# IP-C profiles used by this application
from pylon.resources.UFPTiotAnalogInput import UFPTiotAnalogInput
from pylon.resources.UFPTiotLoad import UFPTiotLoad
from pylon.resources.SFPTclosedLoopSensor import SFPTclosedLoopSensor

# I/O drivers
from led_driver.led_set import LedStrip
# Act on input
from fsr_read.pressure_sensor import PressureSensor

# Constants
MAX_PRESSURE_SENSORS = 4                # Number of hw pressure sensors
PRESSURE_SENSOR_PINS = [18, 23, 24, 25] # Pin number for each sensor
PRESSURE_DIMMING_THRESHOLD = 1000       # Pressure reading below which we cycle
                                        # LED brightness
PRESSURE_VALUE_DELTA = 50               # pressure send on delta

PWM_BOARD_I2C_ADDRESS = 0x40        # Used by the LED object
PWM_FREQ = 1000                     # In Hz, used by the LED object
RED_LED_PWM_CHANNEL = 0             # Used by the LED object
GREEN_LED_PWM_CHANNEL = 1           # Used by the LED object
BLUE_LED_PWM_CHANNEL = 2            # Used by the LED object
LED_OFFSET = 3                      # Used by the LED object
MAX_LEDs = 4                        # Number of hw LEDs supported

MIN_BRIGHTNESS_LEVEL = 0            # used in HLS color space
MAX_BRIGHTNESS_LEVEL = 255          # used in HLS color space
DIMMABLE_LED_INDEX = 0              # let's dim only one LED
DIMMING_STEP = 3                    # step value when dimming up or down
HUE = 0                             # index for hue value in HLS tuple
LUMINANCE = 1                       # index for luminance value in HLS tuple
SATURATION = 2                      # index for saturation value in HLS tuple

#############################################################################
# Main function
#############################################################################

def main():
    """ The script's main function
    """

    # Print startup message
    print('Welcome to the Pilon FiatLux application.')
    print('\n'
          'Initializing...'
          '\n')

    ########################
    # Command line arguments
    ########################

    # Define the command line arguments, with defaults and help
    parser = argparse.ArgumentParser(
        description='The Pilon LED demo script')

    parser.add_argument(
        '-c', '--color',
        default=True,
        action='store_true',
        help='Enable RGB LED hardware')
    try:
        # try getting ip address via zeroconf/bonjour/avahi
        ip_address = this_pi_ip_addr()

        # if no exceptions
        parser.add_argument(
            '-d', '--device',
            default='uc://' + ip_address + ':1628/',
            help='The device URI, e.g. uc://10.0.1.12:1628/')
    except Exception as e:
        # cannot find IP address automatically; ask the user
        parser.add_argument(
            '-d', '--device',
            required=True,
            help='The device URI, e.g. uc://10.0.1.12:1628/ \n' \
                 'Required if IP cannot be determined automatically')
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
        default='single',
        help='Enable pressure sensor hardware: "none" for no sensors, '
             '"single" for one sensor for all LEDs, '
             '"multi" for one sensor per LEDs')
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
            led_controller = LedStrip(PWM_BOARD_I2C_ADDRESS, PWM_FREQ, 
                                      arguments.debug)
        except Exception as e:
            print('Cannot find the LED light controller.')
            print(e)
            # disable color led and sensor
            arguments.color = False
            arguments.sensor = 'none'

        # TODO: detect hw LEDs actually present
        detected_led = []
        for i in range(MAX_LEDs):
            if led_detected(......................) :
                detected_led.append(True)
            else:
                detected_led.append(False)
                        

    # Create the pressure sensor object
    if arguments.sensor == 'single':
        try:
            pressure_sensor = PressureSensor(PRESSURE_SENSOR_PINS[0], 
                                             arguments.debug)
        except Exception as e:
            print('Cannot find the pressure sensor.')
            print(e)
            # disable pressure sensor
            arguments.sensor = False
    # one sensor for each RGB LED
    elif arguments.sensor == 'multi':
        # create an array of sensor objects
        pressure_sensor = []
        for i in range(MAX_PRESSURE_SENSORS):
            pressure_sensor[i] = PressureSensor(PRESSURE_SENSOR_PINS[i],
                                                arguments.debug)
    # no pressure sensore at all
    else:
        pass

    ################
    # init Pilon app
    ################

    # Enable/disable test mode
    pylon.device.stack.test_mode = arguments.test

    # Create and configure the IP-C application object
    app = pylon.device.application.Application(
        use_isi=True,
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

    # Pressure sensor blocks
    if arguments.sensor == 'single':
        # single sensor
        pressure_sensor_block = app.block(
             profile=SFPTclosedLoopSensor(),
             ext_name='FPpressureSensor',
             snvt_xxx=SNVT_count)
    elif arguments.sensor == 'multi':
        # create one sensor per LED
        pressure_sensor_block = tuple(
            app.block(profile=SFPTclosedLoopSensor(),
                      ext_name='FPpressureSensor',
                      snvt_xxx=SNVT_count)
            for i in range(MAX_PRESSURE_SENSORS))
        # give member of the tuple a size and index for later referencing
        for block_index in range(len(pressure_sensor_block)):
            pressure_sensor_block[block_index].array_size = \
                len(pressure_sensor_block)
            pressure_sensor_block[block_index].array_index = block_index
    else:
        # no sensors
        pass

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
            led_iot_block[block_index].array_size = \
                len(led_iot_block)
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
            profile=SFPTclosedLoopSensor(),
            ext_name='FPWhiteLedLight',
            snvt_xxx=SNVT_switch)
        # LED light feedback
        led_legacy_block_fb = app.block(
            profile=SFPTclosedLoopSensor(),
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
                    if sender.data.color.encoding != color_encoding_t.COLOR_RGB:
                        print('Use RGB encoding only in nviLoadControl')
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
                            set_rgb_color(0, 0, 0, led_controller, block_index)

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
                                          led_controller, block_index)

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
                                          led_controller, block_index)

                            # Send feedback
                            led_iot_block[block_index].nvoLoadStatus.data = \
                                led_iot_block[block_index].nviLoadControl.data

                        # if everything is the same
                        else:
                            # just set the color
                            set_rgb_color(new_red, new_green, new_blue,
                                          led_controller, block_index)
                            # Send feedback
                            led_iot_block[block_index].nvoLoadStatus.data = \
                                led_iot_block[block_index].nviLoadControl.data

                    print('LED {0} input is control {1}, state {2}, '
                          'level {3}'.format(i,
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
                        led_controller.set_channel_level(
                            RED_LED_PWM_CHANNEL, brightness)
                        led_controller.set_channel_level(
                            GREEN_LED_PWM_CHANNEL, brightness)
                        led_controller.set_channel_level(
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

    # Define update handler for remote pressure sensor change
    def on_remote_pressure_update(sender, event_data):
        # Simply propagate the new pressure value ???
        # TODO: double check with Rich
        pressure_sensor_block.nvoValue.data = \
            pressure_sensor_block.nviValueFb.data
    # Set the on update handler for the nviValue input
    pressure_sensor_block.nviValueFb.OnUpdate += \
        on_remote_pressure_update


    ######################
    # ISI Assembly objects
    ######################

    # Assembly for the local sensor pressure (output)
    pressure_sensor_output_assembly = pylon.device.isi.Assembly(
        assembly=pressure_sensor_block.nvoValue,
        enrollment=pylon.device.isi.Enrollment(
            direction=pylon.device.isi.IsiDirection.OUTPUT,
            type_id=pressure_sensor_block.nvoValue))

    # Assembly for the pressure arriving to me over the net (input)
    pressure_sensor_input_assembly = pylon.device.isi.Assembly(
        assembly=pressure_sensor_block.nviValueFb,
        enrollment=pylon.device.isi.Enrollment(
            direction=pylon.device.isi.IsiDirection.INPUT,
            type_id=pressure_sensor_block.nviValueFb))

    # Assembly for each LED (input and output)
    ############## done by Rich ##############

    ############
    # ISI events
    ############

    def report(me):
        print('{0}: {1}'.format(time.asctime(), me))

 
    # noinspection PyUnusedLocal
    def on_user_interface(sender, argument):
        parameter = argument.parameter
        category = pylon.device.isi.IsiEvent.category[argument.event_code]

        if category == pylon.device.isi.IsiEventCategory.ENROLLMENT and \
                parameter != pylon.device.isi.NO_ASSEMBLY:
            parameter = pylon.device.isi.Assembly.assemblies[parameter]

        report('ISI User Interface event: {0} {1}, {2}'.format(
               pylon.device.isi.IsiEventCategory.alpha[category],
               pylon.device.isi.IsiEvent.alpha[argument.event_code],
               parameter))
    app.isi.OnUserInterface += on_user_interface

    # noinspection PyUnusedLocal
    def on_enrollment(sender, argument):
        # manual enrollment
        if not argument.automatic:
            advert = argument.enrollment
            # Accept for the remote sensor block:
            if advert.direction == pylon.device.isi.IsiDirection.INPUT and \
                    advert.type_id == \
                        pressure_sensor_input_assembly.enrollment.type_id and \
                    not advert.variant:
                argument.result = pressure_sensor_input_assembly
            # Accept for the pressure sensor block:
            elif advert.direction == pylon.device.isi.IsiDirection.OUTPUT and \
                    advert.type_id == \
                        pressure_sensor_output_assembly.enrollment.type_id and \
                    not advert.variant:
                argument.result = pressure_sensor_output_assembly
        # automatic enrollment
        else:
            pass
    app.isi.OnEnrollment += on_enrollment

    #########
    # Startup
    #########

    # Set properties from command line arguments
    app.device_uri = arguments.device
    app.persistence_path = arguments.nvd
    app.programId = arguments.programId

    # Start the IP-C application
    app.start()
    app.service()

    # Display configuration
    if arguments.test:
        print('IP-C stack disabled.')
    else:
        print(
            'IP-C application running as {0},\n'
            'using non-volatile data from {1} and\n'
            'a unique Id (hardware address) of {2}'.format(
                app.programId,
                app.persistence_path,
                app.uniqueId))

    # Display instructions
    #print('\n')
    if arguments.color:
        print('Color LED hardware enabled.')
    else:
        print('*** DISABLED *** Color LED hardware')
    if arguments.sensor:
        print('Pressure sensor hardware enabled.')
        print('Press the pressure sensor to regulate LED dimming only.')
    else:
        print('*** DISABLED *** Pressure sensor hardware')
    if not arguments.legacy:
        print('Control both color and dimming via the network using the '
              'IoT Load block.')
    else:
        print('Control both color and dimming via the network using the '
              'Actuator block.')
    print('\n'
          '...done.')
    print('\n'
          'Enter "exit" to exit, "wink" to wink the device '
          'or "service" to send a Service message.')
    show_prompt()

    ###########
    # Main loop
    ###########
    try:
        # to exit mail loop
        done = False
        # dimming direction when using pressure sensor
        dimming_down = False

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
                    elif selection == 'open':
                        pass
                        #app.isi.open_enrollment(int(args))
                    elif selection == 'create':
                        pass
                        #app.isi.create_enrollment(int(args[0]))
                    elif selection == 'leave':
                        pass
                        #app.isi.leave_enrollment(int(args))
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
            elif arguments.sensor == 'single':
                try:
                    # Read pressure from the local sensor and from the net 
                    # and get the higher pressure
                    # Note: smaller value == more pressure
                    pressure = get_pressure(pressure_sensor, pressure_sensor_block)
                except Exception as e:
                    print('Cannot read pressure sensor (not running as root?)')
                    print('Error: ' + e)

                # print to console if the sensor is being pushed
                # if pressure < PRESSURE_DIMMING_THRESHOLD:
                #     print("Pressure is: " + str(pressure))
                #     show_prompt()

                # if pressure is high enough and there is a dimmable led
                if (pressure < PRESSURE_DIMMING_THRESHOLD and
                    arguments.color):
                    # for each detected LED do the dimming
                    for i in range(MAX_LEDs):
                        # if we detected LED i
                        if detected_led[i]:
                            # for shorter name
                            nvoLoadStatus = led_iot_block[i].nvoLoadStatus

                            # Read latest RGB color (which implies brightness)
                            old_red = \
                                nvoLoadStatus.data.color.color_value.RGB.red
                            old_green = \
                                nvoLoadStatus.data.color.color_value.RGB.green
                            old_blue = \
                                nvoLoadStatus.data.color.color_value.RGB.blue

                            # get brightness of latest RGB values from HLS space
                            hls_colors = colorsys.rgb_to_hls(old_red, 
                                                             old_green, 
                                                             old_blue)
                            new_brightness = hls_colors[LUMINANCE]

                            # Cycle LED brightness until user presses the sensor
                            # TODO: make dimming proportional to pressure level
                            while pressure < PRESSURE_DIMMING_THRESHOLD:

                                # let Pilon run its course
                                app.service()

                                # update pressure block on delta
                                old_pressure = pressure
                                pressure = get_pressure()
                                # send on delta
                                if abs(pressure - old_pressure) > \
                                        PRESSURE_VALUE_DELTA:
                                    pressure_sensor_block.nvoValue.data = \
                                        pressure

                                if arguments.legacy:
                                    # TODO
                                    # r_dimming_level = led_legacy_block.nviValue.data.value
                                    # g_dimming_level = led_legacy_block.nviValue.data.value
                                    # b_dimming_level = led_legacy_block.nviValue.data.value
                                    pass

                                # if we have real LEDs and iot mode
                                else:
                                    # start changing brightness up or down
                                    if dimming_down:
                                        # dim down
                                        new_brightness = max(
                                            MIN_BRIGHTNESS_LEVEL,
                                            new_brightness - DIMMING_STEP)
                                        # until brightness is minimum
                                        if new_brightness == \
                                            MIN_BRIGHTNESS_LEVEL:
                                            dimming_down = False
                                    else:
                                        # dim up
                                        new_brightness = min(
                                            MAX_BRIGHTNESS_LEVEL,
                                            new_brightness + DIMMING_STEP)
                                        # until brightness is max
                                        if new_brightness == \
                                            MAX_BRIGHTNESS_LEVEL:
                                            dimming_down = True

                                    # reconvert HLS with new brightness to RGB
                                    (new_red, new_green, new_blue) = \
                                        colorsys.hls_to_rgb(
                                            hls_colors[HUE],
                                            new_brightness,
                                            hls_colors[SATURATION])

                                    # set new brightness as RGB color
                                    set_rgb_color(new_red, 
                                                  new_green, 
                                                  new_blue,
                                                  led_controller, i)

                            # Update output LED functional block
                            nvoLoadStatus.data.level = \
                                new_brightness
                            nvoLoadStatus.data.color.color_value.RGB.red = \
                                new_red
                            nvoLoadStatus.data.color.color_value.RGB.green = \
                                new_green
                            nvoLoadStatus.data.color.color_value.RGB.blue = \
                                new_blue

                            # next time we dim the other direction
                            dimming_down = not dimming_down
                        else:
                            # nothing
                            pass







                    
            #pdb.set_trace()
    finally:
        # Stop the IP-C application
        print('\n'
              'Winding down...')
        app.stop()
        if arguments.sensor:
            # Close GPIO
            pressure_sensor.cleanup()
        print('Goodbye')

### End main function ###

if __name__ == '__main__':
    main()

#######################
# Main helper functions
#######################

def get_pressure(this_pressure_sensor, this_pressure_sensor_block):
    # read pressure both from the local sensor and the net
    # NOTE: more pressure ==>> lower read value
    local_pressure = this_pressure_sensor.read_pressure()
    remote_pressure = this_pressure_sensor_block.nviValueFb.data
    
    # if remote pressure is zero (e.g. when the dp in uninitialised) 
    # use the local pressure value
    if remote_pressure == 0:
        return local_pressure
    # else, use whichever pressure is higher (=lower reading value)
    else:
        return min(local_pressure, remote_pressure)
### end get_pressure()

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
        pi_ip_address = socket.gethostbyname(host + '.local')
        print('Host ' + host + ' has IP address ' + pi_ip_address)

        return pi_ip_address

    except Exception as e:
        print("Can't get IP address")
        print(e)
        # pass the same exception up
        raise
### end this_pi_ip_addr()

def show_prompt():
    """ Show a prompt for user input """

    # go to beginning of line, print the prompt
    sys.stdout.write("\r> ")
    # stay on this line
    sys.stdout.flush()
### end show_prompt()

def set_rgb_color(r, g, b, led_strip, led_index):
    """ Set RGB 0-255 values for the specified LED
    """
    led_strip.set_channel_level(
        RED_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
        r)
    led_strip.set_channel_level(
        GREEN_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
        0)  #g)
    led_strip.set_channel_level(
        BLUE_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
        0)  #b)
### end set_rgb_color()




