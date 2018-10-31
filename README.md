# pyetheroll

[![Build Status](https://travis-ci.com/AndreMiras/pyetheroll.svg?branch=develop)](https://travis-ci.com/AndreMiras/pyetheroll)

Python library to Etheroll smart contract


## Usage

Simply set bet size, chances and wallet settings before rolling:
```python
from pyetheroll.etheroll import Etheroll

etheroll = Etheroll()
bet_size_ether = 0.1
chances = 50
wallet_path = 'wallet.json'
wallet_password = 'password'

transaction = etheroll.player_roll_dice(
    bet_size_ether, chances, wallet_path, wallet_password)
```

It's also possible to set different contract address and chain ID:
```python
from pyetheroll.constants import ChainID
from pyetheroll.etheroll import Etheroll

chain_id = ChainID.ROPSTEN
contract_address = '0xe12c6dEb59f37011d2D9FdeC77A6f1A8f3B8B1e8'
etheroll = Etheroll(chain_id, contract_address)
```

## Install

[Latest stable release](https://github.com/AndreMiras/pyetheroll/tree/master):
```sh
pip install --process-dependency-links \
https://github.com/AndreMiras/pyetheroll/archive/master.zip
```

[Development branch](https://github.com/AndreMiras/pyetheroll/tree/develop):
```sh
pip install --process-dependency-links \
https://github.com/AndreMiras/pyetheroll/archive/develop.zip
```
