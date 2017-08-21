"""
Dijkstra's Algorithm

Author: Timothy Moore

Dijkstra's algorithm is an algorithm for
finding the shortest paths between nodes
in a graph.
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

"""
import heapq
import inspect


class Dijkstra(object):
    """Dijkstra object
    Finds the optimal path between two nodes on
    a graph.
    """
    
    def __init__(self):
        pass

    @staticmethod
    def reverse_path(node):
        """
        Walks backward from an end node to the start
        node and reconstructs a path. Meant for internal
        use.
        :param node: dict containing { 'vertex': any hashable, 'parent': dict or None }
        :return:     a list of vertices ending on the node
        """
        result = []
        while node is not None:
            result.insert(0, node['vertex'])
            node = node['parent']
        return result
        
    def find_path(self, graph, start, end):
        """
        Calculates the optimal path from start to end
        on the graph. Weights are ignored.
        
        :param graph: object contains `graphs` as per pygorithm.data_structures.WeightedUndirectedGraph
                      weights are ignored.
        :param start: the start vertex (which is the same type of the verticies in the graph)
        :param end:   the end vertex (which is the same type of the vertices in the graph)
        :return:      a list starting with `start` and ending with `end`, or None if no path is possible.
        """
        
        _open = []
        closed = set()
        
        # the first element in the tuple is the distance from the source. This is used as the primary
        # key for sorting. The second element in the tuple is just a counter and is used to avoid having
        # to hash the dictionary when the distance from the source is not unique.
        
        # performance might be improved by also searching the open list and avoiding adding those nodes
        # but since this algorithm is typically for examples only performance improvements are not made
        
        counter = 0
        heapq.heappush(_open, (0, counter, {'vertex': start, 'parent': None}))
        counter += 1
        
        while len(_open) > 0:
            current = heapq.heappop(_open)
            current_dict = current[2]
            closed.update(current_dict['vertex'])
            
            if current_dict['vertex'] == end:
                return self.reverse_path(current_dict)
            
            neighbors = graph.graph[current_dict['vertex']]
            for neighbor in neighbors:
                if neighbor not in closed:
                    heapq.heappush(_open, (current[0] + 1, counter, {'vertex': neighbor, 'parent': current_dict}))
                    counter += 1
        return None
    
    @staticmethod
    def get_code():
        """
        returns the code for the current class
        """
        return inspect.getsource(Dijkstra)
