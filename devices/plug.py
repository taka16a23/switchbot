#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""plug --

"""
from switchbot.devices.device import Device


class Plug(Device):
    """Plug

    Plug is a Device.
    Short for SwitchBot Plug.
    Model No: SP11.
    Currently only available in Japan.
    """
    DEVICE_TYPE = 'Plug'

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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# plug.py ends here
