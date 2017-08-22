========
Geometry
========

Some geometrical shapes and operations

Quick Start Guide
-----------------

.. code-block:: python

    # import the required shapes and structures
    from pygorithm.geometry import polygon2
    from pygorithm.geometry import vector2
    
    # create a regular polygon
    poly1 = polygon2.Polygon2(regular=True, sides=5, length=5)
    
    # create a polygon from tuple (x, y) - note that the polygon must be concave
    poly2 = polygon2.Polygon2(points=[ (0, 0), (1, 0), (1, 1), (0, 1) ])
    
    # create a polygon from vector2s. 
    poly3 = polygon2.Polygon2(points=[ vector2.Vector2(0, 0), 
                                     vector2.Vector2(1, 1), 
                                     vector2.Vector2(2, 0) ])
    
    # create a polygon by rotating another polygon
    poly4 = poly3.rotate(0.2)
    poly5 = poly3.rotate(degrees = 30)
    
    
    # check intersection
    intrs, mtv = polygon2.Polygon2.find_intersection(poly1, poly2, (0, 0), (1, 0))
    
    if intrs:
        mtv_dist = mtv[0]
        mtv_vec = mtv[1]
        print('They intersect. The best way to push poly1 is {} units along {}'.format(mtv_dist, mtv_vec))
    else:
        print('No intersection')
    
    # check complete overlap
    overlap = polygon2.Polygon2.contains_polygon(poly1, poly2, (0, 2), (3, 1))
    
Features
--------

* Structures available:
    - Vector2 (vector2)
    - Line2 (line2)
    - AxisAlignedLine (axisall)

* Shapes available:
    - Concave Polygons (polygon2)

* Algorithms available:
    - Separating Axis Theorem (polygon2)

Vector2
-------

.. class: Vector2

Defines a simple two-dimensional, mutable vector.

.. note::

    Equality is not overriden on vectors, because it is expected that 
    vectors will be used mutably by directly modifying x and y. However, all 
    functions on vectors are immutable (they return a copy) 

.. attribute:: Vector2.x 

    The first component of this vector. Mutation is allowed where appropriate.

.. attribute:: Vector2.y

    The second component of this vector. Mutation is allowed where appropriate.

.. method:: vector2.Vector2(self, *args, **kwargs)

Accepts a pair of unnamed parameters, a pair of named x, y parameters, 
another Vector2, or a tuple with 2 numerics. Examples of each: 

.. code-block:: python

    from pygorithm.geometry import vector2
    
    # A pair of unnamed parameters
    vec1 = vector2.Vector2(0, 5)
    
    # A pair of named parameters
    vec2 = vector2.Vector2(x = 0, y = 5)
    
    # Another vector2
    vec3 = vector2.Vector2(vec2)
    
    # A tuple with two numerics
    vec4 = vector2.Vector2( (0, 5) )

The following operations on vectors are extremely common and rarely varied, and as such have 
operator support.

.. method:: Vector2.__add__(self, other)

- **other**           : `Vector2` the vector to add to this one
- **Return Value**    : a new `Vector2` by component-based addition

Adds the two vectors component wise. Example:

.. code-block:: python

    from pygorithm.geometry import vector2
    
    vec1 = vector2.Vector2(0, 3)
    vec2 = vector2.Vector2(2, 4)
    
    vec3 = vec1 + vec2
    
    # prints <2, 7>
    print(vec3) 

.. method:: Vector2.__sub__(self, other)

- **other**           : `Vector2` the vector to subtract from this one
- **Return Value**    : a new `Vector2` by component-based subtraction

Subtracts the two vectors component wise. Example:

.. code-block:: python

    from pygorithm.geometry import vector2
    
    vec1 = vector2.Vector2(5, 5)
    vec2 = vector2.Vector2(2, 3)
    
    vec3 = vec1 - vec2
    vec4 = vec2 - vec1
    
    # prints <3, 2>
    print(vec3)
    
    # prints <2, 3>
    print(vec4)
    
.. method:: Vector2.__mul__(self, scale_factor)
.. method:: Vector2.__rmul__(self, scale_factor)

- **scale_factor**    : `numeric` the factor to multiply both components by
- **Return Value**    : a new `Vector2` by component-based multiplication

Scales the vector by the specified factor. Will throw an exception if 
scale_factor is not a numeric - it will not perform the dot product (use 
`dot` for that) Examples: 

.. code-block:: python

    from pygorithm.geometry import vector2
    
    vec1 = vector2.Vector2(4, 8)
    
    vec2 = vec1 * 0.5
    vec3 = 2 * vec2
    
    # prints <2, 4>
    print(vec2)
    
    # prints <8, 16>
    print(vec3)


.. method:: Vector2.__repr__(self)

- **Return Value**    : an unambiguous representation of this vector

.. code-block:: python

    from pygorithm.geometry import vector2
    
    vec = vector2.Vector2(3, 5)
    
    # prints vector2(x=3, y=5)
    print(repr(vec)) 

.. method:: Vector2.__str__(self)

- **Return Value**    : a human-readable representation of this vector

.. code-block:: python

    from pygorithm.geometry import vector2
    
    vec = vector2.Vector2(7, 11)
    
    # prints <7, 11>
    print(str(vec))
    
    # also prints <7, 11>
    print(vec)

.. method:: Vector2.dot(self, other)

- **other**           : `vector2` to perform the dot product on
- **Return Value**    : a numeric from the dot product of the two vectors

The dot product of two vectors is calculated as so::

    Let v1 be a vector such that v1 = <v1_x, v1_y>
    Let v2 be a vector such that v2 = <v2_x, v2_y>
    
    v1 . v2 = v1_x * v2_x + v1_y * v2_y

Example:

.. code-block:: python

    from pygorithm.geometry import vector2
    
    vec1 = vector2.Vector2(3, 5)
    vec2 = vector2.Vector2(7, 11)
    
    dot_12 = vec1.dot(vec2)
    
    # prints 76
    print(dot_12) 
    
.. method:: Vector2.rotate(self, *args, **kwargs)

The named argument "degrees" or "radians" may be passed in to rotate 
this vector by the specified amount in degrees (or radians), 
respectively. If both are omitted, the first unnamed argument is 
assummed to be the amount to rotate in radians. 

Additionally, the named argument "about" may be passed in to specify 
about what the vector should be rotated. If omitted then the first 
unconsumed unnamed argument is assumed to be the vector. If there are 
no unconsumed unamed arguments then the origin is assumed. 

Examples:

.. code-block:: python

    from pygorithm.geometry import vector2
    import math
    
    vec1 = vector2.Vector2(1, 0)
    
    vec2 = vec1.rotate(math.pi * 0.25)
    
    # prints <0.707, 0.707>
    print(vec2)
    
    vec3 = vec1.rotate(degrees = 45)
    
    # prints <0.707, 0.707>
    print(vec3)
    
    # The following operations are all identical
    
    vec4 = vec1.rotate(math.pi, vector2.Vector2(1, 1))
    vec5 = vec1.rotate(radians = math.pi, about = vector2.Vector2(1, 1))
    vec6 = vec1.rotate(degrees = 180, about = vector2.Vector2(1, 1))
    vec7 = vec1.rotate(vector2.Vector2(1, 1), degrees = 180)
    
    # prints <1, 2>
    print(vec4)

.. method:: Vector2.normalize(self)

- **Return Value**    : a `Vector2` in the same direction as this one with a magnitude of 1

Example:

.. code-block:: python

    from pygorithm.geometry import vector2
    
    vec1 = vector2.Vector2(2, 0)
    
    vec2 = vec1.normalize()
    
    # prints <1, 0>
    print(vec2)
    
* Miscellaneous

.. method:: vector2.magnitude(self)

- **Return Value**    : a `numeric` magnitude of this vector

Example:

.. code-block:: python

    from pygorithm.geometry import vector2
    
    vec1 = vector2.Vector2(3, 4)
    magn = vec1.magnitude()
    
    # prints 5
    print(magn)

Line2
-----

.. class:: Line2

Defines a two-dimensional directed line segment defined by two points. 
This class is mostly used as a way to cache information that is 
regularly required when working on geometrical problems.

.. note::

    Lines should be used as if they were completely immutable to ensure 
    correctness. All attributes of Line2 can be reconstructed from the two 
    points, and thus cannot be changed on their own and must be recalculated 
    if there were any changes to `start` or `end`. 

.. note::

    To prevent unnecessary recalculations, many functions on lines accept an 
    'offset' argument, which is used to perform calculations on lines that 
    are simply shifts of other lines.

.. attribute:: Line2.start

    `Vector2` the start of this line
    
.. attribute:: Line2.end

    `Vector2` the end of this line
    
.. attribute:: Line2.delta

    `Vector2` from start to end

.. attribute:: Line2.axis

    `Vector2` normalized `delta`

.. attribute:: Line2.normal

    `Vector2` normalized normal of `axis`

.. attribute:: Line2.magnitude_squared

    `numerical` square of the magnitude of the line
    
.. attribute:: Line2.magnitude

    `numerical` magnitude of the line
    
.. attribute:: Line2.min_x

    `numerical` minimum x-value on the line
    
.. attribute:: Line2.min_y

    `numerical` minimum y-value on the line

.. attribute:: Line2.max_x

    `numerical` maximum x-value on the line
    
.. attribute:: Line2.max_y

    `numerical` maximum y-value on the line
    
.. attribute:: Line2.slope

    `numerical` (including +inf and -inf) slope of the line
    
.. attribute:: Line2.y_intercept

    `numerical or None` y_intercept of the line (or None if `vertical`)
    
.. attribute:: Line2.horizontal

    `bool` true if ``slope == 0``, false otherwise
    
.. attribute:: Line2.vertical 

    `bool` true if ``slope == float('+inf') or slope == float('-inf')``, false otherwise
    
.. staticmethod:: intersects_line(line1, line2, offset1, offset2)

    - **line1**        - `Line2` first line
    - **line2**        - `Line2` second line
    - **offset1**      - `Vector2` offset of first line
    - **offset2**      - `Vector2` offset of second line
    - **Return Value** - `bool, bool` touches, overlaps
    
    Determines if the two lines at the specified offsets are touching and/or
    overlapping. Two lines touch if they share endpoints, two lines overlap 
    if they intersect on any point that is not an endpoint.

Axis-Aligned Line
-----------------

This class provides functions related to axis aligned lines as well as 
acting as a convienent container for them. In this context, an axis 
aligned line is a two-dimensional line that is defined by an axis and 
length on that axis, rather than two points. When working with two lines 
defined as such that have the same axis, many calculations are 
simplified. 

.. class:: AxisAlignedLine

Defines an undirected two-dimensional line by an axis, a minimum and a maximum. 

.. note::

    Though it requires the same amount of memory as a simple representation of
    a 2 dimensional line (4 numerics), it cannot describe all types of lines.
    All lines that can be defined this way intersect (0, 0).

.. note::
    
    `min` and `max` are referring to nearness to negative and positive infinity,
    respectively. The absolute value of `min` may be larger than `max`.

.. note::

    `AxisAlignedLine`s are an intermediary operation, so offsets should be baked 
    into them.

.. attribute AxisAlignedLine.axis

    `Vector2` the axis this line is along.
    
.. attribute AxisAlignedLine.min

    `numeric` the number (closest to negative infinity) that is still on this 
    line when walked along the axis. If negative, it may have a greater absolute
    value than max and implies walking in the opposite direction of the axis.
    
.. attribute AxisAlignedLine.max

    `numeric` the number (closest to positive infinity) that is still on this 
    line when walked along the axis. If negative, it may have a smaller absolute
    value than min and implies walking in the opposite direction of the axis.

.. method:: AxisAlignedLine(self, axis, point1, point2)

    - **axis**    - `Vector2` axis this line is on
    - **point1**  - `numeric` one point on this line
    - **point2**  - `numeric` a different point on this line
    
    Constructs an axis aligned line with the appropriate min and max.

.. staticmethod:: AxisAlignedLine.intersects(line1, line2)

    - **line1**        - `AxisAlignedLine` the first line
    - **line2**        - `AxisAlignedLine` the second line
    - **Return Value** - `bool, bool` touching, overlapping
    
    Determines if the two lines are touching and if they are, if 
    they are overlapping. 
    
    .. note::
    
        It is rarely faster to check intersection before finding intersection if
        you will need the minimum translation vector, since they do mostly 
        the same operations.
    
.. staticmethod:: AxisAlignedLine.find_intersection(line1, line2)

    - **line1**        - `AxisAlignedLine` the first line
    - **line2**        - `AxisAlignedLine` the second line
    - **Return Value** - `bool, numeric or None` touching, mtv against 1
    
    Determines if the two lines are touching, and then returns the 
    minimum translation vector to move line 1 along axis. If the result
    is negative, it means line 1 should be moved in the opposite direction
    of the axis by the magnitude of the result.
    
    Returns `true, None` if the lines are touching.
    
    .. note::
    
        Ensure your program correctly handles `true, None`

.. staticmethod:: AxisAlignedLine.contains_point(line, point)

    - **line**         - `AxisAlignedLine` the line
    - **point**        - `numeric` the point 
    - **Return Value** - `bool` if point is contained (or an edge of) the line
    
    Determines if the line contains the specified point, which is assumed 
    to be defined the same way as min and max.
    
Concave Polygon
---------------

.. class:: Polygon2

Defines a concave polygon defined by a list of points such that each
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
    methods will accept offsets to the polygons.
    
.. note::

    Unfortunately, operations on rotated polygons require recalculating
    the polygon based on its rotated points. This should be avoided 
    unless necessary through the use of Axis-Aligned Bounding Boxes
    and similar tools.
    
.. attribute:: Polygon2.points 
    
    The ordered list of `Vector2`s in this polygon.

.. attribute:: Polygon2.lines

    The ordered list of `Line2`s in this polygon.

.. attribute:: Polygon2.normals

    The orders list of normal `Vector2`s corresponding to the `Line2`'s 
    in lines

.. attribute:: Polygon2.center

    The `Vector2` center of the polygon. Lazily initialized.
    
.. attribute:: Polygon2.aabb

    The `Rect2` bounding box of this polygon. Lazily initialized.
    
.. method:: Polygon2(self, points)

    - **points** - The ordered list of points in this polygon.
    
.. staticmethod:: Polygon2.contains_point(polygon, offset, vec)

    - **polygon** - polygon to check
    - **offset**  - offset of the polygon
    - **vec**     - the vector to check if is inside the polyogn at offset
    
    Determines if the polygon contains vector when at the specified offset.

.. staticmethod:: Polygon2.contains_polygon(poly1, poly2, offset1, offset2)

    - **poly1**        - The polygon that might contain poly2
    - **poly2**        - The polygon that might be contained in poly1
    - **offset1**      - The position of the first polygon
    - **offset2**      - The position of the second polygon
    - **Return Value** - `bool` true if poly2 is completely contained in poly1, false otherwise
    
    Determines if the second polygon is completely contained in the first
    polygon.
    
.. staticmethod:: Polygon2.find_intersection(poly1, poly2, offset1, offset2)

    - **poly1**        - The first polygon
    - **poly2**        - The second polygon
    - **offset1**      - The offset of the first polygon
    - **offset2**      - The offset of the second polygon
    - **Return Value** - `bool, None or Vector2` If there is intersection, the MTV for poly1 or None
    
    Determines if the two polygons intersect, and how to prevent 
    intersection by a move on the first polygon. If the polygons 
    do not intersect, returns `false, None`. If the polygons 
    intersect and overlap, returns `true, Vector2`. If the polygons
    are touching but do not overlap, returns `true, None`.
    
    .. note::
    
        Ensure that the result `true, None` is handled correctly.
    
    


    
    
    