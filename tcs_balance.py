import os
import urllib.request
import json
from lib import tcs


class File:
    def write(name, content):
        f = open(name, "w")
        f.write(content)
        f.close


token = os.environ["TINKOFF_OPENAPI_TOKEN"]
tcs = tcs.TCS(token)
portfolio = tcs.get_portfolio()
portfolio_currencies = tcs.get_portfolio_currencies()

total_usd = 0.0
total_rub = 0.0

for position in portfolio["payload"]["positions"]:
    if position["ticker"] == "USD000UTSTOM":
        continue

    orderbook = tcs.get_orderbook(position["figi"])

    if position["expectedYield"]["currency"] == "USD":
        total_usd += position["balance"] * orderbook["payload"]["lastPrice"]
    elif position["expectedYield"]["currency"] == "RUB":
        total_rub += position["balance"] * orderbook["payload"]["lastPrice"]

for portfolio_currency in portfolio_currencies["payload"]["currencies"]:
    if portfolio_currency["currency"] == "USD":
        total_usd += portfolio_currency["balance"]
    elif portfolio_currency["currency"] == "RUB":
        total_rub += portfolio_currency["balance"]


orderbook = tcs.get_orderbook("BBG0013HGFT4")
total_usd += total_rub / orderbook["payload"]["lastPrice"]

print("TCS\n$%.2f" % (total_usd,))
