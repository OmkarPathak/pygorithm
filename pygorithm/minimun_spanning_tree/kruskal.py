import copy


def get_nodes(edges_weighted: list):
    return set(sum((edge for edge, weight in edges_weighted), ()))


def is_reversed(curr_edge, edge):
    return curr_edge[0] == edge[1] and curr_edge[1] == edge[0]


def has_cycle(edges_w):
    edges_w += [((b, a), weight) for (a, b), weight in edges_w]
    for edge, weight in edges_w:
        if rec_cycle_detector(edge, edge, copy.deepcopy(edges_w), 1):
            return True
    return False


def rec_cycle_detector(s_edge, curr_edge, edges_w, step=None):
    if step > 2 and curr_edge[1] == s_edge[0]:
        return True
    neightbours = ((edge, weight) for edge, weight in edges_w if
                   curr_edge[1] == edge[0] and not is_reversed(curr_edge, edge))
    for neightbour in neightbours:
        edges_w.remove(neightbour)
        if rec_cycle_detector(s_edge, neightbour[0], edges_w, step + 1):
            return True
    return False


def vertex_of(edge_w: tuple) -> set:
    return set(edge_w[0])


def minimum_spanning_tree(edges_weighted: list):
    """
    :param edges_weighted: A list of pair with first element the edge as tuple (e.g. (1,4))
                                          and the weight as second element
    :return:
    """
    edges_weighted.sort(key=lambda pair: pair[1])
    edges_list = []
    e_vertexes = set()
    vertexes = get_nodes(edges_weighted)
    while vertexes != e_vertexes:
        edge_w = edges_weighted.pop(0)
        if (len(edges_list) > 2 and not has_cycle(edges_list + [edge_w])) or len(edges_list) <= 2:
            e_vertexes.update(vertex_of(edge_w))
            edges_list.append(edge_w)
    return edges_list
