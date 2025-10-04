"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Floyd-Warshall Algorithm for All-Pairs Shortest Path
Time Complexity: O(V^3) where V is the number of vertices
Space Complexity: O(V^2)

The Floyd-Warshall algorithm finds shortest paths between all pairs of vertices
in a weighted graph. It can handle negative edge weights but not negative cycles.
"""
import inspect


def floyd_warshall(graph):
    """
    Find shortest paths between all pairs of vertices using Floyd-Warshall algorithm
    
    :param graph: dictionary representing weighted graph {vertex: [(neighbor, weight), ...]}
    :return: tuple (distance_matrix, next_matrix) or None if negative cycle exists
    """
    if not graph:
        return {}, {}
    
    # Get all vertices
    vertices = set(graph.keys())
    for vertex in graph:
        for neighbor, _ in graph[vertex]:
            vertices.add(neighbor)
    
    vertices = sorted(list(vertices))
    n = len(vertices)
    vertex_to_index = {vertex: i for i, vertex in enumerate(vertices)}
    
    # Initialize distance and next matrices
    dist = [[float('inf')] * n for _ in range(n)]
    next_vertex = [[None] * n for _ in range(n)]
    
    # Distance from vertex to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Fill initial distances from graph
    for vertex in graph:
        i = vertex_to_index[vertex]
        for neighbor, weight in graph[vertex]:
            j = vertex_to_index[neighbor]
            dist[i][j] = weight
            next_vertex[i][j] = neighbor
    
    # Floyd-Warshall main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]
    
    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            return None  # Negative cycle detected
    
    # Convert back to vertex-based dictionaries
    distance_matrix = {}
    next_matrix = {}
    
    for i, vertex1 in enumerate(vertices):
        distance_matrix[vertex1] = {}
        next_matrix[vertex1] = {}
        for j, vertex2 in enumerate(vertices):
            distance_matrix[vertex1][vertex2] = dist[i][j]
            next_matrix[vertex1][vertex2] = next_vertex[i][j]
    
    return distance_matrix, next_matrix


def get_shortest_path(source, target, next_matrix):
    """
    Reconstruct shortest path between two vertices
    
    :param source: source vertex
    :param target: target vertex
    :param next_matrix: next matrix from Floyd-Warshall
    :return: list representing the shortest path
    """
    if source not in next_matrix or target not in next_matrix[source]:
        return None
    
    if next_matrix[source][target] is None:
        return None  # No path exists
    
    path = [source]
    current = source
    
    while current != target:
        current = next_matrix[current][target]
        if current is None:
            return None
        path.append(current)
    
    return path


def floyd_warshall_simple(adjacency_matrix):
    """
    Floyd-Warshall algorithm using adjacency matrix representation
    
    :param adjacency_matrix: 2D list representing weighted adjacency matrix
    :return: 2D list of shortest distances or None if negative cycle
    """
    if not adjacency_matrix or not adjacency_matrix[0]:
        return None
    
    n = len(adjacency_matrix)
    
    # Check if matrix is square
    for row in adjacency_matrix:
        if len(row) != n:
            return None
    
    # Create a copy of the adjacency matrix
    dist = [row[:] for row in adjacency_matrix]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            return None
    
    return dist


def print_distance_matrix(distance_matrix):
    """
    Print the distance matrix in a readable format
    
    :param distance_matrix: dictionary of distances
    :return: string representation of the matrix
    """
    if not distance_matrix:
        return "Empty distance matrix"
    
    vertices = sorted(distance_matrix.keys())
    result = "Distance Matrix:\n"
    
    # Header
    result += "     "
    for vertex in vertices:
        result += f"{vertex:>6}"
    result += "\n"
    
    # Rows
    for vertex1 in vertices:
        result += f"{vertex1:>4} "
        for vertex2 in vertices:
            dist = distance_matrix[vertex1][vertex2]
            if dist == float('inf'):
                result += "   ∞  "
            else:
                result += f"{dist:>6}"
        result += "\n"
    
    return result.strip()


def find_shortest_paths_from_vertex(distance_matrix, source):
    """
    Get all shortest paths from a source vertex
    
    :param distance_matrix: distance matrix from Floyd-Warshall
    :param source: source vertex
    :return: dictionary of distances from source
    """
    if source not in distance_matrix:
        return {}
    
    return distance_matrix[source].copy()


def find_diameter(distance_matrix):
    """
    Find the diameter of the graph (longest shortest path)
    
    :param distance_matrix: distance matrix from Floyd-Warshall
    :return: diameter value
    """
    if not distance_matrix:
        return float('inf')
    
    max_distance = 0
    for vertex1 in distance_matrix:
        for vertex2 in distance_matrix[vertex1]:
            if distance_matrix[vertex1][vertex2] != float('inf'):
                max_distance = max(max_distance, distance_matrix[vertex1][vertex2])
    
    return max_distance


def create_sample_adjacency_matrix():
    """
    Create a sample adjacency matrix for testing
    
    :return: 2D list representing adjacency matrix
    """
    INF = float('inf')
    return [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]


def create_sample_graph():
    """
    Create a sample weighted graph for testing
    
    :return: dictionary representing a weighted graph
    """
    return {
        'A': [('B', 3), ('D', 7)],
        'B': [('A', 8), ('C', 2)],
        'C': [('A', 5), ('D', 1)],
        'D': [('A', 2)]
    }


def has_negative_cycle(distance_matrix):
    """
    Check if the graph has a negative cycle
    
    :param distance_matrix: distance matrix
    :return: True if negative cycle exists, False otherwise
    """
    if not distance_matrix:
        return False
    
    for vertex in distance_matrix:
        if distance_matrix[vertex][vertex] < 0:
            return True
    
    return False


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(V^3), Average Case: O(V^3), Worst Case: O(V^3)"


def get_code():
    """
    Easily retrieve the source code of the floyd_warshall function
    :return: source code
    """
    return inspect.getsource(floyd_warshall)