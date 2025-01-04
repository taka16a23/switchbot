#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keypad --

"""
from switchbot.devices.device import Device


class Keypad(Device):
    """Keypad

    Keypad is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Keypad'


    def create_key(self, value):
        """SUMMARY

        create_key(value)

        @Arguments:
        - `value`: { "name": passcode _name_str, "type": passcode_type_str, "password": passcode_str, "startTime": valid_from_long, "endTime": valid_to_long }

        @Return:

        @Error:
        """
        return self.command('createKey', value)

    def delete_key(self, value):
        """SUMMARY

        delete_key(value)

        @Arguments:
        - `value`: { "id": passcode_id_int }

        @Return:

        @Error:
        """
        return self.command('deleteKey', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keypad.py ends here
