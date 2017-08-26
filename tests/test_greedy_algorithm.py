# -*- coding: utf-8 -*-
import unittest

from pygorithm.greedy_algorithm import (
    fractional_knapsack,
    )


class TestFractionalKnapsack(unittest.TestCase):
    def test_fractional_knapsack(self):
        value = [60, 100, 120]
        weight = [10, 20, 30]
        W = 50
        self.assertEqual(fractional_knapsack.knapsack(W, value, weight), 240)

if __name__ == '__main__':
    unittest.main()
