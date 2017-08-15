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

* To see all the available functions in a module there is a `modules()` function available. For example,

.. code:: python

    >>> from pygorithm.data_structures import modules
    >>> modules()
    ['graph', 'heap', 'linked_list', 'queue', 'stack', 'tree']

Stack
-----

.. automodule:: pygorithm.data_structures.stack

   Stack
   -----
   .. autoclass:: Stack
      :members:

.. automodule:: pygorithm.data_structures.stack

 Stack
 -----
 .. autoclass:: InfixToPostfix
    :members:
