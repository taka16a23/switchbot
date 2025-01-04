#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""robot_vacuum_cleaner_s1_plus --

"""
from switchbot.devices.device import Device


class RobotVacuumCleanerS1Plus(Device):
    """RobotVacuumCleanerS1Plus

    RobotVacuumCleanerS1Plus is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Robot Vacuum Cleaner S1 Plus'

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
# robot_vacuum_cleaner_s1_plus.py ends here
