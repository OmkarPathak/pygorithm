"""
Author: Timothy Moore
Created On: 31th August 2017

Defines a 2-dimensional axis-aligned rectangle.
This rectangle does not act as a polygon, but 
there are similar collision methods that accept
polygons.

Unlike Polygon2s, Rect2s are very fast to construct.
"""

import math

from pygorithm.geometry import (vector2, line2, axisall, polygon2)

class Rect2(object):
    """
    A rectangle. Uses SAT collision against polygons and 
    broad-phase collision against other rectangles.
    
    Rectangles are fast to construct and have very fast 
    rectangle-rectangle collision detection.
    
    Rect2 is designed to have almost exactly the opposite performance 
    characteristics as Polygon2 when doing collision against 
    Polygon2s: Fast to construct and complex on first call with 
    many operations incurring expensive recalculations.
    
    .. caution::
    
        Collision detection against a rectangle with cause 
        initialization of the polygon representation of a 
        rectangle. This has the noticeable performance 
        characteristics that are seen whenever a polygon 
        is constructed (see :py:class:~`pygorithm.geometry.polygon2.Polygon2`).
        This operation recurrs only if width and height 
        were modified.
    
    :ivar mincorner: the position of this polygon
    :vartype mincorner: :class:`pygorithm.geometry.vector2.Vector2`
    """
    
    def __init__(self, width, height, mincorner = None):
        """
        Create a new rectangle of width and height.
        
        If mincorner is None, the origin is assumed.
        
        :param width: width of this rect
        :type width: :class:`numbers.Number`
        :param height: height of this rect
        :type height: :class:`numbers.Number`
        :param mincorner: the position of this rect
        :type mincorner: :class:`pygorithm.geometry.vector2.Vector2` or None
        
        :raises ValueError: if width or height are not strictly positive
        """
        pass
        
    @property
    def polygon(self):
        """
        Get the polygon representation of this rectangle, without
        the corners. Lazily initialized and up-to-date with width 
        and height.
        
        .. caution::
        
            This does not include the mincorner (which should be passed as
            offset)
        
        :returns: polygon representation of this rectangle
        :rtype: :class:`pygorithm.geometry.polygon2.Polygon2`
        """
        pass
        
    @property
    def width(self):
        """
        Get or set the width of this rect. 
        
        .. caution::
        
            Setting the width of the rectangle will remove the polygon
            caching required for rectangle-polygon collision.
        
        :returns: width of this rect
        :rtype: :class:`numbers.Number`
        
        :raises ValueError: if trying to set width <= 0
        """
        pass
    
    @width.setter
    def width(self, value):
        pass
        
    @property
    def height(self):
        """
        Get or set the height of this rect
        
        .. caution::
        
            Setting the height of the rectangle will remove the cached 
            operations required for rectangle-polygon collision.
            
        :returns: height of this rect
        :rtype: :class:`numbers.Number`
        
        :raises ValueError: if trying to set height <= 0
        """
        pass
    
    @height.setter
    def height(self, value):
        pass
        
    @property
    def area(self):
        """
        Get the area of this rect
        
        :returns: area of this rect
        :rtype: :class:`numbers.Number`
        """
        pass
    
    @staticmethod
    def project_onto_axis(rect, axis):
        """
        Project the rect onto the specified axis.
        
        .. tip::
        
            This function is extremely fast for vertical or 
            horizontal axises.
        
        :param rect: the rect to project
        :type rect: :class:`pygorithm.geometry.rect2.Rect2`
        :param axis: the axis to project onto
        :type axis: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: the projection of the rect along axis
        :rtype: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        """
        pass
        
    @staticmethod
    def contains_point(rect, point):
        """
        Determine if the rect contains the point
        
        Distinguish between points that are on the edge of the
        rect and those that are not.
        
        .. tip::
        
            This will never return True, True
        
        :param rect: the rect
        :type rect: :class:`pygorithm.geometry.rect2.Rect2`
        :param point: the point
        :type point: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: point on edge, point inside
        :rtype: bool, bool
        """
        pass
    
    @staticmethod
    def find_intersection(find_mtv=True, *args):
        """
        Determine the state of intersection between a rect and a 
        polygon.
        
        For Rect-Polygon intersection:
        
        Must be passed in 3 arguments - a :py:class:~`pygorithm.geometry.rect2.Rect2`,
        a :py:class:~`pygorithm.geometry.polygon2.Polygon2`, and a 
        :py:class:~`pygorithm.geometry.vector2.Vector2`. The vector must come immediately
        after the polygon, but the rect can be either the first or last unnamed argument. 
        If it is the first argument, the mtv is against the rectangle. If it is the last 
        argument, the mtv is against the polygon.
        
        
        For Rect-Rect intersection:
        
        Must be passed in 2 ar
        Examples:
        
        .. code-block:: python
        
            from pygorithm.geometry import (vector2, polygon2, rect2)
            
            octogon = polygon2.Polygon2.from_regular(8, 1)
            oct_offset = vector2.Vector2(0.5, 0)
            
            unit_square = rect2.Rect2(1, 1)
            
            # find mtv for square against octogon
            touching, overlapping, mtv = rect2.Rect2.find_intersection(unit_square, octogon, oct_offset)
            
            # find mtv for octogon against square
            touching, overlapping, mtv = rect2.Rect2.find_intersection(octogon, oct_offset, unit_square)
            
            # find intersection but skip mtv (two options)
            touching, overlapping, alwaysNone = rect2.Rect2.find_intersection(unit_square, octogon, oct_offset, find_mtv=False)
            touching, overlapping, alwaysNone = rect2.Rect2.find_intersection(octogon, oct_offset, unit_square, find_mtv=False)
            
            big_square = rect2.Rect2(2, 2, vector2.Vector2(-1.5, 0))
            
            # find mtv for square against big square
            touching, overlapping, mtv = rect2.Rect2.find_intersection(unit_square, big_square)
            
            # find mtv for big square against square 
            touching, overlapping, mtv = rect2.Rect2.find_intersection(big_square, unit_square)
        
        :param find_mtv: if mtv should be found where possible (default ``True``)
        :type find_mtv: bool
        :param args: 2 arguments for rect-rect, 3 arguments for rect-polygon (see above)
        :type args: list
        :returns: (touching, overlapping, (mtv distance, mtv axis))
        :rtype: (bool, bool, (:class:`numbers.Number`, :class:`pygorithm.geometry.vector2.Vector2`) or None)
        """
        pass
        
    def __repr__(self):
        """
        Create an unambiguous representation of this rectangle.
        
        Example:
        
        .. code-block:: python
        
            from pygorithm.geometry import (vector2, rect2)
            
            unit_square = rect2.Rect2(1, 1, vector2.Vector2(3, 4))
            
            # prints rect2(width=1, height=1, mincorner=vector2(x=3, y=4))
            print(repr(unit_square))
        
        :returns: unambiguous representation of this rectangle
        :rtype: string
        """
        pass
        
    def __str__(self):
        """
        Create a human readable representation of this rectangle
        
        Example:
        
        .. code-block:: python
        
            from pygorithm.geometry import (vector2, rect2)
            
            unit_square = rect2.Rect2(1, 1, vector2.Vector2(3, 4))
            ugly_Rect = rect2.Rect2(0.7071234, 0.7079876, vector2.Vector2(0.56789123, 0.876543))
            
            # prints rect(1x1 at <3, 4>)
            print(str(unit_square))
            
            # prints rect(0.707x0.708 at <0.568, 0.877>)
        """
        pass