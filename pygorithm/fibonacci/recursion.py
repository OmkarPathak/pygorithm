"""
Fibonacci implementation through recursion.
"""
import inspect


def get_sequence(n):
    """
    Return Fibonacci sequence from zero to specified number as list.
    """
    def fib(num):
        """
        Return Fibonacci value by specified number as integer.
        """
        if num <= 1:
            return num

        return fib(num - 1) + fib(num - 2)

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
