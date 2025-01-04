#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""humidifier --

"""
from switchbot.devices.device import Device


class Humidifier(Device):
    """Humidifier

    Humidifier is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Humidifier'

    def turn_off(self, ):
        """equivalent to set position to 100

        turn_off()

        @Return:

        @Error:
        """
        return self.command('turnOff')

    def turn_on(self, ):
        """equivalent to set position to 0

        turn_on()

        @Return:

        @Error:
        """
        return self.command('turnOn')

    def set_mode(self, value):
        """SUMMARY

        set_mode(value)

        @Arguments:
        - `value`: auto or 101 or 102 or 103 or {0~100}

        @Return:

        @Error:
        """
        return self.command('setMode', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# humidifier.py ends here
