import unittest
from datetime import datetime

from pyetheroll.utils import EtherollUtils, timestamp2datetime


class TestEtherollUtils(unittest.TestCase):

    def test_compute_profit(self):
        bet_size = 0.10
        chances_win = 34
        payout = EtherollUtils.compute_profit(bet_size, chances_win)
        self.assertEqual(payout, 0.19)
        bet_size = 0.10
        # chances of winning must be less than 100%
        chances_win = 100
        payout = EtherollUtils.compute_profit(bet_size, chances_win)
        self.assertEqual(payout, None)


class TestUtils(unittest.TestCase):

    def test_timestamp2datetime(self):
        self.assertEqual(
            timestamp2datetime('1566645978'),
            datetime(2019, 8, 24, 11, 26, 18)
        )
        self.assertEqual(
            timestamp2datetime('0x5d611eda'),
            datetime(2019, 8, 24, 11, 26, 18)
        )
