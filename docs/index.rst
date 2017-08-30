=========
Pygorithm
=========

Introduction
------------

``Pygorithm``: A fun way to learn algorithms on the go! Just import the module and start learning, it's that easy.

A Python module written in pure python and for purely educational purposes.
Get the code, time complexities and much more by just importing the required algorithm. A good way to start
learning Python programming. Learn implementation of all major algorithms in Python.
No need to surf the internet to get the required code. Just install this module and get going.

Quick Links
-----------

* `Source Code <https://github.com/OmkarPathak/pygorithm>`_
* `Documentation <http://pygorithm.readthedocs.io/en/latest/>`_

.. toctree::
   :maxdepth: 2
   :caption: Documentation:

   Binary
   Data_Structure
   DynamicP
   Fibonacci
   Geometry
   Greedy
   Math
   Pathfinding
   Searching
   Sorting
   strings

Quick Start Guide
-----------------

* Download and install the Python package. `Installation instructions <http://pygorithm.readthedocs.io/en/latest/#getting-started>`_
* Just import the required algorithm and start learning

.. code-block:: python

    from pygorithm.sorting import bubble_sort

    # This will print the code for bubble sort
    print(bubble_sort.get_code())

    my_list = [12, 4, 2, 14, 3, 7, 5]

    # to sort the list
    sorted_list = bubble_sort.sort(my_list)

Getting Started
---------------

* For getting started, first download the package using Python package manager

::

    pip3 install pygorithm

* For Python 2, you can use pip instead.
* Or you can download the source code from `here <https://github.com/OmkarPathak/pygorithm>`_, and then just install the package using

::

    python setup.py install
