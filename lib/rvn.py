import urllib.request
import json


class Ravencoin:
    def amount(self, address):
        url = "https://ravencoin.network/api/addr/%s/?noTxList=1" % (address,)

        headers = {}
        headers["authority"] = "ravencoin.network"
        headers["pragma"] = "no-cache"
        headers["cache-control"] = "no-cache"
        headers[
            "sec-ch-ua"
        ] = '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"'
        headers["accept"] = "application/json, text/plain, */*"
        headers["dnt"] = "1"
        headers["sec-ch-ua-mobile"] = "?0"
        headers[
            "user-agent"
        ] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        headers["sec-fetch-site"] = "same-origin"
        headers["sec-fetch-mode"] = "cors"
        headers["sec-fetch-dest"] = "empty"
        headers["referer"] = "https://ravencoin.network/"
        headers["accept-language"] = "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7"

        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        raw = response.read().decode("utf-8")
        balance = json.loads(raw)["balance"]
        return balance
