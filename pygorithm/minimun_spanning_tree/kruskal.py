"""
Kruskal algorithm for minimum spanning tree in a weighted graph with union–find data structure
"""
__author__ = "Michele De Vita <mik3dev@gmail.com>"
__date__ = "14/07/2017"


def get_vertexes(edges_weighted: list):
    return set(sum((edge for edge, weight in edges_weighted), ()))


def set_of(vertex, forest):
    for tree in forest:
        if vertex in tree:
            return tree
    return None


def union(u_set, v_set, forest):
    forest.remove(u_set)
    forest.remove(v_set)
    forest.append(v_set + u_set)
    return forest


def minimum_spanning_tree(edges_weighted: list):
    """
    :param edges_weighted: A list of pair with first element the edge as tuple
                                          and the weight as second element (e.g. ((1,4), 5) )
    :return: the list of edges explored
    """
    edges_weighted.sort(key=lambda pair: pair[1])
    edges_explored = []
    forest = [[v] for v in get_vertexes(edges_weighted)]
    for (u, v), weight in edges_weighted:
        u_set, v_set = set_of(u, forest), set_of(v, forest)
        if u_set != v_set:
            forest = union(u_set, v_set, forest)
            edges_explored.append(((u, v), weight))
    return edges_explored


def time_complexities():
    return '''Worst case: O(E log(V)) where E in the number of edges and V the number of vertexes'''


def get_code():
    import inspect
    return inspect.getsource(minimum_spanning_tree)
