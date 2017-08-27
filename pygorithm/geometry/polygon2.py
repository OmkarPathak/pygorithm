"""
polygon2

Author: Timothy Moore

Defines a class for simple 2-d convex polygons. Contains
SAT-intersection.
"""

class Polygon2(object):
    """
    Define a concave polygon defined by a list of points such that each
    adjacent pair of points form a line, the line from the last point to
    the first point form a line, and the lines formed from the smaller 
    index to the larger index will walk clockwise around the polygon.
    
    .. note:: 

        Polygons should be used as if they were completely immutable to
        ensure correctness. All attributes of Polygon2 can be reconstructed
        from the points array, and thus cannot be changed on their own and
        must be recalculated if there were any changes to `points`.

    .. note::
        
        To reduce unnecessary recalculations, Polygons notably do not have 
        an easily modifiable position. However, where relevant, the class 
        methods will accept offsets to the polygons. In all of these cases
        the offset may be None for a minor performance improvement.

    .. note::

        Unfortunately, operations on rotated polygons require recalculating
        the polygon based on its rotated points. This should be avoided 
        unless necessary through the use of Axis-Aligned Bounding Boxes
        and similar tools.

    .. caution::
        
        The normals in the :py:attr:`~pygorithm.geometry.polygon2.Polygon2.normals`
        are not necessarily the same length as 
        :py:attr:`~pygorithm.geometry.polygon2.Polygon2.points` or 
        :py:attr:`~pygorithm.geometry.polygon2.Polygon2.lines`. It is only 
        guarranteed to have no two vectors that are the same or opposite 
        directions, and contain either the vector in the same direction or opposite
        direction of the normal vector for every line in the polygon.
    
    :ivar points: the ordered list of points on this polygon
    :vartype points: list of :class:`pygorithm.geometry.vector2.Vector2`
    
    :ivar lines: the ordered list of lines on this polygon
    :vartype lines: list of :class:`pygorithm.geometry.line2.Line2`
    
    :ivar normals: the unordered list of unique normals on this polygon
    :vartype normals: list of :class:`pygorithm.geometry.vector2.Vector2`
    
    :ivar center: the center of this polygon when unshifted.
    :vartype center: :class:`pygorithm.geometry.vector2.Vector2`
    """
    
    def __init__(self, points, suppress_errors = False):
        """
        Create a new polygon from the set of points
        
        .. caution:: 
        
            A significant amount of calculation is performed when creating
            a polygon. These should be reused whenever possible. This cost
            can be alleviated somewhat by suppressing certain expensive
            sanity checks, but the polygon can behave very unexpectedly
            (and potentially without explicit errors) if the errors are 
            suppressed.
        
        :param points: the ordered set of points on this polygon
        :type points: list of :class:`pygorithm.geometry.vector2.Vector2` or \
        list of (:class:`numbers.Number`, :class:`numbers.Number`)
        
        :param suppress_errors: True to not do somewhat expensive sanity checks
        :type suppress_errors: bool
        
        :raises ValueError: if there are any repeated points (not suppressable)
        :raises ValueError: if there are less than 3 points (not suppressable)
        :raises ValueError: if the polygon is not convex (suppressable)
        :raises ValueError: if the points are not clockwise oriented (suppressable)
        """
        pass
    
    @classmethod
    def from_regular(cls, sides, length, start_rads = None, start_degs = None, center = None):
        """
        Create a new regular polygon.
        
        .. hint::
        
            If no rotation is specified there is always a point at ``(length, 0)``
        
        If no center is specified, the center will be ``(length / 2, length / 2)``
        which makes the top-left bounding box of the polygon the origin. 
        
        May specify the angle of the first point. For example, if the coordinate
        system is x to the right and y upward, then if the starting offset is 0
        then the first point will be at the right and the next point counter-clockwise.
        
        This would make for the regular quad (sides=4) to look like a diamond. To make
        the bottom side a square, the whole polygon needs to be rotated 45 degrees, like
        so:
        
        .. code-block:: python
        
            from pygorithm.geometry import (vector2, polygon2)
            import math
            
            # This is a diamond shape (rotated square) (0 degree rotation assumed)
            diamond = polygon2.Polygon2.from_regular(4, 1)
            
            # This is a flat square
            square = polygon2.Polygon2.from_regular(4, 1, start_degs = 45)
            
            # Creating a flat square with radians 
            square2 = polygon2.Polygon2.from_regular(4, 1, math.pi / 4)
        
        :param sides: the number of sides in the polygon
        :type sides: :class:`numbers.Number`
        :param length: the length of each sides
        :type length: :class:`numbers.Number`
        :param start_rads: the starting radians or None 
        :type start_rads: :class:`numbers.Number` or None
        :param start_degs: the starting degrees or None 
        :type start_degs: :class:`numbers.Number` or None
        :param center: the center of the polygon
        :type center: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: the new regular polygon
        :rtype: :class:`pygorithm.geometry.polygon2.Polygon2`
        
        :raises ValueError: if ``sides < 3`` or ``length <= 0``
        :raises ValueError: if ``start_rads is not None and start_degs is not None``
        """
        pass
        
    @classmethod
    def from_rotated(cls, original, rotation, rotation_degrees = None):
        """
        Create a regular polygon that is a rotation of
        a different polygon.
        
        The rotation must be in radians, or null and rotation_degrees
        must be specified. Positive rotations are clockwise.
        
        Examples:
        
        .. code-block:: python
        
            from pygorithm.goemetry import (vector2, polygon2)
            import math
            
            poly = polygon2.Polygon2.from_regular(4, 1)
            
            # the following are equivalent (within rounding)
            rotated1 = polygon2.Polygon2.from_rotated(poly, math.pi / 4)
            rotated2 = polygon2.Polygon2.from_rotated(poly, None, 45)
        
        :param original: the polygon to rotate
        :type original: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param rotation: the rotation in radians or None
        :type rotation: :class:`numbers.Number`
        :param rotation_degrees: the rotation in degrees or None
        :type rotation_degrees: :class:`numbers.Number`
        :returns: the rotated polygon
        :rtype: :class:`pygorithm.geometry.polygon2.Polygon2`
        
        :raises ValueError: if ``rotation is not None and rotation_degrees is not None``
        :raises ValueError: if ``rotation is None and rotation_degrees is None``
        """
        pass
    
    @property
    def area(self):
        """
        Get the area of this polygon. Lazily initialized.
        
        :returns: area of this polygon
        :rtype: :class:`numbers.Number`
        """
        pass
        
        
    @staticmethod 
    def project_onto_axis(polygon, offset, axis):
        """
        Find the projection of the polygon along the axis.
        
        :param polygon: the polygon to project
        :type polygon: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param offset: the offset of the polygon
        :type offset: :class:`pygorithm.geometry.vector2.Vector2`
        :param axis: the axis to project onto
        :type axis: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: the projection of the polygon along the axis
        :rtype: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        """
        pass
    
    @staticmethod
    def contains_point(polygon, offset, point):
        """
        Determine if the polygon at offset contains point.
        
        Distinguish between points that are on the edge of the polygon and 
        points that are completely contained by the polygon.
        
        .. tip::
        
            This can never return True, True
        
        :param polygon: the polygon 
        :type polygon: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param offset: the offset of the polygon
        :type offset: :class:`pygorithm.geometry.vector2.Vector2` or None
        :param point: the point to check
        :type point: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: (on edge, contained)
        :rtype: (bool, bool)
        """
        pass
        
    @staticmethod
    def find_intersection(poly1, poly2, offset1, offset2, find_mtv = True):
        """
        Find if the polygons are intersecting and how to resolve it.
        
        Distinguish between polygons that are sharing 1 point or a single line 
        (touching) as opposed to polygons that are sharing a 2-dimensional 
        amount of space.
        
        The resulting MTV should be applied to the first polygon (or its offset), 
        or its negation can be applied to the second polyogn (or its offset).
        
        The MTV will be non-null if overlapping is True and find_mtv is True.
        
        .. note::
        
            There is only a minor performance improvement from setting find_mtv to 
            False. It is rarely an improvement to first check without finding 
            mtv and then to find the mtv.
        
        
        :param poly1: the first polygon
        :type poly1: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param poly2: the second polygon
        :type poly2: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param offset1: the offset of the first polygon
        :type offset1: :class:`pygorithm.geometry.vector2.Vector2` or None
        :param offset2: the offset of the second polygon
        :type offset2: :class:`pygorithm.geometry.vector2.Vector2` or None
        :param find_mtv: if False, the mtv is always None and there is a small \
        performance improvement
        :type find_mtv: bool
        :returns: (touching, overlapping, (mtv distance, mtv axis))
        :rtype: (bool, bool, (:class:`numbers.Number`, :class:`pygorithm.geometry.vector2.Vector2`) or None)
        """
        pass