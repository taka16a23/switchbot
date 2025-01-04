#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""lock --

"""
from switchbot.devices.device import Device


class Lock(Device):
    """Lock

    Lock is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Smart Lock'

    def lock(self, ):
        """SUMMARY

        lock()

        @Return:

        @Error:
        """
        return self.command('lock')

    def unlock(self, ):
        """SUMMARY

        unlock()

        @Return:

        @Error:
        """
        return self.command('unlock')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# lock.py ends here
