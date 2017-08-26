"""
axisall

Author: Timothy Moore

Defines a class for handling axis-aligned two-dimensional lines 
segments. This class simplifies intermediary calculations in
SAT and similiar algorithms.

These are 2dimensional axis-aligned objects
https://en.wikipedia.org/wiki/Axis-aligned_object
"""

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
        
        :param axis: axis this line is on
        :type axis: :class:`pygorithm.geometry.vector2.Vector2`
        :param point1: one point on this line
        :type point1: :class:`numbers.Number`
        :param point2: a different point on this line
        :type point2: :class:`numbers.Number`
        """
    
        pass
    
    @staticmethod
    def intersects(line1, line2):
        """
        Determine if the two lines intersect
        
        Determine if the two lines are touching and if they are, if 
        they are overlapping. Lines are touching if they share only
        one end point, whereas they are overlapping if they share 
        infinitely many points.
        
        .. note::
        
            It is rarely faster to check intersection before finding intersection if
            you will need the minimum translation vector, since they do mostly 
            the same operations.
        
        :param line1: the first line
        :type line1: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :param line2: the second line
        :type line2: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :returns: (touching, overlapping)
        :rtype: (bool, bool)
        """
        
        pass
    
    @staticmethod
    def find_intersection(line1, line2):
        """
        Calculate the MTV between line1 and line2 to move line1
        
        Determine if the two lines are touching and/or overlapping and then 
        returns the minimum translation vector to move line 1 along axis. If the 
        result is negative, it means line 1 should be moved in the opposite 
        direction of the axis by the magnitude of the result. 


        Returns `true, None` if the lines are touching.
        
        .. note::
        
            Ensure your program correctly handles `true, None`
        
        
        :param line1: the first line
        :type line1: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :param line2: the second line
        :type line2: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        :returns: (touching, mtv against 1)
        :rtype: (bool, :class:`numbers.Number` or None)
        """
        
        pass
    
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
        pass