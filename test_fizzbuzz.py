import unittest

from fizzbuzz import print_fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_input_less_than_1(self):
        self.assertEqual(print_fizzbuzz(-1), "n must be greater than 0")

    def test_input_greater_than_0(self):
        self.assertEqual(
            print_fizzbuzz(15),
            "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz",
        )
