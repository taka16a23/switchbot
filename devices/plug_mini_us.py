#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""plug_mini --

"""
from switchbot.devices.device import Device


class PlugMiniUS(Device):
    """PlugMiniUS

    PlugMiniUS is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Plug Mini (US)'

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

    def toggle(self, ):
        """toggle state

        toggle()

        @Return:

        @Error:
        """
        return self.command('toggle')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# plug_mini.py ends here
