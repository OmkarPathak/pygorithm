"""
Author: Ashutosh Gupta
Created On: 8/17/2017
Time: 10:03 PM
"""
import inspect


def gcd(x, y):
    """
    Function to find gcm (greatest common divisor) of two numbers
    :param x: first number
    :param y: second number
    :return: gcd of x and y
    """
    while y != 0:
        (x, y) = (y, x % y)
    return x


def lcm_using_gcd(_list):
    """
    function to find LCM for given list of elements

    :param _list: _list of which LCM is to be found out
    """
    lcm = _list[0]
    for element in _list:
        lcm = lcm * element / gcd(lcm, element)
    return lcm


def get_code():
    """
    returns the code for the gcd function
    """
    return inspect.getsource(lcm_using_gcd)
