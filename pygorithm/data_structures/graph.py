# Author: OMKAR PATHAK
# Created On: 12th August 2017
from collections import defaultdict

class Graph(object):
    ''' class for creating a graph '''
    def __init__(self):
        self.graph = defaultdict(list)
        self.count = 0

    def print_graph(self):
        ''' for printing the contents of the graph '''
        for i in self.graph:
            print(i, '->', ' -> '.join([str(j) for j in self.graph[i]]))

    def add_edge(self, from_vertex, to_vertex):
        ''' function to add an edge in the graph '''
        # check if vertex is already present
        self.graph[from_vertex].append(to_vertex)
        self.count += 1

    def get_code(self):
        """ returns the code for the current class """
        import inspect
        return inspect.getsource(Graph)


class WeightedGraph(object):
    """
    A graph with a numerical value (weight) on edges
    """
    def __init__(self):
        self.edges_weighted = []
        self.vertexes = set()

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
        for (u, v), weight in self.edges_weighted:
            print("%d -> %d weight: %d" % (u, v, weight))

    def _set_of(self, vertex):
        for tree in self.forest:
            if vertex in tree:
                return tree
        return None

    def _union(self, u_set, v_set):
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
            u_set, v_set = self._set_of(u), self._set_of(v)
            if u_set != v_set:
                self._union(u_set, v_set)
                edges_explored.append(((u, v), weight))
        return edges_explored

    @staticmethod
    def kruskal_time_complexity():
        return '''Worst case: O(E log(V)) where E in the number of edges and V the number of vertexes'''

    @classmethod
    def kruskal_code(cls):
        ''' Returns the code for current class '''
        import inspect
        return inspect.getsource(cls.kruskal_mst)


class TopologicalSort(Graph):
    def topological_sort(self):
        ''' function for sorting graph elements using topological sort '''
        visited = [False] * self.count  # Marking all vertices as not visited
        stack = []  # Stack for storing the vertex
        for vertex in range(self.count):
            # Call the recursive function only if not visited
            if not visited[vertex]:
                self._topological_sort_rec(vertex, visited, stack)

        return stack

    def _topological_sort_rec(self, vertex, visited, stack):
        ''' Recursive function for topological Sort '''
        # Mark the current node in visited
        visited[vertex] = True

        # mark all adjacent nodes of the current node
        try:
            for adjacent_node in self.graph[vertex]:
                if visited[adjacent_node] == False:
                    self._topological_sort_rec(adjacent_node, visited, stack)
        except KeyError:
            return

        # Push current vertex to stack which stores the result
        stack.insert(0, vertex)

    def get_code(self):
        ''' returns the code for the current class '''
        import inspect
        return inspect.getsource(TopologicalSort)


class CheckCycleDirectedGraph(object):
    ''' Class to check cycle in directed graph '''
    def __init__(self):
        self.graph = {}
        self.count = 0

    def print_graph(self):
        ''' for printing the contents of the graph '''
        for i in self.graph:
            print(i, '->', ' -> '.join([str(j) for j in self.graph[i]]))

    def add_edge(self, from_vertex, to_vertex):
        ''' function to add an edge in the graph '''
        # check if vertex is already present
        if from_vertex in self.graph.keys():
            self.graph[from_vertex].append(to_vertex)
            self.count += 1
        else:
            self.graph[from_vertex] = [to_vertex]
            self.count += 1

    def check_cycle(self):
        ''' This function will return True if graph is cyclic else return False '''
        visited = [False] * len(self.graph)
        stack = [False] * len(self.graph)
        for vertex in range(len(self.graph)):
            if visited[vertex] == False:
                if self._check_cycle_rec(visited, stack, vertex) == True:
                    return True
        return False

    def _check_cycle_rec(self, visited, stack, vertex):
        ''' Recursive function for finding the cycle '''
        # Mark the current node in visited and also add it to the stack
        visited[vertex] = True
        stack[vertex] = True

        # mark all adjacent nodes of the current node
        for adjacentNode in self.graph[vertex]:
            if visited[adjacentNode] == False:
                if self._check_cycle_rec(visited, stack, adjacentNode) == True:
                    return True
            elif stack[adjacentNode] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        stack[vertex] = False
        return False

    def get_code(self):
        ''' returns the code for the current class '''
        import inspect
        return inspect.getsource(CheckCycleDirected)


class CheckCycleUndirectedGraph(object):
    ''' Class to check cycle in undirected graph '''
    def __init__(self):
        self.graph = {}
        self.count = 0

    def print_graph(self):
        ''' for printing the contents of the graph '''
        for i in self.graph:
            print(i, '->', ' -> '.join([str(j) for j in self.graph[i]]))

    def add_edge(self, fromVertex, toVertex):
        ''' for adding the edge between two vertices '''
        # check if vertex is already present,
        if fromVertex in self.graph.keys() and toVertex in self.graph.keys():
            self.graph[fromVertex].append(toVertex)
            self.graph[toVertex].append(fromVertex)
        else:
            # else make a new vertex
            self.graph[fromVertex] = [toVertex]
            self.graph[toVertex] = [fromVertex]

    def check_cycle(self):
        ''' This function will return True if graph is cyclic else return False '''
        visited = [False] * len(self.graph)  # Marking all vertices as not visited
        for vertex in range(len(self.graph)):
            # Call the recursive function only if not visited
            if visited[vertex] == False:
                if self._check_cycle_rec(visited, -1, vertex) == True:
                    return True
        return False

    def _check_cycle_rec(self, visited, parent, vertex):
        ''' Recursive function for finding the cycle '''
        # Mark the current node in visited
        visited[vertex] = True

        # mark all adjacent nodes of the current node
        for adjacentNode in self.graph[vertex]:
            if visited[adjacentNode] == False:
                if self._check_cycle_rec(visited, vertex, adjacentNode) == True:
                    return True
            elif parent != adjacentNode:
                return True

        return False
