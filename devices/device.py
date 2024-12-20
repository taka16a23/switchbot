import sys
class Device(object):
    """Device

    Device is a object.
    Responsibility:
    """
    DEVICE_NAME = ''

    def __init__(self, client, device_id, device_type='', cloud_enabled=None, hub_id=''):
        """

        @Arguments:
        - `client`:
        - `device_id`:
        - `device_name`:
        - `device_type`:
        - `cloud_enabled`:
        - `hub_id`:
        """
        self._client = client
        self.device_id = device_id
        self.device_name = self.DEVICE_NAME
        self.device_type = device_type
        self.cloud_enabled = cloud_enabled
        self.hub_id = hub_id

    def status(self, ):
        """SUMMARY

        status()

        @Return:

        @Error:
        """
        response = self._client.get('devices/{}/status'.format(self.device_id))
        return {key: value for key, value in response["body"].items()}

    def command(self, action, parameter='default'):
        """SUMMARY

        command(action, parameter='default')

        @Arguments:
        - `action`:
        - `parameter`:

        @Return:

        @Error:
        """
        json = {
            "commandType": "command",
            "command": action,
            "parameter": parameter,
        }
        return self._client.post('devices/{}/commands'.format(self.device_id), json=json)

    def __repr__(self):
        return '{}(device_id={}, device_name={}, device_type={}, cloud_enabled={}, hub_id={})'.format(self.__class__.__name__, self.device_name, self.device_type, self.device_type, self.cloud_enabled, self.hub_id)


def _main():
    from switchbot.client import SwitchBotClient
    ACCESS_TOKEN='719b163c91b46336c15e913d025c3a88f5f3d01a3f9a11f3f745c7b3979ef6d0f7335a786697919d3404f57ee62ebc4e'
    SECRET='6396816de07e242d39c171cf8e7b572a'
    sbc = SwitchBotClient(ACCESS_TOKEN, SECRET)
    d = Device(sbc, device_id='F0F5BDC1C6FE')
    print(d.status())
    return 0

if __name__ == '__main__':
    sys.exit(_main())
