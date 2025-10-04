"""
Author: ADWAITA JADHAV
Created On: 4th October 2025

Bellman-Ford Algorithm for Single Source Shortest Path
Time Complexity: O(V * E) where V is vertices and E is edges
Space Complexity: O(V)

The Bellman-Ford algorithm finds shortest paths from a single source vertex
to all other vertices in a weighted graph. Unlike Dijkstra's algorithm,
it can handle negative edge weights and detect negative cycles.
"""
import inspect


def bellman_ford(graph, source):
    """
    Find shortest paths from source to all vertices using Bellman-Ford algorithm
    
    :param graph: dictionary representing weighted graph {vertex: [(neighbor, weight), ...]}
    :param source: source vertex
    :return: tuple (distances, predecessors) or None if negative cycle exists
    """
    if source not in graph:
        return None
    
    # Get all vertices
    vertices = set(graph.keys())
    for vertex in graph:
        for neighbor, _ in graph[vertex]:
            vertices.add(neighbor)
    
    # Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in vertices}
    predecessors = {vertex: None for vertex in vertices}
    distances[source] = 0
    
    # Relax edges repeatedly
    for _ in range(len(vertices) - 1):
        for vertex in graph:
            if distances[vertex] != float('inf'):
                for neighbor, weight in graph[vertex]:
                    if distances[vertex] + weight < distances[neighbor]:
                        distances[neighbor] = distances[vertex] + weight
                        predecessors[neighbor] = vertex
    
    # Check for negative cycles
    for vertex in graph:
        if distances[vertex] != float('inf'):
            for neighbor, weight in graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    return None  # Negative cycle detected
    
    return distances, predecessors


def bellman_ford_with_path(graph, source, target):
    """
    Find shortest path from source to target using Bellman-Ford algorithm
    
    :param graph: dictionary representing weighted graph
    :param source: source vertex
    :param target: target vertex
    :return: tuple (distance, path) or None if no path or negative cycle
    """
    result = bellman_ford(graph, source)
    if result is None:
        return None  # Negative cycle
    
    distances, predecessors = result
    
    if target not in distances or distances[target] == float('inf'):
        return None  # No path to target
    
    # Reconstruct path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    path.reverse()
    return distances[target], path


def detect_negative_cycle(graph):
    """
    Detect if the graph contains a negative cycle
    
    :param graph: dictionary representing weighted graph
    :return: True if negative cycle exists, False otherwise
    """
    if not graph:
        return False
    
    # Try Bellman-Ford from any vertex
    source = next(iter(graph))
    result = bellman_ford(graph, source)
    return result is None


def bellman_ford_all_pairs(graph):
    """
    Find shortest paths between all pairs of vertices
    
    :param graph: dictionary representing weighted graph
    :return: dictionary of distances or None if negative cycle exists
    """
    vertices = set(graph.keys())
    for vertex in graph:
        for neighbor, _ in graph[vertex]:
            vertices.add(neighbor)
    
    all_distances = {}
    
    for source in vertices:
        result = bellman_ford(graph, source)
        if result is None:
            return None  # Negative cycle
        
        distances, _ = result
        all_distances[source] = distances
    
    return all_distances


def create_sample_graph():
    """
    Create a sample weighted graph for testing
    
    :return: dictionary representing a weighted graph
    """
    return {
        'A': [('B', -1), ('C', 4)],
        'B': [('C', 3), ('D', 2), ('E', 2)],
        'C': [],
        'D': [('B', 1), ('C', 5)],
        'E': [('D', -3)]
    }


def create_negative_cycle_graph():
    """
    Create a graph with a negative cycle for testing
    
    :return: dictionary representing a graph with negative cycle
    """
    return {
        'A': [('B', 1)],
        'B': [('C', -3)],
        'C': [('D', 2)],
        'D': [('B', -1)]
    }


def print_distances(distances, source):
    """
    Print the shortest distances from source to all vertices
    
    :param distances: dictionary of distances
    :param source: source vertex
    :return: string representation of distances
    """
    if not distances:
        return "No distances to display"
    
    result = f"Shortest distances from {source}:\n"
    for vertex in sorted(distances.keys()):
        if distances[vertex] == float('inf'):
            result += f"{source} -> {vertex}: ∞\n"
        else:
            result += f"{source} -> {vertex}: {distances[vertex]}\n"
    
    return result.strip()


def is_valid_graph(graph):
    """
    Check if the graph representation is valid
    
    :param graph: dictionary to validate
    :return: True if valid, False otherwise
    """
    if not isinstance(graph, dict):
        return False
    
    for vertex, edges in graph.items():
        if not isinstance(edges, list):
            return False
        for edge in edges:
            if not isinstance(edge, tuple) or len(edge) != 2:
                return False
            neighbor, weight = edge
            if not isinstance(weight, (int, float)):
                return False
    
    return True


def time_complexities():
    """
    Return information on time complexity
    :return: string
    """
    return "Best Case: O(V * E), Average Case: O(V * E), Worst Case: O(V * E)"


def get_code():
    """
    Easily retrieve the source code of the bellman_ford function
    :return: source code
    """
    return inspect.getsource(bellman_ford)