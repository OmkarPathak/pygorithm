import unittest
import math
import time

from pygorithm.pathfinding import (dijkstra, astar)
from pygorithm.data_structures import graph

class TimedTestCase(unittest.TestCase):
    # https://hackernoon.com/timing-tests-in-python-for-fun-and-profit-1663144571
    def setUp(self):
        self._started_at = time.time()
    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))
        
class SimplePathfindingTestCaseTimed(TimedTestCase):
    def find_path(self, my_graph, v1, v2):
        return [ (0, 0), (0, 1), (0, 2), (1, 3), (2, 4), (3, 3), (3, 2), (3, 1), (3, 0) ]
    
    def test_find_path_package_example(self):
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
        
        # calculate a path
        my_path = self.find_path(my_graph, (0, 0), (3, 0))
        
        # check path:
        self.assertIsNotNone(my_path)
        
        total_weight = 0
        for i in range(1, len(my_path)):
            total_weight += my_graph.get_edge_weight(my_path[i - 1], my_path[i])
            
        self.assertAlmostEqual(9.242640687119284, total_weight)
        
class TestDijkstraTimed(SimplePathfindingTestCaseTimed):
    def find_path(self, my_graph, v1, v2):
       my_pathfinder = dijkstra.Dijkstra()
       return my_pathfinder.find_path(my_graph, (0, 0), (3, 0))

class TestAStarUnidirectionalTimed(SimplePathfindingTestCaseTimed):
    def find_path(self, my_graph, v1, v2):
        my_pathfinder = astar.OneDirectionalAStar()
        
        def my_heuristic(graph, v1, v2):
            dx = v2[0] - v1[0]
            dy = v2[1] - v1[1]
            return math.sqrt(dx * dx + dy * dy)
        
        return my_pathfinder.find_path(my_graph, v1, v2, my_heuristic)

class TestAStarBiDirectionalTimed(SimplePathfindingTestCaseTimed):
    def find_path(self, my_graph, v1, v2):
        my_pathfinder = astar.BiDirectionalAStar()
        
        def my_heuristic(graph, v1, v2):
            dx = v2[0] - v1[0]
            dy = v2[1] - v1[1]
            return math.sqrt(dx * dx + dy * dy)
        
        return my_pathfinder.find_path(my_graph, v1, v2, my_heuristic)