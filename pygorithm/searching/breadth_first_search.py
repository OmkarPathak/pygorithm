"""
Author: OMKAR PATHAK
Created On: 1st August 2017
"""
import inspect


def search(graph, start_vertex):
    """
    Breadth first search algorithm
    
    :param graph: 
    :param start_vertex: 
    :return: 
    """

    # Take a list for storing already visited vertexes
    if start_vertex not in graph or graph[start_vertex] is None or graph[start_vertex] == []:
        return None

    # create a list to store all the vertexes for BFS and a set to store the visited vertices
    visited, queue = set(), [start_vertex]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


# TODO: Are these necessary?
def time_complexities():
    """
    Return information on functions
    time complexity
    :return: string
    """
    return "O(V + E) where V = Number of vertices and E = Number of Edges"


def get_code():
    """
    easily retrieve the source code
    of the function

    :return: source code
    """
    return inspect.getsource(search)
