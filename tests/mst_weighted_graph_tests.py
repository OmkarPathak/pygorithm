import unittest

from pygorithm.minimun_spanning_tree import kruskal


class KruskalTest(unittest.TestCase):
    def test_get_nodes(self):
        edge_weighted = [((1, 3), 5), ((2, 4), 10), ((4, 1), 4)]
        nodes = kruskal.get_nodes(edge_weighted)
        expected = {1, 2, 3, 4}
        self.assertEqual(nodes, expected)

    def test_has_cycle(self):
        edge_weighted = [((1, 3), 5), ((3, 4), 10), ((4, 1), 4)]
        self.assertTrue(kruskal.has_cycle(edge_weighted))

    def test_has_not_cycle(self):
        edge_weighted = [((1, 3), 5), ((2, 4), 10), ((4, 1), 4)]
        self.assertFalse(kruskal.has_cycle(edge_weighted))

    def test_has_cycle_2(self):
        edge_weighted = [((1, 3), 5), ((3, 2), 5), ((3, 4), 10), ((4, 1), 4)]
        self.assertTrue(kruskal.has_cycle(edge_weighted))

    def test_has_cycle_3(self):
        edge_weighted = [((2, 3), 8), ((1, 4), 5), ((3, 5), 5), ((4, 6), 6), ((1, 2), 7), ((2, 5), 7)]
        self.assertTrue(kruskal.has_cycle(edge_weighted))

    def test_minimum_spanning_tree(self):
        """
        test taken from the example at the following link: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
        """
        edge_weighted = [((1, 2), 7), ((2, 3), 8), ((1, 4), 5), ((2, 4), 9),
                         ((2, 5), 7), ((3, 5), 5), ((4, 6), 6), ((5, 6), 8),
                         ((5, 7), 9), ((6, 7), 11), ((4, 5), 15)]
        expected = [((1, 4), 5), ((3, 5), 5), ((4, 6), 6), ((1, 2), 7), ((2, 5), 7), ((5, 7), 9)]
        self.assertEqual(kruskal.minimum_spanning_tree(edge_weighted), expected)
