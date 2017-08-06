=========
Searching
=========

Learning searching algorithms easily!

-----------------
Quick Start Guide
-----------------

.. code-block:: python

    # import the required searching algorithm
    from pygorithm.searching import binary_search

    myList = [12, 4, 2, 14, 3, 7, 5]

    # pre-requisite for binary search is that the list should be sorted
    myList.sort()

    # to search en element in the above list
    index = binary_search.search(myList, 7)
    print(index)

--------
Features
--------

* Searching algorithms available:
    - Linear Search (linear_search)
    - Binary Search (binary_search)
    - Breadth First Search (breadth_first_search)
    - Depth First Search (depth_first_search)

* For Searching:
  Remember search() function takes two parameters as a sorted list and the target element to be searched.

.. code-block:: python

    # import the required searching algorithm
    from pygorithm.searching import binary_search

    myList = [12, 4, 2, 14, 3, 7, 5]

    # pre-requisite for binary search is that the list should be sorted
    myList.sort()

    # to search en element in the above list
    index = binary_search.search(myList, 7)
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
