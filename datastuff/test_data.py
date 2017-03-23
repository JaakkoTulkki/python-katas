import unittest

from datastuff.spread import spread

class TestDataStuff(unittest.TestCase):

    def test_calculates_spread_correctly(self):
        min_t = 81
        max_t = 91

        expected_spread = 10
        actual_spread = spread(min_t, max_t)

        self.assertEqual(expected_spread, actual_spread)
