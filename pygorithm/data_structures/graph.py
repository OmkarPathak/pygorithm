"""
Author: OMKAR PATHAK
Created On: 12th August 2017
"""
from collections import defaultdict
import inspect
import math


class Graph(object):
    """Graph object
    Creates the graph
    """

    def __init__(self):
        self.graph = defaultdict(list)
        self.count = 0
    
    def print_graph(self):
        """
        Prints the contents of the graph
        """
        for i in self.graph:
            print(i, '->', ' -> '.join([str(j) for j in self.graph[i]]))
    
    def add_edge(self, from_vertex, to_vertex):
        """
        Adds an edge in the graph
        """
        # check if vertex is already present
        self.graph[from_vertex].append(to_vertex)
        self.count += 1

    def get_code(self):
        """
        returns the code for the current class
        """
        return inspect.getsource(Graph)


class WeightedGraph(object):
    """WeightedGraph object
    A graph with a numerical value (weight) on edges
    """

    def __init__(self):
        self.edges_weighted = []
        self.vertexes = set()
        self.forest = None

    def add_edge(self, u, v, weight):
        """
        :param u: from vertex - type : integer
        :param v: to vertex - type : integer
        :param weight: weight of the edge - type : numeric
        """
        edge = ((u, v), weight)
        self.edges_weighted.append(edge)
        self.vertexes.update((u, v))

    def print_graph(self):
        """
        Print the graph
        :return: None
        """
        for (u, v), weight in self.edges_weighted:
            print("%d -> %d weight: %d" % (u, v, weight))

    def __set_of(self, vertex):
        """
        Helper method
        :param vertex:
        :return:
        """
        for tree in self.forest:
            if vertex in tree:
                return tree
        return None

    def __union(self, u_set, v_set):
        """
        Helper method
        :param u_set:
        :param v_set:
        :return:
        """
        self.forest.remove(u_set)
        self.forest.remove(v_set)
        self.forest.append(v_set + u_set)

    def kruskal_mst(self):
        """
        Kruskal algorithm for finding the minimum spanning tree of a weighted graph.
        This version use a union-find data structure.
        More detailed info here: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
        Author: Michele De Vita <mik3dev@gmail.com>
        """
        # sort by weight
        self.edges_weighted.sort(key=lambda pair: pair[1])
        edges_explored = []
        self.forest = [[v] for v in self.vertexes]
        for (u, v), weight in self.edges_weighted:
            u_set, v_set = self.__set_of(u), self.__set_of(v)
            if u_set != v_set:
                self.__union(u_set, v_set)
                edges_explored.append(((u, v), weight))
        return edges_explored

    # TODO: Is this necessary?
    @staticmethod
    def kruskal_time_complexity():
        """
        Return time complexity of kruskal
        :return: string
        """
        return "Worst case: O(E log(V)) where E in the number of edges and V the number of vertexes"

    @classmethod
    def kruskal_code(cls):
        """
        Returns the code for current class
        """
        return inspect.getsource(cls.kruskal_mst)

class WeightedUndirectedGraph(object):
    """WeightedUndirectedGraph object
    A graph with a numerical value (weight) on edges, which
    is the same for both directions in an undirected graph.
    """
    
    def __init__(self):
        self.graph = {}
        self.weights = {}
        
    def add_edge(self, u, v, weight):
        """
        Adds the specified edge to this graph. If the edge already exists,
        this will only modify the weight (not create duplicates).
        :param u: from vertex
        :param v: to vertex
        :param weight: weight of the edge - type : numeric
        """
        
        changing_weight = (u, v) in self.weights.keys()
        
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight
        
        if changing_weight:
            return
            
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
            
        if v in self.graph.keys():
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]
    
    def get_edge_weight(self, u, v):
        """
        Gets the weight between u and v if such an edge
        exists, or None if it does not.
        :param u: one edge
        :param v: the other edge
        :return: numeric or None
        """
        return self.weights.get((u, v), None)
            
    def remove_edge(self, edge, other_edge_or_none=None):
        """
        Removes the specified edge from the grid entirely or,
        if specified, the connection with one other edge.
        Behavior is undefined if the connection does not
        exist.
        :param edge: the edge to remove
        :param other_edge_or_none: an edge connected to edge or none
        """
        
        if other_edge_or_none is not None:
            del self.weights[(edge, other_edge_or_none)]
            del self.weights[(other_edge_or_none, edge)]
            
            edge_list = self.graph[edge]
            other_edge_list = self.graph[other_edge_or_none]
            
            if len(edge_list) == 1:
                del self.graph[edge]
            else:
                self.graph[edge].remove(other_edge_or_none)
                
            if len(other_edge_list) == 1:
                del self.graph[other_edge_or_none]
            else:
                self.graph[other_edge_or_none].remove(edge)
        else:
            edge_list = self.graph[edge]
            del self.graph[edge]
            for other_edge in edge_list:
                del self.weights[(edge, other_edge)]
                del self.weights[(other_edge, edge)]
                
                other_edge_list = self.graph[other_edge]
                if len(other_edge_list) == 1:
                    del self.graph[other_edge]
                else:
                    other_edge_list.remove(edge)
        
        
    def gridify(self, size, weight):
        """
        Constructs connections from a square grid starting at (0, 0)
        until (size-1, size-1) with connections between adjacent and 
        diagonal nodes. Diagonal nodes have a weight of weight*sqrt(2)
        :param size: the size of the square grid to construct - type : integer
        :param weight: the weight between orthogonal nodes. - type: numeric
        :return: None
        """
        rt2 = math.sqrt(2)
        acceptable_offsets = [ 
            (-1, -1, rt2), (-1, 0, 1), (-1, 1, rt2), 
            (0, -1, 1), (0, 1, 1), 
            (1, -1, rt2), (1, 0, 1), (1, 1, rt2)
        ]
        
        for x in range(0, size):
            for y in range(0, size):
                for offset in acceptable_offsets:
                    nx = x + offset[0]
                    ny = y + offset[1]
                    if nx >= 0 and ny >= 0 and nx < size and ny < size:
                        self.add_edge((x, y), (nx, ny), weight * offset[2])     
                        
class TopologicalSort(Graph):

    def topological_sort(self):
        """
        function for sorting graph elements using topological sort
        """
        # Marking all vertices as not visited
        visited = [False] * self.count
        # Stack for storing the vertex
        stack = []
        for vertex in range(self.count):
            # Call the recursive function only if not visited
            if not visited[vertex]:
                self.__topological_sort_rec(vertex, visited, stack)

        return stack

    def __topological_sort_rec(self, vertex, visited, stack):
        """
        Recursive function for topological Sort
        """
        # Mark the current node in visited
        visited[vertex] = True

        # mark all adjacent nodes of the current node
        try:
            for adjacent_node in self.graph[vertex]:
                if not visited[adjacent_node]:
                    self.__topological_sort_rec(adjacent_node, visited, stack)
        except KeyError:
            return

        # Push current vertex to stack which stores the result
        stack.insert(0, vertex)

    def get_code(self):
        """
        returns the code for the current class
        """
        return inspect.getsource(TopologicalSort)


class CheckCycleDirectedGraph(object):
    """CheckCycleDirectedGraph
    Class to check cycle in directed graph
    """

    def __init__(self):
        self.graph = {}
        self.count = 0

    def print_graph(self):
        """
        for printing the contents of the graph
        """
        for i in self.graph:
            print(i, '->', ' -> '.join([str(j) for j in self.graph[i]]))

    def add_edge(self, from_vertex, to_vertex):
        """
        function to add an edge in the graph
        """
        # check if vertex is already present
        if from_vertex in self.graph.keys():
            self.graph[from_vertex].append(to_vertex)
            self.count += 1
        else:
            self.graph[from_vertex] = [to_vertex]
            self.count += 1

    def check_cycle(self):
        """
        This function will return True if graph is cyclic else return False
        """
        visited = [False] * len(self.graph)
        stack = [False] * len(self.graph)
        for vertex in range(len(self.graph)):
            if not visited[vertex]:
                if self.__check_cycle_rec(visited, stack, vertex):
                    return True
        return False

    def __check_cycle_rec(self, visited, stack, vertex):
        """
        Recursive function for finding the cycle
        """
        # Mark the current node in visited and also add it to the stack
        visited[vertex] = True
        stack[vertex] = True

        # mark all adjacent nodes of the current node
        for adjacentNode in self.graph[vertex]:
            if not visited[adjacentNode]:
                if self.__check_cycle_rec(visited, stack, adjacentNode):
                    return True
            elif stack[adjacentNode]:
                return True

        # The node needs to be popped from
        # recursion stack before function ends
        stack[vertex] = False
        return False

    @staticmethod
    def get_code():
        """
        returns the code for the current class
        """
        return inspect.getsource(CheckCycleDirectedGraph)


class CheckCycleUndirectedGraph(object):
    """CheckCycleUndirectedGraph
    Class to check cycle in undirected graph
    """

    def __init__(self):
        self.graph = {}
        self.count = 0
    
    def print_graph(self):
        """
        for printing the contents of the graph
        """
        for i in self.graph:
            print(i, '->', ' -> '.join([str(j) for j in self.graph[i]]))
    
    def add_edge(self, from_vertex, to_vertex):
        """
        for adding the edge between two vertices
        """
        # check if vertex is already present,
        if from_vertex in self.graph.keys():
            self.graph[from_vertex].append(to_vertex)
        else:
            # otherwise add it to the graph
            self.graph[from_vertex] = [to_vertex]
            
        if to_vertex in self.graph.keys():
            self.graph[to_vertex].append(from_vertex)
        else:
            self.graph[to_vertex] = [from_vertex]

    def check_cycle(self):
        """
        This function will return True if graph is cyclic else return False
        """
        # Marking all vertices as not visited
        visited = [False] * len(self.graph)
        for vertex in range(len(self.graph)):
            # Call the recursive function only if not visited
            if not visited[vertex]:
                if self.__check_cycle_rec(visited, -1, vertex):
                    return True
        return False

    def __check_cycle_rec(self, visited, parent, vertex):
        """
        Recursive function for finding the cycle
        """
        # Mark the current node in visited
        visited[vertex] = True

        # mark all adjacent nodes of the current node
        for adjacentNode in self.graph[vertex]:
            if not visited[adjacentNode]:
                if self.__check_cycle_rec(visited, vertex, adjacentNode):
                    return True
            elif parent != adjacentNode:
                return True
        return False

    @staticmethod
    def get_code():
        """
        returns the code for the current class
        """
        return inspect.getsource(CheckCycleUndirectedGraph)
