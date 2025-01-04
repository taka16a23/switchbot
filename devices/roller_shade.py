#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""roller_shade --

"""
from switchbot.devices.device import Device


class RollerShade(Device):
    """RollerShade

    RollerShade is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Roller Shade'

    def set_position(self, value):
        """SUMMARY

        set_position(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self.command('setPosition', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# roller_shade.py ends here
