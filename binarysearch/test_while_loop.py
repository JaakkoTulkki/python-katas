from .while_loop import chop
import unittest


class TestWhile(unittest.TestCase):

    def test_while(self):
        self.assertEqual(-1, chop(3, []))
        self.assertEqual(-1, chop(3, [1]))
        self.assertEqual(0, chop(1, [1]))

        self.assertEqual(0, chop(1, [1, 3, 5]))
        self.assertEqual(1, chop(3, [1, 3, 5]))
        self.assertEqual(2, chop(5, [1, 3, 5]))
        self.assertEqual(-1, chop(0, [1, 3, 5]))
        self.assertEqual(-1, chop(2, [1, 3, 5]))
        self.assertEqual(-1, chop(4, [1, 3, 5]))
        self.assertEqual(-1, chop(6, [1, 3, 5]))

        self.assertEqual(0, chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

        self.assertEqual(7, chop(13, [1, 3, 5, 7, 9, 10, 11, 13, 14]))
        self.assertEqual(8, chop(14, [1, 3, 5, 7, 9, 10, 11, 13, 14, 17, 19]))
