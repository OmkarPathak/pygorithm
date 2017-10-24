# -*- coding: utf-8 -*-
import unittest

from pygorithm.dynamic_programming import (
    binary_knapsack,
    lis,
    min_cost_path
    )


class TestBinaryKnapsack(unittest.TestCase):
    def test_binary_knapsack(self):
        value = [60, 100, 120]
        weight = [10, 20, 30]
        W = 50
        self.assertEqual(binary_knapsack.knapsack(W, value, weight), 220)

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_lis(self):
        _list = [10, 22, 9, 33, 21, 50, 41, 60]
        ans = lis.longest_increasing_subsequence(_list)
        self.assertEqual(ans[0], 5)
        self.assertEqual(ans[1], [10, 22, 33, 50, 60])

class TestMinCostPath(unittest.TestCase):
    def test_min_cost_path(self):
        matrix = [[5, 3, 10, 17, 1],
                  [4, 2, 9, 8, 5],
                  [11, 12, 3, 9, 6],
                  [1, 3, 4, 2, 10],
                  [7, 11, 13, 7, 3]]
        self.assertEqual(min_cost_path.find_path(matrix), 38)

if __name__ == '__main__':
    unittest.main()
