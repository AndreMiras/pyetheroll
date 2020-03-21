from enum import Enum

ROUND_DIGITS = 2
DEFAULT_GAS_PRICE_GWEI = 4
DEFAULT_GAS_PRICE_WEI = int(DEFAULT_GAS_PRICE_GWEI * 1e9)
DEFAULT_ETHERSCAN_API_KEY = "YourApiKeyToken"
DEFAULT_INFURA_PROJECT_ID = "7c841c560b1e4660a9683507cb27b2f8"


class ChainID(Enum):
    MAINNET = 1
    MORDEN = 2
    ROPSTEN = 3
