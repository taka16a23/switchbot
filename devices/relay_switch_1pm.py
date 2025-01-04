#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""relay_switch_1pm --

"""
from switchbot.devices.device import Device


class RelaySwitch1PM(Device):
    """RelaySwitch1PM

    RelaySwitch1PM is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Relay Switch 1PM'

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
# relay_switch_1pm.py ends here
