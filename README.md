mtmr_finance
============

Shows summary balances (in USD) on [MTMR](https://github.com/Toxblh/MTMR) bar from different markets

Sources
-------

### Tinkoff Invest [OpenAPI](https://github.com/TinkoffCreditSystems/invest-openapi/)

  Input env:
  ```shell
  TINKOFF_OPENAPI_TOKEN
  ```

  MTMR:
  ```json
  {
    "type": "shellScriptTitledButton",
    "width": 130,
    "refreshInterval": 300,
    "source": {
      "inline": "source ~/.zshrc && `which python3` $HOME/mtmr_finance/tcs_balance.py"
    },
    "actions": [],
    "align": "right",
    "bordered": true
  }
  ```

### [Bittrex API](https://bittrex.github.io/api/v3)

  Input env:
  ```shell
  BITTREX_READ_KEY
  BITTREX_READ_SECRET
  ```

  MTMR:
  ```json
  {
      "type": "shellScriptTitledButton",
      "width": 130,
      "refreshInterval": 300,
      "source": {
        "inline": "source ~/.zshrc && `which python3` $HOME/mtmr_finance/bittrex_balance.py"
      },
      "actions": [],
      "align": "right",
      "bordered": true,
    }
  ```

Installation
------------

```shell
brew install python@3.8
git clone https://github.com/a0s/mtmr_finance.git
```
