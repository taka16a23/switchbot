#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""k10_pro_combo --

"""
from switchbot.devices.device import Device


class FloorCleaningRobotS10(Device):
    """FloorCleaningRobotS10

    FloorCleaningRobotS10 is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'S10'

    def start_clean(self, value):
        """SUMMARY

        start_clean(value)

        @Arguments:
        - `value`: {"action": action_str, "param": {"fanLevel": fan_level_int, "times": clean_cycle_int}}

        @Return:

        @Error:
        """
        return self.command('startClean', value)

    def add_water_for_humi(self, ):
        """SUMMARY

        add_water_for_humi()

        @Return:

        @Error:
        """
        return self.command('addWaterForHumi', value)

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

    def self_clean(self, value):
        """SUMMARY

        self_clean(value)

        @Arguments:
        - `value`: 1 or 2 or 3

        @Return:

        @Error:
        """
        return self.command('selfClean', value)

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
