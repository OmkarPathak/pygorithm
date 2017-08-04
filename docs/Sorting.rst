=======
Sorting
=======

Just sort the way you want.

-----------------
Quick Start Guide
-----------------

.. code-block:: python

    from pygorithm.sorting import bubble_sort

    # This will print the code for bubble sort
    print(bubble_sort.get_code())

    myList = [12, 4, 2, 14, 3, 7, 5]

    # to sort the list
    sorted_list = bubble_sort.sort(myList)

--------
Features
--------

* Sorts available:
    - Bubble Sort (bubble_sort)
    - Selection Sort (selection_sort)
    - Insertion Sort (insertion_sort)
    - Merge Sort (merge_sort)
    - Quick Sort (quick_sort)

* Get time complexities of all the sorting algorithms

.. code-block:: python

    from pygorithm.sorting import bubble_sort

    # for printing time complexities of bubble_sort
    print(bubble_sort.time_complexities())

* Get the code used for any of the algorithm

.. code-block:: python

    from pygorithm.sorting import bubble_sort

    # for printing the source code of bubble_sort
    print(bubble_sort.get_code())
