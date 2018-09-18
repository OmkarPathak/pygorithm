
Pygorithm
=========

.. image:: http://pepy.tech/badge/pygorithm
   :target: http://pepy.tech/project/pygorithm
   :alt: Downloads

.. image:: https://readthedocs.org/projects/pygorithm/badge/?version=latest
   :target: http://pygorithm.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/badge/Python-3.6-brightgreen.svg
   :target: https://github.com/OmkarPathak/pygorithm
   :alt: Python 3.6

| A Python module to learn all the major algorithms on the go!
| Purely for educational purposes

Features
~~~~~~~~

* Super easy to use
* A very easy to understand `Documentation <http://pygorithm.readthedocs.io/en/latest/>`_
* Get the code right in your editor
* Get time complexities on the go

Installation
~~~~~~~~~~~~

* Just fire the following command in your terminal:

::

   pip3 install pygorithm

- | It's that easy. If you are using Python 2.7 use pip instead. Depending on your
  | permissions, you might need to use ``pip install --user pygorithm`` to install.

* Or you can download the source code from `here <https://github.com/OmkarPathak/pygorithm>`_, and then just install the package using

::

    python setup.py install


Quick Start Guide
~~~~~~~~~~~~~~~~~

* To sort your list

.. code:: python

    >>> from pygorithm.sorting import bubble_sort
    >>> my_list = [12, 4, 3, 5, 13, 1, 17, 19, 15]
    >>> sorted_list = bubble_sort.sort(my_list)
    >>> print(sorted_list)
    >>> [1, 3, 4, 5, 12, 13, 15, 17, 19]


* To get the code for function used

.. code:: python

    >>> from pygorithm.sorting import bubble_sort
    >>> code = bubble_sort.get_code()
    >>> print(code)


* To get the time complexity of an algorithm

.. code:: python

    >>> from pygorithm.sorting import bubble_sort
    >>> time_complexity = bubble_sort.time_complexities()
    >>> print(time_complexity)

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code:: python

    >>> from pygorithm import sorting
    >>> help(sorting)
        Help on package pygorithm.sorting in pygorithm:

        NAME
            pygorithm.sorting - Collection of sorting methods

        PACKAGE CONTENTS
            bubble_sort
            bucket_sort
            counting_sort
            heap_sort
            insertion_sort
            merge_sort
            modules
            quick_sort
            selection_sort
            shell_sort

    
Tests
~~~~~

* Just type in the following command to run the tests
::

    python3 -m unittest

* This will run all the tests defined in the files of the ``tests/`` directory


Donation
~~~~~~~~

If you have found my softwares to be of any use to you, do consider helping me pay my internet bills. This would encourage me to create many such softwares :)

- `PayPal <https://paypal.me/omkarpathak27>`_
- `₹ (INR) <https://www.instamojo.com/@omkarpathak/>`_
