=======================
Path Finding Algorithms
=======================

Some pathfinding algorithms and their implementations

Quick Start Guide
-----------------

.. code-block:: python

    # import the required pathing algorithm
    from pygorithm.pathing import dijkstra

    # import a graph data structure
    from pygorithm.data_structures import graph

    # initialize the graph with nodes from (0, 0) to (4, 4)
    # with weight corresponding to distance (orthogonal
    # is 1, diagonal is sqrt(2))
    my_graph = graph.WeightedUndirectedGraph()
    my_graph.gridify(5, 1)

    # make the graph more interesting by removing along the
    # x=2 column except for (2,4)
    my_graph.remove_edge((2, 0))
    my_graph.remove_edge((2, 1))
    my_graph.remove_edge((2, 2))
    my_graph.remove_edge((2, 3))

    # calculate a path
    my_path = dijkstra.find_path(my_graph, (0, 0), (3, 0))

    # print path
    print(' -> '.join(my_path))
    # (0, 0) -> (1, 1) -> (0, 2) -> (1, 3) -> (2, 4) -> (3, 3) -> (3, 2) -> (3, 1) -> (3, 0)

Features
--------

* Algorithms available:
    - Dijkstra (dijkstra)
    - Unidirectional AStar (astar)
    - BiDirectional AStar (astar)


* To see all the available functions in a module there is a `modules()` function available. For example,

.. code:: python

    >>> from pygorithm.pathfinding import modules
    >>> modules.modules()
    ['dijkstra', 'astar']

* Get the code used for any of the algorithm

.. code-block:: python

    from pygorithm.pathing import dijkstra

    # for printing the source code of Dijkstra object
    print(dijkstra.Dijikstra.get_code())

Dijkstra
--------

* Functions and their uses

.. function:: dijkstra.Dijkstra.find_path(pygorithm.data_structures.WeightedUndirectedGraph, vertex, vertex)

- **pygorithm.data_structures.WeightedUndirectedGraph** : acts like an object with `graph` (see WeightedUndirectedGraph)
- **vertex** : any hashable type for the start of the path
- **vertex** : any hashable type for the end of the path
- **Return Value**    : returns a `List` of vertexes (of the same type as the graph) starting with from and going to to. This algorithm does *not* respect weights.

.. function:: dijkstra.get_code()

- **Return Value**    : returns the code for the ``Dijkstra`` object

Unidirectional AStar
--------------------

* Functions and their uses

.. function:: astar.OneDirectionalAStar.find_path(pygorithm.data_structures.WeightedUndirectedGraph, vertex, vertex, function)

- **pygorithm.data_structures.WeightedUndirectedGraph** : acts like an object with `graph` and `get_edge_weight` (see WeightedUndirectedGraph)
- **vertex** : any hashable type for the start of the path
- **vertex** : any hashable type for the end of the path
- **function** : `function(graph, vertex, vertex)` returns numeric - a heuristic function for distance between two vertices
- **Return Value** : returns a `List` of vertexes (of the same type of the graph) starting from from and going to to. This algorithm respects weights, but is only guarranteed to be optimal if the heuristic is admissable. An admissable function will never *overestimate* the cost from one node to another (in other words, it is optimistic).

BiDirectional AStar
-------------------

* Functions and their uses

.. function:: astar.BiDirectionalAStar.find_path(pygorithm.data_structures.WeightedUndirectedGraph, vertex, vertex, function)

- **pygorithm.data_structures.WeightedUndirectedGraph** : acts like an object with `graph` and `get_edge_weight` (see WeightedUndirectedGraph)
- **vertex** : any hashable type for the start of the path
- **vertex** : any hashable type for the end of the path
- **function** : `function(graph, vertex, vertex)` returns numeric - a heuristic function for distance between two vertices
- **Return Value** : returns a `List` of vertexes (of the same type of the graph) starting from from and going to to. This algorithm respects weights, but is only guarranteed to be optimal if the heuristic is admissable. An admissable function will never *overestimate* the cost from one node to another (in other words, it is optimistic).