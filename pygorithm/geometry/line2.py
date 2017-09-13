"""
line2

Author: Timothy Moore

Defines a simple two-dimensional line segment
"""

import math

from pygorithm.geometry import (vector2, axisall)

class Line2(object):
    """
    Define a two-dimensional directed line segment defined by two points. 
    This class is mostly used as a way to cache information that is 
    regularly required when working on geometrical problems.

    .. caution::

        Lines should be used as if they were completely immutable to ensure 
        correctness. All attributes of Line2 can be reconstructed from the two 
        points, and thus cannot be changed on their own and must be recalculated 
        if there were any changes to `start` or `end`. 

    .. tip::

        To prevent unnecessary recalculations, many functions on lines accept an 
        'offset' argument, which is used to perform calculations on lines that 
        are simply shifts of other lines.
        
    .. note::
        
        The minimum x is guarranteed to be on either (or both) of
        the start and end. However, minimum x and minimum y might not 
        come from the same point. The same is true for the maximum x
        and maximum y.
        
    :ivar start: the start of this line
    :vartype start: :class:`pygorithm.geometry.vector2.Vector2`
    
    :ivar end: the end of this line
    :vartype end: :class:`pygorithm.geometry.vector2.Vector2`
    """
    
    def __init__(self, start, end):
        """
        Create a new line from start to end.
        
        :param start: the start point
        :type start: :class:`pygorithm.geometry.vector2.Vector2`
        :param end: the end point
        :type end: :class:`pygorithm.geometry.vector2.Vector2`
        
        :raises ValueError: if start and end are at the same point
        """
        
        if start.x == end.x and start.y == end.y:
            raise ValueError('start and end are the same point')
        
        self.start = start
        self.end = end
        self._delta = None
        self._axis = None
        self._normal = None
        self._magnitude_squared = None
        self._magnitude = None
        self._min_x = None
        self._min_y = None
        self._max_x = None
        self._max_y = None
        self._slope = None
        self._y_intercept = None
        self._horizontal = None
        self._vertical = None
        
        
    @property
    def delta(self):
        """
        Get the vector from start to end, lazily initialized.
        
        :returns: delta from start to end
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        
        if self._delta is None:
            self._delta = self.end - self.start
        
        return self._delta
        
    @property
    def axis(self):
        """
        Get the normalized delta vector, lazily initialized
        
        :returns: normalized delta
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        
        if self._axis is None:
            self._axis = self.delta * (1 / self.magnitude)
            
        return self._axis
    
    @property
    def normal(self):
        """
        Get normalized normal vector to axis, lazily initialized.

        Get the normalized normal vector such that the normal
        vector is 90 degrees counter-clockwise from the axis.
        
        :returns: normalized normal to axis
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        
        if self._normal is None:
            self._normal = vector2.Vector2(-self.axis.y, self.axis.x)
            
        return self._normal
    
    @property
    def magnitude_squared(self):
        """
        Get the square of the magnitude of delta, lazily initialized.
        
        :returns: square of magnitude of delta
        :rtype: :class:`numbers.Number`
        """
        
        if self._magnitude_squared is None:
            self._magnitude_squared = self.delta.magnitude_squared()
        
        return self._magnitude_squared
        
    @property
    def magnitude(self):
        """
        Get the magnitude of delta, lazily initialized.
        
        .. note::
        
            It is substantially faster to operate on squared magnitude,
            where possible.
        
        :returns: magnitude of delta
        :rtype: :class:`numbers.Number`
        """
        
        if self._magnitude is None:
            self._magnitude = math.sqrt(self.magnitude_squared)
            
        return self._magnitude
    
    @property
    def min_x(self):
        """
        Get the minimum x that this line contains, lazily initialized.
        
        :returns: minimum x this line contains
        :rtype: :class:`numbers.Number`
        """
        
        if self._min_x is None:
            self._min_x = min(self.start.x, self.end.x)
        
        return self._min_x
        
    @property
    def min_y(self):
        """
        Get the minimum y that this line contains, lazily initialized.
        
        :returns: minimum x this line contains
        :rtype: :class:`numbers.Number`
        """
        
        if self._min_y is None:
            self._min_y = min(self.start.y, self.end.y)
        
        return self._min_y
    
    @property
    def max_x(self):
        """
        Get the maximum x that this line contains, lazily initialized.
        
        :returns: maximum x this line contains
        :rtype: :class:`numbers.Number`
        """
        
        if self._max_x is None:
            self._max_x = max(self.start.x, self.end.x)
            
        return self._max_x
    
    @property
    def max_y(self):
        """
        Get the maximum y that this line contains, lazily initialized.
        
        :returns: maximum x this line contains 
        :rtype: :class:`numbers.Number`
        """
        
        if self._max_y is None:
            self._max_y = max(self.start.y, self.end.y)
            
        return self._max_y
        
    @property
    def slope(self):
        """
        Get the slope of this line, lazily initialized.
       
        .. caution::
       
            The slope may be 0 (horizontal line) or positive or negative
            infinity (vertical lines). It may be necessary to handle 
            these lines seperately, typically through checking the
            :py:attr:`~pygorithm.geometry.line2.Line2.horizontal` and 
            :py:attr:`~pygorithm.geometry.line2.Line2.vertical` properties.
            
        
        :returns: the slope of this line (rise over run).
        :rtype: :class:`numbers.Number`
        """
        
        if self._slope is None:
            if self.delta.x == 0:
                if self.delta.y > 0:
                    self._slope = float('+inf')
                else:
                    self._slope = float('-inf')
            else:
                self._slope = self.delta.y / self.delta.x
        
        return self._slope
    
    @property
    def y_intercept(self):
        """
        Get the y-intercept of this line, lazily initialized.
        
        This does not take into account any offset of the 
        line and may return None if this is a vertical line.
        
        .. caution::
        
            This function will return a y-intercept for non-vertical 
            line segments that do not reach ``x=0``. 
        
        .. caution::
        
            The y-intercept will change based on the offset in a somewhat
            complex manner. 
            :py:meth:`~pygorithm.geometry.line2.Line2.calculate_y_intercept` 
            accepts an offset parameter.
        
        :returns: the y-intercept of this line when unshifted
        :rtype: :class:`numbers.Number` or None
        """
        
        if self.vertical:
            return None
        
        if self._y_intercept is None:
            self._y_intercept = self.start.y - self.slope * self.start.x
        
        return self._y_intercept
        
        
    @property
    def horizontal(self):
        """
        Get if this line is horizontal, lazily initialized.
        
        A line is horizontal if it has a slope of 0. This also
        means that ``start.y == end.y``
        
        :returns: if this line is horizontal
        :rtype: bool
        """
        
        if self._horizontal is None:
            self._horizontal = self.delta.y == 0
        
        return self._horizontal
        
    @property
    def vertical(self):
        """
        Get if this line is vertical, lazily initialized.
        
        A line is vertical if it has a slope of +inf or -inf. This
        also means that ``start.x == end.x``.
        
        :returns: if this line is vertical
        :rtype: bool
        """
        
        if self._vertical is None:
            self._vertical = self.delta.x == 0
            
        return self._vertical
        
    def __repr__(self):
        """
        Get an unambiguous representation of this line
        
        Example:
        
        .. code-block:: python
        
            from pygorithm.geometry import (vector2, line2)
            
            vec1 = vector2.Vector2(1, 1)
            vec2 = vector2.Vector2(3, 4)
            
            line = line2.Line2(vec1, vec2)
            
            # prints line2(start=vector2(x=1, y=1), end=vector2(x=3, y=4))
            print(repr(line))
        
        :returns: unambiguous representation of this line
        :rtype: string
        """
            
        return "line2(start={}, end={})".format(repr(self.start), repr(self.end))
    
    def __str__(self):
        """
        Get a human-readable representation of this line
        
        Example:
        
        .. code-block:: python
        
            from pygorithm.geometry import (vector2, line2)
            
            vec1 = vector2.Vector2(1, 1)
            vec2 = vector2.Vector2(3, 4)
            
            line = line2.Line2(vec1, vec2)
            
            # prints <1, 1> -> <3, 4>
            print(str(line))
            
            # same as above
            print(line)
        
        :returns: human-readable representation of this line
        :rtype: string
        """
        
        return "{} -> {}".format(self.start, self.end)
    
    def calculate_y_intercept(self, offset):
        """
        Calculate the y-intercept of this line when it is at the
        specified offset.
        
        If the offset is None this is exactly equivalent to y_intercept
        
        :param offset: the offset of this line for this calculations
        :type offset: :class:`pygorithm.geometry.vector2.Vector2` or None
        :returns: the y-intercept of this line when at offset
        :rtype: :class:`numbers.Number`
        """
        
        if offset is None:
            return self.y_intercept
        
        if self.vertical:
            return None
        # y = mx + b -> b = y - mx
        return self.start.y + offset.y - self.slope * (self.start.x + offset.x)
    
    @staticmethod
    def are_parallel(line1, line2):
        """
        Determine if the two lines are parallel.
        
        Two lines are parallel if they have the same or opposite slopes.
        
        :param line1: the first line 
        :type line1: :class:`pygorithm.geometry.line2.Line2`
        :param line2: the second line
        :type line2: :class:`pygorithm.geometry.line2.Line2`
        :returns: if the lines are parallel
        :rtype: bool
        """
        
        if line1.vertical and line2.vertical:
            return True
        
        return math.isclose(line1.slope, line2.slope)
    
    @staticmethod
    def contains_point(line, point, offset = None):
      """
      Determine if the line contains the specified point.
      
      Optionally, specify an offset for the line. Being
      on the line is determined using `math.isclose`.
      
      :param line: the line
      :type line: :class:`pygorithm.geometry.line2.Line2`
      :param point: the point
      :type point: :class:`pygorithm.geometry.vector2.Vector2`
      :param offset: the offset of the line or None for the origin
      :type offset: :class:`pygorithm.geometry.vector2.Vector2` or None
      :returns: if the point is on the line
      :rtype: bool
      """
      
      if line.vertical:
        x = line.start.x + offset.x if offset is not None else line.start.x
        if not math.isclose(point.x, x, abs_tol=1e-07):
          return False
        ymin = line.min_y + offset.y if offset is not None else line.min_y
        ymax = line.max_y + offset.y if offset is not None else line.max_y
        if math.isclose(point.y, ymin, abs_tol=1e-07) or math.isclose(point.y, ymax, abs_tol=1e-07):
          return True
        return point.y > ymin and point.y < ymax
      
      xmin = line.min_x + offset.x if offset is not None else line.min_x
      xmax = line.max_x + offset.x if offset is not None else line.max_x
      
      if not (math.isclose(point.x, xmin, abs_tol=1e-07) or point.x > xmin):
        return False
      
      if not (math.isclose(point.x, xmax, abs_tol=1e-07) or point.x < xmax):
        return False
        
      ystart = line.start.y + offset.y if offset is not None else line.start.y
      if line.horizontal:
        return math.isclose(ystart, point.y, abs_tol=1e-07)
      
      yint = line.calculate_y_intercept(offset)
      yatx = line.slope * point.x + yint
      return math.isclose(point.y, yatx, abs_tol=1e-07)
      
    @staticmethod
    def find_intersection(line1, line2, offset1 = None, offset2 = None):
        """
        Find the intersection between the two lines.
        
        The lines may optionally be offset by a fixed amount. This 
        will incur a minor performance penalty which is less than 
        that of recreating new lines.
        
        Two lines are considered touching if they only share exactly
        one point and that point is an edge of one of the lines. 
        
        If two lines are parallel, their intersection could be a line.
        
        .. tip::
        
            This will never return True, True
        
        :param line1: the first line
        :type line1: :class:`pygorithm.geometry.line2.Line2`
        :param line2: the second line
        :type line2: :class:`pygorithm.geometry.line2.Line2`
        :param offset1: the offset of line 1
        :type offset1: :class:`pygorithm.geometry.vector2.Vector2` or None
        :param offset2: the offset of line 2
        :type offset2: :class:`pygorithm.geometry.vector2.Vector2` or None
        :returns: (touching, overlapping, intersection_location)
        :rtype: (bool, bool, :class:`pygorithm.geometry.line2.Line2` or :class:`pygorithm.geometry.vector2.Vector2` or None)
        """
        
        
        # We will ensure that: 
        #  - If one line is vertical and one horizontal, line1 is the vertical line
        #  - If only one line is vertical, line1 is the vertical line
        #  - If only one line is horizontal, line1 is the horizontal line
        
        if line2.vertical and not line1.vertical:
            return Line2.find_intersection(line2, line1, offset2, offset1)
        if line2.horizontal and not line1.horizontal and not line1.vertical:
            return Line2.find_intersection(line2, line1, offset2, offset1)
            
        l1_st_x = line1.start.x + (offset1.x if offset1 is not None else 0)
        l1_st_y = line1.start.y + (offset1.y if offset1 is not None else 0)
        l1_en_x = line1.end.x + (offset1.x if offset1 is not None else 0)
        l1_en_y = line1.end.y + (offset1.y if offset1 is not None else 0)
        
        l2_st_x = line2.start.x + (offset2.x if offset2 is not None else 0)
        l2_st_y = line2.start.y + (offset2.y if offset2 is not None else 0)
        l2_en_x = line2.end.x + (offset2.x if offset2 is not None else 0)
        l2_en_y = line2.end.y + (offset2.y if offset2 is not None else 0)
        
        if line1.vertical and line2.vertical:
            # Two vertical lines
            if not math.isclose(l1_st_x, l2_st_x):
                return False, False, None
            
            aal1 = axisall.AxisAlignedLine(None, l1_st_y, l1_en_y)
            aal2 = axisall.AxisAlignedLine(None, l2_st_y, l2_en_y)
            
            touch, mtv = axisall.AxisAlignedLine.find_intersection(aal1, aal2)
            
            if not touch:
                return False, False, None
            elif mtv[0] is None:
                return True, False, vector2.Vector2(l1_st_x, mtv[1])
            else:
                return False, True, Line2(vector2.Vector2(l1_st_x, mtv[1]), vector2.Vector2(l1_st_x, mtv[2]))
            
        if line1.horizontal and line2.horizontal:
            # Two horizontal lines
            if not math.isclose(l1_st_y, l2_st_y):
                return False, False, None
            
            aal1 = axisall.AxisAlignedLine(None, l1_st_x, l1_en_x)
            aal2 = axisall.AxisAlignedLine(None, l2_st_x, l2_st_y)
            
            touch, mtv = axisall.AxisAlignedLine.find_intersection(aal1, aal2)
            
            if not touch:
                return False, False, None
            elif mtv[0] is None:
                return True, False, vector2.Vector2(mtv[1], l1_st_y)
            else:
                return False, True, Line2(vector2.Vector2(mtv[1], l1_st_x), vector2.Vector2(mtv[2], l1_st_y))
        
        if Line2.are_parallel(line1, line2):
            # Two non-vertical, non-horizontal, parallel lines
            yintr1 = line1.calculate_y_intercept(offset1)
            yintr2 = line2.calculate_y_intercept(offset2)
            if not math.isclose(yintr1, yintr2):
                return False, False, None
            
            axis = line1.axis
            aal1 = axisall.AxisAlignedLine(axis, l1_st_x * axis.x + l1_st_y * axis.y, l1_en_x * axis.x + l1_en_y * axis.y)
            aal2 = axisall.AxisAlignedLine(axis, l2_st_x * axis.x + l2_st_y * axis.y, l2_en_x * axis.x + l2_en_y * axis.y)
            
            touch, mtv = axisall.AxisAlignedLine.find_intersection(aal1, aal2)
            
            def unshift_vec(vec):
                numerator = line1.slope * vec.x - yintr1 * axis.x * axis.x
                denominator = axis.x * axis.y + line1.slope * axis.y * axis.y
                
                new_x = numerator / denominator
                new_y = line1.slope * new_x + yintr1
                
                return vector2.Vector2(new_x, new_y)
                
            if not touch:
                return False, False, None
            elif mtv[0] is None:
                return True, False, unshift_vec(axis * mtv[1])
            else:
                return False, True, Line2(unshift_vec(axis * mtv[1]), unshift_vec(axis * mtv[2]))
                
        if line1.vertical and line2.horizontal:
            # A vertical and horizontal line
            l1_min = min(l1_st_y, l1_en_y) if offset1 is not None else line1.min_y
            l1_max = max(l1_st_y, l1_en_y) if offset1 is not None else line1.max_y
            
            if l2_st_y < l1_min or l2_st_y > l2_max:
                return False, False, None
            
            l2_min = min(l2_st_x, l2_en_x) if offset2 is not None else line2.min_x
            l2_max = max(l2_st_x, l2_en_x) if offset2 is not None else line2.max_x
            
            if l1_st_x < l2_min or l1_st_x > l2_max:
                return False, False, None
            
            pt = vector2.Vector2(l1_st_x, l2_st_y)
            
            if math.isclose(l2_st_y, l1_min) or math.isclose(l2_st_y, l2_max) or math.isclose(l1_st_x, l2_min) or math.isclose(l2_st_y, l2_max):
                return True, False, pt
            else:
                return False, True, pt
        
        if line1.vertical:
            # A vertical and non-horizontal, non-vertical line
            line2_y_at_line1_x = line2.slope * l1_st_x + line2.calculate_y_intercept(offset2)
            
            l1_min = min(l1_st_y, l1_en_y) if offset1 is not None else line1.min_y
            l1_max = max(l1_st_y, l1_en_y) if offset1 is not None else line1.max_y
            
            if math.isclose(line2_y_at_line1_x, l1_min) or math.isclose(line2_y_at_line1_x, l1_max):
                return True, False, vector2.Vector2(l1_st_x, line2_y_at_line1_x)
            elif line2_y_at_line1_x < l1_min or line2_y_at_line1_x > l2_max:
                return False, False, None
            else:
                return False, True, vector2.Vector2(l1_st_x, line2_y_at_line1_x)
        
        if line1.horizontal:
            # A horizontal and non-vertical, non-horizontal line
            # y = mx + b -> x = (y - b) / m
            line2_x_at_line1_y = (l1_st_y - line2.calculate_y_intercept(offset2)) / line2.slope
            
            l1_min = min(l1_st_x, l1_en_x) if offset1 is not None else line1.min_x
            l1_max = max(l1_st_x, l1_en_x) if offset1 is not None else line1.max_x
            
            if math.isclose(line2_x_at_line1_y, l1_min) or math.isclose(line2_x_at_line1_y, l1_max):
                return True, False, vector2.Vector2(line2_x_at_line1_y, l1_st_y)
            elif line2_x_at_line1_y < l1_min or line2_x_at_line1_y > l1_max:
                return False, False, None
            else:
                return False, True, vector2.Vector2(line2_x_at_line1_y, l1_st_y)
        
        # Two non-vertical, non-horizontal, non-parallel lines
        
        # y = m1 x + b1 
        # y = m2 x + b2
        # m1 x + b1 = m2 x + b2
        # m1 x - m2 x = b2 - b1
        # x = (b2 - b1) / (m1 - m2)
        
        yintr1 = line1.calculate_y_intercept(offset1)
        yintr2 = line2.calculate_y_intercept(offset2)
        intr_x = (yintr2 - yintr1) / (line1.slope - line2.slope)
        
        # Some caution needs to be taken here to ensure we do approximately before range
        # checks. It's possible for _approx(a, b) to be True and a < b to be True
        
        on_edge1 = math.isclose(intr_x, l1_st_x) or math.isclose(intr_x, l1_en_x)
        on_edge2 = math.isclose(intr_x, l2_st_x) or math.isclose(intr_x, l2_en_x)
        
        if on_edge1 and on_edge2:
            intr_y = line1.slope * intr_x + yintr1
            return True, False, vector2.Vector2(intr_x, intr_y)
        
        l1_min_x = min(l1_st_x, l1_en_x) if offset1 is not None else line1.min_x
        l1_max_x = max(l1_st_x, l1_en_x) if offset1 is not None else line1.max_x
        l2_min_x = min(l2_st_x, l2_en_x) if offset2 is not None else line2.min_x
        l2_max_x = max(l2_st_x, l2_en_x) if offset2 is not None else line2.max_x
        
        on_line1 = on_edge1 or (intr_x > l1_min_x and intr_x < l1_max_x)
        on_line2 = on_edge2 or (intr_x > l2_min_x and intr_x < l2_max_x)
        
        if on_line1 and on_line2:
            intr_y = line1.slope * intr_x + yintr1
            is_edge = on_edge1 or on_edge2
            return is_edge, not is_edge, vector2.Vector2(intr_x, intr_y)
        
        return False, False, None
        