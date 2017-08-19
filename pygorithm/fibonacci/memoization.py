"""
Fibonacci implementation through cache.
"""
import inspect
# TODO: Fix shadowed parameter names


def get_sequence(n):
    """
    Return Fibonacci sequence from zero to specified number.
    """
    cache = {0: 0, 1: 1}

    def fib(n):
        """
        Return Fibonacci value by specified number as integer.
        """
        if n in cache:
            return cache[n]
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

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
