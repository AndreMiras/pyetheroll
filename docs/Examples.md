# Examples

Here is a list of common things the library can help with.

## Get address last rolls
Basically what you need is the `Etheroll.get_last_bets_transactions()` method.
See example [rolls2csv.py](rolls2csv.py) for a detailed example.

## Read contract
Access the web3 contract directly from the `Etheroll` instance:
```python
etheroll = Etheroll()
min_bet = etheroll.contract.functions.minBet().call()
```
