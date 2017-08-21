import heapq

class OneDirectionalAStar(object):
    """AStar object
    Finds the optimal path between two nodes on
    a graph while taking into account weights.
    """
    
    # Some miscellaneous notes:
    
    # River example neighbors
    # Imagine you had a graph that was constructed by the time it
    # would take to get to different strategic locations on a map.
    # Suppose there is a river that cuts the map in half vertically,
    # and two bridges that allow crossing at the top and bottom of
    # the map, but swimming is an option but very slow.
    # For simplicity, on each side there is 1 base that acts as a 
    # strategic location, both sides of the each bridge, and both
    # sides of the river directly in the vertical center, for a total
    # graph of 8 nodes (see imgs/onedirectionalastar_riverexample.png)
    #
    # Now suppose the heuristic naively used euclidean distance while 
    # the actual weights were based on precalculated paths.
    #
    # Looking at the picture, if you were going from one base to the other
    # middle side of the river, you would first expand the base and find
    # 3 nodes: top (15 + 10), your side of center (5 + 3), bottom (15 + 10).
    #
    # You would expand your side of center and find the top and bottom at 
    # (5 + 12) - WORSE than just going to them. This is the case where we
    # would NOT add the path base->center->top to the open list because
    # (for these weights) it will never be better than base->top.
    #
    # You would also add the new node (55 + 0) or the destination.
    #
    # Then you expand the top node (or bottom) on the other side of
    # river with a cost of (18 + 12).
    #
    # You expand the top node on the other side of the river next and find
    # one of the neighbors is already on the open list (the destination)
    # at a score of (55 + 0), but your cost to get there is (30 + 0). This
    # is where you would REPLACE the old path with yourself.
    
    def __init__(self):
        pass
    
    def reverse_path(self, node):
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
    
    def find_path(self, graph, start, end, heuristic_fn):
        """
        Calculates the optimal path from start to end
        on the graph. Weights are taken into account.
        This implementation is one-directional expanding
        from the start to the end. This implementation is
        faster than dijkstra based on how much better the
        heuristic is than flooding.
        
        The heuristic must never overestimate the distance
        between two nodes (in other words, the heuristic
        must be "admissible"). Note however that, in practice,
        it is often acceptable to relax this requirement and
        get very slightly incorrect paths if:
            - The distance between nodes are small
            - There are too many nodes for an exhaustive search 
              to ever be feasible.
            - The world is mostly open (ie there are many paths
              from the start to the end that are acceptable)
            - Execution speed is more important than accuracy.
        The best way to do this is to make the heuristic slightly
        pessimistic (typically by multiplying by small value such
        as 1.1). This will have the algorithm favor finishing its
        path rather than finding a better one. This optimization
        needs to be tested based on the map.
        
        :param graph:        object contains `graphs` as per pygorithm.data_structures.WeightedUndirectedGraph
                             and `get_edge_weight` in the same manner.
        :param start:        the start vertex (which is the same type of the verticies in the graph)
        :param end:          the end vertex (which is the same type of the vertices in the graph)
        :param heuristic_fn: function(graph, start, end) that when given two vertices returns an expected cost to get
                             to get between the two vertices.
        :return:      a list starting with `start` and ending with `end`, or None if no path is possible.
        """
        
        # It starts off very similiar to Dijkstra. However, we will need to lookup
        # nodes in the open list before. There can be thousands of nodes in the open
        # list and any unordered search is too expensive, so we trade some memory usage for
        # more consistent performance by maintaining a dictionary (O(1) lookup) between
        # vertices and their nodes. 
        open_lookup = {}
        open = []
        closed = set()
        
        # We require a bit more information on each node than Dijkstra
        # and we do slightly more calculation, so the heuristic must
        # prune enough nodes to offset those costs. In practice this
        # is almost always the case if their are any large open areas
        # (nodes with many connected nodes).
        
        # Rather than simply expanding nodes that are on the open list
        # based on how close they are to the start, we will expand based
        # on how much distance we predict is between the start and end 
        # node IF we go through that parent. That is a combination of 
        # the distance from the start to the node (which is certain) and
        # the distance from the node to the end (which is guessed).
        
        # We use the counter to enforce consistent ordering between nodes
        # with the same total predicted distance.
        
        counter = 0 
        heur = heuristic_fn(graph, start, end)
        open_lookup[start] = { 'vertex': start, 'dist_start_to_here': 0, 'pred_dist_here_to_end': heur, 'pred_total_dist': heur, 'parent': None }
        heapq.heappush(open, (heur, counter, start))
        counter += 1
        
        while len(open) > 0:
            current = heapq.heappop(open)
            current_vertex = current[2]
            current_dict = open_lookup[current_vertex]
            del open_lookup[current_vertex]
            closed.update(current_vertex)
            
            if current_vertex == end:
                return self.reverse_path(current_dict)
            
            neighbors = graph.graph[current_vertex]
            for neighbor in neighbors:
                if neighbor in closed:
                    # If we already expanded it it's definitely not better
                    # to go through this node, or we would have expanded this
                    # node first.
                    continue
                
                cost_start_to_neighbor = current_dict['dist_start_to_here'] + graph.get_edge_weight(current_vertex, neighbor)
                neighbor_from_lookup = open_lookup.get(neighbor, None) # avoid searching twice
                if neighbor_from_lookup is not None:
                    # If our heuristic is NOT consistent or the grid is NOT uniform,
                    # it is possible that there is a better path to a neighbor of a 
                    # previously expanded node. See above, ctrl+f "river example neighbors"
                    
                    # Note that the heuristic distance from here to end will be the same for
                    # both, so the only difference will be in start->here through neighbor
                    # and through the old neighbor.
                    
                    old_dist_start_to_neighbor = neighbor_from_lookup['dist_start_to_here']
                    
                    if cost_start_to_neighbor < old_dist_start_to_neighbor:
                        pred_dist_neighbor_to_end = neighbor_from_lookup['pred_dist_here_to_end']
                        pred_total_dist_through_neighbor_to_end = cost_start_to_neighbor + pred_dist_neighbor_to_end
                        # Note, we've already shown that neighbor (the vector) is already in the open list,
                        # but unfortunately we don't know where and we have to do a slow lookup to fix the 
                        # key its sorting by to the new predicted total distance.
                        
                        # In case we're using a fancy debugger we want to search in user-code so when 
                        # this lookup freezes we can see how much longer its going to take.
                        found = None
                        for i in range(0, len(open)):
                            if open[i][2] == neighbor:
                                found = i
                                break
                        if found is None:
                            raise Exception('A vertex is in the open lookup but not in open. This is impossible, please submit an issue + include the graph!')
                        # todo I'm not certain about the performance characteristics of doing this with heapq, nor if 
                        # it would be better to delete heapify and push or rather than replace
                        open[i] = (pred_total_dist_through_neighbor_to_end, counter, neighbor)
                        counter += 1
                        heapq.heapify(open)
                        open_lookup[neighbor] = { 'vertex': neighbor,
                                                  'dist_start_to_here': cost_start_to_neighbor, 
                                                  'pred_dist_here_to_end': pred_dist_neighbor_to_end, 
                                                  'pred_total_dist': pred_total_dist_through_neighbor_to_end, 
                                                  'parent': current_dict }
                    continue
                    
                
                # We've found the first possible way to the path!
                pred_dist_neighbor_to_end = heuristic_fn(graph, neighbor, end)
                pred_total_dist_through_neighbor_to_end = cost_start_to_neighbor + pred_dist_neighbor_to_end
                heapq.heappush(open, (pred_total_dist_through_neighbor_to_end, counter, neighbor))
                open_lookup[neighbor] = { 'vertex': neighbor,
                                          'dist_start_to_here': cost_start_to_neighbor,
                                          'pred_dist_here_to_end': pred_dist_neighbor_to_end,
                                          'pred_total_dist': pred_total_dist_through_neighbor_to_end,
                                          'parent': current_dict }
        
        return None
            
    @staticmethod
    def get_code(self):
        """
        returns the code for the current class
        """
        return inspect.getsource(OneDirectionalAStar)
        
        
        