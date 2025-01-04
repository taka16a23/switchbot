#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""air_purifiler_table_pm25 --

"""
from switchbot.devices.device import Device


class AirPurifilerTablePM25(Device):
    """AirPurifilerTablePM25

    AirPurifilerPM25 is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Air Purifier Table PM2.5'

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
        - `value`:

        @Return:

        @Error:
        """
        return self.command('setMode', value)

    def set_childlock(self, value):
        """SUMMARY

        set_childlock(value)

        @Arguments:
        - `value`: 1 or 0

        enable or disable child lock. 1, enable; 0, disable

        @Return:

        @Error:
        """
        return self.command('setChildLock', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# air_purifiler_table_pm25.py ends here
