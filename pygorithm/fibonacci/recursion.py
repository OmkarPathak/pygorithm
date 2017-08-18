"""
Fibonacci implementation through recursion.
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
        if n <= 1:
            return n

        return fib(n - 1) + fib(n - 2)

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
