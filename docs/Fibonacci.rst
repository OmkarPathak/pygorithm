=========
Fibonacci
=========

Learning fibonacci implementations in few ways!

Quick Start Guide
-----------------

.. code-block:: python

    from pygorithm.fibonacci import recursion as fib_recursion

    sequence = fib_recursion.get_sequence(10)
    print(sequence)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

Features
--------

* Fibonacci implementations available:
    - Generator
    - Golden ratio
    - Memorization (which saves some recursions to avoid computation of same series again and again)
    - Recursion

* Get the code used for any of the implementation

.. code:: python

    from pygorithm.fibonacci import recursion as fib_recursion

    code = fib_recursion.get_code()
    print(code)

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code:: python

    >>> from pygorithm import fibonacci
    >>> help(fibonacci)
            Help on package pygorithm.fibonacci in pygorithm:

            NAME
            pygorithm.fibonacci - Collection of fibonacci methods and functions

            PACKAGE CONTENTS
            generator
            goldenratio
            memoization
            modules
            recursion


Implementations API
-------------------

* Functions and their uses

.. function:: get_sequence(number)

- **number**          : arbitrary integer, that need to be calculated in Fibonacci number type
- **Return Value**    : return Fibonacci value by specified number as integer

.. function:: get_code()

- **Return Value**    : returns the code for the ``get_sequence()`` function
