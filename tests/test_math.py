import unittest

from pygorithm.math import (
    lcm,
    lcm_using_gcd,
    sieve_of_eratosthenes,
    factorial,
    conversion)

class TestLCM(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm.lcm([3, 12, 16]), 48)

    def test_lcm_using_gcd(self):
        self.assertEqual(lcm_using_gcd.lcm_using_gcd([3, 12, 16]), 48)

class TestSieveOfEratosthenes(unittest.TestCase):
    def test_sieve_of_eratosthenes(self):
        self.assertEqual(sieve_of_eratosthenes.sieve_of_eratosthenes(10), [2, 3, 5, 7])

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial.factorial(10), 3628800)

class TestConversion(unittest.TestCase):
    def test_dec_to_bin(self):
        self.assertEqual(conversion.decimal_to_binary(2), '10')

    def test_bin_to_dec(self):
        self.assertEqual(conversion.binary_to_decimal('1010'), 10)

    def test_dec_to_hex(self):
        self.assertEqual(conversion.decimal_to_hex(30), '1E')

    def test_hex_to_dex(self):
        self.assertEqual(conversion.hex_to_decimal('1E'), 30)

if __name__ == '__main__':
    unittest.main()
