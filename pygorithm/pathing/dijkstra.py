import heapq
class Dijkstra(object):
    """Dijkstra object
    Finds the optimal path between two nodes on
    a graph."""
    
    def __init__(self):
        pass
    
    def reverse_path(self, node):
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
        
        open = []
        closed = set()
        
        # the first element in the tuple is the distance from the source. This is used as the primary
        # key for sorting. The second element in the tuple is just a counter and is used to avoid having
        # to hash the dictionary when the distance from the source is not unique.
        
        counter = 0
        heapq.heappush(open, (0, counter, { 'vertex': start, 'parent': None }))
        counter += 1
        
        while len(open) > 0:
            current = heapq.heappop(open)
            closed.update(current[2]['vertex'])
            
            if current[2]['vertex'] == end:
                return self.reverse_path(current[2])
            
            neighbors = graph.graph[current[2]['vertex']]
            for neighbor in neighbors:
                if neighbor not in closed:
                    heapq.heappush(open, (current[0] + 1, counter, { 'vertex': neighbor, 'parent': current[2] }))
                    counter += 1
            
        
        return None
    
    @staticmethod
    def get_code(self):
        """
        returns the code for the current class
        """
        return inspect.getsource(Dijkstra)