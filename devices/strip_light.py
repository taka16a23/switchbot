#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""strip_light --

"""
from switchbot.devices.device import Device


class StripLight(Device):
    """StripLight

    StripLight is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Strip Light'

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

    def set_brightness(self, value):
        """set brightness

        set_brightness(value)

        @Arguments:
        - `value`: {1-100}

        @Return:

        @Error:
        """
        # require

        # do

        # ensure
        return self.command('setBrightness', value)

    def set_color(self, red, green, blue):
        """set RGB color value

        set_color(red, green, blue)

        @Arguments:
        - `red`: {0-255}
        - `green`: {0-255}
        - `blue`: {0-255}
        @Return:

        @Error:
        """
        value = '{}:{}:{}'.format(red, green, blue)
        # require

        # do

        # ensure
        return self.command('setColor', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# strip_light.py ends here
