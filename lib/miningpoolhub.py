import time
import os
import json
import urllib.request


class Miningpoolhub:
    def __init__(self, api_key):
        self.api_key = api_key

    def headers(self):
        headers = {}
        headers["authority"] = "ravencoin.miningpoolhub.com"
        headers["pragma"] = "no-cache"
        headers["cache-control"] = "no-cache"
        headers[
            "sec-ch-ua"
        ] = '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"'
        headers["sec-ch-ua-mobile"] = "?0"
        headers["dnt"] = "1"
        headers["upgrade-insecure-requests"] = "1"
        headers[
            "user-agent"
        ] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        headers[
            "accept"
        ] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        headers["sec-fetch-site"] = "none"
        headers["sec-fetch-mode"] = "navigate"
        headers["sec-fetch-user"] = "?1"
        headers["sec-fetch-dest"] = "document"
        headers["accept-language"] = "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7"
        return headers

    def rvn_hashrate(self):
        url = (
            "https://ravencoin.miningpoolhub.com/index.php?page=api&api_key=%s&action=getuserhashrate"
            % (self.api_key,)
        )
        request = urllib.request.Request(url, headers=self.headers())
        response = urllib.request.urlopen(request)
        raw = response.read().decode("utf-8")
        hashrate = json.loads(raw)["getuserhashrate"]["data"]
        return hashrate

    def rvn_balance(self):
        url = (
            "https://ravencoin.miningpoolhub.com/index.php?page=api&api_key=%s&action=getuserbalance"
            % (self.api_key,)
        )
        request = urllib.request.Request(url, headers=self.headers())
        response = urllib.request.urlopen(request)
        raw = response.read().decode("utf-8")
        balance = json.loads(raw)["getuserbalance"]["data"]["confirmed"]
        return balance

    def eth_hashrate(self):
        url = (
            "https://ethereum.miningpoolhub.com/index.php?page=api&api_key=%s&action=getuserhashrate"
            % (self.api_key,)
        )
        request = urllib.request.Request(url, headers=self.headers())
        response = urllib.request.urlopen(request)
        raw = response.read().decode("utf-8")
        hashrate = json.loads(raw)["getuserhashrate"]["data"]
        return hashrate

    def eth_balance(self):
        url = (
            "https://ethereum.miningpoolhub.com/index.php?page=api&api_key=%s&action=getuserbalance"
            % (self.api_key,)
        )
        request = urllib.request.Request(url, headers=self.headers())
        response = urllib.request.urlopen(request)
        raw = response.read().decode("utf-8")
        balance = json.loads(raw)["getuserbalance"]["data"]["confirmed"]
        return balance
