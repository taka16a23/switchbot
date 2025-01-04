#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""k10_pro_combo --

"""
from switchbot.devices.device import Device


class K10ProCombo(Device):
    """K10ProCombo

    K10ProCombo is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Robot Vacuum Cleaner K10+ Pro Combo'

    def start_clean(self, value):
        """SUMMARY

        start_clean(value)

        @Arguments:
        - `value`: {"action": action_str, "param": {"fanLevel": fan_level_int, "times": clean_cycle_int}}

        @Return:

        @Error:
        """
        return self.command('startClean', value)

    def pause(self, ):
        """SUMMARY

        pause()

        @Return:

        @Error:
        """
        return self.command('pause', value)

    def dock(self, ):
        """SUMMARY

        dock()

        @Return:

        @Error:
        """
        return self.command('dock', value)

    def set_volume(self, value):
        """SUMMARY

        set_volume(value)

        @Arguments:
        - `value`: {0-100}

        @Return:

        @Error:
        """
        return self.command('setVolume', value)

    def change_param(self, value):
        """SUMMARY

        change_param(value)

        @Arguments:
        - `value`: {"fanLevel": fan_level_int, "waterLevel": water_level_int, "times": clean_cycle_int}

        @Return:

        @Error:
        """
        return self.command('changeParam', value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# k10_pro_combo.py ends here
