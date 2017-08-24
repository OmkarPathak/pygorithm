"""
Author: OMKAR PATHAK
Created On: 22 August 2017
"""
import inspect


def factorial(number):
    """
    This recursive function calculates the factorial of a number

    In math, the factorial function is
    represented by (!) exclamation mark.

    Example:

        3! = 3 * 2 * 1
           = (6) * 1
        3! =  6

    """
    if not isinstance(number, int):
        raise Exception('Enter an integer number to find the factorial')
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def get_code():
    """
    returns the code for the factorial function
    """
    return inspect.getsource(factorial)
