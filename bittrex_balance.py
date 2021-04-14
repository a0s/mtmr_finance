import time
import os
import hmac
import hashlib
import json
from lib import bittrex

btx = bittrex.Bittrex(os.environ["BITTREX_READ_KEY"], os.environ["BITTREX_READ_SECRET"])

account_balance_usdt = 0.0
account_balance_btc = 0.0

tickers_arr = btx.get_tickers()
tickers = {}
for ticker in tickers_arr:
    tickers[ticker["symbol"]] = ticker

balances_arr = btx.get_balances()
for balance in balances_arr:
    total = float(balance["total"])
    ticker = balance["currencySymbol"]

    if total < 0.0000000001:
        continue

    ticker_usd = "%s-USD" % (ticker,)
    ticker_usdt = "%s-USDT" % (ticker,)
    ticker_btc = "%s-BTC" % (ticker,)

    # currency -> usdt -> usd
    if ticker == "USD":
        account_balance_usdt += total

    elif ticker_usd in tickers:
        account_balance_usdt += float(total) * float(
            tickers[ticker_usd]["lastTradeRate"]
        )

    elif (ticker_usdt in tickers) and ("USDT-USD" in tickers):
        account_balance_usdt += (
            float(total)
            * float(tickers[ticker_usdt]["lastTradeRate"])
            * float(tickers["USDT-USD"]["lastTradeRate"])
        )

    elif (ticker_btc in tickers) and ("BTC-USD" in tickers):
        account_balance_usdt += (
            float(total)
            * float(tickers[ticker_btc]["lastTradeRate"])
            * float(tickers["BTC-USD"]["lastTradeRate"])
        )

    # currency -> btc -> usd
    if ticker == "USD":
        account_balance_btc += total

    elif ticker_usd in tickers:
        account_balance_btc += float(total) * float(
            tickers[ticker_usd]["lastTradeRate"]
        )

    elif (ticker_btc in tickers) and ("BTC-USD" in tickers):
        account_balance_btc += (
            float(total)
            * float(tickers[ticker_btc]["lastTradeRate"])
            * float(tickers["BTC-USD"]["lastTradeRate"])
        )

    elif (ticker_usdt in tickers) and ("USDT-USD" in tickers):
        account_balance_btc += (
            float(total)
            * float(tickers[ticker_usdt]["lastTradeRate"])
            * float(tickers["USDT-USD"]["lastTradeRate"])
        )

print(
    "Bittrex\n$%.2f | $%.2f"
    % (
        account_balance_usdt,
        account_balance_btc,
    )
)
