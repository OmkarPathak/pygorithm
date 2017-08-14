=======================
Minimum spanning tree
=======================


Given a weighted connected graph (a graph with weights on the edges), the minimum spanning tree is a spanning tree that
minimize the weights of the edges.


==========================
Features
==========================

* Algorithms implemented:
    - Kruskal

* To create the Minimum spanning tree use the *minimum_spanning_tree* function, it takes in input the list of weighted edges, that it is represented in python as a tuple composed by the edge, a tuple of two vertexes identified by numbers, and the weight, a number (e.g. ((2,5), 5))

* Code example:

.. code-block:: python

    from pygorithm.minimum_spanning_tree import kruskal
    edges_weighted = [((1,2), 4), ((2, 4), 5), ((1,3), 13), ((2, 3),  9), ((1, 4), 1)]
    kruskal.minimum_spanning_tree(edges_weighted) #[((1, 4), 1), ((1, 2), 4), ((2, 3), 9)]