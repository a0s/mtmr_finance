import time
import os
import hmac
import hashlib
import urllib.request
import json


class Bittrex:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def request(self, url):
        headers = {}
        headers["Api-Key"] = self.api_key
        headers["Api-Timestamp"] = int(time.time() * 1000)
        headers["Api-Content-Hash"] = hashlib.sha512("".encode()).hexdigest()

        preSign = "".join(
            [str(headers["Api-Timestamp"]), url, "GET", headers["Api-Content-Hash"]]
        )

        headers["Api-Signature"] = hmac.new(
            bytearray(self.api_secret.encode()),
            bytearray(preSign.encode()),
            hashlib.sha512,
        ).hexdigest()

        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        return html

    def get_tickers(self):
        url = "https://api.bittrex.com/v3/markets/tickers"
        return json.loads(self.request(url))

    def get_balances(self):
        url = "https://api.bittrex.com/v3/balances"
        return json.loads(self.request(url))