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

#
# Imports
#
# Import standard Python modules
import argparse
import logging
import math
# import time
import select
import socket
import sys
import colorsys
from collections import namedtuple

# import pdb

# sys.path.append('/usr/local/lib/python3.2/dist-packages')

# Import Pilon
import pylon.device

# IoT datapoint types used by this application
import pylon.resources.datapoints.count
import pylon.resources.datapoints.switch
import pylon.resources.enumerations.color_encoding_t as ColorEncoding
import pylon.resources.enumerations.load_control_t as LoadControl
import pylon.resources.datapoints.iot_load_control

# IoT profiles used by this application
import pylon.resources.profiles.iotAnalogInput
import pylon.resources.profiles.iotLoad
import pylon.resources.profiles.closedLoopSensor

# I/O drivers
from pylon.examples.common.fsr_driver.pressure_sensor import PressureSensor
from pylon.examples.common.led_driver.pwm_led_set2 import LedStripDriver
from pylon.examples.common.led_driver.pwm_led_set2 import RGBLed

#from pylon.examples.common.led_driver.piface_led_set import PiFaceLed

# Constants
MAX_PRESSURE_SENSORS = 4                # Number of hw pressure sensors
PRESSURE_SENSOR_PINS = [18, 23, 24, 25] # Pin number for each sensor
PRESSURE_DIMMING_THRESHOLD = 1000       # Pressure reading below which we cycle
                                        # LED brightness
PRESSURE_VALUE_DELTA = 50               # Pressure send on delta

PWM_BOARD_I2C_ADDRESS = 0x40            # Used by the LED object
PWM_FREQ = 1000                         # In Hz, used by the LED object
RED_LED_PWM_CHANNEL = 0                 # Used by the LED object
GREEN_LED_PWM_CHANNEL = 1               # Used by the LED object
BLUE_LED_PWM_CHANNEL = 2                # Used by the LED object
LED_OFFSET = 3                          # Used by the LED object
MAX_LEDs = 2                            # Number of hw LEDs supported

MIN_BRIGHTNESS_LEVEL = 0
MAX_BRIGHTNESS_LEVEL = 255
MIN_LUMINANCE_LEVEL = 0                 # Used in HLS color space
MAX_LUMINANCE_LEVEL = 255               # Used in HLS color space
MIN_HUE_LEVEL = 0
MAX_HUE_LEVEL = 255
MIN_SATURATION_LEVEL = 0
MAX_SATURATION_LEVEL = 255
MIN_RED_LEVEL = 0
MAX_RED_LEVEL = 255
MIN_GREEN_LEVEL = 0
MAX_GREEN_LEVEL = 255
MIN_BLUE_LEVEL = 0
MAX_BLUE_LEVEL = 255
DIMMING_STEP = 3                        # Step value when dimming up or down
HUE = 0                                 # Index for hue coordinate in HLS tuple
LUMINANCE = 1                           # Index for luminance coordinate in HLS tuple
SATURATION = 2                          # Index for saturation coordinate in HLS tuple
RED = 0                                 # Index for red coordinate in RGB tuple
GREEN = 1                               # Index for green coordinate in RGB tuple
BLUE = 2                                # Index for blue coordinate in RGB tuple
RGB_TYPE = ColorEncoding.color_encoding_t.COLOR_RGB
                                        # RGB color type



#
# Main function
#
def main():
    """ The script's main function
    """

    # Define properties for objects
    pressure_sensors = []
    Sensor = namedtuple('Sensor', ['sensor', 'block', 'is_enabled'])
    leds = []
    Led = namedtuple('Led', ['led', 'block', 'is_enabled'])

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
        default=True,
        action='store_true',
        help='Enable RGB LED hardware')
    parser.add_argument(
        '-C', '--pycharm',
        default=False,
        action='store_true',
        help='Enable debugging with PyCharm')
    try:
        # Try getting ip address via zeroconf/bonjour/avahi
        ip_address = this_pi_ip_addr()

        # Add argument with default if no exceptions
        parser.add_argument(
            '-d', '--device',
            default='mc://' + ip_address + ':1628/',
            help='The device URI, e.g. mc://10.0.1.12:1628/')
    except Exception as e:
        # Cannot find IP address automatically; add argument with no default
        parser.add_argument(
            '-d', '--device',
            required=True,
            help='The device URI, e.g. mc://10.0.1.12:1628/ \n'
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
        '-N', '--scenes',
        default=8,
        action='store_true',
        help='Set the number of scenes available in the device')
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
        help='Enable pressure sensor hardware: "none" for no sensors,'
             ' "single" for one sensor for all LEDs,'
             ' "multi" for one sensor per LEDs')
    parser.add_argument(
        '-S', '--standalone',
        default=False,
        action='store_true',
        help='Enable ISI standalone mode (disable ISI connections)')
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
    # Initialize the Pilon app
    #

    # Enable/disable test mode
    pylon.device.stack.test_mode = arguments.test

    # Create and configure the Pilon application object
    app = pylon.device.application.Application(
        #use_isi=True,
        use_isi=False,
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR)

    # Create the stack logger
    logger = logging.getLogger('pylon-rtk.led')

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
    def on_service_led(sender, event_data):
        logger.info('Processing service LED status event')
        print('Service LED status changed to {0}.'.format(arguments.state))
        show_prompt()
    app.OnServiceLed += on_service_led

    # noinspection PyUnusedLocal
    def on_wink(sender, event_data):
        logger.info('Received wink message')
        print('Wink!')
        show_prompt()
    app.OnWink += on_wink

    # noinspection PyUnusedLocal
    def on_online(sender, event_data):
        logger.info('Received Online event')
        print('We are now online!')
        show_prompt()
    app.OnOnline += on_online

    # noinspection PyUnusedLocal
    def on_offline(sender, event_data):
        logger.info('Received Offline event')
        print('We are now offline.')
        show_prompt()
    app.OnOffline += on_offline


    #
    # Initialize pressure sensors
    #

    # Check how many sensors are needed
    if arguments.sensor == 'single':
        # One pressure sensor for all LEDs
        total_pressure_sensors = 1
    elif arguments.sensor == 'multi':
        # One pressure sensor for each RGB LED
        total_pressure_sensors = MAX_PRESSURE_SENSORS
    else:
        # No sensors at all
        total_pressure_sensors = 0

    # Create the required sensors
    for i in range(total_pressure_sensors):

        # Add a sensor object to the list
        pressure_sensors.append(Sensor)

        # Add the hw pressure sensor
        try:
            pressure_sensors[i].sensor = PressureSensor(PRESSURE_SENSOR_PINS[i],
                                                        arguments.debug)
        except Exception as e:
            print('Cannot find pressure sensor number ' + str(i))
            print(e)
            # Disable pressure sensor
            pressure_sensors[i].is_enabled = False

        # Create the pressure sensor blocks
        pressure_sensors[i].block = app.block(
            profile=pylon.resources.profiles.closedLoopSensor.closedLoopSensor(),
            ext_name='FPpressureSensor{0}'.format(i),
            xxx=pylon.resources.datapoints.count.count)

        # Give each block a size and index for later referencing
        pressure_sensors[i].block.array_size = total_pressure_sensors
        pressure_sensors[i].block.array_index = i

        # enable the sensor
        pressure_sensors[i].is_enabled = True

    # Update handlers for remote pressure sensor change
    def on_pressure_nvi_value_fb_update(sender, event_data):
        # TODO: double check with Rich
        # Simply propagate the new pressure value
        pressure_sensors[sender.block.array_index].block.nvoValue.data = \
            sender.data
    for i in range(len(pressure_sensors)):
        pressure_sensors[i].block.nviValueFb.OnUpdate += \
            on_pressure_nvi_value_fb_update


    #
    # Initialize LEDs
    #

    # Create the LED objects
    if not arguments.legacy and (arguments.color or arguments.piface):
        for i in range(MAX_LEDs):

            # Add an led object to the list
            leds.append(Led)

            # Add the hw LED
            if arguments.color:
                try:
                    leds[i] = RGBLed(i, arguments.debug)
                    # Detect which LEDs are actually present
                    if True:  # TODO: actually detect it
                        leds[i].is_enabled = True
                    else:
                        leds[i].is_enabled = False
                except Exception as e:
                    print('Cannot find the LED light controller.')
                    print(e)
                    # Disable color LED and sensor
                    arguments.color = False
                    arguments.sensor = 'none'
            elif arguments.piface:
                try:
                    leds[i] = PiFaceLed(arguments.debug)
                except Exception as e:
                    print('Cannot find the PiFace board')
                    print(e)
                    # Disable PiFace and sensor
                    arguments.piface = False
                    arguments.sensor = 'none'

            # Add the LED block
            leds[i].block = app.block(
                    profile=pylon.resources.profiles.iotLoad.iotLoad(),
                    ext_name='ColorLamp{0}'.format(i),
                    # specify the number of scenes I want to save. Default is 2
                    array_desc={'cpScene': arguments.scenes})

        # Give each block of the LED list a size and index for later referencing
        for block_index in range(len(leds)):
            leds[block_index].block.array_size = len(leds)
            leds[block_index].block.array_index = block_index

    # Other IoT mode blocks
    if not arguments.legacy:

        # Create the power monitor blocks as tuples of IoT Analog Input blocks,
        # one for each physical LED
        power_monitor_iot_blocks = tuple(
            app.block(
                profile=pylon.resources.profiles.iotAnalogInput.iotAnalogInput(),
                ext_name='LampPowerMonitor{0}'.format(i))
            for i in range(MAX_LEDs))
        # Give each member of the tuple a size and index for later referencing
        for block_index in range(len(power_monitor_iot_blocks)):
            power_monitor_iot_blocks[block_index].array_size = \
                len(power_monitor_iot_blocks)
            power_monitor_iot_blocks[block_index].array_index = block_index

        # Create the energy monitor blocks as tuples of IoT Analog Input blocks,
        # one for each physical LED
        energy_monitor_iot_blocks = tuple(
            app.block(
                profile=pylon.resources.profiles.iotAnalogInput.iotAnalogInput(),
                ext_name='LampEnergyMonitor{0}'.format(i))
            for i in range(MAX_LEDs))
        # Give each member of the tuple a size and index for later referencing
        for block_index in range(len(energy_monitor_iot_blocks)):
            energy_monitor_iot_blocks[block_index].array_size = \
                len(energy_monitor_iot_blocks)
            energy_monitor_iot_blocks[block_index].array_index = block_index

    # Legacy mode blocks
    else:
        # Create functional blocks based on simple legacy profiles
        # Use our RGB LED as a standard white light
        led_legacy_block = app.block(
            profile=pylon.resources.profiles.closedLoopSensor.closedLoopSensor(),
            ext_name='FPWhiteLedLight',
            xxx=pylon.resources.datapoints.switch)

    #
    # Input datapoint update event handlers
    #
    # Define the on update handler for the IoT Load Control nviLoadControl input
    if not arguments.legacy:
        # noinspection PyUnusedLocal
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
                    # Get the index of the block to access the correct element
                    # of the tuple of blocks
                    sender_block_index = sender.block.array_index

                    if sender.data.control == LoadControl.load_control_t.LOAD_SET:
                        # Set the LED state, level, and color to the specified values
                        set_led_status(sender.data.state, sender.data.level, sender.data.color.encoding,
                                       sender.data.color.color_value.RGB.red, sender.data.color.color_value.RGB.green,
                                       sender.data.color.color_value.RGB.blue, sender.data.scene_number, leds,
                                       sender_block_index, leds[sender_block_index].block, arguments)
                    elif sender.data.control == LoadControl.load_control_t.LOAD_RECALL_SCENE:

                        # recall an existing scene
                        if sender.data.scene_number < arguments.scenes:
                            scene = leds[sender_block_index].block.cpScene[sender.data.scene_number]
                            set_led_status(
                                scene.state,
                                scene.level,
                                RGB_TYPE,
                                scene.color.color_value.RGB.red,
                                scene.color.color_value.RGB.green,
                                scene.color.color_value.RGB.blue,
                                sender.data.scene_number,
                                leds,
                                sender_block_index,
                                leds[sender_block_index].block,
                                arguments)

                        # or recall hard-coded scenes instead
                        if sender.data.state == arguments.scenes:
                            set_led_status(0, float('nan'), RGB_TYPE, 255, 255, 255, 65535, leds, 0,
                                           leds[0], arguments)
                            set_led_status(0, float('nan'), RGB_TYPE, 255, 255, 255, 65535, leds, 1,
                                           leds[1], arguments)
                        elif sender.data.scene_number == arguments.scenes + 1:
                            set_led_status(1, float('nan'), RGB_TYPE, 100, 0, 0, 65535, leds, 0,
                                           leds[0], arguments)
                            set_led_status(1, float('nan'), RGB_TYPE, 100, 100, 0, 65535, leds, 1,
                                           leds[1], arguments)
                        elif sender.data.scene_number == arguments.scenes + 2:
                            set_led_status(1, float('nan'), RGB_TYPE, 0, 100, 0, 65535, leds, 0,
                                           leds[0], arguments)
                            set_led_status(1, float('nan'), RGB_TYPE, 0, 100, 100, 65535, leds, 1,
                                           leds[1], arguments)
                        elif sender.data.scene_number == arguments.scenes + 3:
                            set_led_status(1, float('nan'), RGB_TYPE, 0, 0, 100, 65535, leds, 0,
                                           leds[0], arguments)
                            set_led_status(1, float('nan'), RGB_TYPE, 100, 0, 255, 65535, leds, 1,
                                           leds[1], arguments)
                        elif sender.data.scene_number == arguments.scenes + 4:
                            set_led_status(1, float('nan'), RGB_TYPE, 10, 200, 10, 65535, leds, 0,
                                           leds[0], arguments)
                            set_led_status(1, float('nan'), RGB_TYPE, 100, 100, 150, 65535, leds, 1,
                                           leds[1], arguments)

                    elif sender.data.control == LoadControl.load_control_t.LOAD_INCREMENT:
                        # increment the current level by adding the new input level
                        set_led_status(sender.data.state,
                                       max(MIN_LUMINANCE_LEVEL,
                                           min(MAX_LUMINANCE_LEVEL,
                                               leds[sender_block_index].block.nvoLoadStatus.data.level +
                                                   sender.data.level)),
                                       sender.data.color.encoding,
                                       sender.data.color.color_value.RGB.red,
                                       sender.data.color.color_value.RGB.green,
                                       sender.data.color.color_value.RGB.blue,
                                       sender.data.scene_number,
                                       leds,
                                       sender_block_index,
                                       leds[sender_block_index].block,
                                       arguments)
                    elif sender.data.control == LoadControl.load_control_t.LOAD_INCREMENT_HUE:
                        # convert to HLS
                        hls_color = colorsys.rgb_to_hls(
                            leds[sender_block_index].block.nvoLoadStatus.data.color.color_value.RGB.red,
                            leds[sender_block_index].block.nvoLoadStatus.data.color.color_value.RGB.green,
                            leds[sender_block_index].block.nvoLoadStatus.data.color.color_value.RGB.blue)
                        # Increase hue and make sure it's within boundaries
                        adjusted_rgb = colorsys.hls_to_rgb(
                            max(MIN_HUE_LEVEL,
                                min(MAX_HUE_LEVEL,
                                    hls_color[HUE]+sender.data.level)),
                            hls_color[LUMINANCE],
                            hls_color[SATURATION])
                        # Update led
                        set_led_status(sender.data.state,
                                       sender.data.level,
                                       sender.data.color.encoding,
                                       adjusted_rgb[RED],
                                       adjusted_rgb[GREEN],
                                       adjusted_rgb[BLUE],
                                       sender.data.scene_number,
                                       leds,
                                       sender_block_index,
                                       leds[sender_block_index].block,
                                       arguments)
                    # extract required values from input dp, and save them in the specified scene
                    elif sender.data.control == LoadControl.load_control_t.LOAD_STORE_SCENE:
                        if sender.data.scene_number < arguments.scenes:
                            # if the specified scene number is within boundaries
                            define_scene_from_load_dp(
                                leds[sender_block_index].block.cpScene[sender.data.scene_number],
                                sender)

                    # save snapshot of current status into the specified scene
                    elif sender.data.control == LoadControl.load_control_t.LOAD_LEARN_SCENE:
                        if sender.data.scene_number < arguments.scenes:
                            # if the specified scene number is within boundaries
                            define_scene_from_load_dp(
                                leds[sender_block_index].block.cpScene[sender.data.scene_number],
                                leds[sender_block_index].block.nvoLoadStatus)

                    print('LED {0} input is control {1}, state {2}, '
                          'level {3}, color {4}R : {5}G : {6}B, scene {7}'.format(
                               sender_block_index, sender.data.control, sender.data.state, sender.data.level,
                               sender.data.color.color_value.RGB.red, sender.data.color.color_value.RGB.green,
                               sender.data.color.color_value.RGB.blue, sender.data.scene_number))
            except Exception as rgb_exception:
                print('Something just went wrong when updating RGB values '
                      'in on_led_nvi_load_control_update({0}):'
                      '{1}'.format(sender, rgb_exception))
            finally:
                show_prompt()
        # Create the on update handler for the nviValue input
        for i in range(MAX_LEDs):
            led_iot_blocks[i].nviLoadControl.OnUpdate += \
                on_led_nvi_load_control_update

    # Define the on update handler for the Actuator nviValue input
    if arguments.legacy:
        # noinspection PyUnusedLocal
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
                            leds[0].set_led_status(
                                RED_LED_PWM_CHANNEL, brightness)
                            leds[0].set_channel_level(
                                GREEN_LED_PWM_CHANNEL, brightness)
                            leds[0].set_channel_level(
                                BLUE_LED_PWM_CHANNEL, brightness)

                        elif arguments.piface:
                            leds.set_channel_level(0, brightness)

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


    #
    # ISI Assembly objects
    #
    if app.isi and not arguments.standalone:
        led_assembly = pylon.device.isi.Assembly(
            assembly=(
                (leds[0].nviLoadControl,
                 leds[0].nvoLoadStatus)),
            enrollment=pylon.device.isi.Enrollment(
                direction=pylon.device.isi.IsiDirection.VARIOUS,
                type_id=leds[0].nviLoadControl))

        if arguments.sensor != 'none':
            # Assembly for the local sensor
            pressure_sensor_output_assembly = pylon.device.isi.Assembly(
                assembly=(
                    (pressure_sensors[0].block.nviValueFb,
                     pressure_sensors[0].block.nvoValue)),
                enrollment=pylon.device.isi.Enrollment(
                    direction=pylon.device.isi.IsiDirection.VARIOUS,
                    type_id=pressure_sensors[0].block.nviValueFb))

    #
    #   ISI user interface event handler
    #
    # noinspection PyUnusedLocal
    if app.isi:
        def on_user_interface(sender, argument):
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

    # Start the Pilon application
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
    if arguments.color:
        print('Color LED hardware enabled.')
    elif arguments.piface:
        print('PiFace hardware enabled.')
    else:
        print('*** DISABLED *** Color LED and PiFace hardware')
    if arguments.sensor != 'none':
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
          'Enter "help" for a list of commands')
    show_prompt()

    #
    # Main loop
    #
    try:
        # To exit main loop
        done = False
        # Dimming direction when using pressure sensor
        dimming_down = False

        while not done:
            # Service the IoT stack
            app.service()

            # Test for and process interactive user input
            if kbhit(0.005):
                done = menu(app, leds, led_iot_blocks, arguments)

            # Process pressure sensor input if the sensor is enabled
            # TODO: move to a separate thread
            elif arguments.sensor == 'single':
                try:
                    # Read pressure from the local sensor and from the net whichever is higher
                    # Note: more pressure == smaller value
                    pressure = get_pressure(pressure_sensors[0].sensor,
                                            pressure_sensors[0].block)
                except Exception as e:
                    print('Cannot read pressure sensor (not running as root?)')
                    print('Error: {0}'.format(e))

                # Print to console if the sensor is being pushed
                # if pressure < PRESSURE_DIMMING_THRESHOLD:
                #     print("Pressure is: " + str(pressure))
                #     show_prompt()

                # If pressure is high enough and there are dimmable leds
                if pressure < PRESSURE_DIMMING_THRESHOLD and arguments.color:

                    # Next time we dim the other direction
                    dimming_down = not dimming_down

                    # Cycle LED brightness until user presses the sensor
                    while pressure < PRESSURE_DIMMING_THRESHOLD:
                        # Service the IoT stack
                        app.service()

                        if arguments.legacy:
                            # TODO
                            # r_dimming_level = led_legacy_block.nviValue.data.value
                            # g_dimming_level = led_legacy_block.nviValue.data.value
                            # b_dimming_level = led_legacy_block.nviValue.data.value
                            pass

                        else:
                            # For each detected LED set the new color
                            for i in range(MAX_LEDs):
                                # If we detected LED i
                                if leds.detected_led[i]:
                                    # For shorter name
                                    load_status = led_iot_blocks[i].nvoLoadStatus

                                    # Read latest RGB color (which implies brightness)
                                    old_red = load_status.data.color.color_value.RGB.red
                                    old_green = load_status.data.color.color_value.RGB.green
                                    old_blue = load_status.data.color.color_value.RGB.blue

                                    # Get brightness of latest RGB values from HLS space
                                    hls_colors = colorsys.rgb_to_hls(old_red,
                                                                     old_green,
                                                                     old_blue)
                                    new_brightness = hls_colors[LUMINANCE]

                                    # start changing brightness up or down
                                    if dimming_down:
                                        # Dim down
                                        new_brightness = max(
                                            MIN_LUMINANCE_LEVEL ,
                                            new_brightness - DIMMING_STEP)
                                        # Until brightness is minimum
                                        if new_brightness == \
                                            MIN_LUMINANCE_LEVEL :
                                            dimming_down = False
                                    else:
                                        # Dim up
                                        new_brightness = min(
                                            MAX_LUMINANCE_LEVEL,
                                            new_brightness + DIMMING_STEP)
                                        # Until brightness is max
                                        if new_brightness == \
                                            MAX_LUMINANCE_LEVEL:
                                            dimming_down = True

                                    # Reconvert HLS with new brightness to RGB
                                    rgb_colors = colorsys.hls_to_rgb(
                                                    hls_colors[HUE],
                                                    new_brightness,
                                                    hls_colors[SATURATION])

                                    # Set new brightness as RGB color
                                    set_rgb_color(rgb_colors[RED],
                                                  rgb_colors[GREEN],
                                                  rgb_colors[BLUE],
                                                  leds,
                                                  i,
                                                  arguments)
                                    # Update output LED functional block
                                    load_status.data.level = new_brightness
                                    load_status.data.color.color_value.RGB.red = rgb_colors[RED]
                                    load_status.data.color.color_value.RGB.green = rgb_colors[GREEN]
                                    load_status.data.color.color_value.RGB.blue = rgb_colors[BLUE]

                        # Update pressure block on delta
                        old_pressure = pressure
                        pressure = get_pressure(pressure_sensors,
                                                pressure_sensors.block)
                        # Send on delta
                        if abs(pressure - old_pressure) > PRESSURE_VALUE_DELTA:
                            pressure_sensors[0].block.nvoValue.data = pressure

    finally:
        # Stop the IP-C application
        print('\n'
              'Winding down...')
        app.stop()
        if arguments.sensor != 'none':
            # Close GPIO
            for i in range(len(pressure_sensors)):
                pressure_sensors[i].cleanup()
        if arguments.color:
            # reset LEDs
            leds.cleanup()
        print('Goodbye')

### End main function ###


def set_led_status(state, level, color_type, red, green, blue, scene_number, led_obj, led_index, led_block,
                   arguments):
    """ Set the state, level, and color for an LED. """
    led_block.nvoLoadStatus.data.state = state
    if state:
        # State is on; set level and color; clear the level if color is specified
        if color_type == ColorEncoding.color_encoding_t.COLOR_RGB:
            # Color specified; clear level and set color
            led_block.nvoLoadStatus.data.level = float('nan')
            led_block.nvoLoadStatus.data.color.color_value.RGB.red = red
            led_block.nvoLoadStatus.data.color.color_value.RGB.green = green
            led_block.nvoLoadStatus.data.color.color_value.RGB.blue = blue
        elif led_block.nvoLoadStatus.data.level >= 0.:
            # Color not specified and the level is specified; set the level
            level = max(level, MIN_BRIGHTNESS_LEVEL)
            level = min(level, MAX_BRIGHTNESS_LEVEL)
            led_block.nvoLoadStatus.data.level = level
    if led_block.nvoLoadStatus.data.scene_number != 65535:
        # Scene specified; set it
        led_block.nvoLoadStatus.data.scene_number = scene_number
    normalize_led_settings(led_block)
    set_led_output(led_obj, led_index, led_block, arguments)

def normalize_led_settings(led_block):
    """ Normalize the state, level, and color for an LED block so that they are
    consistent with each other when the state is on.  No changes are made if the
    state is off. """
    led_block.nvoLoadStatus.data.control = LoadControl.load_control_t.LOAD_REPORT
    if led_block.nvoLoadStatus.data.state:
        # State is on; get the color and check the level
        red_coordinate = float(led_block.nvoLoadStatus.data.color.color_value.RGB.red) / float(MAX_RED_LEVEL)
        green_coordinate = float(led_block.nvoLoadStatus.data.color.color_value.RGB.green) / float(MAX_GREEN_LEVEL)
        blue_coordinate = float(led_block.nvoLoadStatus.data.color.color_value.RGB.blue) / float(MAX_BLUE_LEVEL)
        is_black = True if red_coordinate + blue_coordinate + green_coordinate == 0. else False
        print('Normalize LED settings for {0}R:{1}G:{2}B, is_black={3}, and level={4}'.format(
                red_coordinate, green_coordinate, blue_coordinate,
                is_black, led_block.nvoLoadStatus.data.level))
        if math.isnan(led_block.nvoLoadStatus.data.level) or \
                        led_block.nvoLoadStatus.data.level < 0.:
            # Level not specified; check the color
            if is_black:
                # Color is black; set to white and set level to 100%
                led_block.nvoLoadStatus.data.color.encoding = ColorEncoding.color_encoding_t.COLOR_RGB
                led_block.nvoLoadStatus.data.color.color_value.RGB.red = MAX_RED_LEVEL
                led_block.nvoLoadStatus.data.color.color_value.RGB.green = MAX_GREEN_LEVEL
                led_block.nvoLoadStatus.data.color.color_value.RGB.blue = MAX_BLUE_LEVEL
                led_block.nvoLoadStatus.data.level = float(MAX_BRIGHTNESS_LEVEL)
            else:
                # Color specified; set the level from the color
                hls_color = colorsys.rgb_to_hls(red_coordinate,
                                                green_coordinate, blue_coordinate)
                led_block.nvoLoadStatus.data.level = \
                    float((hls_color[LUMINANCE]/MAX_LUMINANCE_LEVEL)*MAX_BRIGHTNESS_LEVEL)
            print('Level not specified; new level is {0}'.format(
                    led_block.nvoLoadStatus.data.level))
        else:
            # Level specified
            print('Level specified as {0}'.format(led_block.nvoLoadStatus.data.level))
            if led_block.nvoLoadStatus.data.level == 0.:
                # State is on but level if 0; set the level to 100%
                led_block.nvoLoadStatus.data.level = float(MAX_BRIGHTNESS_LEVEL)
                print('Level changed from 0 to {0}'.format(led_block.nvoLoadStatus.data.level))
            if is_black:
                # State is on but color is black; set to white then adjust the level
                red_coordinate = 1.0
                green_coordinate = 1.0
                blue_coordinate = 1.0
        # Level and color specified; adjust color to match the level
        print('Adjusted level is {0}'.format(led_block.nvoLoadStatus.data.level))
        lightness_coordinate = led_block.nvoLoadStatus.data.level / float(MAX_BRIGHTNESS_LEVEL)
        hls_color = colorsys.rgb_to_hls(red_coordinate, green_coordinate, blue_coordinate)
        adjusted_rgb = colorsys.hls_to_rgb(hls_color[HUE], lightness_coordinate, hls_color[SATURATION])
        led_block.nvoLoadStatus.data.color.encoding = ColorEncoding.color_encoding_t.COLOR_RGB
        led_block.nvoLoadStatus.data.color.color_value.RGB.red = int(adjusted_rgb[RED] * 255.)
        led_block.nvoLoadStatus.data.color.color_value.RGB.green = int(adjusted_rgb[GREEN] * 255.)
        led_block.nvoLoadStatus.data.color.color_value.RGB.blue = int(adjusted_rgb[BLUE] * 255.)
        print('Adjusted color: {0}H:{1}L:{2}S, {3}R:{4}G:{5}B, {6}HLS'.format(
              hls_color[HUE], lightness_coordinate, hls_color[SATURATION],
              adjusted_rgb[RED], adjusted_rgb[GREEN], adjusted_rgb[BLUE], hls_color))

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
    print('Set LED {0} RGB color to {1}R:{2}G:{3}B'.format(led_index, r, g, b))
    if arguments.color:
        print('Control 3 PWMs')
        led_obj.set_channel_level(
            RED_LED_PWM_CHANNEL + (led_index * LED_OFFSET), r)
        led_obj.set_channel_level(
            GREEN_LED_PWM_CHANNEL + (led_index * LED_OFFSET), 0)#g)
        led_obj.set_channel_level(
            BLUE_LED_PWM_CHANNEL + (led_index * LED_OFFSET), 0)#b)
    # If there are the PiFace LEDs, set a single LED
    elif arguments.piface:
        print('Control PiFace')
        led_obj.set_channel_level(led_index, r or g or b)

def define_scene_from_load_dp(destination_scene, source_dp):

    # save useful values into the scene
    destination_scene.scene_number = source_dp.data.scene_number
    destination_scene.state = source_dp.data.state
    destination_scene.level = source_dp.data.level
    destination_scene.angle = source_dp.data.angle
    destination_scene.color = source_dp.data.color
    destination_scene.delay = source_dp.data.delay
    destination_scene.duration = source_dp.data.duration

    # TODO: Rich, what do we put here?
    destination_scene.unoccupied_scene_number = source_dp.data.scene_number
    destination_scene.standby_scene_number = source_dp.data.scene_number
    destination_scene.next_scene__number = source_dp.data.scene_number

    # unused values
    # destination_scene.action = source_dp.data.action
    # destination_scene.control = source_dp.data.control
    # destination_scene.level_multiplier = source_dp.data.level_multiplier
    # #destination_scene.reduction_multiplier = ???
    # destination_scene.area_occupancy = source_dp.data.area_occupancy
    # destination_scene.fade = source_dp.data.fade
    # #destination_scene.hold = ???
    # destination_scene.priority = source_dp.data.priority
    # destination_scene.load_groups = source_dp.data.load_groups

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
def menu(app, led_obj, led_block, arguments):
    """ Function to acquire commands from the console, and execute them.
    The call is blocking. """
    # noinspection PyUnusedLocal
    def menu_cancel(args):
        app.isi.cancel_enrollment()
        return False

    # noinspection PyUnusedLocal
    def menu_color(args):
        """ Set the LED color.  The LED is selected with the argument.
        When no argument is given, set the color for all LEDs. """
        split_args = str.split(args)
        if len(split_args) < 1:
            print('Color value is required for the color command -- specify color <color> [<channel>]')
        elif len(split_args) > 2:
            print('Too many arguments -- specify color <color> [<channel>]')
        else:
            if len(split_args) == 2:
                # Set LED color for the selected channel
                print('Set LED color for channel {0} to {1}'.format(int(split_args[1]), int(split_args[0])))
                start_index = int(split_args[1])
                stop_index = start_index + 1
            else:
                # Set the LED color for all LEDs
                print('Set LED color for all channels to {0}'.format(int(split_args[0])))
                start_index = 0
                stop_index = len(led_block)
            rgb_color = int(split_args[0])
            for led_index in range(start_index, stop_index):
                led_block[led_index].nvoLoadStatus.data.state = 1
                led_block[led_index].nvoLoadStatus.data.level = float('nan')
                led_block[led_index].nvoLoadStatus.data.color.encoding = RGB_TYPE
                led_block[led_index].nvoLoadStatus.data.color.color_value.RGB.red \
                    = rgb_color >> 16 & 0xFF
                led_block[led_index].nvoLoadStatus.data.color.color_value.RGB.green \
                    = rgb_color >> 8 & 0xFF
                led_block[led_index].nvoLoadStatus.data.color.color_value.RGB.blue \
                    = rgb_color & 0xFF
                normalize_led_settings(led_block[led_index])
                set_led_output(led_obj, led_index, led_block[led_index], arguments)
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
            normalize_led_settings(led_block[led_index])
            set_led_output(led_obj, led_index, led_block[led_index], arguments)
        return False

    # noinspection PyUnusedLocal
    def menu_on(args):
        """ Set the LED state to on.  The LED is selected with the argument.
        When no argument is given, set all LED states to on. """
        print('On Command: arguments are {0}'.format(args))
        if len(args):
            # Turn LED for the selected channel on
            start_index = int(args)
            stop_index = start_index + 1
        else:
            # Turn all LEDs on
            start_index = 0
            stop_index = len(led_block)
        for led_index in range(start_index, stop_index):
            print('Turn on LED {0}'.format(led_index))
            led_block[led_index].nvoLoadStatus.data.state = 1
            normalize_led_settings(led_block[led_index])
            set_led_output(led_obj, led_index, led_block[led_index], arguments)
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
    # Menu items dictionary: command -> (handler function, comment)
    # Handler functions return True to exit the program.
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
        'wink':    (menu_wink,     '             Simulate receipt of a Wink message')
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
        else:
            print('Enter "help" for a list of commands')
        show_prompt()
    except Exception as e:
        print(e)
    return result

if __name__ == '__main__':
    main()





