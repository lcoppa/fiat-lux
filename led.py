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
# import pdb

sys.path.append('/usr/local/lib/python3.2/dist-packages')

# Import Pilon
import pylon.device

# IP-C datapoint types used by this application
import pylon.resources.datapoints.count
import pylon.resources.datapoints.switch
import pylon.resources.enumerations.color_encoding_t as color_encoding
import pylon.resources.enumerations.load_control_t as load_control

# IP-C profiles used by this application
import pylon.resources.profiles.iotAnalogInput
import pylon.resources.profiles.iotLoad
import pylon.resources.profiles.closedLoopSensor

# I/O drivers
from pylon.examples.common.fsr_driver.pressure_sensor import PressureSensor
from pylon.examples.common.led_driver.pwm_led_set import LedStrip
from pylon.examples.common.led_driver.piface_led_set import PiFaceLed

# Constants
PWM_BOARD_I2C_ADDRESS = 0x40            # Used by the LED object
PWM_FREQ = 1000                         # In Hz, used by the LED object
RED_LED_PWM_CHANNEL = 0                 # Used by the LED object
GREEN_LED_PWM_CHANNEL = 1               # Used by the LED object
BLUE_LED_PWM_CHANNEL = 2                # Used by the LED object
LED_OFFSET = 3                          # Used by the LED object
MAX_LEDs = 2                            # Number of hw LEDs supported

MIN_BRIGHTNESS_LEVEL = 0                # Used in HLS color space
MAX_BRIGHTNESS_LEVEL = 255              # Used in HLS color space
DIMMABLE_LED_INDEX = 0                  # Let's dim only one LED
DIMMING_STEP = 3                        # Step value when dimming up or down
HUE = 0                                 # Index for hue coordinate in HLS tuple
LUMINANCE = 1                           # Index for luminance coordinate in HLS tuple
SATURATION = 2                          # Index for saturation coordinate in HLS tuple
RED = 0                                 # Index for red coordinate in RGB tuple
GREEN = 1                               # Index for green coordinate in RGB tuple
BLUE = 2                                # Index for blue coordinate in RGB tuple

MAX_PRESSURE_SENSORS = MAX_LEDs         # One pressure sensor per LED
PRESSURE_SENSOR_PINS = [18, 23, 24, 25] # Pin number for each sensor
PRESSURE_DIMMING_THRESHOLD = 1000       # Pressure reading below which we cycle
                                        # LED brightness
PRESSURE_VALUE_DELTA = 50               # pressure send on delta


#
# Main function
#
def main():
    """ The script's main function
    """

    # Print startup message
    print('Welcome to the Pilon LED Controller application.')
    print('\n'
          'Initializing...'
          '\n')

    #
    # Command line arguments
    #
    parser = argparse.ArgumentParser(
        description='The Pilon LED demo script')

    parser.add_argument(
        '-c', '--color',
        default=False,
        action='store_true',
        help='Enable RGB LED hardware')
    parser.add_argument(
        '-C', '--pycharm',
        default=False,
        action='store_true',
        help='Enable debugging with PyCharm')
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
        '-P', '--piface',
        default=False,
        action='store_true',
        help='Enable PiFace I/O hardware')
    parser.add_argument(
        '-s', '--sensor',
        default='single',
        help='Enable pressure sensor hardware: "none" for no sensors, '
             '"single" for one sensor for all LEDs, '
             '"multi" for one sensor per LEDs')
    parser.add_argument(
        '-S', '--standalone',
        default=False,
        action='store_true',
        help='Enable ISI standalone mode (disable ISI connections)'
    )
    parser.add_argument(
        '-t', '--test',
        default=False,
        action='store_true',
        help='Enable test mode (disables the IP-C stack)')

    # Parse the command line
    arguments = parser.parse_args()

    # Connect to the PyCharm debugger if enabled
    if arguments.pycharm:
        from pydev import pydevd
        pydevd.settrace('192.168.60.9', port=5678, stdoutToServer=True, stderrToServer=True)

    #
    # Initialize I/O
    #
    # Create the LED controller if the PWM hardware is attached
    if arguments.color:
        # Assume the PWM board for the LEDs is at address 0x40 if not
        # changed in the constants above; check out the tutorial here
        # learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi
        try:
            #import pdb; pdb.set_trace()  # XXX BREAKPOINT
            led_controller = LedStrip(PWM_BOARD_I2C_ADDRESS, PWM_FREQ, 
                                      arguments.debug)
            # Create flags for detected LED in the strip
            led_controller.detected_led = []
            # Detect hw LEDs actually present
            for i in range(MAX_LEDs):
                if True: # TODO: actually detect it
                    led_controller.detected_led.append(True)
                else:
                    led_controller.detected_led.append(False)
        except Exception as e:
            print('Cannot find the LED light controller.')
            print(e)
            # Disable color led and sensor
            arguments.color = False
            arguments.sensor = 'none'

    elif arguments.piface:
        try:
            led_controller = PiFaceLed(arguments.debug)
        except Exception as e:
            print('Cannot find the PiFace board')
            print(e)
            # Disable PiFace and sensor
            arguments.piface = False
            arguments.sensor = 'none'

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
    # One sensor for each RGB LED
    elif arguments.sensor == 'multi':
        # create an array of sensor objects
        pressure_sensor = []
        for i in range(MAX_PRESSURE_SENSORS):
            pressure_sensor[i].append(PressureSensor(PRESSURE_SENSOR_PINS[i],
                                                     arguments.debug))
    # No pressure sensor at all
    else:
        pass

    #
    # Initialize the Pilon app
    #
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

    #
    # System event handlers definition and registration
    #
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

    #
    # Functional blocks
    #
    # Pressure sensor blocks
    if arguments.sensor == 'single':
        # single sensor
        pressure_sensor_block = app.block(
             profile= \
                pylon.resources.profiles.closedLoopSensor.closedLoopSensor(),
             ext_name='FPpressureSensor',
             xxx=pylon.resources.datapoints.count)
    elif arguments.sensor == 'multi':
        # create one sensor per LED
        pressure_sensor_block = tuple(app.block(
            profile= \
                pylon.resources.profiles.closedLoopSensor.closedLoopSensor(),
            ext_name='FPpressureSensor',
            xxx=pylon.resources.datapoints.count)
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
        # IoT mode--create the LED blocks as tuples of IoT Load Control
        # blocks, one for each physical LED
        led_iot_block = tuple(
            app.block(
                profile=pylon.resources.profiles.iotLoad.iotLoad(),
                ext_name='Color Lamp')
            for i in range(MAX_LEDs))
        # Give each member of the tuple a size and index for later referencing
        for block_index in range(len(led_iot_block)):
            led_iot_block[block_index].array_size = len(led_iot_block)
            led_iot_block[block_index].array_index = block_index

        # Create the power monitor blocks as tuples of IoT Analog Input blocks,
        # one for each physical LED
        power_monitor_iot_block = tuple(
            app.block(
                profile=pylon.resources.profiles.iotAnalogInput.iotAnalogInput(),
                ext_name='Lamp Power Monitor')
            for i in range(MAX_LEDs))
        # Give each member of the tuple a size and index for later referencing
        for block_index in range(len(power_monitor_iot_block)):
            power_monitor_iot_block[block_index].array_size = \
                len(power_monitor_iot_block)
            power_monitor_iot_block[block_index].array_index = block_index

        # Create the energy monitor blocks as tuples of IoT Analog Input blocks,
        # one for each physical LED
        energy_monitor_iot_block = tuple(
            app.block(
                profile=pylon.resources.profiles.iotAnalogInput.iotAnalogInput(),
                ext_name='Lamp Energy Monitor')
            for i in range(MAX_LEDs))
        # Give each member of the tuple a size and index for later referencing
        for block_index in range(len(energy_monitor_iot_block)):
            energy_monitor_iot_block[block_index].array_size = \
                len(energy_monitor_iot_block)
            energy_monitor_iot_block[block_index].array_index = block_index

    else:
        # Legacy mode: create functional blocks based on legacy profiles
        # Use our RGB LED as a standard white light
        led_legacy_block = app.block(
            profile=pylon.resources.profiles.closedLoopSensor.closedLoopSensor(),
            ext_name='FPWhiteLedLight',
            xxx=pylon.resources.datapoints.switch)

    #
    # Input datapoint update event handlers
    #
    # Define the on update handler for the IoT Load Control
    # nviLoadControl input
    if not arguments.legacy:
        def on_led_nvi_load_control_update(sender, event_data):
            print('Processing network variable update {0}'.format(sender))
            print('Scene number {0}'.format(sender.data.scene_number))
            print('Red {0}'.format(sender.data.color.color_value.RGB.red))
            print('Blue {0}'.format(sender.data.color.color_value.RGB.blue))
            print('Green {0}'.format(sender.data.color.color_value.RGB.green))
            print('State {0}'.format(sender.data.state))
            logger.info('Processing network variable update'
                        ' {0}'.format(sender))

            try:
                with sender:
                    # Get the index of the block to access the correct
                    # element of the tuple of blocks
                    block_index = sender.block.array_index

                    # Variables with short name for convenience
                    led_block = led_iot_block[block_index]
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

                    if(sender.data.control == load_control.load_control_t.LOAD_SET):
                        # Set the LED state, level, and color to the specified values
                        led_block.nvoLoadStatus.data.control = load_control.load_control_t.LOAD_REPORT
                        led_block.nvoLoadStatus.state = new_state
                        if new_state:
                            # State is on; set level and color; clear the level if color is specified
                            if sender.data.color.encoding == color_encoding.color_encoding_t.COLOR_RGB:
                                led_block.nvoLoadStatus.data.level = 'nan'
                                led_block.nvoLoadStatus.data.color.color_value.RGB.red = new_red
                                led_block.nvoLoadStatus.data.color.color_value.RGB.green = new_green
                                led_block.nvoLoadStatus.data.color.color_value.RGB.blue = new_blue
                            else:
                                led_block.nvoLoadStatus.data.level = new_brightness
                            normalize_led_state(led_block)
                            set_led_output(led_controller, block_index, led_block, arguments)
                    elif(sender.data.control == load_control.load_control_t.LOAD_RECALL_SCENE):
                        # Set the LED state, level, and color to hard-coded scene settints
                        if(sender.data.state == 0):
                            set_led_status(0, 'nan', 255, 255, 255, 65535, led_controller, 0, led_iot_block[0], arguments)
                            set_led_status(0, 'nan', 255, 255, 255, 65535, led_controller, 1, led_iot_block[1], arguments)
                        elif(sender.data.scene_number == 1):
                            set_led_status(1, 'nan', 100, 0, 0, 65535, led_controller, 0, led_iot_block[0], arguments)
                            set_led_status(1, 'nan', 100, 100, 0, 65535, led_controller, 1, led_iot_block[1], arguments)
                        elif(sender.data.scene_number == 2):
                            set_led_status(1, 'nan', 0, 100, 0, 65535, led_controller, 0, led_iot_block[0], arguments)
                            set_led_status(1, 'nan', 0, 100, 100, 65535, led_controller, 1, led_iot_block[1], arguments)
                        elif(sender.data.scene_number == 3):
                            set_led_status(1, 'nan', 0, 0, 100, 65535, led_controller, 0, led_iot_block[0], arguments)
                            set_led_status(1, 'nan', 100, 0, 255, 65535, led_controller, 1, led_iot_block[1], arguments)
                        elif(sender.data.scene_number == 4):
                            set_led_status(1, 'nan', 10, 200, 10, 65535, led_controller, 0, led_iot_block[0], arguments)
                            set_led_status(1, 'nan', 100, 100, 150, 65535, led_controller, 1, led_iot_block[1], arguments)
                        normalize_led_state(led_iot_block[0])
                        set_led_output(led_controller, 0, led_iot_block[0], arguments)
                        normalize_led_state(led_iot_block[1])
                        set_led_output(led_controller, 0, led_iot_block[1], arguments)

                    # Act on input
                    if arguments.color:
                        # Real LEDs available
                        #
                        # NOTE:
                        # nviLoadControl contains info about both brightness
                        # ('level') and color ('color'); color implies
                        # brightness in all color encodings used
                        # (RGB or CIE 1931); so we change brightness only
                        # if color stays the the same

                        # If the state is off turn everything off
                        if not new_state:
                            # Turn off the LED
                            print("led off")
                            set_rgb_color(0, 0, 0, led_controller, block_index, arguments)

                            # Send feedback
                            # 1:1 copy of the input is propagated
                            # leave the RGB and brightness output as they are
                            # led_iot_block[block_index].nvoLoadStatus.data = \
                            #    led_iot_block[block_index].nviLoadControl.data

                        # If any of the three color values changed compared to
                        # what's saved in the output datapoint
                        elif (new_red != old_red or new_green != old_green or
                              new_blue != old_blue):
                            # set the new color
                            set_rgb_color(new_red, new_green, new_blue, led_controller, block_index, arguments)

                            # New RGB values mean new brightness level
                            # so in the o/p dp we want to update it:
                            # translate this new RGB value to HLS space
                            hls_colors = colorsys.rgb_to_hls(new_red, new_green, new_blue)
                            # get the second value of the tuple (=brightness)
                            new_brightness = hls_colors[LUMINANCE]

                            # Send feedback: this will propagate twice!!
                            # led_iot_block[block_index].nvoLoadStatus.data = \
                            #    led_iot_block[block_index].nviLoadControl.data
                            # TODO: how to update a field of the output dp without
                            # propagating it to the network?
                            # led_iot_block[block_index].nvoLoadStatus.data.level = new_brightness

                            # now I should propagate!!!

                        elif new_brightness != old_brightness:
                            # The color is the same; change brightness only

                            # Make sure the new brightness is within boundaries
                            new_brightness = max(new_brightness, MIN_BRIGHTNESS_LEVEL)
                            new_brightness = min(new_brightness, MAX_BRIGHTNESS_LEVEL)

                            # Translate the old RGB value to HLS space
                            hls_colors = colorsys.rgb_to_hls(new_red, new_green, new_blue)

                            # Update brightness (=luminance=L) in HLS color space
                            # Luminance is the second member of the tuple
                            hls_colors[LUMINANCE] = new_brightness

                            # Reconvert new brightness to RGB color space
                            (new_red, new_green, new_blue) = \
                                colorsys.hls_to_rgb(
                                    old_red,
                                    old_green,
                                    old_blue)

                            # Set new brightness as RGB color
                            set_rgb_color(new_red, new_green, new_blue, led_controller, block_index, arguments)

                            # Send feedback
                            # led_iot_block[block_index].nvoLoadStatus.data = \
                            #    led_iot_block[block_index].nviLoadControl.data

                        # If everything is the same
                        else:
                            # Set the color
                            set_rgb_color(new_red, new_green, new_blue, led_controller, block_index, arguments)
                            # Send feedback
                            # led_iot_block[block_index].nvoLoadStatus.data = \
                            #    led_iot_block[block_index].nviLoadControl.data

                    print('LED {0} input is control {1}, state {2}, '
                          'level {3}, color {4}R : {5}G : {6}B'.format(i,
                                             sender.data.control,
                                             sender.data.state,
                                             sender.data.level,
                                             sender.data.color.color_value.RGB.red,
                                             sender.data.color.color_value.RGB.green,
                                             sender.data.color.color_value.RGB.blue))
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

                        # Check data point state field first
                        if led_legacy_block.nviValue.data.state == 1:
                            brightness = led_legacy_block.nviValue.data.value
                        else:
                            brightness = 0

                        # Set the new brightness
                        if arguments.color:
                            led_controller.set_channel_level(
                                RED_LED_PWM_CHANNEL, brightness)
                            led_controller.set_channel_level(
                                GREEN_LED_PWM_CHANNEL, brightness)
                            led_controller.set_channel_level(
                                BLUE_LED_PWM_CHANNEL, brightness)

                        elif arguments.piface:
                            led_controller.set_channel_level(0, brightness)

                        print("LED has now value {0}, state {1}".format(
                            led_legacy_block.nviValue.data.value,
                            led_legacy_block.nviValue.data.state))

                    # Propagate feedback even if no real LED is present
                    led_legacy_block.nvoValue.data = \
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
    if arguments.sensor != 'none':
        def on_remote_pressure_update(sender, event_data):
            # Simply propagate the new pressure value ???
            # TODO: double check with Rich
            pressure_sensor_block.nvoValue.data = \
                pressure_sensor_block.nviValueFb.data
        # Set the on update handler for the nviValue input
        pressure_sensor_block.nviValueFb.OnUpdate += \
            on_remote_pressure_update

    #
    # ISI Assembly objects
    #
    if not arguments.standalone:
        led_assembly = pylon.device.isi.Assembly(
            assembly=(
                (led_iot_block[0].nviLoadControl,
                 led_iot_block[0].nvoLoadStatus)),
            enrollment=pylon.device.isi.Enrollment(
                direction=pylon.device.isi.IsiDirection.VARIOUS,
                type_id=led_iot_block[0].nviLoadControl))

        if arguments.sensor != 'none':
            # Assembly for the local sensor pressure (output)
            # TODO: make one assembly per sensor with VARIOUS direction
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

    #
    #   ISI user interface event handler
    #
    # noinspection PyUnusedLocal
    def on_user_interface(sender, argument):
        parameter = argument.parameter
        # category = pylon.device.isi.IsiEvent.category[argument.event_code]

        if argument.event_code == pylon.device.isi.IsiEvent.WARM:
            if not arguments.standalone:
                print("auto enroll sent")
                app.isi.initiate_auto_enrollment(led_assembly)
    # Event handler registration
    app.isi.OnUserInterface += on_user_interface

    #
    # Startup
    #
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

    #
    # Main loop
    #
    try:
        # To exit mail loop
        done = False
        # Dimming direction when using pressure sensor
        dimming_down = False
        # New color values
        new_red = 0
        new_blue = 0
        new_green = 0

        while not done:
            # Service the IoT stack
            app.service()

            # Test for and process interactive user input
            if kbhit(0.005):
                done = menu(app, led_controller, led_iot_block, led_controller)

            # Process pressure sensor input if the sensor is enabled
            # TODO: move to a separate thread
            elif arguments.sensor == 'single':
                try:
                    # Read pressure from the local sensor and from the net 
                    # whichever is higher
                    # Note: more pressure == smaller value
                    pressure = get_pressure(pressure_sensor, pressure_sensor_block)
                except Exception as e:
                    print('Cannot read pressure sensor (not running as root?)')
                    print('Error: {0}'.format(e))

                # Print to console if the sensor is being pushed
                # if pressure < PRESSURE_DIMMING_THRESHOLD:
                #     print("Pressure is: " + str(pressure))
                #     show_prompt()

                # If pressure is high enough and there is a dimmable led
                if (pressure < PRESSURE_DIMMING_THRESHOLD and
                    arguments.color):
                    # For each detected LED do the dimming
                    for i in range(MAX_LEDs):
                        # If we detected LED i
                        if led_controller.detected_led[i]:
                            # For shorter name
                            load_status = led_iot_block[i].nvoLoadStatus

                            # Read latest RGB color (which implies brightness)
                            old_red = \
                                load_status.data.color.color_value.RGB.red
                            old_green = \
                                load_status.data.color.color_value.RGB.green
                            old_blue = \
                                load_status.data.color.color_value.RGB.blue

                            # Get brightness of latest RGB values from HLS space
                            hls_colors = colorsys.rgb_to_hls(old_red, 
                                                             old_green, 
                                                             old_blue)
                            new_brightness = hls_colors[LUMINANCE]

                            # Cycle LED brightness until user presses the sensor
                            # TODO: make dimming proportional to pressure level
                            while pressure < PRESSURE_DIMMING_THRESHOLD:
                                # Service the IoT stack
                                app.service()

                                # Update pressure block on delta
                                old_pressure = pressure
                                pressure = get_pressure(pressure_sensor, 
                                                        pressure_sensor_block)
                                # Send on delta
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

                                else:
                                    # IoT mode with real LEDs;
                                    # start changing brightness up or down
                                    if dimming_down:
                                        # Dim down
                                        new_brightness = max(
                                            MIN_BRIGHTNESS_LEVEL,
                                            new_brightness - DIMMING_STEP)
                                        # Until brightness is minimum
                                        if new_brightness == \
                                            MIN_BRIGHTNESS_LEVEL:
                                            dimming_down = False
                                    else:
                                        # Dim up
                                        new_brightness = min(
                                            MAX_BRIGHTNESS_LEVEL,
                                            new_brightness + DIMMING_STEP)
                                        # Until brightness is max
                                        if new_brightness == \
                                            MAX_BRIGHTNESS_LEVEL:
                                            dimming_down = True

                                    # Reconvert HLS with new brightness to RGB
                                    (new_red, new_green, new_blue) = \
                                        colorsys.hls_to_rgb(
                                            hls_colors[HUE],
                                            new_brightness,
                                            hls_colors[SATURATION])

                                    # Set new brightness as RGB color
                                    set_rgb_color(new_red, new_green, new_blue, led_controller, i, arguments)

                            # Update output LED functional block
                            load_status.data.level = \
                                new_brightness
                            load_status.data.color.color_value.RGB.red = \
                                new_red
                            load_status.data.color.color_value.RGB.green = \
                                new_green
                            load_status.data.color.color_value.RGB.blue = \
                                new_blue

                            # Next time we dim the other direction
                            dimming_down = not dimming_down
                        else:
                            # Nothing
                            pass
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

def set_led_status(state, level, red, green, blue, scene_number, led_obj, 
                   led_index, led_block, arguments):
    """ Set the state, level, and color for an LED. """
    led_block.nvoLoadStatus.data.state = state
    led_block.nvoLoadStatus.data.scene_number = scene_number
    if state:
        led_block.nvoLoadStatus.data.level = level
        led_block.nvoLoadStatus.data.color.color_value.RGB.red = red
        led_block.nvoLoadStatus.data.color.color_value.RGB.green = green
        led_block.nvoLoadStatus.data.color.color_value.RGB.blue = blue
    normalize_led_state(led_block)
    set_led_output(led_obj, led_index, led_block, arguments)

def normalize_led_state(led_block):
    """ Normalize the state, level, and color for an LED block so that they are
    consistent with each other when the state is on.  No changes are made if the
    state is off. """
    led_block.nvoLoadStatus.data.control = load_control.load_control_t.LOAD_REPORT
    if led_block.nvoLoadStatus.data.state:
        # State is on; get the color and check the level
        red_coordinate = float(led_block.nvoLoadStatus.data.color.color_value.RGB.red) / 255.
        blue_coordinate = float(led_block.nvoLoadStatus.data.color.color_value.RGB.blue) / 255.
        green_coordinate = float(led_block.nvoLoadStatus.data.color.color_value.RGB.green) / 255.
        lightness_coordinate = led_block.nvoLoadStatus.data.level / 100.
        is_black = True if red_coordinate + blue_coordinate + green_coordinate > 0. else False
        if lightness_coordinate == 'nan':
            # Level not specified; check the color
            if is_black:
                # Color is black; set to white and set level to 100%
                led_block.nvoLoadStatus.data.color.encoding = color_encoding.color_encoding_t.COLOR_RGB
                led_block.nvoLoadStatus.data.color.color_value.RGB.red = 255
                led_block.nvoLoadStatus.data.color.color_value.RGB.green = 255
                led_block.nvoLoadStatus.data.color.color_value.RGB.blue = 255
                led_block.nvoLoadStatus.data.level = 100.
            else:
                # Color specified; set the level from the color
                hls_color = colorsys.rgb_to_hls(red_coordinate, green_coordinate, blue_coordinate)
                led_block.nvoLoadStatus.data.level = hls_color[LUMINANCE] * 100.
        else:
            # Level specified; check the color
            if is_black:
                # Color is black; set to white then adjust the level
                red_coordinate = 1.
                green_coordinate = 1.
                blue_coordinate = 1.
            # Level and color specified; adjust color to match the level
            hls_color = colorsys.rgb_to_hls(red_coordinate, green_coordinate, blue_coordinate)
            adjusted_rgb = colorsys.hls_to_rgb(hls_color[HUE], lightness_coordinate, hls_color[SATURATION])
            led_block.nvoLoadStatus.data.color.encoding = color_encoding.color_encoding_t.COLOR_RGB
            led_block.nvoLoadStatus.data.color.color_value.RGB.red = int(adjusted_rgb[RED] * 255.)
            led_block.nvoLoadStatus.data.color.color_value.RGB.green = int(adjusted_rgb[GREEN] * 255.)
            led_block.nvoLoadStatus.data.color.color_value.RGB.blue = int(adjusted_rgb[BLUE] * 255.)

def set_led_output(led_obj, led_index, led_block, arguments):
    """ Set the state for an LED channel based on the nvoLoadStatus settings.
    Call normalize_led_state() first to normalize the settings. """
    if led_block.nvoLoadStatus.data.state:
        # State is on; set color
        set_rgb_color(
            led_block.nvoLoadStatus.data.color.color_value.RGB.red,
            led_block.nvoLoadStatus.data.color.color_value.RGB.green,
            led_block.nvoLoadStatus.data.color.color_value.RGB.blue,
            led_obj, led_index, arguments)
    else:
        # State is off; set black
        set_rgb_color(0, 0 , 0, led_obj, led_index, arguments)

def get_pressure(this_pressure_sensor, this_pressure_sensor_block):
    """ Read pressure both from the local sensor and the net
    NOTE: more pressure ==>> lower read value """
    local_pressure = this_pressure_sensor.read_pressure()
    remote_pressure = this_pressure_sensor_block.nviValueFb.data
    
    # If remote pressure is zero (e.g. when the dp in uninitialised) 
    # use the local pressure value
    if remote_pressure == 0:
        return local_pressure
    # else, use whichever pressure is higher (=lower reading value)
    else:
        return min(local_pressure, remote_pressure)

def this_pi_ip_addr():
    """ Returns the IP address of this computer.
        Require AVAHID installed (apt-get install avahid) which should
        be installed by default in Raspbian as of summer 2013 """
    try:
        # Get text hostname of the local machine
        host = socket.gethostname()

        # Get the numeric IP address from the hostname;
        # this might require avahid
        pi_ip_address = socket.gethostbyname(host + '.local')
        print('Host ' + host + ' has IP address ' + pi_ip_address)

        return pi_ip_address

    except Exception as e:
        print("Can't get IP address")
        print(e)
        # pass the same exception up
        raise

def show_prompt():
    """ Show a prompt for user input """

    # Go to beginning of line, print the prompt
    sys.stdout.write("\r> ")
    # Stay on this line
    sys.stdout.flush()


def set_rgb_color(r, g, b, led_obj, led_index, arguments):
    """ Set RGB 0-255 values for the specified LED """

    # If there are color LEDs, set each color
    if arguments.color:
        led_obj.set_channel_level(
            RED_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
            r)
        led_obj.set_channel_level(
            GREEN_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
            g)
        led_obj.set_channel_level(
            BLUE_LED_PWM_CHANNEL + (led_index * LED_OFFSET),
            b)
    # If there are the PiFace LEDs, set the whole LED
    elif arguments.piface:
        led_obj.set_channel_level(led_index, r or g or b)

def kbhit(timeout):
    """
    Similar to kbhit() on Windows platforms. This implementation will not
    work on Windows platforms. On Windows, use kbhit() from the MSCRT
    instead; see the standard Python module 'msvcrt' for more on
    http://docs.python.org/3.3/library/msvcrt.html

    To support multiple platforms use sys.platform to determine the
    platform and automatically do the right thing.  This function returns
    true if input is waiting on the console, and stops waiting for input
    when the timeout expires.
    """
    i, o, e = select.select([sys.stdin], [], [], timeout)
    return len(i)


#	Utilities for reading input from the console and executing
#	commands. Just type a command and hit Enter.
def menu(app, led_obj, led_block, led_controller):
    """
    Function to acquire commands from the console, and execute them.
    The call is blocking.
    :param led_obj:
    :param led_block:
    """
    # noinspection PyUnusedLocal
    def menu_cancel(args):
        app.isi.cancel_enrollment()
        return False

    # noinspection PyUnusedLocal
    def menu_color(args):
        """ Set the LED color.  The LED is selected with the argument.
        When no argument is given, set the color for all LEDs. """
        if len(args[1]):
            # Set LED color for the selected channel
            start_index = int(args[1])
            stop_index = start_index + 1
        else:
            # Set the LED color for all LEDs
            start_index = 0
            stop_index = len(led_block)
        rgb_color = 0xFFFFFF if len(args[0]) else int(args[0])
        for led_index in range(start_index, stop_index):
            led_block[led_index].nvoLoadStatus.data.color.color_value.RGB.red \
                = rgb_color >> 8 & 0xFF
            led_block[led_index].nvoLoadStatus.data.color.color_value.RGB.green \
                = rgb_color >> 4 & 0xFF
            led_block[led_index].nvoLoadStatus.data.color.color_value.RGB.blue \
                = rgb_color & 0xFF
            normalize_led_state(led_block[led_index])
            set_led_output(led_obj, led_index, led_block[led_index], led_controller)
        return False

    # noinspection PyUnusedLocal
    def menu_create(args):
        app.isi.create_enrollment(int(args[0]))
        return False

    # noinspection PyUnusedLocal
    def menu_eval(args):
        """ Evaluate Python expressions within a running program.
        For example, type 'eval print(1234)' to print this number on the
        console. You can interface with the pylon Application class using
        the global variable 'app' defined above, and you can use the
        pseudo-protected app._lts to reach the stack adapter class in this
        manner. """
        try:
            eval(args)
        finally:
            return False    # Return True to terminate script.

    # noinspection PyUnusedLocal
    def menu_exit(args):
        return True

    # noinspection PyUnusedLocal
    def menu_extend(args):
        app.isi.extend_enrollment(int(args))
        print('Enrollment extended')
        return False

    # noinspection PyUnusedLocal
    def menu_help(args):
        """ Show the available commands """
        if not len(args):
            for k in items:
                print('{0:12}\t{1}'.format(k, items[k][1]))
        else:
            if args in items:
                print('{0:12}\t{1}'.format(args, items[args][1]))
            else:
                print('No such command: {0}'.format(args))
        return False

    # noinspection PyUnusedLocal
    def menu_isconnected(args):
        print('Assembly {0} is {1}connected'.format(
            args,
            '' if app.isi.is_connected(int(args)) else 'not '
        ))
        return False

    # noinspection PyUnusedLocal
    def menu_leave(args):
        app.isi.leave_enrollment(int(args))
        return False

    # noinspection PyUnusedLocal
    def menu_list_datapoints(args):
        """ List all the datapoints name and index available in each block """
        for dp in app.datapoints:
            print('%s Datapoint %s Index %s' % (str(dp.block).ljust(20), str(dp.name.decode('utf-8')).ljust(20), dp.index))

        return False

    # noinspection PyUnusedLocal
    def menu_off(args):
        """ Set the LED state to off.  The LED is selected with the argument.
        When no argument is given, set all LED states to off. """
        if len(args):
            # Turn LED for the selected channel off
            start_index = int(args)
            stop_index = start_index + 1
        else:
            # Turn all LEDs off
            start_index = 0
            stop_index = len(led_block)
        for led_index in range(start_index, stop_index):
            led_block[led_index].nvoLoadStatus.data.state = 0
            normalize_led_state(led_block[led_index])
            set_led_output(led_obj, led_index, led_block[led_index], led_controller)
        return False

    # noinspection PyUnusedLocal
    def menu_on(args):
        """ Set the LED state to on.  The LED is selected with the argument.
        When no argument is given, set all LED states to on. """
        if len(args):
            # Turn LED for the selected channel on
            start_index = int(args)
            stop_index = start_index + 1
        else:
            # Turn all LEDs on
            start_index = 0
            stop_index = len(led_block)
        for led_index in range(start_index, stop_index):
            led_block[led_index].nvoLoadStatus.data.state = 1
            normalize_led_state(led_block[led_index])
            set_led_output(led_obj, led_index, led_block[led_index], led_controller)
        return False

    # noinspection PyUnusedLocal
    def menu_open(args):
        app.isi.open_enrollment(int(args))
        print('Enrollment opened')
        return False

    # noinspection PyUnusedLocal
    def menu_service(args):
        """ Send a service message and an ISI DRUM message """
        app.send_service_message()
        app.isi.send_drum()
        print('Service and DRUM messages sent')
        show_prompt()
        return False

    # noinspection PyUnusedLocal
    def menu_wink(args):
        """ Simulate receipt of a Wink message for testing purposes """
        app.OnWink.fire(app, None)
        print('Wink message sent')
        show_prompt()
        return False

    #
    #	Menu items dictionary: command -> (handler function, comment)
    #	Handler functions return True to exit the program.
    items = {
        'cancel':  (menu_cancel,   '             Cancel the pending enrollment'),
        'color':   (menu_color,    'color, chan  Set specified LED channel color; or all if none specified'),
        'create':  (menu_create,   'id           Create an enrollment'),
        'eval':    (menu_eval, 	   'stmts        Evaluate a Python statement'),
        'exit':    (menu_exit, 	   '             Exit the script'),
        'extend':  (menu_extend,   'id           Extend an enrollment'),
        'is_connected': (menu_isconnected,
                                   'id           Whether assembly ID is connected'),
        'help':    (menu_help, 	   '             Display this help'),
        'list':    (menu_list_datapoints,
                                   '             List all the datapoints name and index'),
        'leave':   (menu_leave,    'id           Leave an existing enrollment'),
        'off':     (menu_off,      'chan         Turn off selected LED channel or all LEDs if none specified'),
        'on':      (menu_on,       'chan         Turn on selected LED channel or all LEDs if none specified'),
        'open':    (menu_open,     'id           Open enrollment'),
        'service': (menu_service,  '             Send service and DRUM messages'),
        'wink':    (menu_wink,
                                   '      Simulate receipt of a Wink message')
    }

    result = False

    try:
        cmd = sys.stdin.readline().strip().split()
        if len(cmd) > 0:
            command = cmd[0].lower()
            if command in items:
                result = items[command][0](' '.join(cmd[1:]))
            else:
                print('Not a valid command. Try \'help\'')
                show_prompt()
    except Exception as e:
        print(e)
    return result

if __name__ == '__main__':
    main()





