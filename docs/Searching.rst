=========
Searching
=========

Learning searching algorithms easily!

Quick Start Guide
-----------------

.. code-block:: python

    # import the required searching algorithm
    from pygorithm.searching import binary_search

    my_list = [12, 4, 2, 14, 3, 7, 5]

    # pre-requisite for binary search is that the list should be sorted
    my_list.sort()

    # to search an element in the above list
    index = binary_search.search(my_list, 7)
    print(index)

Features
--------

* Searching algorithms available:
    - Linear Search (linear_search)
    - Binary Search (binary_search)
    - Breadth First Search (breadth_first_search)
    - Depth First Search (depth_first_search)

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code:: python

    >>> from pygorithm import searching
    >>> help(searching)
            Help on package pygorithm.searching in pygorithm:

            NAME
            pygorithm.searching - Collection of searching algorithms

            PACKAGE CONTENTS
            binary_search
            breadth_first_search
            depth_first_search
            linear_search
            modules
            quick_select


* For Searching:
  Remember ``search()`` function in `binary_search` module takes two parameters as a sorted list and the target element to be searched.

.. code-block:: python

    # import the required searching algorithm
    from pygorithm.searching import binary_search

    my_list = [12, 4, 2, 14, 3, 7, 5]

    # pre-requisite for binary search is that the list should be sorted
    my_list.sort()

    # to search an element in the above list
    index = binary_search.search(my_list, 7)
    print(index)

* Get time complexities of all the searching algorithms

.. code-block:: python

    from pygorithm.searching import binary_search

    # for printing time complexities of binary_search
    print(binary_search.time_complexities())

* Get the code used for any of the algorithm

.. code-block:: python

    from pygorithm.searching import binary_search

    # for printing the source code of bubble_sort
    print(binary_search.get_code())


Binary Search
-------------

* Functions and their uses

.. function:: binary_search.search(_list, target)
   :module: pygorithm.searching

- **_list**            : *Sorted* list in which the target is to be searched
- **target**             : target to be searched in the list
- **Return Value**    : returns the position (index) of the target if target found, else returns False

.. function:: binary_search.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: binary_search.get_code()

- **Return Value**    : returns the code for the ``binary_search.search()`` function

Linear Search
-------------

* Functions and their uses

.. function:: linear_search.search(_list, target)

- **_list**            : the list in which item is to searched
- **target**             : target to be searched in the list
- **Return Value**    : returns the position (index) of the target if target found, else returns False

.. function:: linear_search.time_complexities()

- **Return value**      : returns time complexities (Best, Average, Worst)

.. function:: linear_search.get_code()

- **Return Value**      : returns the code for the ``linear_search.search()`` function

Breadth First Search
--------------------

* Functions and their uses

.. function:: breadth_first_search.search(graph, startVertex)

- **graph**           : takes the graph data structures with edges and vertices
- **startVertex**     : it tells the function the vertex to start with
- **Return Value**    : returns the `set` of bfs for the ``graph``

.. function:: breadth_first_search.time_complexities()

- **Return Value**    : returns time complexities

.. function:: breadth_first_search.get_code()

- **Return Value**    : returns the code for the ``breadth_first_search.search()`` function

Depth First Search
------------------

* Functions and their uses

.. function:: breadth_first_search.search(graph, start, path)

- **graph**           : takes the graph data structures with edges and vertices
- **start**           : it tells the function the vertex to start with
- **path**            : returns the list containing the required dfs
- **Return Value**    : returns the `list` of dfs for the ``graph``

.. function:: breadth_first_search.time_complexities()

- **Return Value**    : returns time complexities

.. function:: breadth_first_search.get_code()

- **Return Value**    : returns the code for the ``depth_first_search.search()`` function

Quick Select Search
------------------

* Functions and their uses

.. function:: quick_select.search(array, n)

- **array**           : an unsorted array
- **n**               : nth number to be searched in the given `array`
- **Return Value**    : returns the nth element

.. function:: quick_select.time_complexities()

- **Return Value**    : returns time complexities

.. function:: quick_select.get_code()

- **Return Value**    : returns the code for the ``quick_select.search()`` function

Interpolation Search
--------------------

* Functions and their uses

.. function:: interpolation_search.search(_list, target)
   :module: pygorithm.searching

- **_list**           : *Sorted* list in which the target is to be searched
- **target**          : target to be searched in the list
- **Return Value**    : returns the position (index) of the target if target found, else returns False

.. function:: interpolation_search.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: interpolation_search.get_code()

- **Return Value**    : returns the code for the ``interpolation_search.search()`` function
