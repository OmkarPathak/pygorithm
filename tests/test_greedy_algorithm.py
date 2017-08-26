# -*- coding: utf-8 -*-
import unittest

from pygorithm.greedy_algorithm import (
    fractional_knapsack,
    activity_selection,
    )


class TestFractionalKnapsack(unittest.TestCase):
    def test_fractional_knapsack(self):
        value = [60, 100, 120]
        weight = [10, 20, 30]
        W = 50
        self.assertEqual(fractional_knapsack.knapsack(W, value, weight), 240)

class TestActivitySelectionProblem(unittest.TestCase):
    def test_activity_selection(self):
        start_times = [1 , 3 , 0 , 5 , 8 , 5]
        finish_times = [2 , 4 , 6 , 7 , 9 , 9]

        self.assertEqual(activity_selection.activity_selection(start_times, finish_times), [0, 1, 3, 4])

if __name__ == '__main__':
    unittest.main()
