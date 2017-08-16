# Author: OMKAR PATHAK
# Created On: 1st August 2017

#  depth first search algorithm
def search(graph, start, path = []):
    # check if graph is empty or start vertex is none
    if start not in graph or graph[start] is None or graph[start] == []:
        return None
    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path = search(graph, edge, path)
    return path

# time complexities
def time_complexities():
    return '''O(V + E) where V = Number of vertices and E = Number of Edges'''

# easily retrieve the source code of the dfs function
def get_code():
    import inspect
    return inspect.getsource(search)
