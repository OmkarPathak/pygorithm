import unittest

from pygorithm.searching import (linear_search,
                                  binary_search,
                                  breadth_first_search,
                                  depth_first_search)

class SearchingAlgorithmTest(unittest.TestCase):
    def setUp(self):
        # to test numeric numbers
        self.array = list(range(15))

        # to test alphabets
        string = 'pythonisawesome'
        self.alphaArray = list(string)

class LinearSearch(SearchingAlgorithmTest):
    def test_linear_search(self):
        result = linear_search.search(self.array, 7)
        self.assertIs(result, 7)

        alpha_result = linear_search.search(self.alphaArray, 'n')
        self.assertIs(alpha_result, 5)

        alpha_result = linear_search.search(self.array, 'n')
        self.assertIs(alpha_result, -1)

class BinarySearch(SearchingAlgorithmTest):
    def test_binary_search(self):
        result = binary_search.search(self.array, 7)
        self.assertIs(result, 7)

        alpha_result = binary_search.search(self.alphaArray, 'n')
        self.assertIs(alpha_result, 5)

        alpha_result = binary_search.search(self.array, 'n')
        self.assertIs(alpha_result, -1)

class BFSSearch(unittest.TestCase):
    def test_bfs(self):
        self.graph = {
            'A': {'B', 'C', 'E'},
            'B': {'A', 'D', 'F'},
            'C': {'A', 'G'},
            'D': {'B'},
            'F': {'B'},
            'E': {'A'},
            'G': {'C'}
        }
        result = breadth_first_search.bfs(self.graph, 'A')
        self.assertEqual(result, {'A', 'B', 'D', 'F', 'C', 'G', 'E'})
        result = breadth_first_search.bfs(self.graph, 'G')
        self.assertEqual(result, {'G', 'C', 'A', 'B', 'D', 'F', 'E'})

class DFSSearch(unittest.TestCase):
    def test_dfs(self):
        self.graph = {
            'A': ['B', 'C', 'E'],
            'B': ['A', 'D', 'F'],
            'C': ['A', 'G'],
            'D': ['B'],
            'F': ['B'],
            'E': ['A'],
            'G': ['C']
        }
        result = depth_first_search.dfs(self.graph, 'A')
        self.assertEqual(result, ['A', 'B', 'D', 'F', 'C', 'G', 'E'])
        result = depth_first_search.dfs(self.graph, 'G')
        self.assertEqual(result, ['G', 'C', 'A', 'B', 'D', 'F', 'E'])

if __name__ == '__main__':
    unittest.main()
