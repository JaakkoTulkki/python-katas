import unittest
from datastuff.football import goal_diff, print_smallest_difference

class TestFootball(unittest.TestCase):

    def test_returns_absolute_difference_correctly(self):
        expected_diff = 3
        actual = goal_diff(4, 7)
        self.assertEqual(actual, expected_diff)

        expected_diff = 2
        actual = goal_diff(6, 4)
        self.assertEqual(actual, expected_diff)

    def test_prints_one_with_one_with_lowest_difference(self):
        self.assertEqual("The team with the smallest difference is Aston_Villa with a difference of 1", print_smallest_difference())



