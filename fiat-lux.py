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

# Useful imports
import sys, select, logging, socket

# Import standard Python modules required by Pilon
import argparse
import logging
import select
import sys

# Import Pilon
import pylon.device

# Import Pilon resources used by this application
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SFPTopenLoopSensor import SFPTopenLoopSensor
from pylon.resources.SFPTopenLoopActuator import SFPTopenLoopActuator

# Import for I/O
from led_driver.led_set import LED
from fsr_read.pressure_sensor import PRESSURE_SENSOR

# Enable/disable test mode
#pylon.lts.TESTMODE = True

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
# Init
###############################################################################
print('Initialising the FiatLux Application.')
print('Type CTRL-c to exit.')
if pylon.lts.TESTMODE:
    print('\n*** Note this application is running in test mode\n')


###########
# init I/O
###########
# Create the object to control the LEDs. Assume the PWM board for the LEDs
# is at address 0x40 if not change it in the constants above
# chek out the tutorial here
# http://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/
# library-reference
myLed = LED(PWM_BOARD_I2C_ADDRESS, PWM_FREQ, True)

# Create the pressure sensor object
mySensor = PRESSURE_SENSOR()

############
# init Pilon
############


def main():
    # create application object
    app = pylon.device.application.Application(
        use_isi=False,
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR
    )

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

    # Determine IP-852 device URI and the node's unique Id, based on
    # the unique hostname. You could add definitions matching your
    # configuration to this dictionary.
    #
    # The IP address in the URI must be numeric or fqdn; no .local address will
    # work (for now)
    myMachines = {
        'luca-raspi3':          pylon.lts.UNIQUE_ID_TYPE(0xFE, 0xAA,
                                                         0xC5, 0xE8,
                                                         0x4C, 0x92),
        'luca-ubuntu-vm':       pylon.lts.UNIQUE_ID_TYPE(0xFE, 0xAA,
                                                         0xC5, 0xE8,
                                                         0x4C, 0x93),
        'luca-debian-full-vm':  pylon.lts.UNIQUE_ID_TYPE(0xFE, 0xAA,
                                                         0xC5, 0xE8,
                                                         0x4C, 0x94)
        }

    # get text hostname of the local machine
    host = socket.gethostname()
    # get the numeric IP address from the hostname; this might require avahid
    ipAddr = socket.gethostbyname(host+'.local')
    print('Host '+host+' has IP address '+ipAddr)

    # fill in the app network properties
    if host in myMachines:
        # URI format is '//192.168.1.14:1628/uc'
        app.device_uri = '//'+ipAddr+':1628/uc'
        print ("Host URI is " + app.device_uri)
        app.programId = myMachines[host]
        print ("Host PID is " + str(app.programId))


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
                        # Simulate receipt of  a Wink message for testing:
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







print('Joining the channel at {0}'.format(app.deviceUri))

# Create the node object
app.block(app.node_object_profile())

###############################################################################
# Creating my functional block
#
# IP-C Lamp Actuator Functional Block based on a new functional profile based on the ISI Lamp Actuator with the following changes:
# -- An IP-C Switch input and feedback output instead of a SNVT_switch_2 input and feedback output.
#    The IP-C Switch type is similar to SNVT_switch_2 with the following changes:
#        -- A timestamp field specifying the date and time the value was measured or the status was updated.
#        -- A new IP-C state enumeration will be defined and used for the state field.
#           The type will be based on the switch_state_t enumeration, with changes required
#           for the other changes in this list.
#        -- The value field will be defined as a 32-bit float instead of a union.
#        -- The group_number, button_number, delay, and multiplier fields will be moved out of
#           the value union into separate fields.
#        -- be consolidated into the value field.
#        -- A priority field specifying the relative priority of this value.
#        -- A status field defined as an enumeration reporting the status of the switch.
# -- Power and Energy outputs based on the IP-C Sensor type.
# -- Required color input and feedback output instead of optional.
# -- Required multiplier output instead of optional.
# -- Required runtime output instead of optonal.
# -- A 60-character Name CP instead of three 12-character name CPs.
# -- A 60-character Location CP instead of a 31-character location CP.
# -- IP-C Network Timing CPs for the power and energy outputs instead of a maximum send time and minimum send time CPs.
################################################################################

# types I need (in alphabetical order)
SNVT_color_2 = pylon.resources.SNVT_color_2.SNVT_color_2
SNVT_elapsed_tm = pylon.resources.SNVT_elapsed_tm.SNVT_elapsed_tm
SNVT_elec_kwh = pylon.resources.SNVT_elec_kwh.SNVT_elec_kwh
SNVT_occupancy = pylon.resources.SNVT_occupancy.SNVT_occupancy
SNVT_power = pylon.resources.SNVT_power.SNVT_power
SNVT_switch = pylon.resources.SNVT_switch.SNVT_switch

# inputs
nviValue = app.InputNetworkVariable(SNVT_switch, name='nviValue')
nviOccup = app.InputNetworkVariable(SNVT_occupancy, name='nviOccup')
# optional inputs
nviColor = app.InputNetworkVariable(SNVT_color_2, name='nviColor')

# outputs
nvoValueFb = app.OutputNetworkVariable(SNVT_switch, name='nvoValueFb')
nvoPower = app.OutputNetworkVariable(SNVT_power, name='nvoPower')
nvoOccupancyFb = app.OutputNetworkVariable(SNVT_occupancy, name='nvoOccupancyFb')
# optional outputs
nvoRunHours = app.OutputNetworkVariable(SNVT_elapsed_tm, name='nvoRunHours')
nvoEnergyHi = app.OutputNetworkVariable(SNVT_elec_kwh, name='nvoEnergyHi')
nvoMultiplierFb = app.OutputNetworkVariable(SNVT_switch, name='nvoMultiplierFb')
nvoColorFb = app.OutputNetworkVariable(SNVT_color_2, name='nvoColorFb')
nvoEnergyLo = app.OutputNetworkVariable(SNVT_elec_kwh, name='nvoEnergyLo')

####################################################################################
#   Input NVs updates event handlers
####################################################################################

def onNviValueUpdate(sender, arguments):
    logger.info('Processing network variable update {0}'.format(sender))
    try:
        # TODO
            # turn leds on/off
        # propagate feedback
        nvoValueFb.value <<= nviValue.value
        print("LED has now value {0}, state {1}".format(nvoValueFb.value.value, nvoValueFb.value.state))
    except Exception as e:
        print('Something just went wrong in onNviValueUpdate({0}): {1}'.format(sender, e))
nviValue.OnUpdate += onNviValueUpdate


def onNviOccupUpdate(sender, arguments):
    logger.info('Processing network variable update {0}'.format(sender))
    try:
        # TODO
        print()
    except Exception as e:
        print('Something just went wrong in onNviOccupUpdate({0}): {1}'.format(sender, e))
nviOccup.OnUpdate += onNviOccupUpdate

def onNviColorUpdate(sender, arguments):
    logger.info('Processing network variable update {0}'.format(sender))
    try:
        # TODO
        print()
    except Exception as e:
        print('Something just went wrong in onNviColorUpdate({0}): {1}'.format(sender, e))
nviColor.OnUpdate += onNviColorUpdate


############################################################################################
#
#   System event handlers definition and registration
#
############################################################################################
def onServiceLed(sender, arguments):
    logger.info('Processing service LED status event')
    print('Service LED status changed to {0}.'.format(arguments.state))
app.OnServiceLed += onServiceLed

def onWink(sender, arguments):
    logger.info('Recevied wink message')
    print('Wink.')
app.OnWink += onWink

def onOnline(sender, argument):
    logger.info('Received Online event')
    print('We are now on line.')
app.OnOnline += onOnline

def onOffline(sender, argument):
    logger.info('Received Offline event')
    print('We are now off line.')
app.OnOffline += onOffline


##############################################################################################
#   Start and main loop
##############################################################################################
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










