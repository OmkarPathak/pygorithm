# Author: OMKAR PATHAK
# Created On: 12th August 2017

class AdjacencyList(object):
    def __init__(self):
        self.graph = {}
        self.count = 0

    def print_graph(self):
        for i  in self.graph:
            print(i,'->',' -> '.join([str(j) for j in self.graph[i]]))

    def add_edge(self, from_vertex, to_vertex):
        ''' function to add an edge in the graph '''
        # check if vertex is already present
        if from_vertex in self.graph.keys():
            self.graph[from_vertex].append(to_vertex)
            self.count += 1
        else:
            self.graph[from_vertex] = [to_vertex]
            self.graph[to_vertex] = []
            self.count += 1

    def get_code(self):
        ''' returns the code for the current class '''
        import inspect
        return inspect.getsource(AdjacencyList)

class TopologicalSort(AdjacencyList):
    def topological_sort(self):
        visited = [False] * self.count           # Marking all vertices as not visited
        stack = []                               # Stack for storing the vertex
        for vertex in range(self.count):
            # Call the recursive function only if not visited
            if visited[vertex] == False:
                self.topological_sort_rec(vertex, visited, stack)

        return stack

    # Recursive function for topological Sort
    def topological_sort_rec(self, vertex, visited, stack):

        # Mark the current node in visited
        visited[vertex] = True

        # mark all adjacent nodes of the current node
        try:
            for adjacent_node in self.graph[vertex]:
                if visited[adjacent_node] == False:
                    self.topological_sort_rec(adjacent_node, visited, stack)
        except KeyError:
            return

        # Push current vertex to stack which stores the result
        stack.insert(0,vertex)

    def get_code(self):
        ''' returns the code for the current class '''
        import inspect
        return inspect.getsource(TopologicalSort)
