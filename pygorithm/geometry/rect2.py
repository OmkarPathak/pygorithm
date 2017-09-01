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
        
        Collision detection against a polygon with cause 
        initialization of the polygon representation of a 
        rectangle. This has the noticeable performance 
        characteristics that are seen whenever a polygon 
        is constructed (see :py:class:`.Polygon2`).
        This operation recurrs only if width and height 
        were modified.
    
    :ivar mincorner: the position of this polygon
    :vartype mincorner: :class:`pygorithm.geometry.vector2.Vector2`
    """
    
    def __init__(self, width, height, mincorner = None):
        """
        Create a new rectangle of width and height.
        
        If ``mincorner is None``, the origin is assumed.
        
        :param width: width of this rect
        :type width: :class:`numbers.Number`
        :param height: height of this rect
        :type height: :class:`numbers.Number`
        :param mincorner: the position of this rect
        :type mincorner: :class:`pygorithm.geometry.vector2.Vector2` or None
        
        :raises ValueError: if width or height are not strictly positive
        """
        self.width = width
        self.height = height
        self.mincorner = mincorner if mincorner is not None else vector2.Vector2(0, 0)
        
    @property
    def polygon(self):
        """
        Get the polygon representation of this rectangle, without
        the offset. Lazily initialized and up-to-date with width 
        and height.
        
        .. caution::
        
            This does not include the :py:attr:`.mincorner`
            (which should be passed as offset for polygon operations)
        
        :returns: polygon representation of this rectangle
        :rtype: :class:`pygorithm.geometry.polygon2.Polygon2`
        """
        if self._polygon is None:
            self._polygon = polygon2.Polygon2([ vector2.Vector2(0, 0), 
                                                vector2.Vector2(0, self._height), 
                                                vector2.Vector2(self._width, self._height),
                                                vector2.Vector2(self._width, 0) ])
        
        return self._polygon
        
    @property
    def width(self):
        """
        Get or set the width of this rect. 
        
        .. caution::
        
            Setting the width of the rectangle will remove the polygon
            caching required for rectangle-polygon collision.
        
        :returns: width of this rect
        :rtype: :class:`numbers.Number`
        
        :raises ValueError: if trying to set ``width <= 1e-07``
        """
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 1e-07:
            raise ValueError('width cannot be <= 1e-07 but is {}'.format(value))
        
        self._width = value
        self._polygon = None
        
    @property
    def height(self):
        """
        Get or set the height of this rect
        
        .. caution::
        
            Setting the height of the rectangle will remove the cached 
            operations required for rectangle-polygon collision.
            
        :returns: height of this rect
        :rtype: :class:`numbers.Number`
        
        :raises ValueError: if trying to set ``height <= 1e-07``
        """
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 1e-07:
            raise ValueError("height cannot be <= 1e07 but is {}".format(value))
        
        self._height = value
        self._polygon = None
        
    @property
    def area(self):
        """
        Get the area of this rect
        
        :returns: area of this rect
        :rtype: :class:`numbers.Number`
        """
        return self._width * self._height
    
    @staticmethod
    def project_onto_axis(rect, axis):
        """
        Project the rect onto the specified axis.
        
        .. tip::
        
            This function is extremely fast for vertical or 
            horizontal axises.
        
        :param rect: the rect to project
        :type rect: :class:`pygorithm.geometry.rect2.Rect2`
        :param axis: the axis to project onto (normalized)
        :type axis: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: the projection of the rect along axis
        :rtype: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        """
        
        if axis.x == 0:
            return axisall.AxisAlignedLine(axis, rect.mincorner.y * axis.y, (rect.mincorner.y + rect.height) * axis.y)
        elif axis.y == 0:
            return axisall.AxisAlignedLine(axis, rect.mincorner.x * axis.x, (rect.mincorner.x + rect.width) * axis.x)
        
        p1 = rect.mincorner.dot(axis)
        p2 = vector2.Vector2(rect.mincorner.x + rect.width, rect.mincorner.y).dot(axis)
        p3 = vector2.Vector2(rect.mincorner.x + rect.width, rect.mincorner.y + rect.height).dot(axis)
        p4 = vector2.Vector2(rect.mincorner.x, rect.mincorner.y + rect.height).dot(axis)
        
        _min = min(p1, p2, p3, p4)
        _max = max(p1, p2, p3, p4)
        return axisall.AxisAlignedLine(axis, _min, _max)
        
    @staticmethod
    def contains_point(rect, point):
        """
        Determine if the rect contains the point
        
        Distinguish between points that are on the edge of the
        rect and those that are not.
        
        .. tip::
        
            This will never return ``True, True``
        
        :param rect: the rect
        :type rect: :class:`pygorithm.geometry.rect2.Rect2`
        :param point: the point
        :type point: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: point on edge, point inside
        :rtype: bool, bool
        """
        
        edge_x = math.isclose(rect.mincorner.x, point.x, abs_tol=1e-07) or math.isclose(rect.mincorner.x + rect.width, point.x, abs_tol=1e-07)
        edge_y = math.isclose(rect.mincorner.y, point.y, abs_tol=1e-07) or math.isclose(rect.mincorner.y + rect.height, point.y, abs_tol=1e-07)
        if edge_x and edge_y:
            return True, False
        
        contains = (edge_x or (point.x > rect.mincorner.x and point.x < rect.mincorner.x + rect.width)) and \
                   (edge_y or (point.y > rect.mincorner.y and point.y < rect.mincorner.y + rect.height))
        if not contains:
            return False, False
        elif edge_x or edge_y:
            return True, False
        else:
            return False, True
    
    @classmethod
    def _find_intersection_rects(cls, rect1, rect2, find_mtv = True):
        """
        Find the intersection between two rectangles. 
        
        Not intended for direct use. See 
        :py:meth:`.find_intersection`
        
        :param rect1: first rectangle
        :type rect1: :class:`pygorithm.geometry.rect2.Rect2`
        :param rect2: second rectangle
        :type rect2: :class:`pygorithm.geometry.rect2.Rect2`
        :param find_mtv: False to never find mtv (may allow small performance improvement)
        :type find_mtv: bool
        :returns: (touching, overlapping, (mtv distance, mtv axis))
        :rtype: (bool, bool, (:class:`numbers.Number`, :class:`pygorithm.geometry.vector2.Vector2`) or None)
        """
        
        # caution to make sure isclose checks are before greater than/less than checks!
        
        # you could save which edge here if you needed that information
        x_touching = math.isclose(rect1.mincorner.x + rect1.width, rect2.mincorner.x, abs_tol=1e-07)
        x_touching = x_touching or math.isclose(rect1.mincorner.x, rect2.mincorner.x + rect2.width, abs_tol=1e-07)
        y_touching = math.isclose(rect1.mincorner.y, rect2.mincorner.y + rect2.height, abs_tol=1e-07)
        y_touching = y_touching or math.isclose(rect1.mincorner.y + rect1.height, rect2.mincorner.y, abs_tol=1e-07)
        
        if x_touching and y_touching:
            return True, False, None # sharing 1 corner
        
        
        # we don't need to calculate if the touching is True
        x_overlap = False if x_touching else (rect1.mincorner.x < rect2.mincorner.x and rect1.mincorner.x + rect1.width > rect2.mincorner.x) or \
                                             (rect2.mincorner.x < rect1.mincorner.x and rect2.mincorner.x + rect2.width > rect1.mincorner.x)
        y_overlap = False if y_touching else (rect1.mincorner.y < rect2.mincorner.y and rect1.mincorner.y + rect1.height > rect2.mincorner.y) or \
                                             (rect2.mincorner.y < rect1.mincorner.y and rect2.mincorner.y + rect2.height > rect1.mincorner.y)
        if x_touching:
            if y_overlap:
                return True, False, None # sharing an x edge
            else:
                return False, False, None
        elif y_touching:
            if x_overlap:
                return True, False, None # sharing a y edge
            else:
                return False, False, None
        elif not x_overlap or not y_overlap:
            return False, False, None
        
        # They overlap
        if not find_mtv:
            return False, True, None
        
        # four options:
        #   move rect1 min x to rect2 max x
        #   move rect1 max x to rect2 min x 
        #   move rect1 min y to rect2 max y 
        #   move rect1 max y to rect2 min y 
        # 
        # we will look at all 4 of these and choose
        # the one that requires the least movement
        opt1 = rect2.mincorner.x + rect2.width - rect1.mincorner.x
        opt2 = rect2.mincorner.x - rect1.mincorner.x - rect1.width
        opt3 = rect2.mincorner.y + rect2.height - rect1.mincorner.y
        opt4 = rect2.mincorner.y - rect1.mincorner.y - rect1.height
        
        abs1 = abs(opt1)
        abs2 = abs(opt2)
        abs3 = abs(opt3)
        abs4 = abs(opt4)
        # the following could be simplified by making an array, at a
        # minor performance hit
        if abs1 < abs2:
            if abs1 < abs3:
                if abs1 < abs4:
                    return False, True, (opt1, vector2.Vector2(1, 0))
                else:
                    return False, True, (opt4, vector2.Vector2(0, 1))
            else:
                if abs3 < abs4:
                    return False, True, (opt3, vector2.Vector2(0, 1))
                else:
                    return False, True, (opt4, vector2.Vector2(0, 1))
        else:
            if abs2 < abs3:
                if abs2 < abs4:
                    return False, True, (opt2, vector2.Vector2(1, 0))
                else:
                    return False, True, (opt4, vector2.Vector2(0, 1))
            else:
                if abs3 < abs4:
                    return False, True, (opt3, vector2.Vector2(0, 1))
                else:
                    return False, True, (opt4, vector2.Vector2(0, 1))
                
            
        
        
        
        
    
    @classmethod
    def _find_intersection_rect_poly(cls, rect, poly, offset, find_mtv = True):
        """
        Find the intersection between a rect and polygon.
        
        Not intended for direct use. See 
        :py:meth:`.find_intersection`
        
        :param rect: rectangle
        :type rect: :class:`pygorithm.geometry.rect2.Rect2`
        :param poly: polygon
        :type poly: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param offset: offset for the polygon
        :type offset: :class:`pygorithm.geometry.vector2.Vector2`
        :param find_mtv: False to never find mtv (may allow small performance improvement)
        :type find_mtv: bool
        :returns: (touching, overlapping, (mtv distance, mtv axis))
        :rtype: (bool, bool, (:class:`numbers.Number`, :class:`pygorithm.geometry.vector2.Vector2`) or None)
        """
        return polygon2.Polygon2.find_intersection(rect.polygon, poly, rect.mincorner, offset, find_mtv)
        
    @classmethod
    def _find_intersection_poly_rect(cls, poly, offset, rect, find_mtv = True):
        """
        Find the intersection between a polygon and rect.
        
        Not intended for direct use. See 
        :py:meth:`.find_intersection`
        
        :param poly: polygon
        :type poly: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param offset: offset for the polygon
        :type offset: :class:`pygorithm.geometry.vector2.Vector2`
        :param rect: rectangle
        :type rect: :class:`pygorithm.geometry.rect2.Rect2`
        :param find_mtv: False to never find mtv (may allow small performance improvement)
        :type find_mtv: bool
        :returns: (touching, overlapping, (mtv distance, mtv axis))
        :rtype: (bool, bool, (:class:`numbers.Number`, :class:`pygorithm.geometry.vector2.Vector2`) or None)
        """
        return polygon2.Polygon2.find_intersection(poly, rect.polygon, offset, rect.mincorner, find_mtv)
        
    @classmethod
    def find_intersection(cls, *args, **kwargs):
        """
        Determine the state of intersection between a rect and a 
        polygon.
        
        For Rect-Polygon intersection:
        
        Must be passed in 3 arguments - a :py:class:`.Rect2`,
        a :py:class:`.Polygon2`, and a 
        :py:class:`.Vector2`. The vector must come immediately
        after the polygon, but the rect can be either the first or last unnamed argument. 
        If it is the first argument, the mtv is against the rectangle. If it is the last 
        argument, the mtv is against the polygon.
        
        For Rect-Rect intersection:
        
        Must be passed in 2 arguments (both rects).
        
        
        .. note::
       
            The first argument is checked with ``isinstance(arg, Rect2)``. If this is 
            False, the first argument is assumed to be a Polygon2. If you want to 
            use a compatible rectangle class for which this check would fail, you 
            can call 
            :py:meth:`._find_intersection_rect_poly`
            directly or pass the polygon first and invert the resulting mtv (if 
            one is found). If two unnamed arguments are provided, they are assumed 
            to be both rects without further checks. 

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
        find_mtv = kwargs.get("find_mtv", True)
        
        if len(args) == 2:
            return cls._find_intersection_rects(args[0], args[1], find_mtv)
        else:
            assert len(args) == 3, "Incorrect number of unnamed arguments to Rect2.find_intersection (got {} expected 2 or 3)".format(len(args))
            
            if isinstance(args[0], Rect2):
                return cls._find_intersection_rect_poly(args[0], args[1], args[2], find_mtv)
            else:
                return cls._find_intersection_poly_rect(args[0], args[1], args[2], find_mtv)
            
            
        
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
        return "rect2(width={}, height={}, mincorner={})".format(self._width, self._height, repr(self.mincorner))
        
    def __str__(self):
        """
        Create a human readable representation of this rectangle
        
        Example:
        
        .. code-block:: python
        
            from pygorithm.geometry import (vector2, rect2)
            
            unit_square = rect2.Rect2(1, 1, vector2.Vector2(3, 4))
            ugly_rect = rect2.Rect2(0.7071234, 0.7079876, vector2.Vector2(0.56789123, 0.876543))
            
            # prints rect(1x1 at <3, 4>)
            print(str(unit_square))
            
            # prints rect(0.707x0.708 at <0.568, 0.877>)
            print(str(ugly_rect))
        
        :returns: human-readable representation of this rectangle
        :rtype: string
        """
        
        
        pretty_width = round(self._width * 1000) / 1000
        if pretty_width == math.floor(pretty_width):
            pretty_width = math.floor(pretty_width)
            
        pretty_height = round(self._height * 1000) / 1000
        if pretty_height == math.floor(pretty_height):
            pretty_height = math.floor(pretty_height)
        return "rect({}x{} at {})".format(pretty_width, pretty_height, str(self.mincorner))