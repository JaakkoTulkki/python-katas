import unittest

from datastuff.spread import Weather

class TestDataStuff(unittest.TestCase):

    def setUp(self):
        self.weather = Weather('./weather.dat')

    def test_calculates_spread_correctly(self):
        min_t = 81
        max_t = 91

        expected_spread = 10
        actual_spread = self.weather.spread(min_t, max_t)

        self.assertEqual(expected_spread, actual_spread)

    def test_opens_file_correctly(self):
        data = self.weather.open_file()
        self.assertTrue(isinstance(data, list), data)
        self.assertTrue(data)
