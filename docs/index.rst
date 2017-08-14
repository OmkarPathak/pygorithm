=========
Pygorithm
=========

``Pygorithm``: A fun way to learn algorithms on the go! Just import the module and start learning, it's that easy.

A Python module written in pure python and for purely educational purposes.
Get the code, time complexities and much more by just importing the required algorithm.

Table of Contents:
------------------

.. toctree::
   :titlesonly:
   
   Sorting
   Searching
   Minimum spanning tree


-----------------
Quick Start Guide
-----------------

* Just import the required algorithm and start learning

.. code-block:: python

    from pygorithm.sorting import bubble_sort

    # This will print the code for bubble sort
    print(bubble_sort.get_code())

    myList = [12, 4, 2, 14, 3, 7, 5]

    # to sort the list
    sorted_list = bubble_sort.sort(myList)

---------------
Getting Started
---------------

* For getting started, first download the package using Python package manager

::

    pip3 install pygorithm

* For Python 2, you can use pip instead. Depending on your user permissions, you might need to ``sudo`` before installing


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
