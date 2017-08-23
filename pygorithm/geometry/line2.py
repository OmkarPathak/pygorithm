"""
line2

Author: Timothy Moore

Defines a simple two-dimensional line segment
"""

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

    .. note::

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
        
        pass
        
    @property
    def delta(self):
        """
        Get the vector from start to end, lazily initialized.
        
        :returns: delta from start to end
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        pass
        
    @property
    def axis(self):
        """
        Get the normalized delta vector, lazily initialized
        
        :returns: normalized delta
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        pass
    
    @property
    def normal(self):
        """
        Get normalized normal vector to axis, lazily initialized.

        Get the normalized normal vector such that the normal
        vector is 90 degrees counter-clockwise from the axis.
        
        :returns: normalized normal to axis
        :rtype: :class:`pygorithm.geometry.vector2.Vector2`
        """
        pass
    
    @property
    def magnitude_squared(self):
        """
        Get the square of the magnitude of delta, lazily initialized.
        
        :returns: square of magnitude of delta
        :rtype: :class:`numbers.Number`
        """
        pass
        
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
        pass
    
    @property
    def min_x(self):
        """
        Get the minimum x that this line contains, lazily initialized.
        
        :returns: minimum x this line contains
        :rtype: :class:`numbers.Number`
        """
        pass
        
    @property
    def min_y(self):
        """
        Get the minimum y that this line contains, lazily initialized.
        
        :returns: minimum x this line contains
        :rtype: :class:`numbers.Number`
        """
        pass
    
    @property
    def max_x(self):
        """
        Get the maximum x that this line contains, lazily initialized.
        
        :returns: maximum x this line contains
        :rtype: :class:`numbers.Number`
        """
        pass
    
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
        pass
    
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
        pass
        
    @property
    def horizontal(self):
        """
        Get if this line is horizontal, lazily initialized.
        
        A line is horizontal if it has a slope of 0. This also
        means that ``start.y == end.y``
        
        :returns: if this line is horizontal
        :rtype: bool
        """
        pass
        
    @property
    def vertical(self):
        """
        Get if this line is vertical, lazily initialized.
        
        A line is vertical if it has a slope of +inf or -inf. This
        also means that ``start.x == end.x``.
        
        :returns: if this line is vertical
        :rtype: bool
        """
        pass
        
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
            
        pass
    
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
        
        pass
    
    def calculate_y_intercept(offset):
        """
        Calculate the y-intercept of this line when it is at the
        specified offset.
        
        :param offset: the offset of this line for this calculations
        :type offset: :class:`pygorithm.geometry.vector2.Vector2`
        :returns: the y-intercept of this line when at offset
        :rtype: :class:`numbers.Number`
        """
        pass
    
    @staticmethod
    def find_intersection(line1, line2, offset1 = None, offset2 = None, find_mtv = True):
        """
        Find the intersection between the two lines.
        
        The lines may optionally be offset by a fixed amount. This 
        will incur a minor performance penalty which is less than 
        that of recreating new lines.
        
        .. note::
        
            There is only a very minor performance improvement by setting find_mtv to 
            false. It is rare that, if an mtv will be necessary, to find any performance
            improvement by first searching with ``find_mtv=False`` and then later 
            with :``find_mtv=True``
        
        .. note::
            
            The resulting mtv is broken up into distance and axis. This falls naturally out
            of the algorithm and is often convienent. To find the full mtv, simply multiply
            the two.
        
        :param line1: the first line
        :type line1: :class:`pygorithm.geometry.line2.Line2`
        :param line2: the second line
        :type line2: :class:`pygorithm.geometry.line2.Line2`
        :param offset1: the offset of line 1
        :type offset1: :class:`pygorithm.geometry.vector2.Vector2` or None
        :param offset2: the offset of line 2
        :type offset2: :class:`pygorithm.geometry.vector2.Vector2` or None
        :param find_mtv: if false, mtv will always be null.
        :returns: (touching, overlapping, (distance, axis))
        :rtype: (bool, bool, (:class:`numbers.Number`, :class:`pygorithm.geometry.vector2.Vector2`) or None)
        """
        pass
        
        
        