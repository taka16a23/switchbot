#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""lock_pro --

"""
from switchbot.devices.device import Device


class LockPro(Device):
    """LockPro

    LockPro is a Device.
    Responsibility:
    """
    DEVICE_TYPE = 'Smart Lock Pro'

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
# lock_pro.py ends here
