"""
Fibonacci implementation through cache.
"""
import inspect


def get_sequence(n):
    """
    Return Fibonacci sequence from zero to specified number.
    """
    cache = {0: 0, 1: 1}

    def fib(num):
        """
        Return Fibonacci value by specified number as integer.
        """
        if num in cache:
            return cache[num]
        cache[num] = fib(num - 1) + fib(num - 2)
        return cache[num]

    def sequence(num):
        """
        Return sequence of Fibonacci values as list.
        """
        return [fib(value) for value in range(num + 1)]

    return sequence(n)


def get_code():
    """
    Return source code of Fibonacci sequence logic's implementation.
    """
    return inspect.getsource(get_sequence)
