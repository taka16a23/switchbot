#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""curtain --

"""
from switchbot.devices.device import Device


class Curtain(Device):
    """Curtain

    Curtain is a Device.
    Short for SwitchBot Curtain.
    Model No: W0701600.
    """
    def set_position(self, index0, mode0, position0):
        """SUMMARY

        set_position(index0, mode0, position0)

        @Arguments:
        - `index0`:
        - `mode0`: 0 (Performance Mode), 1 (Silent Mode), ff (default mode)
        - `position0`: 0~100 (0 means open, 100 means closed)

        @Return:

        @Error:
        """
        value = '{},{},{}'.format(index0, mode0, position0)
        return self.command('setPosition', value)

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

    def pause(self, ):
        """set to PAUSE state

        pause()

        @Return:

        @Error:
        """
        return self.command('pause')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# curtain.py ends here