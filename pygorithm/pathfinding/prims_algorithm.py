"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Prim's Algorithm for Minimum Spanning Tree
Time Complexity: O(E log V) with priority queue, O(V^2) with adjacency matrix
Space Complexity: O(V)

Prim's algorithm finds a minimum spanning tree for a weighted undirected graph.
It builds the MST by starting from an arbitrary vertex and repeatedly adding
the minimum weight edge that connects a vertex in the MST to a vertex outside.
"""
import inspect
import heapq


def prims_mst(graph, start_vertex=None):
    """
    Find Minimum Spanning Tree using Prim's algorithm
    
    :param graph: dictionary representing weighted undirected graph {vertex: [(neighbor, weight), ...]}
    :param start_vertex: starting vertex (if None, uses first vertex)
    :return: tuple (mst_edges, total_weight) where mst_edges is list of (vertex1, vertex2, weight)
    """
    if not graph:
        return [], 0
    
    # Get all vertices
    vertices = set(graph.keys())
    for vertex in graph:
        for neighbor, _ in graph[vertex]:
            vertices.add(neighbor)
    
    if start_vertex is None:
        start_vertex = next(iter(vertices))
    
    if start_vertex not in vertices:
        return [], 0
    
    mst_edges = []
    total_weight = 0
    visited = {start_vertex}
    
    # Priority queue: (weight, vertex1, vertex2)
    edge_queue = []
    
    # Add all edges from start vertex to queue
    if start_vertex in graph:
        for neighbor, weight in graph[start_vertex]:
            heapq.heappush(edge_queue, (weight, start_vertex, neighbor))
    
    while edge_queue and len(visited) < len(vertices):
        weight, vertex1, vertex2 = heapq.heappop(edge_queue)
        
        # Skip if both vertices are already in MST
        if vertex2 in visited:
            continue
        
        # Add edge to MST
        mst_edges.append((vertex1, vertex2, weight))
        total_weight += weight
        visited.add(vertex2)
        
        # Add all edges from newly added vertex
        if vertex2 in graph:
            for neighbor, edge_weight in graph[vertex2]:
                if neighbor not in visited:
                    heapq.heappush(edge_queue, (edge_weight, vertex2, neighbor))
    
    return mst_edges, total_weight


def prims_mst_adjacency_matrix(adj_matrix, vertices=None):
    """
    Find MST using Prim's algorithm with adjacency matrix
    
    :param adj_matrix: 2D list representing weighted adjacency matrix (use float('inf') for no edge)
    :param vertices: list of vertex names (if None, uses indices)
    :return: tuple (mst_edges, total_weight)
    """
    if not adj_matrix or not adj_matrix[0]:
        return [], 0
    
    n = len(adj_matrix)
    
    # Check if matrix is square
    for row in adj_matrix:
        if len(row) != n:
            return [], 0
    
    if vertices is None:
        vertices = list(range(n))
    elif len(vertices) != n:
        return [], 0
    
    mst_edges = []
    total_weight = 0
    visited = [False] * n
    min_edge = [float('inf')] * n
    parent = [-1] * n
    
    # Start from vertex 0
    min_edge[0] = 0
    
    for _ in range(n):
        # Find minimum edge
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        visited[u] = True
        
        if parent[u] != -1:
            mst_edges.append((vertices[parent[u]], vertices[u], min_edge[u]))
            total_weight += min_edge[u]
        
        # Update minimum edges
        for v in range(n):
            if not visited[v] and adj_matrix[u][v] < min_edge[v]:
                min_edge[v] = adj_matrix[u][v]
                parent[v] = u
    
    return mst_edges, total_weight


def is_connected_graph(graph):
    """
    Check if the graph is connected (required for MST)
    
    :param graph: dictionary representing the graph
    :return: True if connected, False otherwise
    """
    if not graph:
        return True
    
    # Get all vertices
    vertices = set(graph.keys())
    for vertex in graph:
        for neighbor, _ in graph[vertex]:
            vertices.add(neighbor)
    
    if len(vertices) <= 1:
        return True
    
    # DFS to check connectivity
    start_vertex = next(iter(vertices))
    visited = set()
    stack = [start_vertex]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex in graph:
                for neighbor, _ in graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
    
    return len(visited) == len(vertices)


def print_mst(mst_edges, total_weight):
    """
    Print the Minimum Spanning Tree in a readable format
    
    :param mst_edges: list of MST edges
    :param total_weight: total weight of MST
    :return: string representation of MST
    """
    if not mst_edges:
        return "No MST found (graph might be disconnected)"
    
    result = "Minimum Spanning Tree:\n"
    result += "Edges:\n"
    
    for vertex1, vertex2, weight in mst_edges:
        result += f"  {vertex1} -- {vertex2} : {weight}\n"
    
    result += f"Total Weight: {total_weight}"
    return result


def create_sample_graph():
    """
    Create a sample weighted undirected graph for testing
    
    :return: dictionary representing a weighted graph
    """
    return {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1), ('E', 4)],
        'C': [('A', 3), ('B', 1), ('E', 5)],
        'D': [('B', 1), ('E', 1)],
        'E': [('B', 4), ('C', 5), ('D', 1)]
    }


def create_sample_adjacency_matrix():
    """
    Create a sample adjacency matrix for testing
    
    :return: tuple (adjacency_matrix, vertex_names)
    """
    INF = float('inf')
    matrix = [
        [0, 2, 3, INF, INF],
        [2, 0, 1, 1, 4],
        [3, 1, 0, INF, 5],
        [INF, 1, INF, 0, 1],
        [INF, 4, 5, 1, 0]
    ]
    vertices = ['A', 'B', 'C', 'D', 'E']
    return matrix, vertices


def validate_mst(graph, mst_edges):
    """
    Validate if the given edges form a valid MST
    
    :param graph: original graph
    :param mst_edges: proposed MST edges
    :return: True if valid MST, False otherwise
    """
    if not graph or not mst_edges:
        return False
    
    # Get all vertices
    vertices = set(graph.keys())
    for vertex in graph:
        for neighbor, _ in graph[vertex]:
            vertices.add(neighbor)
    
    # MST should have exactly V-1 edges
    if len(mst_edges) != len(vertices) - 1:
        return False
    
    # Check if all edges exist in original graph
    graph_edges = set()
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edge = tuple(sorted([vertex, neighbor])) + (weight,)
            graph_edges.add(edge)
    
    for vertex1, vertex2, weight in mst_edges:
        edge = tuple(sorted([vertex1, vertex2])) + (weight,)
        if edge not in graph_edges:
            return False
    
    # Check connectivity using Union-Find
    parent = {}
    
    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    components = len(vertices)
    for vertex1, vertex2, _ in mst_edges:
        if union(vertex1, vertex2):
            components -= 1
    
    return components == 1


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(E log V), Average Case: O(E log V), Worst Case: O(E log V) with priority queue"


def get_code():
    """
    Easily retrieve the source code of the prims_mst function
    :return: source code
    """
    return inspect.getsource(prims_mst)