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
    
    Touching is not considered intersecting in this module, unless otherwise
    stated. Touching is determined using `math.isclose`
    
"""

from pygorithm.geometry import (vector2, line2, polygon2, axisall)
import math

def __calc_one_moving_one_stat_vertical_velocity(point, velocity, line, offset):
  line_as_axisall = axisall.AxisAlignedLine(None, line.min_x + offset.x, line.max_x + offset.x)
  outer, inner = axisall.AxisAlignedLine.contains_point(line_as_axisall, point.x)
  if not outer and not inner:
    return False, None
  
  if line.vertical:
    if velocity.y > 0:
      if point.y < line.min_y + offset.y:
        dist = line.min_y + offset.y - point.y
        return True, dist
      else:
        return False, None
    else:
      if point.y > line.max_y + offset.y:
        dist = point.y - line.max_y - offset.y
        return True, dist
      else:
        return False, None
  
  line_yintr = line.calculate_y_intercept(offset)
  liney_at_pointx = line.slope * point.x + line_yintr
  
  point_to_line = liney_at_pointx - point.y
  if not math.isclose(math.copysign(1, point_to_line), math.copysign(1, velocity.y)):
    return False, None
  
  return True, abs(point.y - liney_at_pointx)
  
def __calc_one_moving_one_stat_vertical_line(point, velocity, line, offset):
  # nonvertical velocity, point not on line
  
  if math.isclose(point.x, line.start.x, abs_tol = 1e-07):
    # it's impossible that the point intersects a vertical line that it 
    # is at the start of except at the point, but that's checked previously
    return False, None
  
  if velocity.x > 0 and (line.start.x + offset.x) < point.x:
    return False, None
  if velocity.x < 0 and (line.start.x + offset.x) > point.x:
    return False, None
    
  point_slope = velocity.y / velocity.x
  point_yintr = point.y - point_slope * point.x
  
  point_y_at_line_x = point_slope * (line.start.x + offset.x) + point_yintr
  
  line_as_axisall = axisall.AxisAlignedLine(None, line.min_y + offset.y, line.max_y + offset.y)
  outer, inner = axisall.AxisAlignedLine.contains_point(line_as_axisall, point_y_at_line_x)
  if not outer and not inner:
    return False, None
  
  dist = (vector2.Vector2(line.start.x + offset.x, point_y_at_line_x) - point).magnitude()
  return True, dist
  
def __calc_one_moving_one_stat_parallel(point, velocity, line, offset, point_slope):
  # vel not vertical, line not vertical, point not on line, line is parallel to velocity
  
  if not math.isclose(line.slope, point_slope, abs_tol=1e-07):
    return False, None
  
  line_as_axisall = axisall.AxisAlignedLine(line.axis, (line.start + offset).dot(line.axis), (line.end + offset).dot(line.axis))
  point_on_axis = point.dot(line.axis)
  vel_on_axis_sign = math.copysign(1, velocity.dot(line.axis))
  
  if point_on_axis < line_as_axisall.min:
    if vel_on_axis_sign < 0:
      return False, None
    else:
      return True, line_as_axisall.min - point_on_axis
  else:
    if vel_on_axis_sign > 0:
      return False, None
    else:
      return True, point_on_axis - line_as_axisall.max 
  
def calculate_one_moving_point_and_one_stationary_line(point, velocity, line, offset):
    """
    Determine if the point moving at velocity will intersect the line.
    
    The line is positioned at offset. Given a moving point and line segment,
    determine if the point will ever intersect the line segment.
    
    .. caution::
        
        Points touching at the start are considered to be intersection. This 
        is because there is no way to get the "direction" of a stationary
        point like you can a line or polygon.
    
    :param point: the starting location of the point
    :type point: :class:`pygorithm.geometry.vector2.Vector2`
    :param velocity: the velocity of the point 
    :type velocity: :class:`pygorithm.geometry.vector2.Vector2`
    :param line: the geometry of the stationary line
    :type line: :class:`pygorithm.geometry.line2.Line2`
    :param offset: the offset of the line
    :type offset: :class:`pygorithm.geometry.vector2.Vector2`
    :returns: if the point will intersect the line, distance until intersection
    :rtype: bool, :class:`numbers.Number` or None
    """
    if offset is None:
      offset = vector2.Vector2(0, 0)
    
    if line2.Line2.contains_point(line, point, offset):
      return True, 0
    
    if math.isclose(velocity.x, 0, abs_tol=1e-07):
      return __calc_one_moving_one_stat_vertical_velocity(point, velocity, line, offset)
    if line.vertical:
      return __calc_one_moving_one_stat_vertical_line(point, velocity, line, offset)
    
    point_slope = velocity.y / velocity.x
    if math.isclose(line.slope, point_slope, abs_tol=1e-07):
      return __calc_one_moving_one_stat_parallel(point, velocity, line, offset, point_slope)
    
    point_yintr = point.y - point_slope * point.x
    line_yintr = line.calculate_y_intercept(offset)
    
    # m1x + b1 = m2x + b2
    # x = b2 - b1 / m1 - m2
    intr_x = (line_yintr - point_yintr) / (point_slope - line.slope)
    intr_y = point_slope * intr_x + point_yintr 
    intr_vec = vector2.Vector2(intr_x, intr_y)
    if not line2.Line2.contains_point(line, intr_vec, offset):
      return False, None
    
    point_to_intr = intr_vec - point
    vel_normal = velocity.normalize()
    ptintr_dot_veln = point_to_intr.dot(vel_normal)
    
    if ptintr_dot_veln < 0:
      return False, None 
    
    return True, ptintr_dot_veln
    
def calculate_one_moving_line_and_one_stationary_line(line1, offset1, velocity1, _line2, offset2):
    """
    Determine if the moving line will intersect the stationary line.
    
    Given two line segments, one moving and one not, determine if they will ever 
    intersect.
    
    :param line1: the geometry of the moving line 
    :type line1: :class:`pygorithm.geometry.line2.Line2`
    :param offset1: the starting location of the moving line
    :type offset1: :class:`pygorithm.geometry.vector2.Vector2`
    :param velocity1: the velocity of the moving line
    :type velocity1: :class:`pygorithm.geometry.vector2.Vector2`
    :param _line2: the geometry of the second line
    :type _line2: :class:`pygorithm.geometry.line2.Line2`
    :param offset2: the location of the second line
    :type offset2: :class:`pygorithm.geometry.vector2.Vector2`
    :returns: if the lines will ever intersect, distance until intersection
    :rtype: bool, :class:`numbers.Number` or None
    """
    return False, -1
    
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
    return -1

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