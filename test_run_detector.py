import unittest
from run_detector import detect_runs

class TestRunDetector(unittest.TestCase):
    def test_positive_run_sell_signal(self):
        prices = [10, 11, 12, 13, 14]
        # Run length of 2 means we need 2 consecutive increases.
        # i=0 (10): None
        # i=1 (11): None (run=1)
        # i=2 (12): 'SELL' (run=2)
        # i=3 (13): 'SELL' (run=3)
        # i=4 (14): 'SELL' (run=4)
        signals = detect_runs(prices, 2)
        self.assertEqual(signals, [None, None, 'SELL', 'SELL', 'SELL'])

    def test_negative_run_buy_signal(self):
        prices = [20, 19, 18, 17]
        # Run length of 3 means we need 3 consecutive decreases.
        # i=0 (20): None
        # i=1 (19): None (run=-1)
        # i=2 (18): None (run=-2)
        # i=3 (17): 'BUY' (run=-3)
        signals = detect_runs(prices, 3)
        self.assertEqual(signals, [None, None, None, 'BUY'])

    def test_mixed_runs(self):
        prices = [10, 11, 12, 11, 10, 9]
        # run_length = 2
        # i=0 (10): None
        # i=1 (11): None (run=1)
        # i=2 (12): 'SELL' (run=2)
        # i=3 (11): None (run=-1, reset because decrease)
        # i=4 (10): 'BUY' (run=-2)
        # i=5 (9): 'BUY' (run=-3)
        signals = detect_runs(prices, 2)
        self.assertEqual(signals, [None, None, 'SELL', None, 'BUY', 'BUY'])

    def test_flat_run_reset(self):
        prices = [10, 11, 11, 12, 13]
        # run_length = 2
        # i=0 (10): None
        # i=1 (11): None (run=1)
        # i=2 (11): None (run=0, flat)
        # i=3 (12): None (run=1)
        # i=4 (13): 'SELL' (run=2)
        signals = detect_runs(prices, 2)
        self.assertEqual(signals, [None, None, None, None, 'SELL'])

    def test_invalid_run_length(self):
        with self.assertRaises(ValueError):
            detect_runs([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            detect_runs([1, 2, 3], -1)

if __name__ == '__main__':
    unittest.main()
