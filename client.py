import sys
import time
import uuid
import hmac
import base64
import hashlib
import urllib.parse

import requests


class SwitchBotClient(object):
    """SwitchBotClient

    SwitchBotClient is a object.
    Responsibility:
    """

    BASE_URL = "https://api.switch-bot.com/v1.1/"

    def __init__(self, token, secret):
        """

        @Arguments:
        - `token`:
        - `secret`:
        """
        self.token = token
        self.secret = secret

    def _headers(self, ):
        """SUMMARY

        _header()

        @Return:

        @Error:
        """
        timestamp = int(round(time.time() * 1000))
        nonce = str(uuid.uuid4())
        message = '{}{}{}'.format(self.token, timestamp, nonce)
        signature = base64.b64encode(
            hmac.new(self.secret.encode(), msg=message.encode(),
                     digestmod=hashlib.sha256).digest()
        )
        header = {}
        header['Authorization'] = self.token
        header['Content-Type'] = 'application/json'
        header['charset'] = 'utf8'
        header['t'] = str(timestamp)
        header['sign'] = signature
        header['nonce'] = nonce
        return header

    def request(self, method, subpath, **kwargs):
        """SUMMARY

        request(method, subpath)

        @Arguments:
        - `method`:
        - `subpath`:

        @Return:

        @Error:
        """
        url = urllib.parse.urljoin(self.BASE_URL, subpath)
        response = requests.request(method, url, headers=self._headers(), **kwargs)
        if response.ok != True:
            raise RuntimeError("Response status {}".format(response.status_code))
        return response.json()

    def get(self, subpath, **kwargs):
        """SUMMARY

        get(subpath)

        @Arguments:
        - `subpath`:
        - `kwargs`:

        @Return:

        @Error:
        """
        return self.request("GET", subpath, **kwargs)

    def post(self, subpath, **kwargs):
        """SUMMARY

        post(subpath)

        @Arguments:
        - `subpath`:

        @Return:

        @Error:
        """
        return self.request("POST", subpath, **kwargs)

    def put(self, subpath, **kwargs):
        """SUMMARY

        put(subpath)

        @Arguments:
        - `subpath`:

        @Return:

        @Error:
        """
        return self.request("PUT", subpath, **kwargs)

    def delete(self, subpath, **kwargs):
        """SUMMARY

        delete(subpath)

        @Arguments:
        - `subpath`:
        - `subpath`:

        @Return:

        @Error:
        """
        return self.request("DELETE", subpath, **kwargs)
