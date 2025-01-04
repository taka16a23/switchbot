#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""blind_tilt --

"""
from switchbot.devices.device import Device


class BlindTilt(Device):
    """BlindTilt

    BlindTilt is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Blind Tilt'

    def set_position(self, value):
        """SUMMARY

        set_position(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self.command('setPosition', value)

    def fully_open(self, ):
        """SUMMARY

        fully_open()

        @Return:

        @Error:
        """
        return self.command('fullyOpen')

    def close_up(self, ):
        """SUMMARY

        close_up()

        @Return:

        @Error:
        """
        return self.command('closeUp')

    def close_down(self, ):
        """SUMMARY

        close_down()

        @Return:

        @Error:
        """
        return self.command('closeDown')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# blind_tilt.py ends here
