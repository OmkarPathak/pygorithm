import unittest

from pygorithm.pathing import (dijkstra)

class TestDijkstra(unittest.TestCase):
    def test_exists(self):
        pather = dijkstra.Dijkstra()
        
        self.assertIsNotNone(pather)
        self.assertIsNotNone(pather.find_path)
        self.assertIsNotNone(pather.get_code)
    
    def test_find_path_package_example(self):
        # import the required pathing
        from pygorithm.pathing import dijkstra
        
        # import a graph data structure
        from pygorithm.data_structures import graph
        
        # initialize the graph with nodes from (0, 0) to (4, 4)
        # with weight corresponding to distance (orthogonal 
        # is 1, diagonal is sqrt(2))
        my_graph = graph.WeightedUndirectedGraph()
        my_graph.gridify(5, 1)
        
        # make the graph more interesting by removing along the 
        # x=2 column except for (2,4)
        my_graph.remove_edge((2, 0))
        my_graph.remove_edge((2, 1))
        my_graph.remove_edge((2, 2))
        my_graph.remove_edge((2, 3))
        
        # create a pathfinder
        my_pathfinder = dijkstra.Dijkstra()
        
        # calculate a path
        my_path = my_pathfinder.find_path(my_graph, (0, 0), (3, 0))
        
        # check path:
        expected_path = [ (0, 0), (0, 1), (0, 2), (1, 3), (2, 4), (3, 3), (3, 2), (3, 1), (3, 0) ]
        self.assertListEqual(expected_path, my_path)