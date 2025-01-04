#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Humidifier2 --

"""
from switchbot.devices.device import Device


class Humidifier2(Device):
    """Humidifier2

    Humidifier2 is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Humidifier2'

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
        - `value`: {"mode": mode_int, "targetHumidify": humidity_int}

        set the mode. mode_int, 1, level 4; 2, level 3; 3, level 2; 4, level 1; 5,
        humidity mode; 6, sleep mode; 7, auto mode; 8, drying mode; targetHumidify,
        the target humidity level in percentage, 0~100.

        @Return:

        @Error:
        """
        return self.command('setMode', value)

    def set_childlock(self, value):
        """SUMMARY

        set_childlock(value)

        @Arguments:
        - `value`: true or false

        enable or disable child lock. true, enable; false, disable

        @Return:

        @Error:
        """
        return self.command('setChildLock', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# Humidifier2.py ends here
