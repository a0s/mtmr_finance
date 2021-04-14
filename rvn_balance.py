import json
import os
from lib import bittrex, rvn, miningpoolhub

total = 0.0

btx = bittrex.Bittrex(os.environ["BITTREX_READ_KEY"], os.environ["BITTREX_READ_SECRET"])
rvn_ticker = json.loads(
    btx.request("https://api.bittrex.com/api/v1.1/public/getticker?market=USD-RVN")
)
rvn_currency = rvn_ticker["result"]["Ask"]

rvn = rvn.Ravencoin()
for wallet in os.environ["RVN_WALLETS"].split(","):
    total += rvn.amount(wallet)

mining = miningpoolhub.Miningpoolhub(os.environ["MININGPOOLHUB_API_TOKEN"])
hashrate = mining.rvn_hashrate()
total += mining.rvn_balance()

print(
    "RVN | %.0f/s\n$%.2f"
    % (
        hashrate,
        total * rvn_currency,
    )
)
