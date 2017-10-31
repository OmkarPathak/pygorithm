import unittest
import random

from pygorithm.sorting import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    counting_sort,
    bucket_sort,
    shell_sort,
    heap_sort,
    radix_sort)


class TestSortingAlgorithm(unittest.TestCase):
    def setUp(self):
        # to test numeric numbers
        self.array = list(range(15))
        random.shuffle(self.array)
        self.sorted_array = list(range(15))

        # to test alphabets
        string = 'pythonisawesome'
        self.alphaArray = list(string)
        random.shuffle(self.alphaArray)
        self.sorted_alpha_array = sorted(string)


class TestBubbleSort(TestSortingAlgorithm):
    def test_bubble_sort(self):
        self.result = bubble_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = bubble_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestInsertionSort(TestSortingAlgorithm):
    def test_insertion_sort(self):
        self.result = insertion_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = insertion_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestSelectionSort(TestSortingAlgorithm):
    def test_selection_sort(self):
        self.result = selection_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = selection_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestMergeSort(TestSortingAlgorithm):
    def test_merge_sort(self):
        self.result = merge_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = merge_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestQuickSort(TestSortingAlgorithm):
    def test_quick_sort(self):
        self.result = quick_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = quick_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestCountingSort(TestSortingAlgorithm):
    def test_counting_sort(self):
        # counting sort is an integer based sort
        self.result = counting_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)


class TestBucketSort(TestSortingAlgorithm):
    def test_bucket_sort(self):
        self.result = bucket_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = bucket_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestShellSort(TestSortingAlgorithm):
    def test_shell_sort(self):
        self.result = shell_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = shell_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestHeapSort(TestSortingAlgorithm):
    def test_heap_sort(self):
        self.result = heap_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = heap_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


class TestRadixSort(TestSortingAlgorithm):
    def test_radix_sort(self):
        self.result = radix_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        # TODO: Fix radix sort to sort alphabetically
        # self.alphaResult = radix_sort.sort(self.alphaArray)
        # self.assertEqual(self.alphaResult, self.sorted_alpha_array)


if __name__ == '__main__':
    unittest.main()
