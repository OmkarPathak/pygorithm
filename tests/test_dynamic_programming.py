# -*- coding: utf-8 -*-
import unittest

from pygorithm.dynamic_programming import (
    binary_knapsack,
    lis
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

if __name__ == '__main__':
    unittest.main()
