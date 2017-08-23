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

    :ivar points: the ordered set of points on this polygon
    :vartype points: list of :class:`pygorithm.geometry.vector2.Vector2`
    
    :ivar lines: the ordered set of lines on this polygon
    :vartype lines: list of :class:`pygorithm.geometry.line2.Line2`
    
    :ivar normals: the ordered set of normals on this polygon
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
        :type points: list of :class:`pygorithm.geometry.vector2.Vector2`
        
        :param suppress_errors: True to not do somewhat expensive sanity checks
        :type suppress_errors: bool
        
        :raises ValueError: if there are any repeated points (not suppressable)
        :raises ValueError: if there are less than 3 points (not suppressable)
        :raises ValueError: if the polygon is not convex (suppressable)
        :raises ValueError: if the points are not clockwise oriented (suppressable)
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