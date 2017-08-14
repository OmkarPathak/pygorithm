import unittest

from pygorithm.minimun_spanning_tree import kruskal


class KruskalTest(unittest.TestCase):

    def test_minimum_spanning_tree(self):
        """
        test inspired from the example at the following link: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
        """
        edges_weighted = [((1, 2), 7), ((2, 3), 8), ((1, 4), 5), ((2, 4), 9),
                         ((2, 5), 7), ((3, 5), 5), ((4, 6), 6), ((5, 6), 8),
                         ((5, 7), 9), ((6, 7), 11), ((4, 5), 15)]
        expected = [((1, 4), 5), ((3, 5), 5), ((4, 6), 6), ((1, 2), 7), ((2, 5), 7), ((5, 7), 9)]
        self.assertEqual(kruskal.minimum_spanning_tree(edges_weighted), expected)

    def test_minimum_spanning_tree_2(self):
        """
        Test inspired by the gif at the left of the page https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
        """
        edges_weighted = [((1,2), 3), ((1, 5), 1), ((2, 5), 4), ((2, 3), 5), ((3, 5), 6), ((3, 4), 2), ((4, 5), 7)]
        expected = [((1, 5), 1), ((3, 4), 2), ((1, 2), 3), ((2, 3), 5)]
        self.assertEqual(kruskal.minimum_spanning_tree(edges_weighted), expected)
