import urllib
import json


class TCS:
    def __init__(self, token):
        self.token = token

    def get_portfolio(self):
        url = "https://api-invest.tinkoff.ru/openapi/portfolio"
        headers = {"Authorization": "Bearer %s" % (self.token,)}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        raw = response.read().decode("utf-8")
        return json.loads(raw)

    def get_portfolio_currencies(self):
        url = "https://api-invest.tinkoff.ru/openapi/portfolio/currencies"
        headers = {"Authorization": "Bearer %s" % (self.token,)}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        raw = response.read().decode("utf-8")
        return json.loads(raw)

    def get_orderbook(self, figi, depth=1):
        url = (
            "https://api-invest.tinkoff.ru/openapi/market/orderbook?figi=%s&depth=%i"
            % (
                figi,
                depth,
            )
        )
        headers = {"Authorization": "Bearer %s" % (self.token,)}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        raw = response.read().decode("utf-8")
        return json.loads(raw)
