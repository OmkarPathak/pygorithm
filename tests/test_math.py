import unittest

from pygorithm.math import (
    lcm,
    sieve_of_eratosthenes)

class TestLCM(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm.lcm([3, 12, 16]), 48)

class TestSieveOfEratosthenes(unittest.TestCase):
    def test_sieve_of_eratosthenes(self):
        self.assertEqual(sieve_of_eratosthenes.sieve_of_eratosthenes(10), [2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()
