# Author: Ashutosh Gupta
# Created On: 8/15/2017
# Time: 3:24 PM

"""
nth fibonacci number - Space Optimized
"""

import inspect


def get_sequence(n):
    """
    Return Fibonacci sequence from zero to specified number as list.
    """

    def fib(n):
        """
        Return Fibonacci value by specified number as integer.
        """
        a = 0
        b = 1

        if n == 0:
            return a

        if n == 1:
            return b

        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

    def sequence(n):
        """
        Return sequence if Fibonacci values as list.
        """
        return [fib(value) for value in range(n + 1)]

    return sequence(n)


def get_code():
    """
    Return source code of Fibonacci sequence logic's implementation.
    """
    return inspect.getsource(get_sequence)

# Time Complexity: O(n)
# Extra Space: O(1)
