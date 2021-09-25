import json
import os
from lib import bittrex, miningpoolhub

total = 0.0

btx = bittrex.Bittrex(os.environ["BITTREX_READ_KEY"], os.environ["BITTREX_READ_SECRET"])
eth_ticker = json.loads(
    btx.request("https://api.bittrex.com/api/v1.1/public/getticker?market=USD-ETH")
)
eth_currency = eth_ticker["result"]["Ask"]

# rvn = rvn.Ravencoin()
# for wallet in os.environ["RVN_WALLETS"].split(","):
#     total += rvn.amount(wallet)

mining = miningpoolhub.Miningpoolhub(os.environ["MININGPOOLHUB_API_TOKEN"])
hashrate = mining.eth_hashrate()
total += mining.eth_balance()

print(
    "ETH %.0f/MHs\n$%.2f"
    % (
        hashrate,
        total * eth_currency,
    )
)
