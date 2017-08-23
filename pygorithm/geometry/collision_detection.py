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


class Body:
    """Body
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


def broad_phase(body1, body2):
    """
    :type body1: object
    :type body2: object
    """
    d1x = body2.min_x - body1.max_x
    d1y = body2.min_y - body1.max_y
    d2x = body1.min_x - body2.max_x
    d2y = body1.min_y - body2.max_y

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

if __name__ == '__main__':
    coord1 = Coord(1, 1)
    coord2 = Coord(6, 8)
    body1 = Body(coord1, coord2)
    coord3 = Coord(4, 0)
    coord4 = Coord(7, 4)
    body2 = Body(coord3, coord4)
    print(broad_phase(body1, body2))