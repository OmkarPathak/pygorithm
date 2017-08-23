====
Math
====

Some of the mathematical algorithms and their implementations

Quick Start Guide
-----------------

.. code-block:: python

    # import the required math
    from pygorithm.math import lcm

    # find the lcm for all the elements in the list
    ans = lcm.lcm([3, 12, 16])

    #print the result
    print(ans)

Features
--------

* Algorithms available:
    - LCM (lcm)
    - Sieve of Eratostenes (sieve_of_eratosthenes)
    - Factorial
    - Binary To decimal conversion
    - Decimal to binary conversion
    - Hex To decimal conversion
    - Decimal to hex conversion

* To see all the available functions in a module there is a `modules()` function available. For example,

.. code:: python

    >>> from pygorithm.math import modules
    >>> modules.modules()
    ['lcm', 'sieve_of_eratosthenes']

* Get the code used for any of the algorithm

.. code-block:: python

    from pygorithm.math import lcm

    # for printing the source code of LCM function
    print(lcm.get_code())


LCM
---

* Functions and their uses

.. function:: lcm.lcm(List)

- **List**            : `list` or `array` of which LCM is to be found
- **Return Value**    : returns the integer value of LCM

.. function:: lcm.get_code()

- **Return Value**    : returns the code for the ``lcm.lcm()`` function

Sieve of Eratostenes
--------------------

* Functions and their uses

.. function:: sieve_of_eratostenes.sieve_of_eratostenes(n)

- **n**               : upper limit upto which prime numbers are to be found
- **Return Value**    : returns the `list` of all primes upto n

.. function:: sieve_of_eratostenes.get_code()

- **Return Value**    : returns the code for the ``sieve_of_eratostenes.sieve_of_eratostenes()`` function

Factorial
---------

* Functions and their uses

.. function:: factorial.factorial(number)

- **number**          : integer number of which factorial is to be found
- **Return Value**    : returns the integer of factorial of the number

.. function:: factorial.get_code()

- **Return Value**    : returns the code for the ``factorial.factorial()`` function


Conversion
----------

* Functions and their uses

.. function:: conversion.decimal_to_binary(number)

- **number**          : decimal number in string or integer format
- **Return Value**    : returns the string of equivalent binary number

.. function:: conversion.binary_to_decimal(number)

- **number**          : binary number in string or integer format
- **Return Value**    : returns the integer of equivalent decimal number

.. function:: conversion.decimal_to_hex(number)

- **number**          : decimal number in string or integer format
- **Return Value**    : returns the string of equivalent hex number

.. function:: conversion.hex_to_decimal(number)

- **number**          : hex number in string or integer format
- **Return Value**    : returns the integer of equivalent decimal number
