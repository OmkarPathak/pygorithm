"""
axisall

Author: Timothy Moore

Defines a class for handling axis-aligned two-dimensional lines 
segments. This class simplifies intermediary calculations in
SAT and similiar algorithms.

These are 2dimensional axis-aligned objects
https://en.wikipedia.org/wiki/Axis-aligned_object
"""

import math

class AxisAlignedLine(object):
    """
    Define an axis aligned line.
    
    This class provides functions related to axis aligned lines as well as 
    acting as a convienent container for them. In this context, an axis 
    aligned line is a two-dimensional line that is defined by an axis and 
    length on that axis, rather than two points. When working with two lines 
    defined as such that have the same axis, many calculations are 
    simplified. 

    .. note::

        Though it requires the same amount of memory as a simple representation of
        a 2 dimensional line (4 numerics), it cannot describe all types of lines.
        All lines that can be defined this way intersect (0, 0).
    
    .. note::
    
        `min` and `max` are referring to nearness to negative and positive infinity,
        respectively. The absolute value of `min` may be larger than that of `max`.

    .. note::

        AxisAlignedLines are an intermediary operation, so offsets should be baked 
        into them.
    
    :ivar axis: the axis this line is on
    :vartype axis: :class:`pygorithm.geometry.vector2.Vector2`
    :ivar min: the point closest to negative infinity
    :vartype min: :class:`numbers.Number`
    :ivar max: the point closest to positive infinity
    :vartype max: :class:`numbers.Number`
    """
    
    def __init__(self, axis, point1, point2):
        """
        Construct an axis aligned line with the appropriate min and max.
        
        :param axis: axis this line is on (for bookkeeping only, may be None)
        :type axis: :class:`pygorithm.geometry.vector2.Vector2`
        :param point1: one point on this line
        :type point1: :class:`numbers.Number`
        :param point2: a different point on this line
        :type point2: :class:`numbers.Number`
        """
    
        self.axis = axis
        self.min = min(point1, point2)
        self.max = max(point1, point2)
    
    @staticmethod
    def intersects(line1, line2):
        """
        Determine if the two lines intersect
        
        Determine if the two lines are touching, if they are overlapping, or if 
        they are disjoint. Lines are touching if they share only one end point, 
        whereas they are overlapping if they share infinitely many points. 
        
        .. note::
        
            It is rarely faster to check intersection before finding intersection if
            you will need the minimum translation vector, since they do mostly 
            the same operations.
        
        .. tip::
        
            This will never return ``True, True``
        
        :param line1: the first line
        :type line1: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :param line2: the second line
        :type line2: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :returns: (touching, overlapping)
        :rtype: (bool, bool)
        """
        
        if math.isclose(line1.max, line2.min):
            return True, False
        elif math.isclose(line1.min, line2.max):
            return True, False
        elif line1.max < line2.min:
            return False, False
        elif line1.min > line2.max:
            return False, False
        
        return False, True
    
    @staticmethod
    def find_intersection(line1, line2):
        """
        Calculate the MTV between line1 and line2 to move line1
        
        Determine if the two lines are touching and/or overlapping and then 
        returns the minimum translation vector to move line 1 along axis. If the 
        result is negative, it means line 1 should be moved in the opposite 
        direction of the axis by the magnitude of the result. 


        Returns `true, (None, touch_point_numeric, touch_point_numeric)` if the lines are touching
        and not overlapping.
        
        .. note::
        
            Ensure your program correctly handles `true, (None, numeric, numeric)`
        
        
        :param line1: the first line
        :type line1: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :param line2: the second line
        :type line2: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :returns: (touching, (mtv against 1, intersection min, intersection max))
        :rtype: (bool, (:class:`numbers.Number` or None, :class:`numbers.Number`, :class:`numbers.Number`) or None)
        """
        
        if math.isclose(line1.max, line2.min):
            return True, (None, line2.min, line2.min)
        elif math.isclose(line1.min, line2.max):
            return True, (None, line1.min, line1.min)
        elif line1.max < line2.min or line2.max < line1.min:
            return False, None
        else:
            opt_1 = line2.min - line1.max
            opt_2 = line2.max - line1.min
            
            res_min = max(line1.min, line2.min)
            res_max = min(line1.max, line2.max)
            
            if abs(opt_1) < abs(opt_2):
                return True, (opt_1, res_min, res_max)
            else:
                return True, (opt_2, res_min, res_max)
    
    @staticmethod
    def contains_point(line, point):
        """
        Determine if the line contains the specified point.
        
        The point must be defined the same way as min and max.
        
        .. tip::
        
            It is not possible for both returned booleans to be `True`.
        
        :param line: the line
        :type line: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :param point: the point
        :type point: :class:`numbers.Number`
        :returns: (if the point is an edge of the line, if the point is contained by the line)
        :rtype: (bool, bool)
        """
        
        if math.isclose(line.min, point) or math.isclose(line.max, point):
            return True, False
        elif point < line.min or point > line.max:
            return False, False
        else:
            return False, True
            
    def __repr__(self):
        """
        Create an unambiguous representation of this axis aligned
        line.
        
        Example:
        
        .. code-block:: python
        
            from pygorithm.geometry import axisall
            
            aal = axisall.AxisAlignedLine(None, 3, 5)
            
            # prints AxisAlignedLine(axis=None, min=3, max=5)
            print(repr(aal))
        
        :returns: un-ambiguous representation of this line
        :rtype: string
        """
        
        return "AxisAlignedLine(axis={}, min={}, max={})".format(repr(self.axis), self.min, self.max)
    
    def __str__(self):
        """
        Create a human-readable representation of this axis aligned line.
        
        Example:
        
        .. code-block:: python
        
            from pygorithm.geometry import axisall
            
            aal = axisall.AxisAlignedLine(None, 0.7071234, 0.7071234)
            
            # prints axisall(along None from 0.707 to 0.707)
            print(aal)
        
        :returns: human-readable representation of this line
        :rtype: string
        """
        
        pretty_min = round(self.min * 1000) / 1000
        if pretty_min == math.floor(pretty_min):
            pretty_min = math.floor(pretty_min)
            
        pretty_max = round(self.max * 1000) / 1000
        if pretty_max == math.floor(pretty_max):
            pretty_max = math.floor(pretty_max)
        
        return "axisall(along {} from {} to {})".format(str(self.axis), pretty_min, pretty_max)