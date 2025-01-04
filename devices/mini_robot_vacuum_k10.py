#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""mini_robot_vacuum_k10 --

"""
from switchbot.devices.device import Device


class MiniRobotVacuumCleanerK10(Device):
    """MiniRobotVacuumCleanerK10

    MiniRobotVacuumCleanerK10 is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'K10+'

    def start(self, ):
        """SUMMARY

        start()

        @Return:

        @Error:
        """
        return self.command('start')

    def stop(self, ):
        """SUMMARY

        stop()

        @Return:

        @Error:
        """
        return self.command('stop')

    def dock(self, ):
        """SUMMARY

        dock()

        @Return:

        @Error:
        """
        return self.command('dock')

    def pow_level(self, value):
        """SUMMARY

        pow_level(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self.command('PowLevel',  value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mini_robot_vacuum_k10.py ends here
