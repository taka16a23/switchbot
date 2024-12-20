import sys
from switchbot.client import SwitchBotClient


class SwitchBot(object):
    """SwitchBot

    SwitchBot is a object.
    Responsibility:
    """
    class DevicesList(list):
        """DevicesList

        DevicesList is a list.
        Responsibility:
        """

    def __init__(self, token, secret):
        """

        @Arguments:
        - `token`:
        - `secret`:
        """
        self.client = SwitchBotClient(token, secret)

    def list_devices(self, ):
        """SUMMARY

        list_devices()

        @Return:

        @Error:
        """
        response = self.client.get('devices')
        body = response.get('body', None)
        if body is None:
            return DevicesList()
        device_list = body.get('deviceList', None)
        if device_list is None:
            return DevicesList()

        return device_list

    def list_remotes(self, ):
        """SUMMARY

        list_remotes()

        @Return:

        @Error:
        """
        # require

        # do

        # ensure

        return

    def list_scenes(self, ):
        """SUMMARY

        list_scenes()

        @Return:

        @Error:
        """
        # require

        # do

        # ensure

        return



def _main():
    ACCESS_TOKEN = '719b163c91b46336c15e913d025c3a88f5f3d01a3f9a11f3f745c7b3979ef6d0f7335a786697919d3404f57ee62ebc4e'
    SECRET = '6396816de07e242d39c171cf8e7b572a'
    s = SwitchBot(ACCESS_TOKEN, SECRET)
    print(s.list_devices())
    return 0

if __name__ == '__main__':
    sys.exit(_main())
