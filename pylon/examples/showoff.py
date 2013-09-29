#!/usr/bin/env python3
"""An internal application to demonstrate and discuss many features and aspects
   of the pilon package and API.
"""
#
# This application is for internal use only.
# Copyright (C) 2013 Echelon Corporation.  All rights reserved.
#

# *** PLEASE NOTE ***
# Please note that this script is an internal demo script. When copying code
# and/or comments from this script into any script for public exposure (demos,
# shipping examples, etc), please review comments and code carefully. Most
# comments in this script are aimed at example developers at Echelon.
# Also note that this example script evolves rapidly. If you choose to copy
# parts of it into your scripts, you should keep these portions up-to-date
# with each version of pilon.
# This internal demo script also takes liberties with PEP 8 / 257 compliance.

#
# Importing required standard Python modules. See
# http://docs.python.org/3.3/library/index.html
# for comprehensive documentation of the very large Python standard library.
#
import argparse
import logging
import math
import select
import sys

#
# Import pylon, and all interoperable types necessary.
#
# Notice two (of many possible) forms of importing pilon into the script.
# The plan 'import pylon' statement brings in the pilon runtime kit, while
# the from pylon.resources..... statements import specific resource type
# definitions. Imported in this manner, the script can access these resources
# with their simple name (e.g. SNVT_count), but if importing of resources into
# the application namespace is not desired, consider using
# import pylon.resources.SNVT_count
#
import pylon.device

from pylon.resources.SNVT_count import SNVT_count
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_ppm_f import SNVT_ppm_f
from pylon.resources.switch_state_t import switch_state_t
from pylon.resources.SNVT_switch_2 import SNVT_switch_2
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SFPTopenLoopSensor import SFPTopenLoopSensor
from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg
from pylon.resources.SCPTmaxSndT import SCPTmaxSndT
from pylon.resources.SCPTdefOutput import SCPTdefOutput


def main():
    """The script's main function"""
    #
    # Enable/disable test mode
    #
    pylon.device.stack.test_mode = False
    unit_test = False

    #
    #	Say hi
    #
    print("Welcome to the Pylon Show-off Application.")
    print("Enter 'exit' to exit. Try 'help' for help.\n")

    #
    #   Command line arguments:
    #
    parser = argparse.ArgumentParser(
        description="The Pilon Show-off script"
    )
    parser.add_argument(
        '-d', '--device',
        required=True,
        help='The device URI, e.g. uc://10.0.1.12:1628'
    )
    parser.add_argument(
        '-n', '--nvd',
        default='showoff-nvd',
        help='Path to non-volatile data storage (folder)'
    )
    parser.add_argument(
        '-p', '--programId',
        default='9F:FF:FF:00:00:00:9A:01',
        help='The colon-separated program ID'
    )
    parser.add_argument(
        '-l', '--log',
        default='showoff',
        help='The base location and name for log files'
    )
    parser.add_argument(
        '-D', '--debug',
        default=False,
        action='store_true',
        help='Enables full trace logging'
    )

    arguments = parser.parse_args()

    #
    #	Get rollin'
    #
    if pylon.device.stack.test_mode:
        print('\n*** Note this application is running in test mode\n')

    app = pylon.device.application.Application(
        use_isi=False,
        log_file=arguments.log + '-rtk.log',
        log_level=logging.DEBUG if arguments.debug else logging.ERROR
    )
    logger = logging.getLogger('pylon-rtk.showoff')

    #
    #	Utilities for reading input from the console and executing
    #	commands. Just type a command and hit Enter.
    #
    def kbhit(timeout):
        """
        Similar to kbhit() on Windows platforms. Note this implementation here
        will not work on Windows platforms. On Windows, you'd use kbhit() from
        the MSCRT instead; see the standard Python module 'msvcrt' for more on
        http://docs.python.org/3.3/library/msvcrt.html

        You could use sys.platform to determine the platform, then
        automatically do the right thing, if you wanted to support Windows and
        Linux platforms.
        This function returns true if input is waiting on the console, but
        stops waiting for input when the timeout expires.
        """
        i, o, e = select.select([sys.stdin], [], [], timeout)
        return len(i)

    def menu():
        """
        Function to acquire commands from the console, and execute them.
        The call is blocking.
        """
        def menu_eval(args):
            """
            eval evaluates Python expressions within a running program.
            For example, type 'eval print(1234)' to print this number on the
            console. You can interface with the pylon Application class using
            the global variable 'app' defined above, and you can use the
            pseudo-protected app._lts to reach the stack adapter class in this
            manner.
            """
            try:
                eval(args)
            finally:
                return False    # False: continue. True to terminate script.

        # noinspection PyUnusedLocal
        def menu_exit(args):
            print('Winding down...')
            return True

        def menu_help(args):
            """
            help shows the available commands.
            """
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
        def menu_service(args):
            """
            Sends a service message.
            Equivalent to 'eval app.send_service_message()'
            """
            app.send_service_message()
            return False

        # noinspection PyUnusedLocal
        def menu_wink(args):
            """
            Simulate receipt of a Wink message for testing purposes.
            """
            app.OnWink.fire(app, None)
            return False

        #
        #	Menu items dictionary: command -> ( handler, usage hint )
        #	Handlers return True to exit the program, False to continue.
        items = {
            'eval':     (menu_eval, 		'Evaluate a statement'),
            'exit':     (menu_exit, 		'Exit the script'),
            'service':  (menu_service, 	    'Send a Service Pin message'),
            'help':     (menu_help, 		'Display this help'),
            'wink':     (menu_wink,
                         'Simulate receipt of a Wink message')
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
        except Exception as e:
            print(e)
        return result

    app.device_uri = arguments.device
    app.persistence_path = arguments.nvd
    app.programId = arguments.programId

    #
    # Stack trace logging
    # Simply do not set this property if you do not wish to have this low-level
    # trace logging enabled.
    #
    if arguments.debug:
        app.stack_tracefile = arguments.log + '-lts.log'
        if app.isi:
            app.isi.tracefile(arguments.log + '-isi.log', False)

    #
    # Creating a pair of SNVT_count input and output datapoints.
    #
    # Note the distinction between local and external names: a local name is
    # the name you give to a variable such as my_value_input in this example.
    # This is the name of the Python variable, and the name you use in your
    # script. The datapoint factory, however, also accepts a 'name' argument.
    # This refers to the external name, the name exposed to the network and the
    # network tool through the ISO/IEC 14908 self-identification data.
    # The external name is optional but recommended.
    # When external names are used, they should meet the established naming
    # conventions and use an nvi, nci (alt: cp) or nvo prefix. The internal
    # names, on the other hand, should meet Python coding standards and
    # guidelines.
    #
    # External names help managing the device without printed documentation,
    # but these names consume storage space and, because they must be
    # discovered by the network tool, may prolong discovery and some management
    # processes. These steps occur infrequently, but the extra time required
    # can add up when using large numbers of devices on slow channels.
    #
    my_value_input = app.input_datapoint(
        data=SNVT_count(),
        name='nviValue'
    )

    my_value_output = app.output_datapoint(
        data=SNVT_count(),
        name='nvoValue'
    )

    #
    # Creating a pair of SNVT_switch variables.
    #
    # This example demonstrates another feature: initial values.
    # By default, all resource types implement their default values as defined
    # with the resource definition. For datapoint types, the default values are
    # always zero. To define a datapoint or property item with a different
    # default value, create the item first, then assign the desired values.
    # Optionally, call the _accept_as_default() utility to conserve the current
    # values as default values. This is useful if a logical reset can occur,
    # which returns all data items to their respective default values.
    # In this context, a logical reset refers to the invocation of the _reset()
    # API support by all items derived from pylon.resources.base.DataType.
    #

    my_switch_input = app.input_datapoint(
        data=SNVT_switch(),
        name='nviSwitch'
    )
    my_switch_input.data.value = 80.5
    my_switch_input.data.state = 1
    my_switch_input.data._accept_as_default()

    my_switch_output = app.output_datapoint(
        data=SNVT_switch(),
        name='nvoSwitch'
    )

    #
    # Creating a pair of SNVT_ppm_f single precision floating point variables.
    #
    my_ppm_input = app.input_datapoint(
        data=SNVT_ppm_f(),
        name='nviPpm'
    )

    my_ppm_output = app.output_datapoint(
        data=SNVT_ppm_f(),
        name='nvoPpm'
    )

    #
    # A simple "freelance" union type.
    #
    class MyUnion(pylon.resources.base.Union):
        """A freelance union resource.

        This type definition is an internal test case for
        pylon.resources.base.Union, but it also demonstrates how new
        "resources" can be created in Pilon: because pilon does not use DRF,
        resources don't need to be defined in DRF. You can simply define
        resources using Python, so long as the definitions are correct and
        based on pilon.resources.base. Note, however, that this leads to a not
        interoperable and not LonMark-certifiable device.

        The MyUnion class isn't particularly useful, but it might be a good
        idea for you to try understand what it implements and why it behaves
        the way it does.

        """
        def __init__(self, value=0):
            super().__init__(key=-1, scope=-1)
            self.__vi = pylon.resources.base.Scaled(
                size=4,
                signed=False,
                key=-1,
                scope=-1,
                default=value,
                scaling=(1, 0),
            )
            self._register(('vi', self.__vi))

            self.__vw = pylon.resources.base.Scaled(
                size=2,
                signed=True,
                key=-1,
                scope=-1,
                default=value,
                scaling=(0.01, 0),
            )
            self._register(('vw', self.__vw))

            self.__vf = pylon.resources.base.Float(
                single=True,
                key=-1, scope=-1
            )
            self._register(('vf', self.__vf))

        def __set_vi(self, v):
            self.__vi._value = v

        def __set_vw(self, v):
            self.__vw._value = v

        def __set_vf(self, v):
            self.__vf._value = v

        vi = property(lambda self: self.__vi, __set_vi)
        vw = property(lambda self: self.__vw, __set_vw)
        vf = property(lambda self: self.__vf, __set_vf)

        def __set(self, v):
            if not isinstance(v, MyUnion):
                raise TypeError('Expected instance of MyUnion, got {0}'.format(
                    type(v)
                ))
            self.__set_vi(v.__vi)
            self.__set_vw(v.__vw)
            self.__set_vf(v.__vf)

        _value = property(lambda self: self, __set)

        def __len__(self):
            return 4

    include_array_test = False

    if include_array_test:
        #
        # base.Array test case - a freelance Array
        #
        class MyArray(pylon.resources.base.Array):
            def __init__(self):
                super().__init__((
                    SNVT_switch(), SNVT_switch(), SNVT_switch()
                ))

        my_array = MyArray()
        print(my_array)
        print(my_array[1])
        my_array[2].value = 123
        print(my_array)
        for i in range(len(my_array)):
            print('Index {0} = {1}: {2}'.format(
                i, repr(my_array[i]), str(my_array[i])
            ))

    my_union_input = app.input_datapoint(
        data=MyUnion(),
        name='nviUnion'
    )

    my_union_output = app.output_datapoint(
        data=MyUnion(),
        name='nvoUnion',
        sd='this is an SD comment'
    )

    #
    # A pair of SNVT_switch_2 variables.
    # Notice that these do not export an external name.
    #

    my_sw2_output = app.output_datapoint(
        data=SNVT_switch_2()
    )

    my_sw2_input = app.input_datapoint(
        data=SNVT_switch_2()
    )

        #
    #	Define the datapoint update event handlers
    #
    def on_value_update(sender, arguments):
        logger.info('Processing update {0}'.format(sender))
        try:
            my_value_output.data = my_value_input.data * 3
            print('Just so you know, 3 * {0} is {1}'.format(
                my_value_input.data,
                my_value_output.data
            ))
            #
            # Access to the update source is provided through the 'source'
            # property of the Datapoint.OnUpdateEventArgs object.
            #
            # Returns a ReceiveAddress object (defined in stack.py).
            # You might want to simply print it (using str() or repr()) for
            # logging purposes. To evaluate, query its domain_index, source
            # and destination properties.
            # Note that the destination property returns one of five possible
            # object types; use isinstance() to determine the type of receive
            # destination address object, if necessary.
            #
            if arguments.source:
                print(arguments.source)
        except Exception as e:
            print('Something went wrong in on_value_update({0}): {1}'.format(
                sender, e
            ))

    # noinspection PyUnusedLocal
    def on_switch_update(sender, arguments):
        logger.info('Processing update {0}'.format(sender))
        try:
            my_switch_output.data = my_switch_input.data
            my_switch_output.get_data_item()._accept_as_minimum()
            print('The switch is now reported as {0}'.format(
                str(my_switch_output.data)
            ))
        except Exception as e:
            print('Something went wrong in on_switch_update({0}): {1}'.format(
                sender, e
            ))

    # noinspection PyUnusedLocal
    def on_ppm_update(sender, arguments):
        logger.info('Processing update {0}'.format(sender))
        try:
            my_ppm_output.data = my_ppm_input.data * 2 * math.pi
            print('Floating-point operation: 2 * PI * {0} = {1}'.format(
                my_ppm_input.data,
                my_ppm_output.data
            ))
        except Exception as e:
            print('Something went wrong in on_switch_update({0}): {1}'.format(
                sender, e
            ))

    # noinspection PyUnusedLocal
    def on_union_update(sender, arguments):
        logger.info('Processing update {0}'.format(sender))
        try:
            my_union_output.data = my_union_input.data
            print('Initial union input {0}, output {1}'.format(
                my_union_input.data,
                my_union_output.data
            ))

            my_union_output.data.vw = my_union_input.data.vw
            print('After vw assignment: union input {0}, output {1}'.format(
                my_union_input.data,
                my_union_output.data
            ))

        except Exception as e:
            print('Something went wrong in on_switch_update({0}): {1}'.format(
                sender, e
            ))

    # noinspection PyUnusedLocal
    def on_sw2_update(sender, arguments):
        logger.info('Processing update {0}'.format(sender))
        try:
            with my_sw2_output, my_sw2_input:
                # The with block defines a critical section, and locks all
                # datapoints listed with the 'with' statement for the duration
                # of the 'with' block. The with-block unlocks and registers the
                # datapoints for processing when exiting.

                my_sw2_output.data = my_sw2_input.data
                print('Initial sw2 input {0}, output {1}'.format(
                    my_sw2_input.data,
                    my_sw2_output.data
                ))

                if my_sw2_input.data.state == switch_state_t.SW_SET_FAN_DOWN:
                    my_sw2_output.data.setting.fan_level = \
                        my_sw2_input.data.setting.fan_level
                    print('Now blowing down at {0}'.format(
                        my_sw2_output.data.setting
                    ))
                elif my_sw2_input.data.state == switch_state_t.SW_SET_FAN_UP:
                    my_sw2_output.data.setting.fan_level = \
                        my_sw2_input.data.setting.fan_level
                    print('Now blowing up at {0}'.format(
                        my_sw2_output.data.setting
                    ))
                else:
                    print('Not implemented: {0}, scene {1}'.format(
                        my_sw2_input.data.state,
                        my_sw2_input.data.scene_number
                    ))

        except Exception as e:
            print('Something went wrong in on_sw2_update({0}): {1}'.format(
                sender, e
            ))

    #
    #	Register the network variable event handlers.
    #
    my_value_input.OnUpdate += on_value_update
    my_switch_input.OnUpdate += on_switch_update
    my_ppm_input.OnUpdate += on_ppm_update
    my_union_input.OnUpdate += on_union_update
    my_sw2_input.OnUpdate += on_sw2_update

    #
    #	Some other event handlers
    #
    # noinspection PyUnusedLocal
    def on_service_led(sender, arguments):
        logger.info('Processing service LED status event')
        print('Service LED status changed to {0}.'.format(
            arguments.state
        ))

    # noinspection PyUnusedLocal
    def on_wink(sender, arguments):
        logger.info('Received wink message')
        print('Wink, wink, wink. Brilliant.')

    # noinspection PyUnusedLocal
    def on_online(sender, argument):
        logger.info('Received Online event')
        print('We are now on line.')

    # noinspection PyUnusedLocal
    def on_offline(sender, argument):
        logger.info('Received Offline event')
        print('We are now off line.')

    #
    #	Event handler registration
    #
    app.OnServiceLed += on_service_led
    app.OnWink += on_wink
    app.OnOnline += on_online
    app.OnOffline += on_offline

    #
    # Enter the world of profiles, blocks and properties!
    #
    # The following implements two open loop sensors, one using SNVT_ppm_f, the
    # other using SNVT_temp_p to resolve the SNVT_xxx placeholder from the
    # profile definition.
    # The example here creates an fblock tuple just to illustrate how this can
    # be done; there is no value in doing so with regards to self-
    # identification or self-documentation data however.
    # Notice that the addition of the second profile triggers the automatic
    # implementation of the node object.
    #
    olSensors = (
        app.block(
            profile=SFPTopenLoopSensor(),
            ext_name='ols',
            snvt_xxx=SNVT_ppm_f
        ),
        app.block(
            profile=SFPTopenLoopSensor(),
            ext_name='ols',
            snvt_xxx=SNVT_temp_p
        )
    )

    #
    # Blocks implemented in this manner automatically have all mandatory
    # datapoint and property members implemented. You can access these as
    # instance variables using the member's name from the profile. For example,
    # SFPTopenLoopSensor defines a nviValue datapoint member, so you could
    # attach an OnUpdate event handler simply by saying
    # olSensors[0].nvoValue.OnUpdate += my_handler.
    #
    # Blocks implemented in this manner automatically implement all mandatory
    # datapoint members, all mandatory properties applying to these datapoint
    # members, and all mandatory properties applying to the block as a whole.
    #
    # Note that profiles are presented slightly different than Resource Editor
    # and DRF does: in DRF, profiles are flat. All property members are listed
    # under the profile, and a special "applies-to" field indicates for each
    # property whether it applies to the profile or to a specific member
    # datapoint (NV).
    # In Pilon, the profile has a list of property members, as has each of the
    # profile's datapoint members. The "applies-to" information is thus encoded
    # in the profile definition.
    #
    # See below for an example of implementing optional members.
    #
    # Access the node object if you like. Note this property may return None if
    # a node object has not (yet) been created. You do not normally have to
    # deal with this, unless you wish to extend the default behavior.
    # A default node object is automatically created when the second block is
    # constructed by the block factory, using the app.node_object_profile type
    # (which defaults to SFPTnodeObject). You can change node_object_profile to
    # a different profile (which must derive from SFPTnodeObject), or you can
    # explicitly create a node object using the block factory before the
    # automatic node object factory kicks in.
    #
    # Note that, at this point, support for inheriting profiles is incomplete.
    #
    # This is a regular block like any other, by default supplying the
    # mandatory members nviRequest and nvoStatus.
    #
    # (Once ISI/pi is integrated and Pilon properties are supported, the
    # default node object may also automatically implement the optional
    # nciNwrkCnfg property, subject to the script's preferences w.r.t. ISI).
    #
    # The Application class supplies a default node object implementation,
    # which implements the three mandatory node object commands (RQ_NORMAL,
    # RQ_UPDATE_STATUS, RQ_REPORT_MASK) and two optional ones: RQ_DISABLED,
    # RQ_ENABLE.
    #
    # To supply additional functionality, remove any previously registered
    # handlers with app.node_object.nviRequest.OnUpdate.reset(), then register
    # your own. You can still call the default implementation
    # (app.on_nviRequest_update with the same sender and arguments parameters
    # as received in your handler.
    #
    node_object = app.node_object

    #
    # optional member support:
    #
    # Implement an optional member with the block's implement() method,
    # specifying the member's name as defined in the profile.
    #
    olSensors[0].implement('nvoRawHwData')
    #
    # Implement an optional property member on a block, specifying the property
    # name as defined in the profile.
    # Note that this particular property may already be implemented
    # automatically, subject to your ISI-related preferences. In this case,
    # you'll get the same property returned.
    #
    node_object.implement('nciNetConfig')

    #
    # Implement an optional property on a member datapoint, specifying the
    # property name as defined in the profile.
    # Note that the implement() methods always return the implemented item.
    # The examples above ignored these, but if you plan on accessing these
    # items (for example in order to attach an update event handler), you
    # could simply assign the result to a variable.
    #
    # noinspection PyUnusedLocal
    my_nciMaxStsSendT = node_object.nvoStatus.implement('nciMaxStsSendT')

    #
    #   device properties
    #
    # You can implement a valid property type and apply it to the device as a
    # whole. This is a device property. You can add as many property types as
    # you wish, provided that each property type is only applied once. (There
    # can only be one SCPTlocation, for example.)
    #
    # To do so, use the Application.implement() method. The new property is
    # returned. The new property can also be retrieved through the
    # app.properties property, and as an instance variable of the given name.
    #
    app.implement('nciNwrkCnfg', SCPTnwrkCnfg)
    app.implement('nciMaxSndT', SCPTmaxSndT)

    if unit_test:
        try:
            # failure expected: type-inheriting device property not possible
            app.implement('nciDefOut', SCPTdefOutput)
        except pylon.device.toolkit.PylonError as e:
            print(e)

        try:
            # failure expected: duplicate instance variable name
            app.implement('nciNwrkCnfg', SCPTnwrkCnfg)
        except NameError as e:
            print(e)

        try:
            # failure expected: duplicate type
            app.implement('nciNetworkConfiguration', SCPTnwrkCnfg)
        except pylon.device.toolkit.PylonError as e:
            print(e)

    #
    #   shared properties
    #
    # ### TODO ~~~~~~~~~~~~~~~~~~~~~~~~ TBD

    #
    #   program ID
    #
    # You must specify a program Id prior to calling start(). There is not
    # good default for a program Id, so it must be specified explicitly.
    # However, you could start with a value derived from
    # '9F:FF:FF:00:00:00:9A:00,' where you change the zeroes to a meaningful
    # value in the context of your script.
    #
    # At the very least increment the model number (the last byte) every time
    # the script's external interface changes.
    #
    app.programId = '9F:FF:FF:00:0:00:9A:00'

    #
    #	Now *really* get started
    #
    app.start()
    app.send_service_message()

    print(
        'The script is now running as {0},\n'
        'using non-volatile data from {1} and\n'
        'a unique Id (hardware address) of {2}'.format(
            app.programId,
            app.persistence_path,
            app.uniqueId
        )
    )

    system_object_demo = False

    if system_object_demo:
        #
        # System access:
        #
        # The Application.system property returns a pylon.system.System
        # object, which in turn provides access to low-level system tools such
        # as the domain table, or the node's status and statistics.
        #
        system = app.system

        #   Read current status, and clear the status
        # noinspection PyUnusedLocal
        stats = system.status
        system.status = None

        #
        # Play with the domain table using the System object's query_domain() /
        # update_domain() method pair.
        #
        d = (
            system.query_domain(0),
            system.query_domain(1)
        )

        d[1].domain_id = '03:03:03'
        d[1].subnet_id = 4
        d[1].node_id = 5

        # print('Domain 0: ' + str(d[0]))
        # system.update_domain(1, d[1])

        #
        # Address table
        # pilon's System object supports a query_address() / update_address()
        # method pair. Note that these methods return and accept one of several
        # possible object types, according to the type of address:
        # SubnetNodeAddress, GroupAddress, etc.
        #
        a0 = system.query_address(0)
        print('Address [0]: ' + str(a0))
        print('Address [1]: ' + str(system.query_address(1)))

        # Set address 0 to a group address:
        z = pylon.device.system.GroupAddress()

        z.group, z.size, z.member = 8, 2, 1
        z.domain = 0
        z.receive_timer = pylon.device.system.ReceiveTimer.RCV384
        z.repeat_timer = pylon.device.system.RepeatTimer.RPT192
        z.transmit_timer = pylon.device.system.TransmitTimer.TX96
        z.retries = 3

        system.update_address(0, z)
        print('Expect {0}, is now {1}'.format(
            z,
            system.query_address(0)
        ))

        # Clear address 0 again
        system.update_address(0, pylon.device.system.UnusedAddress())
        print('Address[0] table returned to {0}'.format(
            system.query_address(0)
        ))

        #
        # Datapoint configuration table
        #

        #
        # Fetch a datapoint configuration table record by index, or with the
        # related datapoint object.
        #
        dpcA = system.query_datapoint_config(0)
        dpcB = system.query_datapoint_config(my_sw2_output)

        # Notice that the DatapointConfig.__str__ function provides an
        # overview, not a comprehensive list of all aspects of this object.
        print('Datapoint config table {0}: {1}'.format(
            0,
            dpcA
        ))
        print('Datapoint config table for {0}: {1}'.format(
            my_sw2_output,
            dpcB
        ))

        #
        # Update a datapoint configuration record in the same manner as above,
        # again using the index or the related datapoint object.
        #
        dpcB.selector = 321
        system.update_datapoint_config(my_sw2_output, dpcB)

        #
        # Alias table
        #

        #
        # Fetch an alias through its index with query_alias.
        #
        alias3 = system.query_alias_config(3)
        print('Alias 3: {0}'.format(alias3))

        #
        # Modify and assign:
        #
        alias3.primary = my_ppm_input
        alias3.selector = 0x1234
        alias3.address_index = 0
        system.update_alias_config(3, alias3)
        print('Alias 3 is now {0}'.format(system.query_alias_config(3)))

    timer_demo = False

    if timer_demo:
        ticktock = pylon.device.toolkit.Timer(app, 12)    # twelve seconds
        print(
            'ticktock is now running with a resolution of {0}s'.format(
                ticktock.resolution
            )
        )

    try:
        done = False

        while not done:
            app.service()

            if timer_demo:
                if ticktock.is_expired:
                    print('Another 12 precious seconds are gone and lost '
                          'forever.')
                    ticktock.start(12)

            # <do whatever else you need to do>
            if kbhit(0.002):
                done = menu()
    finally:
        app.stop()

        print("""
    It passed on! This application is no more! It has ceased to be! It's
    expired and gone to meet its maker!
    It's a stiff! Bereft of life, it rests in peace! If you hadn't nailed it to
    the perch it'd be pushing up the daisies! Its metabolic processes are now
    'istory! It's off the twig! It kicked the bucket, it shuffled off its
    mortal coil, run down the curtain and joined the bleedin' choir invisible!!
    THIS IS AN EX-APPLICATION!!
            """)

if __name__ == '__main__':
    main()
