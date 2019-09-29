"""
Author: Anthony Nguyen
Created On: 28 September 2019
"""

import math


def quadratic():
    """
    This function returns the x values that are the solutions to a quadratic equation given a, b, and c

    The quadratic equation is formed by ax^2+bx+c=0
    """
    a = float(input('Enter a:'))
    if a == 0:
        return 'You cannot have "a" be 0 in a standard quadratic equation. Try again.'
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
    d1 = math.sqrt((b ** 2) - (4 * a * c))
    d2 = -1 * (math.sqrt((b ** 2) - (4 * a * c)))
    return ((-1 * b) + d1) / (2 * a) and ((-1 * b) + d2) / (2 * a)
