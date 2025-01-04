import sys


class Device(object):
    """Device

    Device is a object.
    Responsibility:
    """
    DEVICE_TYPE = ''

    def __init__(self, client, device_id, device_name='', cloud_enabled=None, hub_id=''):
        """

        @Arguments:
        - `client`:
        - `device_id`:
        - `device_name`:
        - `cloud_enabled`:
        - `hub_id`:
        """
        self._client = client
        self.device_id = device_id
        self.device_name = device_name
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
        return '{}(device_id={}, device_name={}, DEVICE_TYPE={}, cloud_enabled={}, hub_id={})'.format(
            self.__class__.__name__, self.device_id, self.device_name, self.DEVICE_TYPE, self.cloud_enabled, self.hub_id)
