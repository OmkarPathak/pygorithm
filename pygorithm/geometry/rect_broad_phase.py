"""
Author: ALEXEY SARAPULOV
Created On: 23 August 2017
"""

# To test if two rectangle intersect, we only have to find out
# if their projections intersect on all of the coordinate axes

import inspect


class Coord:
    """Coord
    Class to initialize Coordinate of one point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class SimpleRectangle:
    """SimpleRectangle
    Class to initialize Body of Object
    """

    def __init__(self, coord1, coord2):
        """
        :type coord1: object of class Coord
        :type coord2: object of class Coord
        """
        self.min_x = coord1.x
        self.min_y = coord1.y
        self.max_x = coord2.x
        self.max_y = coord2.y


def broad_phase(simpleRect1, simpleRect2):
    """
    :type simpleRect1: object
    :type simpleRect2: object
    """
    d1x = simpleRect2.min_x - simpleRect1.max_x
    d1y = simpleRect2.min_y - simpleRect1.max_y
    d2x = simpleRect1.min_x - simpleRect2.max_x
    d2y = simpleRect1.min_y - simpleRect2.max_y

    if d1x > 0 or d1y > 0:
        return False

    if d2x > 0 or d2y > 0:
        return False

    return True


def get_code():
    """
    returns the code for the broad phase function
    """
    return inspect.getsource(broad_phase)