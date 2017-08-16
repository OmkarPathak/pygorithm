"""
Test for Fibonacci implementations logic.
"""

import unittest

from pygorithm.fibonacci import generator, goldenratio, memoization, recursion


class TestFibonacciImplementations(unittest.TestCase):
    """
    Tests for Fibonacci implementations.
    """

    def test_implementations_same_result(self):
        """
        Verify that all implementations have same result.
        """
        fibonacci_implementations = [generator, goldenratio, memoization, recursion]

        for implementation in fibonacci_implementations:
            result = getattr(implementation, 'get_sequence')(0)
            self.assertEqual([0], result)

            result = getattr(implementation, 'get_sequence')(1)
            self.assertEqual([0, 1], result)

            result = getattr(implementation, 'get_sequence')(10)
            self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], result)

if __name__ == '__main__':
    unittest.main()
