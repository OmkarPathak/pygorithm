"""
A*

Author: Timothy Moore

A* is an informed search algorithm, or a best-first search,
meaning that it solves problems by searching among all possible
paths to the solution (goal) for the one that incurs the smallest
cost (least distance travelled, shortest time, etc.), and among
these paths it first considers the ones that appear to lead most
quickly to the solution.
https://en.wikipedia.org/wiki/A*_search_algorithm
"""
import heapq
import inspect

from enum import Enum


class OneDirectionalAStar(object):
    """OneDirectionalAStar object
    Finds the optimal path between two nodes on a graph while taking
    into account weights. Expands the start node first until it finds
    the end node.
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
    # would NOT add the path base->center->top to the _open list because
    # (for these weights) it will never be better than base->top.
    #
    # You would also add the new node (55 + 0) or the destination.
    #
    # Then you expand the top node (or bottom) on the other side of
    # river with a cost of (18 + 12).
    #
    # You expand the top node on the other side of the river next and find
    # one of the neighbors is already on the _open list (the destination)
    # at a score of (55 + 0), but your cost to get there is (30 + 0). This
    # is where you would REPLACE the old path with yourself.
    
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
            result.append(node['vertex'])
            node = node['parent']
        result.reverse()
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
            - The world is mostly _open (ie there are many paths
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
        # nodes in the _open list before. There can be thousands of nodes in the _open
        # list and any unordered search is too expensive, so we trade some memory usage for
        # more consistent performance by maintaining a dictionary (O(1) lookup) between
        # vertices and their nodes. 
        _open_lookup = {}
        _open = []
        closed = set()
        
        # We require a bit more information on each node than Dijkstra
        # and we do slightly more calculation, so the heuristic must
        # prune enough nodes to offset those costs. In practice this
        # is almost always the case if their are any large _open areas
        # (nodes with many connected nodes).
        
        # Rather than simply expanding nodes that are on the _open list
        # based on how close they are to the start, we will expand based
        # on how much distance we predict is between the start and end 
        # node IF we go through that parent. That is a combination of 
        # the distance from the start to the node (which is certain) and
        # the distance from the node to the end (which is guessed).
        
        # We use the counter to enforce consistent ordering between nodes
        # with the same total predicted distance.
        
        counter = 0 
        heur = heuristic_fn(graph, start, end)
        _open_lookup[start] = {'vertex': start,
                               'dist_start_to_here': 0,
                               'pred_dist_here_to_end': heur,
                               'pred_total_dist': heur,
                               'parent': None}
        heapq.heappush(_open, (heur, counter, start))
        counter += 1
        
        while len(_open) > 0:
            current = heapq.heappop(_open)
            current_vertex = current[2]
            current_dict = _open_lookup[current_vertex]
            del _open_lookup[current_vertex]
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
                
                cost_start_to_neighbor = current_dict['dist_start_to_here'] \
                    + graph.get_edge_weight(current_vertex, neighbor)
                # avoid searching twice
                neighbor_from_lookup = _open_lookup.get(neighbor, None)
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
                        # Note, we've already shown that neighbor (the vector) is already in the _open list,
                        # but unfortunately we don't know where and we have to do a slow lookup to fix the 
                        # key its sorting by to the new predicted total distance.
                        
                        # In case we're using a fancy debugger we want to search in user-code so when 
                        # this lookup freezes we can see how much longer its going to take.
                        found = None
                        for i in range(0, len(_open)):
                            if _open[i][2] == neighbor:
                                found = i
                                break
                        assert(found is not None)
                        # TODO: I'm not certain about the performance characteristics of doing this with heapq, nor if
                        # TODO: it would be better to delete heapify and push or rather than replace

                        _open[found] = (pred_total_dist_through_neighbor_to_end, counter, neighbor)
                        counter += 1
                        heapq.heapify(_open)
                        _open_lookup[neighbor] = {'vertex': neighbor,
                                                  'dist_start_to_here': cost_start_to_neighbor, 
                                                  'pred_dist_here_to_end': pred_dist_neighbor_to_end, 
                                                  'pred_total_dist': pred_total_dist_through_neighbor_to_end, 
                                                  'parent': current_dict}
                    continue

                # We've found the first possible way to the path!
                pred_dist_neighbor_to_end = heuristic_fn(graph, neighbor, end)
                pred_total_dist_through_neighbor_to_end = cost_start_to_neighbor + pred_dist_neighbor_to_end
                heapq.heappush(_open, (pred_total_dist_through_neighbor_to_end, counter, neighbor))
                _open_lookup[neighbor] = {'vertex': neighbor,
                                          'dist_start_to_here': cost_start_to_neighbor,
                                          'pred_dist_here_to_end': pred_dist_neighbor_to_end,
                                          'pred_total_dist': pred_total_dist_through_neighbor_to_end,
                                          'parent': current_dict}
        
        return None
            
    @staticmethod
    def get_code():
        """
        returns the code for the current class
        """
        return inspect.getsource(OneDirectionalAStar)

class BiDirectionalAStar(object):
    """BiDirectionalAStar object
    Finds the optimal path between two nodes on a graph while taking
    account weights. Expands from the start node and the end node 
    simultaneously
    """
    
    class NodeSource(Enum):
        """NodeSource enum
        Used to distinguish how a node was located
        """
        
        BY_START = 1,
        BY_END = 2
    
    def __init__(self):
        pass
        
    @staticmethod
    def reverse_path(node_from_start, node_from_end):
        """
        Reconstructs the path formed by walking from
        node_from_start backward to start and combining
        it with the path formed by walking from 
        node_from_end to end. Both the start and end are
        detected where 'parent' is None.
        :param node_from_start: dict containing { 'vertex': any hashable, 'parent': dict or None }
        :param node_from_end: dict containing { 'vertex' any hashable, 'parent': dict or None }
        :return: list of vertices starting at the start and ending at the end
        """
        list_from_start = []
        current = node_from_start
        while current is not None:
            list_from_start.append(current['vertex'])
            current = current['parent']
        list_from_start.reverse()
        
        list_from_end = []
        current = node_from_end
        while current is not None:
            list_from_end.append(current['vertex'])
            current = current['parent']
        
        return list_from_start + list_from_end
    
    def find_path(self, graph, start, end, heuristic_fn):
        """
        Calculates the optimal path from the start to the end. The
        search occurs from both the start and end at the same rate,
        which makes this algorithm have more consistent performance
        if you regularly are trying to find paths where the destination
        is unreachable and in a small room.
        
        The heuristic requirements are the same as in unidirectional A*
        (it must be admissable).
        
        :param graph: the graph with 'graph' and 'get_edge_weight' (see WeightedUndirectedGraph)
        :param start: the start vertex (must be hashable and same type as the graph)
        :param end: the end vertex (must be hashable and same type as the graph)
        :param heuristic_fn: an admissable heuristic. signature: function(graph, start, end) returns numeric
        :return: a list of vertices starting at start ending at end or None
        """
        
        # This algorithm is really just repeating unidirectional A* twice,
        # but unfortunately it's just different enough that it requires 
        # even more work to try to make a single function that can be called 
        # twice.
        
        
        # Note: The nodes in by_start will have heuristic distance to the end,
        # whereas the nodes in by_end will have heuristic distance to the start.
        # This means that the total predicted distance for the exact same node
        # might not match depending on which side we found it from. However, 
        # it won't make a difference since as soon as we evaluate the same node
        # on both sides we've finished.
        #
        # This also means that we can use the same lookup table for both.
        
        open_by_start = []
        open_by_end = []
        open_lookup = {}
        
        closed = set()
        
        # used to avoid hashing the dict.
        counter_arr = [0]
        
        total_heur_distance = heuristic_fn(graph, start, end)
        heapq.heappush(open_by_start, (total_heur_distance, counter_arr[0], start))
        counter_arr[0] += 1
        open_lookup[start] = { 'vertex': start, 
                               'parent': None, 
                               'source': self.NodeSource.BY_START, 
                               'dist_start_to_here': 0,
                               'pred_dist_here_to_end': total_heur_distance,
                               'pred_total_dist': total_heur_distance }
        
        heapq.heappush(open_by_end, (total_heur_distance, counter_arr, end))
        counter_arr[0] += 1
        open_lookup[end] = { 'vertex': end,
                             'parent': None,
                             'source': self.NodeSource.BY_END, 
                             'dist_end_to_here': 0,
                             'pred_dist_here_to_start': total_heur_distance,
                             'pred_total_dist': total_heur_distance }
        
        # If the start runs out then the start is in a closed room,
        # if the end runs out then the end is in a closed room,
        # either way there is no path from start to end.
        while len(open_by_start) > 0 and len(open_by_end) > 0:
            result = self._evaluate_from_start(graph, start, end, heuristic_fn, open_by_start, open_by_end, open_lookup, closed, counter_arr)
            if result is not None:
                return result
            
            result = self._evaluate_from_end(graph, start, end, heuristic_fn, open_by_start, open_by_end, open_lookup, closed, counter_arr)
            if result is not None:
                return result
        
        return None
            
    def _evaluate_from_start(self, graph, start, end, heuristic_fn, open_by_start, open_by_end, open_lookup, closed, counter_arr):
        """
        Intended for internal use only. Expands one node from the open_by_start list.
        
        :param graph: the graph (see WeightedUndirectedGraph)
        :param start: the start node
        :param end: the end node
        :heuristic_fn: the heuristic function (signature function(graph, start, end) returns numeric)
        :open_by_start: the open vertices from the start
        :open_by_end: the open vertices from the end
        :open_lookup: dictionary of vertices -> dicts
        :closed: the already expanded vertices (set)
        :counter_arr: arr of one integer (counter)
        """
        current = heapq.heappop(open_by_start)
        current_vertex = current[2]
        current_dict = open_lookup[current_vertex]
        del open_lookup[current_vertex]
        closed.update(current_vertex)
        
        neighbors = graph.graph[current_vertex]
        for neighbor in neighbors:
            if neighbor in closed:
                continue
            
            neighbor_dict = open_lookup.get(neighbor, None)
            if neighbor_dict is not None and neighbor_dict['source'] is self.NodeSource.BY_END:
                return self.reverse_path(current_dict, neighbor_dict)
            
            dist_to_neighb_through_curr_from_start = current_dict['dist_start_to_here'] \
                + graph.get_edge_weight(current_vertex, neighbor)
            
            if neighbor_dict is not None:
                assert(neighbor_dict['source'] is self.NodeSource.BY_START)
                
                if neighbor_dict['dist_start_to_here'] <= dist_to_neighb_through_curr_from_start:
                    continue
                
                pred_dist_neighbor_to_end = neighbor_dict['pred_dist_here_to_end']
                pred_total_dist_through_neighbor = dist_to_neighb_through_curr_from_start + pred_dist_neighbor_to_end
                open_lookup[neighbor] = { 'vertex': neighbor,
                                          'parent': current_dict,
                                          'source': self.NodeSource.BY_START,
                                          'dist_start_to_here': dist_to_neighb_through_curr_from_start, 
                                          'pred_dist_here_to_end': pred_dist_neighbor_to_end, 
                                          'pred_total_dist': pred_total_dist_through_neighbor }
                
                # TODO: I'm pretty sure theres a faster way to do this
                found = None
                for i in range(0, len(open_by_start)):
                    if open_by_start[i][2] == neighbor:
                        found = i
                        break
                assert(found is not None)
                
                open_by_start[found] = (pred_total_dist_through_neighbor, counter_arr[0], neighbor)
                counter_arr[0] += 1
                heapq.heapify(open_by_start)
                continue
            
            pred_dist_neighbor_to_end = heuristic_fn(graph, neighbor, end)
            pred_total_dist_through_neighbor = dist_to_neighb_through_curr_from_start + pred_dist_neighbor_to_end
            open_lookup[neighbor] = { 'vertex': neighbor,
                                      'parent': current_dict,
                                      'source': self.NodeSource.BY_START,
                                      'dist_start_to_here': dist_to_neighb_through_curr_from_start, 
                                      'pred_dist_here_to_end': pred_dist_neighbor_to_end, 
                                      'pred_total_dist': pred_total_dist_through_neighbor }
            heapq.heappush(open_by_start, (pred_total_dist_through_neighbor, counter_arr[0], neighbor))
            counter_arr[0] += 1
    
    def _evaluate_from_end(self, graph, start, end, heuristic_fn, open_by_start, open_by_end, open_lookup, closed, counter_arr):
        """
        Intended for internal use only. Expands one node from the open_by_end list.
        
        :param graph: the graph (see WeightedUndirectedGraph)
        :param start: the start node
        :param end: the end node
        :heuristic_fn: the heuristic function (signature function(graph, start, end) returns numeric)
        :open_by_start: the open vertices from the start
        :open_by_end: the open vertices from the end
        :open_lookup: dictionary of vertices -> dicts
        :closed: the already expanded vertices (set)
        :counter_arr: arr of one integer (counter)
        """
        current = heapq.heappop(open_by_end)
        current_vertex = current[2]
        current_dict = open_lookup[current_vertex]
        del open_lookup[current_vertex]
        closed.update(current_vertex)
        
        neighbors = graph.graph[current_vertex]
        for neighbor in neighbors:
            if neighbor in closed:
                continue
            
            neighbor_dict = open_lookup.get(neighbor, None)
            if neighbor_dict is not None and neighbor_dict['source'] is self.NodeSource.BY_START:
                return self.reverse_path(neighbor_dict, current_dict)
            
            dist_to_neighb_through_curr_from_end = current_dict['dist_end_to_here'] \
                + graph.get_edge_weight(current_vertex, neighbor)
            
            if neighbor_dict is not None:
                assert(neighbor_dict['source'] is self.NodeSource.BY_END)
                
                if neighbor_dict['dist_end_to_here'] <= dist_to_neighb_through_curr_from_end:
                    continue
                
                pred_dist_neighbor_to_start = neighbor_dict['pred_dist_here_to_start']
                pred_total_dist_through_neighbor = dist_to_neighb_through_curr_from_end + pred_dist_neighbor_to_start
                open_lookup[neighbor] = { 'vertex': neighbor,
                                          'parent': current_dict,
                                          'source': self.NodeSource.BY_END,
                                          'dist_end_to_here': dist_to_neighb_through_curr_from_end, 
                                          'pred_dist_here_to_start': pred_dist_neighbor_to_start, 
                                          'pred_total_dist': pred_total_dist_through_neighbor }
                
                # TODO: I'm pretty sure theres a faster way to do this
                found = None
                for i in range(0, len(open_by_end)):
                    if open_by_end[i][2] == neighbor:
                        found = i
                        break
                assert(found is not None)
                
                open_by_end[found] = (pred_total_dist_through_neighbor, counter_arr[0], neighbor)
                counter_arr[0] += 1
                heapq.heapify(open_by_end)
                continue
            
            pred_dist_neighbor_to_start = heuristic_fn(graph, neighbor, start)
            pred_total_dist_through_neighbor = dist_to_neighb_through_curr_from_end + pred_dist_neighbor_to_start
            open_lookup[neighbor] = { 'vertex': neighbor,
                                      'parent': current_dict,
                                      'source': self.NodeSource.BY_END,
                                      'dist_end_to_here': dist_to_neighb_through_curr_from_end, 
                                      'pred_dist_here_to_start': pred_dist_neighbor_to_start, 
                                      'pred_total_dist': pred_total_dist_through_neighbor }
            heapq.heappush(open_by_end, (pred_total_dist_through_neighbor, counter_arr[0], neighbor))
            counter_arr[0] += 1
        
    @staticmethod
    def get_code():
        """
        returns the code for the current class
        """
        return inspect.getsource(BiDirectionalAStar)