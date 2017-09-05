"""
polygon2

Author: Timothy Moore

Defines a class for simple 2-d convex polygons. Contains
SAT-intersection.
"""

import math

from pygorithm.geometry import (vector2, axisall, line2)

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
        
        The length of :py:attr:`~pygorithm.geometry.polygon2.Polygon2.normals`
        is not necessarily the same as 
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
        
        The center of the polygon is calculated as the average of the points.
        
        The lines of the polygon are constructed using line2. 
        
        The normals of the lines are calculated using line2.
        
        A simple linear search is done to check for repeated points.
        
        The area is calculated to check for clockwise order using the
        `Shoelace Formula <https://en.wikipedia.org/wiki/Shoelace_formula>`
        
        The polygon is proven to be convex by ensuring the cross product of 
        the line from the point to previous point and point to next point is
        positive or 0, for all points.
        
        :param points: the ordered set of points on this polygon
        :type points: list of :class:`pygorithm.geometry.vector2.Vector2` or \
        list of (:class:`numbers.Number`, :class:`numbers.Number`)
        
        :param suppress_errors: True to not do somewhat expensive sanity checks
        :type suppress_errors: bool
        
        :raises ValueError: if there are less than 3 points (not suppressable)
        :raises ValueError: if there are any repeated points (suppressable)
        :raises ValueError: if the points are not clockwise oriented (suppressable)
        :raises ValueError: if the polygon is not convex (suppressable)
        """
        if len(points) < 3:
            raise ValueError("Not enough points (need at least 3 to define a polygon, got {}".format(len(points)))
        
        self.points = []
        self.lines = []
        self.normals = []
        _sum = vector2.Vector2(0, 0)
        
        for pt in points:
            act_pt = pt if type(pt) == vector2.Vector2 else vector2.Vector2(pt)
            
            if not suppress_errors:
                for prev_pt in self.points:
                    if math.isclose(prev_pt.x, act_pt.x) and math.isclose(prev_pt.y, act_pt.y):
                        raise ValueError('Repeated points! points={} (repeated={})'.format(points, act_pt))
            
            
            _sum += act_pt
            self.points.append(act_pt)
        self.center = _sum * (1 / len(self.points))
        
        _previous = self.points[0]
        for i in range(1, len(self.points) + 1):
            pt = self.points[i % len(self.points)]
            _line = line2.Line2(_previous, pt)
            self.lines.append(_line)
            norm = vector2.Vector2(_line.normal)
            if norm.x < 0 or (norm.x == 0 and norm.y == -1):
                norm.x *= -1
                norm.y *= -1
            
            already_contains = next((v for v in self.normals if math.isclose(v.x, norm.x) and math.isclose(v.y, norm.y)), None)
            if already_contains is None:
                self.normals.append(norm)
            
            _previous = pt
        
        
        self._area = None
        
        if not suppress_errors:
            # this will check counter-clockwisedness
            a = self.area 
            
            # if the polygon is convex and clockwise, if you look at any point
            # and take the cross product with the line from the point to the 
            # previous point and the line from the point to the next point 
            # the result will be positive
            for leftpointin in range(len(self.points)):
                middlepointin = (leftpointin + 1) % len(self.points)
                rightpointin = (middlepointin + 1) % len(self.points)
                
                leftpoint = self.points[leftpointin]
                middlepoint = self.points[middlepointin]
                rightpoint = self.points[rightpointin]
                
                vec1 = middlepoint - leftpoint
                vec2 = middlepoint - rightpoint
                cross_product = vec1.cross(vec2)
                if cross_product < -1e-09:
                    raise ValueError('Detected concavity at index {} - {} cross {} = {}\nself={}'.format(middlepointin, vec1, vec2, cross_product, str(self)))
            
    @classmethod
    def from_regular(cls, sides, length, start_rads = None, start_degs = None, center = None):
        """
        Create a new regular polygon.
        
        .. hint::
        
            If no rotation is specified there is always a point at ``(length, 0)``
        
        If no center is specified, the center will be calculated such that
        all the vertexes positive and the bounding box includes (0, 0). This
        operation requires O(n) time (where n is the number if sides)
        
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
        
        Uses the `definition of a regular polygon <https://en.wikipedia.org/wiki/Regular_polygon>`
        to find the angle between each vertex in the polygon. Then converts the side
        length to circumradius using the formula explained `here <http://mathworld.wolfram.com/RegularPolygon.html>`
        
        Finally, each vertex is found using ``<radius * cos(angle), radius * sin(angle)>``
        
        If the center is not specified, the minimum of the bounding box of the 
        polygon is calculated while the vertices are being found, and the inverse
        of that value is offset to the rest of the points in the polygon. 
        
        :param sides: the number of sides in the polygon
        :type sides: :class:`numbers.Number`
        :param length: the length of any side of the polygon
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
        
        if (start_rads is not None) and (start_degs is not None):
            raise ValueError('One or neithter of start_rads and start_degs may be defined, but not both. (got start_rads={}, start_degs={})'.format(start_rads, start_degs))
        
        if sides < 3 or length <= 0:
            raise ValueError('Too few sides or too non-positive length (sides={}, length={})'.format(sides, length))
        
        if start_degs is not None:
            start_rads = (start_degs * math.pi) / 180
            
        if start_rads is None:
            start_rads = 0
        
        _recenter = False
        radius = length / (2 * math.sin( math.pi / sides ))
        if center is None:
            _recenter = True
            center = vector2.Vector2(0, 0)
            
            
        angle = start_rads
        increment = -(math.pi * 2) / sides
        
        pts = []
        _minx = 0
        _miny = 0
        for i in range(sides):
            x = center.x + math.cos(angle) * radius
            y = center.y + math.sin(angle) * radius
            pts.append(vector2.Vector2(x, y))
            angle += increment
            
            if _recenter:
                _minx = min(_minx, x)
                _miny = min(_miny, y)
        
        if _recenter:
            _offset = vector2.Vector2(-_minx, -_miny)
            for i in range(sides):
                pts[i] += _offset
        
        return cls(pts, suppress_errors = True)
        
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
        
        Uses the `2-d rotation matrix <https://en.wikipedia.org/wiki/Rotation_matrix>`
        to rotate each point.
        
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
        if (rotation is None) == (rotation_degrees is None):
            raise ValueError("rotation must be specified exactly once (rotation={}, rotation_degrees={})".format(rotation, rotation_degrees))
            
        if rotation_degrees is not None:
            rotation = rotation_degrees * math.pi / 180
        
        new_pts = []
        for pt in original.points:
            shifted = pt - original.center
            new_pts.append(vector2.Vector2(original.center.x + shifted.x * math.cos(rotation) - shifted.y * math.sin(rotation), 
                                           original.center.y + shifted.y * math.cos(rotation) + shifted.x * math.sin(rotation)))
        
        result = cls(new_pts, suppress_errors = True)
        result._area = original._area
        return result
    
    @property
    def area(self):
        """
        Get the area of this polygon. Lazily initialized.
        
        Uses the `Shoelace Formula <https://en.wikipedia.org/wiki/Shoelace_formula>` to
        calculate the signed area, allowing this to also test for correct polygon 
        orientation.
        
        :returns: area of this polygon
        :rtype: :class:`numbers.Number`
        
        :raises ValueError: if the polygon is not in clockwise order
        """
        
        if self._area is None:
            _edgesum = 0
            _previous = self.points[0]
            for i in range(1, len(self.points) + 1):
                pt = self.points[i % len(self.points)]
                _edgesum += (pt.x - _previous.x) * (pt.y + _previous.y)
                _previous = pt
                
            if _edgesum < 0:
                raise ValueError("Points are counter-clockwise oriented (signed square area: {})".format(_edgesum))
            
            self._area = _edgesum / 2
        
        return self._area
        
        
    @staticmethod 
    def project_onto_axis(polygon, offset, axis):
        """
        Find the projection of the polygon along the axis.
        
        Uses the `dot product <https://en.wikipedia.org/wiki/Dot_product>`
        of each point on the polygon to project those points onto the axis,
        and then finds the extremes of the projection.
        
        :param polygon: the polygon to project
        :type polygon: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param offset: the offset of the polygon
        :type offset: :class:`pygorithm.geometry.vector2.Vector2`
        :param axis: the axis to project onto
        :type axis: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: the projection of the polygon along the axis
        :rtype: :class:`pygorithm.geometry.axisall.AxisAlignedLine`
        """
        
        dot_min = None
        dot_max = None
        for pt in polygon.points:
            dot = (pt + offset).dot(axis)
            
            dot_min = min(dot, dot_min) if dot_min is not None else dot
            dot_max = max(dot, dot_max) if dot_max is not None else dot
        
        return axisall.AxisAlignedLine(axis, dot_min, dot_max)
    
    @staticmethod
    def contains_point(polygon, offset, point):
        """
        Determine if the polygon at offset contains point.
        
        Distinguish between points that are on the edge of the polygon and 
        points that are completely contained by the polygon.
        
        .. tip::
        
            This can never return True, True
        
        This finds the cross product of this point and the two points comprising
        every line on this polygon. If any are 0, this is an edge. Otherwise,
        they must all be negative (when traversed clockwise).
        
        :param polygon: the polygon 
        :type polygon: :class:`pygorithm.geometry.polygon2.Polygon2`
        :param offset: the offset of the polygon
        :type offset: :class:`pygorithm.geometry.vector2.Vector2` or None
        :param point: the point to check
        :type point: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: on edge, contained
        :rtype: bool, bool
        """
        
        _previous = polygon.points[0]
        for i in range(1, len(polygon.points) + 1):
            curr = polygon.points[i % len(polygon.points)]
            
            vec1 = _previous + offset - point
            vec2 = curr + offset - point
            cross = vec1.cross(vec2)
            _previous = curr
            
            if math.isclose(cross, 0, abs_tol=1e-07):
                return True, False
            
            if cross > 0:
                return False, False
        
        return False, True
        
        
    @staticmethod
    def find_intersection(poly1, poly2, offset1, offset2, find_mtv = True):
        """
        Find if the polygons are intersecting and how to resolve it.
        
        Distinguish between polygons that are sharing 1 point or a single line 
        (touching) as opposed to polygons that are sharing a 2-dimensional 
        amount of space.
        
        The resulting MTV should be applied to the first polygon (or its offset), 
        or its negation can be applied to the second polygon (or its offset).
        
        The MTV will be non-null if overlapping is True and find_mtv is True.
        
        .. note::
        
            There is only a minor performance improvement from setting find_mtv to 
            False. It is rarely an improvement to first check without finding 
            mtv and then to find the mtv.
        
        .. caution::
            
            The first value in the mtv could be negative (used to inverse the direction
            of the axis)
        
        This uses the `Seperating Axis Theorem <http://www.dyn4j.org/2010/01/sat/> to 
        calculate intersection.
        
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
        
        unique_normals = list(poly1.normals)
        for n in poly2.normals:
            found = False
            for old_n in poly1.normals:
                if math.isclose(n.x, old_n.x) and math.isclose(n.y, old_n.y):
                    found = True
                    break
            if not found:
                unique_normals.append(n)
        
        
        not_overlapping = False
        best_mtv = None
        for norm in unique_normals:
            proj1 = Polygon2.project_onto_axis(poly1, offset1, norm)
            proj2 = Polygon2.project_onto_axis(poly2, offset2, norm)
            
            touch, mtv = axisall.AxisAlignedLine.find_intersection(proj1, proj2)
            
            if not touch:
                return False, False, None
            
            if mtv[0] is None:
                not_overlapping = True
                best_mtv = None
            elif find_mtv and not not_overlapping:
                if best_mtv is None or abs(mtv[0]) < abs(best_mtv[0]):
                    best_mtv = (mtv[0], norm)
            
        if not_overlapping:
            return True, False, None
        else:
            return False, True, best_mtv
            
    
    @staticmethod
    def _create_link(pts):
        """
        Create a webmath link to display the polygon. 
        
        This isn't a perfect drawing since it doesn't show connections (so order is
        invisible). Avoid programatically connecting to the website. This is mostly
        used because it's very difficult to visualize polygons from lists of points.
        
        :param pts: a set of points (order, number, etc. are irrelevant)
        :type pts: list of :class:`pygorithm.geometry.vector2.Vector2`
        """
        
        param0 = "+".join(('%28{}%2C+{}%29'.format(round(v.x, 3), round(v.y, 3))) for v in pts)
        xmin = pts[0].x
        xmax = xmin
        ymin = pts[1].y
        ymax = ymin
        for v in pts:
            xmin = min(xmin, v.x)
            xmax = max(xmax, v.x)
            ymin = min(ymin, v.y)
            ymax = max(ymax, v.y)
        
        return "www.webmath.com/cgi-bin/grapher.cgi?param0={}&xmin={}&xmax={}&ymin={}&ymax={}&to_plot=points".format(param0, xmin-5, xmax+5, ymin-5, ymax+5)
    
    def __repr__(self):
        """
        Creates an unambiguous representation of this polygon, only
        showing the list of points.
        
        :returns: unambiguous representation of this polygon
        :rtype: string
        """
        
        return "polygon2(points={})".format(self.points)
        
    def __str__(self):
        """
        Creates a human-readable representation of this polygon and 
        includes a link to visualize it
        
        :returns: human-readable representation
        :rtype: string
        """
        
       
        return "polygon2(points={}, view={})".format(', '.join(str(p) for p in self.points), Polygon2._create_link(self.points))
        
        