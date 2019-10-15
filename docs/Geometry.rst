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
    poly1 = polygon2.Polygon2.from_regular(5, 5)
    
    # create a polygon from tuple (x, y) - note that the polygon must be convex
    # and the points must be clockwise
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
    
Features
--------

* Structures available:
    - Vector2 (vector2)
    - Line2 (line2)
    - AxisAlignedLine (axisall)

* Shapes available:
    - Concave Polygons (polygon2)
    - Rectangles (rect2)

* Algorithms available:
    - Separating Axis Theorem (polygon2)
    - Broad-phase (rect2)
    - Extrapolated intersection (extrapolated_intersection)

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

.. autoclass:: pygorithm.geometry.polygon2.Polygon2
    :members:
    :special-members:

Axis-Aligned Rectangle
----------------------

.. autoclass:: pygorithm.geometry.rect2.Rect2
    :members:
    :special-members:
    :private-members:

Extrapolated Intersection
-------------------------

.. automodule:: pygorithm.geometry.extrapolated_intersection
    :members:
    
    