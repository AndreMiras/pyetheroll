from etherscan.accounts import Account as EtherscanAccount
from etherscan.contracts import Contract as EtherscanContract

from pyetheroll.constants import ChainID


class RopstenEtherscanContract(EtherscanContract):
    """https://github.com/corpetty/py-etherscan-api/issues/24"""

    PREFIX = "https://api-ropsten.etherscan.io/api?"


class ChainEtherscanContractFactory:
    """Creates Contract class type depending on the chain ID."""

    CONTRACTS = {
        ChainID.MAINNET: EtherscanContract,
        ChainID.ROPSTEN: RopstenEtherscanContract,
    }

    @classmethod
    def create(cls, chain_id=ChainID.MAINNET):
        ChainEtherscanContract = cls.CONTRACTS[chain_id]
        return ChainEtherscanContract


class RopstenEtherscanAccount(EtherscanAccount):
    """https://github.com/corpetty/py-etherscan-api/issues/24"""

    PREFIX = "https://api-ropsten.etherscan.io/api?"


class ChainEtherscanAccountFactory:
    """Creates Account class type depending on the chain ID."""

    ACCOUNTS = {
        ChainID.MAINNET: EtherscanAccount,
        ChainID.ROPSTEN: RopstenEtherscanAccount,
    }

    @classmethod
    def create(cls, chain_id=ChainID.MAINNET):
        ChainEtherscanAccount = cls.ACCOUNTS[chain_id]
        return ChainEtherscanAccount
