=========
Pygorithm
=========

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


Quick Start Guide
~~~~~~~~~~~~~~~~~

* To sort your list

.. code:: python

    from pygorithm.sorting import bubble_sort
    myList = [12, 4, 3, 5, 13, 1, 17, 19, 15]
    sortedList = bubble_sort.sort(myList)
    print(sortedList)


* To get the code for function used

.. code:: python

    from pygorithm.sorting import bubble_sort
    code = bubble_sort.get_code()
    print(code)


* To get the time complexity of an algorithm

.. code:: python

    from pygorithm.sorting import bubble_sort
    time_complexity = bubble_sort.time_complexities()
    print(time_complexity)
