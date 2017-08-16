# Author: OMKAR PATHAK
# Created On: 1st August 2017

#  breadth first search algorithm
def search(graph, startVertex):
    # Take a list for stoting already visited vertexes
    if startVertex not in graph or graph[startVertex] is None or graph[startVertex] == []:
        return None

    # create a list to store all the vertexes for BFS and a set to store the visited vertices
    visited, queue = set(), [startVertex]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited

# time complexities
def time_complexities():
    return '''O(V + E) where V = Number of vertices and E = Number of Edges'''

# easily retrieve the source code of the bfs function
def get_code():
    import inspect
    return inspect.getsource(search)
