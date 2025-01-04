#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""relay_switch1 --

"""
from switchbot.devices.device import Device


class RelaySwitch1(Device):
    """RelaySwitch1

    RelaySwitch1 is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Relay Switch 1'

    def turn_off(self, ):
        """set to OFF state

        turn_off()

        @Return:

        @Error:
        """
        return self.command('turnOff')

    def turn_on(self, ):
        """set to ON state

        turn_on()

        @Return:

        @Error:
        """
        return self.command('turnOn')

    def toggle(self, ):
        """toggle state

        toggle()

        @Return:

        @Error:
        """
        return self.command('toggle')

    def set_mode(self, value):
        """SUMMARY

        set_mode(value)

        @Arguments:
        - `value`: set the switch mode. 0, toggle mode; 1, edge switch mode; 2, detached switch mode; 3, momentary switch mode

        @Return:

        @Error:
        """
        return self.command('setMode', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# relay_switch1.py ends here
