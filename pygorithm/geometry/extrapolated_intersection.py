"""
Author: Timothy Moore
Created On: 4th September 2017

Contains various approaches to determining if a polygon will 
intersect another polygon as one or both polygons go along 
a a single direction at a constant speed.

This problem could be thought of as one of extrapolation -
given these initial conditions, extrapolate to determine 
if intersections will occur.

.. note::
    
    Touching is not considered intersecting in this module. Touching 
    is determined using `math.isclose`
    
"""

def calculate_one_moving_and_one_stationary(poly1, poly1_offset, poly1_velocity, poly2, poly2_offset):
    """
    Determine if the moving polygon will intersect the stationary polygon.
    
    This is the simplest question. Given two polygons, one moving and one not,
    determine if the two polygons will ever intersect (assuming they maintain
    constant velocity).
    
    :param poly1: the geometry of the polygon that is moving
    :type poly1: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly1_offset: the starting location of the moving polygon
    :type poly1_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly1_velocity: the velocity of the moving polygon 
    :type poly1_velocity: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly2: the geometry of the stationary polygon
    :type poly2: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly2_offset: the offset of the stationary polygon
    :type poly2_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :returns: if they will intersect
    :rtype: bool
    """
    pass

def calculate_one_moving_one_stationary_distancelimit(poly1, poly1_offset, poly1_velocity, poly2, poly2_offset, max_distance):
    """
    Determine if the moving polygon will intersect the stationary polygon 
    within some distance.
    
    This is a step up, and very similar to the actual problem many any-angle 
    pathfinding algorithms run into. Given two polygons, 1 moving and 1 
    stationary, determine if the first polygon will intersect the second 
    polygon before moving a specified total distance.
    
    :param poly1: the geometry of the polygon that is moving
    :type poly1: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly1_offset: the starting location of the moving polygon
    :type poly1_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly1_velocity: the velocity of the moving polygon 
    :type poly1_velocity: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly2: the geometry of the stationary polygon
    :type poly2: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly2_offset: the offset of the stationary polygon
    :type poly2_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :param max_distance: the max distance that poly1 can go
    :type max_distance: :class:`numbers.Number`
    :returns: if they will intersect
    :rtype: bool
    """
    pass

def calculate_one_moving_one_stationary_along_path(poly1, poly1_start, poly1_end, poly2, poly2_offset):
    """
    Determine if the moving polygon will intersect the stationary polygon as 
    it moves from the start to the end.
    
    This is a rewording of :py:func:`.calculate_one_moving_one_stationary_distancelimit` 
    that is more common. Given two polygons, 1 moving and 1 stationary, where the 
    moving polygon is going at some speed from one point to another, determine if 
    the two polygons will intersect.
    
    :param poly1: the geometry of the polygon that is moving
    :type poly1: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly1_start: where the moving polygon begins moving from
    :type poly1_start: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly1_end: where the moving polygon stops moving
    :type poly1_end: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly2: the geometry of the stationary polygon
    :type poly2: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly2_offset: the location of the second polygon
    :type poly2_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :returns: if they will intersect
    :rtype: bool
    """
    pass
    

def calculate_one_moving_many_stationary(poly1, poly1_offset, poly1_velocity, other_poly_offset_tuples):
    """
    Determine if the moving polygon will intersect anything as it 
    moves at a constant direction and speed forever.
    
    This is the simplest arrangement of this problem with a collection 
    of stationary polygons. Given many polygons of which 1 is moving, 
    determine if the moving polygon intersects the other polygons now or at 
    some point in the future if it moves at some constant direction and 
    speed forever. 
    
    This does not verify the stationary polygons are not intersecting.
    
    :param poly1: the geometry of the polygon that is moving
    :type poly1: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly1_offset: the starting location of the moving polygon
    :type poly1_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly1_velocity: the velocity of the moving polygon 
    :type poly1_velocity: :class:`pygorithm.geometry.vector2.Vector2`
    :param other_poly_offset_tuples: list of (polygon, offset) of the stationary polygons
    :type other_poly_offset_tuples: list of (:class:`pygorithm.geometry.polygon2.Polygon2`, :class:`pygorithm.geometry.vector2.Vector2`)
    :returns: if an intersection will occur
    :rtype: bool
    """
    pass

def calculate_one_moving_many_stationary_distancelimit(poly1, poly1_offset, poly1_velocity, max_distance, other_poly_offset_tuples):
    """
    Determine if the moving polygon will intersect anyything as 
    it moves in a constant direction and speed for a certain 
    distance.
    
    This does not verify the stationary polygons are not intersecting.
    
    :param poly1: the geometry of the polygon that is moving
    :type poly1: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly1_offset: the starting location of the moving polygon
    :type poly1_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly1_velocity: the velocity of the moving polygon 
    :type poly1_velocity: :class:`pygorithm.geometry.vector2.Vector2`
    :param max_distance: the max distance the polygon will go 
    :type max_distance: :class:`numbers.Number`
    :param other_poly_offset_tuples: list of (polygon, offset) of the stationary polygons
    :type other_poly_offset_tuples: list of (:class:`pygorithm.geometry.polygon2.Polygon2`, :class:`pygorithm.geometry.vector2.Vector2`)
    :returns: if an intersection will occur
    :rtype: bool
    """
    pass
    
def calculate_one_moving_many_stationary_along_path(poly1, poly1_start, poly1_end, other_poly_offset_tuples):
    """
    Determine if a polygon that moves from one point to another
    will intersect anything.
    
    This is the question that the Theta* family of pathfinding 
    algorithms require. It is simply a rewording of 
    :py:func:`.calculate_one_moving_many_stationary_distancelimit`
    
    This does not verify the stationary polygons are not intersecting.
    
    :param poly1: the geometry of the polygon that is moving
    :type poly1: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly1_start: where the polygon begins moving from
    :type poly1_start: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly1_end: where the polygon stops moving at 
    :type poly1_end: :class:`pygorithm.geometry.vector2.Vector2`
    :param other_poly_offset_tuples: list of (polygon, offset) of the stationary polygons
    :type other_poly_offset_tuples: list of (:class:`pygorithm.geometry.polygon2.Polygon2`, :class:`pygorithm.geometry.vector2.Vector2`)
    :returns: if an intersection will occur
    :rtype: bool
    """
    
def calculate_two_moving(poly1, poly1_offset, poly1_vel, poly2, poly2_offset, poly2_vel):
    """
    Determine if two moving polygons will intersect at some point.
    
    This is the simplest question when there are multiple moving polygons.
    Given two polygons moving at a constant velocity and direction forever,
    determine if an intersection will occur.
    
    It should be possible for the reader to extrapolate from this function 
    and the process for stationary polygons to create similar functions to 
    above where all or some polygons are moving. 
    
    :param poly1: the first polygon
    :type poly1: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly1_offset: where the first polygon starts at 
    :type poly1_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly1_vel: the velocity of the first polygon
    :type poly1_vel: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly2: the second polygon 
    :type poly2: :class:`pygorithm.geometry.polygon2.Polygon2`
    :param poly2_offset: where the second polygon starts at 
    :type poly2_offset: :class:`pygorithm.geometry.vector2.Vector2`
    :param poly2_vel: the velocity of the second polygon
    :type poly2_vel: :class:`pygorithm.geometry.vector2.Vector2`
    :returns: if an intersectino will occur
    :rtype: bool
    """
    pass