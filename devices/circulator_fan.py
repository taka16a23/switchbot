#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""battery_circulator_fan --

"""
from switchbot.devices.device import Device


class CirculatorFan(Device):
    """CirculatorFan

    CirculatorFan is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Circulator Fan'

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

    def set_night_light_mode(self, value):
        """SUMMARY

        set_night_light_mode(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self.command('setNightLightMode', value)

    def set_wind_mode(self, value):
        """SUMMARY

        set_wind_mode(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self.command('setWindMode', value)

    def set_wind_speed(self, value):
        """SUMMARY

        set_wind_speed(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self.command('setWindSpeed', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# battery_circulator_fan.py ends here
