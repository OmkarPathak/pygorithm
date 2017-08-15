# Author: Ashutosh Gupta
# Created On: 8/15/2017
# Time: 3:24 PM

"""
nth fibonacci number - Space Optimized
Time Complexity: O(n)
Extra Space: O(1)
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
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b

        return a

    def sequence(n):
        """
        Return sequence of Fibonacci values as list.
        """
        return [fib(value) for value in range(n + 1)]

    return sequence(n)


def get_code():
    """
    Return source code of Fibonacci sequence logic's implementation.
    """
    return inspect.getsource(get_sequence)
