import unittest

from pygorithm.math import (
    lcm,
    lcm_using_gcd,
    sieve_of_eratosthenes,
    factorial,
    conversion,
    matrix_operations)

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

class TestMatrixOperations(unittest.TestCase):
    def test_matrix_addition(self):
        X = [[12,7,3],
            [4 ,5,6],
            [7 ,8,9]]

        Y = [[5,8,1],
            [6,7,3],
            [4,5,9]]

        matrix = matrix_operations.Matrix(X, Y)
        self.assertEqual(matrix.add(), [[17, 15, 4], [10, 12, 9], [11, 13, 18]])


    def test_matrix_subtraction(self):
        X = [[12,7,3],
            [4,5,6],
            [7,8,9]]

        Y = [[5,8,1],
            [6,7,3],
            [4,5,9]]

        matrix = matrix_operations.Matrix(X, Y)
        self.assertEqual(matrix.subtract(), [[7, -1, 2], [-2, -2, 3], [3, 3, 0]])


    def test_matrix_multiplication(self):
        X = [[12,7,3],
            [4,5,6],
            [7,8,9]]

        Y = [[5,8,1,2],
            [6,7,3,0],
            [4,5,9,1]]

        matrix = matrix_operations.Matrix(X, Y)
        self.assertEqual(matrix.multiply(), [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]])


    def test_matrix_transpose(self):
        X = [[12,7],
            [4 ,5],
            [3 ,8]]

        matrix = matrix_operations.Matrix(X)
        self.assertEqual(matrix.transpose(), [[12, 4, 3],[7, 5, 8]])


    def test_matrix_rotate(self):
        X =[[1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]]

        matrix = matrix_operations.Matrix(X)
        self.assertEqual(matrix.rotate(), [[5, 1, 2, 3], [9, 10, 6, 4], [13, 11, 7, 8], [14, 15, 16, 12]])


    def test_matrix_unique_paths(self):
        matrix = matrix_operations.Matrix()
        self.assertEqual(matrix.count_unique_paths(3, 3), 6)

    def test_matrix_exceptions(self):
        X = [[12,7,3],
            [4,5,6],
            [7,8,9]]

        Y = [[5,8],
            [6,7],
            [4,5]]

        matrix = matrix_operations.Matrix(X, Y)

        # test exception
        self.assertRaises(Exception, matrix.add)
        self.assertRaises(Exception, matrix.subtract)

if __name__ == '__main__':
    unittest.main()
