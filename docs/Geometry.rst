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

.. autoclass:: pygorithm.geometry.vector2.Vector2
    :members:
    :special-members:
    
Line2
-----

.. autoclass:: pygorithm.geometry.line2.Line2
    :members:
    :special-members:
    
Axis-Aligned Line
-----------------

.. autoclass:: pygorithm.geometry.axisall.AxisAlignedLine
    :members:
    :special-members:
    
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
    
    The ordered list of Vector2s in this polygon.

.. attribute:: Polygon2.lines

    The ordered list of Line2s in this polygon.

.. attribute:: Polygon2.normals

    The orders list of normal Vector2s corresponding to the Line2s 
    in lines

.. attribute:: Polygon2.center

    The Vector2 center of the polygon. Lazily initialized.

.. attribute:: Polygon2.aabb

    The Rect2 bounding box of this polygon. Lazily initialized.

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
    
    


    
    
    