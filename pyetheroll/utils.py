import os
from datetime import datetime

from pyetheroll.constants import (
    DEFAULT_ETHERSCAN_API_KEY,
    DEFAULT_INFURA_PROJECT_ID,
    ROUND_DIGITS,
)


class EtherollUtils:
    @staticmethod
    def compute_profit(bet_size, chances_win):
        """Helper method to compute profit given a bet_size and chances_win."""
        if chances_win <= 0 or chances_win >= 100:
            return
        house_edge = 1.0 / 100
        chances_loss = 100 - chances_win
        payout = ((chances_loss / chances_win) * bet_size) + bet_size
        payout *= 1 - house_edge
        profit = payout - bet_size
        profit = round(profit, ROUND_DIGITS)
        return profit


def timestamp2datetime(timestamp: str) -> datetime:
    """
    Converts a timestamp string to datetime.
    Handles both decimal and hexadecimal bases, this is needed since Etherscan
    API can return timestamps in both bases.
    https://www.reddit.com/r/etherscan/comments/cus1m8/
    >>> timestamp2datetime('1566645978')
    datetime.datetime(2019, 8, 24, 11, 26, 18)
    >>> timestamp2datetime('0x5d611eda')
    datetime.datetime(2019, 8, 24, 11, 26, 18)
    """
    base = 10
    if timestamp.startswith("0x"):
        base = 16
    date_time = datetime.utcfromtimestamp(int(timestamp, base))
    return date_time


def get_etherscan_api_key():
    """Returns ETHERSCAN_API_KEY from environment variable."""
    return os.environ.get("ETHERSCAN_API_KEY", DEFAULT_ETHERSCAN_API_KEY)


def get_infura_project_id():
    """Returns WEB3_INFURA_PROJECT_ID from environment variable."""
    return os.environ.get("WEB3_INFURA_PROJECT_ID", DEFAULT_INFURA_PROJECT_ID)
