"""
Fibonacci implementation through generator.
"""
import inspect


def get_sequence(n):
    """
    Return Fibonacci sequence from zero to specified number as list.
    """
    def fib():
        """
        Return Fibonacci value by specified number as integer.

        Golden ratio — https://en.wikipedia.org/wiki/Golden_ratio
        Fibonacci's relation to the golden ratio — https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
        """
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    def sequence(_n):
        """
        Return sequence of Fibonacci values as list.
        """
        f = fib()
        return [f.__next__() for _ in range(_n + 1)]

    return sequence(n)


def get_code():
    """
    Return source code of Fibonacci sequence logic's implementation.
    """
    return inspect.getsource(get_sequence)
