"""
Fibonacci implementation through golden ratio (math formula).
"""
import inspect
import math


def get_sequence(n):
    """
    Return Fibonacci sequence from zero
    to specified number as list.
    """
    return sequence(n)


def fib(n):
    """
    Return Fibonacci value by specified number as integer.

    Golden ratio —
    https://en.wikipedia.org/wiki/Golden_ratio
    Fibonacci's relation to the golden ratio —
    https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
    """
    golden_ratio = (1 + math.sqrt(5)) / 2

    val = (golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5)

    return int(val)


def sequence(n):
    """
    Return sequence of Fibonacci values as list.
    """
    return [fib(value) for value in range(n + 1)]


def get_code():
    """
    Return source code of Fibonacci sequence logic's implementation.
    """
    return inspect.getsource(get_sequence)
