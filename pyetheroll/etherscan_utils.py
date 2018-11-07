import json
import logging
import os

from etherscan.accounts import Account as EtherscanAccount
from etherscan.contracts import Contract as EtherscanContract

from pyetheroll.constants import ChainID

logger = logging.getLogger(__name__)


def get_etherscan_api_key(api_key_path: str = None) -> str:
    """
    Tries to retrieve etherscan API key from path or from environment.
    The files content should be in the form:
    ```json
    { "key" : "YourApiKeyToken" }
    ```
    """
    DEFAULT_API_KEY_TOKEN = 'YourApiKeyToken'
    etherscan_api_key = os.environ.get('ETHERSCAN_API_KEY')
    if etherscan_api_key is not None:
        return etherscan_api_key
    elif api_key_path is None:
            logger.warning(
                'Cannot get Etherscan API key. '
                f'No path provided, defaulting to {DEFAULT_API_KEY_TOKEN}.')
            return DEFAULT_API_KEY_TOKEN
    else:
        try:
            with open(api_key_path, mode='r') as key_file:
                etherscan_api_key = json.loads(key_file.read())['key']
        except FileNotFoundError:
            logger.warning(
              f'Cannot get Etherscan API key. File {api_key_path} not found, '
              f'defaulting to {DEFAULT_API_KEY_TOKEN}.')
            return DEFAULT_API_KEY_TOKEN
    return etherscan_api_key


class RopstenEtherscanContract(EtherscanContract):
    """
    https://github.com/corpetty/py-etherscan-api/issues/24
    """
    PREFIX = 'https://api-ropsten.etherscan.io/api?'


class ChainEtherscanContractFactory:
    """
    Creates Contract class type depending on the chain ID.
    """

    CONTRACTS = {
        ChainID.MAINNET: EtherscanContract,
        ChainID.ROPSTEN: RopstenEtherscanContract,
    }

    @classmethod
    def create(cls, chain_id=ChainID.MAINNET):
        ChainEtherscanContract = cls.CONTRACTS[chain_id]
        return ChainEtherscanContract


class RopstenEtherscanAccount(EtherscanAccount):
    """
    https://github.com/corpetty/py-etherscan-api/issues/24
    """
    PREFIX = 'https://api-ropsten.etherscan.io/api?'


class ChainEtherscanAccountFactory:
    """
    Creates Account class type depending on the chain ID.
    """

    ACCOUNTS = {
        ChainID.MAINNET: EtherscanAccount,
        ChainID.ROPSTEN: RopstenEtherscanAccount,
    }

    @classmethod
    def create(cls, chain_id=ChainID.MAINNET):
        ChainEtherscanAccount = cls.ACCOUNTS[chain_id]
        return ChainEtherscanAccount
