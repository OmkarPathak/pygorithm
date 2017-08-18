===============
Data Structures
===============

Implementing Data Structures purely in Python.

Quick Start Guide
-----------------

.. code-block:: python

    # import the required data structure
    from pygorithm.data_structures import stack

    # create a stack with default stack size 10
    myStack = stack.Stack()
    myStack.push(2)

    # print the contents of stack
    print(myStack)

Features
--------

* Data Structures implementations available:
    - **Stack**
        - Stack (data_structures.stack.Stack)
        - Infix to Postfix conversion (data_structures.stack.InfixToPostfix)
    - **Queue**
        - Queue (data_structures.queue.Queue)
        - Deque (data_structures.queue.Deque)
    - **Linked List**
        - Singly Linked List (data_structures.linked_list.SinglyLinkedList)
        - Doubly Linked List (data_structures.linked_list.DoublyLinkedList)
    - **Tree**
        - Binary Tree (data_structures.tree.BinaryTree)
        - Binary Seach Tree (data_structures.tree.BinarySearchTree)
    - **Graph**
        - Graph (data_structures.graph.Graph)
        - Topological Sort (data_structures.graph.TopologicalSort)
        - Check cycle in Directed Graph (data_structures.graph.CheckCycleDirectedGraph)
        - Check cycle in Undirected Graph (data_structures.graph.CheckCycleUndirectedGraph)
    - **Heap**
        - Heap (data_structures.heap.Heap)

* Get the code used for any of the implementation

.. code:: python

    from pygorithm.data_structures.stack import Stack

    myStack = Stack()
    print(myStack.get_code())

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code:: python

    >>> from pygorithm import data_structures
    >>> help(data_structures)
            Help on package pygorithm.data_structures in pygorithm:

            NAME
            pygorithm.data_structures

            PACKAGE CONTENTS
            graph
            heap
            linked_list
            modules
            queue
            stack
            tree
    >>> from pygorithm.data_structures import graph
    >>> help(graph)

Stack
-----

.. automodule:: pygorithm.data_structures.stack

    Stack
    -----
    .. autoclass:: Stack
       :members:

.. automodule:: pygorithm.data_structures.stack

    Infix to Postfix
    ----------------
    .. autoclass:: InfixToPostfix
       :members:



Queue
-----

.. automodule:: pygorithm.data_structures.queue

    Queue
    -----
    .. autoclass:: Queue
     :members:

.. automodule:: pygorithm.data_structures.queue

    Deque
    -----
    .. autoclass:: Deque
      :members:


Linked Lists
------------

.. automodule:: pygorithm.data_structures.linked_list

    Node
    ----
    .. autoclass:: Node
       :members:

.. automodule:: pygorithm.data_structures.linked_list

    Singly Linked List
    ------------------
    .. autoclass:: SinglyLinkedList
       :members:

.. automodule:: pygorithm.data_structures.linked_list

   Doubly Linked List
   ------------------
   .. autoclass:: DoublyLinkedList
      :members:

Tree
----

.. automodule:: pygorithm.data_structures.tree

    Node
    ----
    .. autoclass:: Node
       :members:

.. automodule:: pygorithm.data_structures.tree

    Binary Tree
    -----------
    .. autoclass:: BinaryTree
       :members:

.. automodule:: pygorithm.data_structures.tree

    Binary Search Tree Node
    -----------------------
    .. autoclass:: BSTNode
       :members:

    Binary Search Tree
    ------------------
    .. autoclass:: BinarySearchTree
       :members:

Graph
-----

.. automodule:: pygorithm.data_structures.graph

    Graph
    -----
    .. autoclass:: Graph
       :members:

.. automodule:: pygorithm.data_structures.graph

    Weighted Graph
    --------------
    .. autoclass:: WeightedGraph
       :members:

.. automodule:: pygorithm.data_structures.graph

    Topological Sort
    ----------------
    .. autoclass:: TopologicalSort
       :members:

.. automodule:: pygorithm.data_structures.graph

    Check Cycle in Directed Graph
    -----------------------------
    .. autoclass:: CheckCycleDirectedGraph
       :members:

.. automodule:: pygorithm.data_structures.graph

    Check Cycle in Undirected Graph
    -------------------------------
    .. autoclass:: CheckCycleUndirectedGraph
       :members:

Heap
----

.. automodule:: pygorithm.data_structures.heap

    Heap
    -----
    .. autoclass:: Heap
       :members:
