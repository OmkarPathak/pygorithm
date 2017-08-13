=======
Sorting
=======

Just sort the way you want.

Quick Start Guide
-----------------

.. code-block:: python

    # import the required sort
    from pygorithm.sorting import bubble_sort

    myList = [12, 4, 2, 14, 3, 7, 5]

    # to sort the list
    sorted_list = bubble_sort.sort(myList)

Features
--------

* Sorts available:
    - Bubble Sort (bubble_sort)
    - Selection Sort (selection_sort)
    - Insertion Sort (insertion_sort)
    - Merge Sort (merge_sort)
    - Quick Sort (quick_sort)
    - Bucket Sort (bucket_sort)
    - Counting Sort (counting_sort)
    - Heap Sort (heap_sort)
    - Shell Sort (shell_sort)

* To see all the available functions in a module there is a `modules()` function available. For example,

.. code:: python

    >>> from pygorithm.sorting import modules
    >>> modules.modules()
    ['bubble_sort', 'bucket_sort', 'counting_sort', 'heap_sort', 'insertion_sort', 'merge_sort', 'quick_sort', 'selection_sort', 'shell_sort']

* For sorting:
  Remember ``sort()`` function takes its parameter as a list only.

.. code-block:: python

    # import the required sort
    from pygorithm.sorting import bubble_sort

    myList = [12, 4, 2, 14, 3, 7, 5]

    # to sort the list
    sorted_list = bubble_sort.sort(myList)

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


Bubble Sort
-----------

* Functions and their uses

.. function:: bubble_sort.sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: bubble_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: bubble_sort.get_code()

- **Return Value**    : returns the code for the ``bubble_sort.sort()`` function

* For improved Bubble sort

.. function:: bubble_sort.improved_sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

Bucket Sort
-----------

* Functions and their uses

.. function:: bucket_sort.sort(List, bucketSize)

- **List**            : `list` or `array` to be sorted
- **bucketSize**      : size of the bucket. Default is **5**
- **Return Value**    : returns the sorted `list`

.. function:: bucket_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: bucket_sort.get_code()

- **Return Value**    : returns the code for the ``bucket_sort.sort()`` function

Counting Sort
-------------

* Functions and their uses

.. function:: counting_sort.sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: counting_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: counting_sort.get_code()

- **Return Value**    : returns the code for the ``counting_sort.sort()`` function

Heap Sort
---------

* Functions and their uses

.. function:: heap_sort.sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: heap_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: heap_sort.get_code()

- **Return Value**    : returns the code for the ``heap_sort.sort()`` function

Insertion Sort
--------------

* Functions and their uses

.. function:: insertion_sort.sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: insertion_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: insertion_sort.get_code()

- **Return Value**    : returns the code for the ``insertion_sort.sort()`` function

Merge Sort
----------

* Functions and their uses

.. function:: merge_sort.sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: merge_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: merge_sort.get_code()

- **Return Value**    : returns the code for the ``merge_sort.sort()`` function

Quick Sort
----------

* Functions and their uses

.. function:: quick_sort.sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: quick_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: quick_sort.get_code()

- **Return Value**    : returns the code for the ``quick_sort.sort()`` function

Selection Sort
--------------

* Functions and their uses

.. function:: selection_sort.sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: selection_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: selection_sort.get_code()

- **Return Value**    : returns the code for the ``selection_sort.sort()`` function

Shell Sort
----------

* Functions and their uses

.. function:: shell_sort.sort(List)

- **List**            : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: shell_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: shell_sort.get_code()

- **Return Value**    : returns the code for the ``shell_sort.sort()`` function
