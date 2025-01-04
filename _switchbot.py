import sys
from switchbot.client import SwitchBotClient
from switchbot.device_factory import DeviceFactory


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
        list_result = SwitchBot.DevicesList()
        if body is None:
            return list_result
        device_list = body.get('deviceList', None)
        if device_list is None:
            return list_result
        list_result.extend([ x for x in [DeviceFactory.create(x, self.client) for x in device_list] if x is not None])
        return list_result

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
