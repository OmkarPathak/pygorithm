import unittest
import math
import random
import sys

from pygorithm.geometry import (
    rect_broad_phase,
    vector2,
    axisall,
    line2,
    polygon2,
    rect2
    )

class TestCollisionDetection(unittest.TestCase):
    def setUp(self):
        # first pair of objects
        self.coord1 = rect_broad_phase.Coord(1, 1)
        self.coord2 = rect_broad_phase.Coord(6, 8)
        self.simpleRect1 = rect_broad_phase.SimpleRectangle(self.coord1, self.coord2)
        self.coord3 = rect_broad_phase.Coord(4, 0)
        self.coord4 = rect_broad_phase.Coord(7, 4)
        self.simpleRect2 = rect_broad_phase.SimpleRectangle(self.coord3, self.coord4)
        # second pair
        self.coord1 = rect_broad_phase.Coord(1, 1)
        self.coord2 = rect_broad_phase.Coord(2, 3)
        self.simpleRect3 = rect_broad_phase.SimpleRectangle(self.coord1, self.coord2)
        self.coord3 = rect_broad_phase.Coord(4, 3)
        self.coord4 = rect_broad_phase.Coord(7, 8)
        self.simpleRect4 = rect_broad_phase.SimpleRectangle(self.coord3, self.coord4)


class TestBroadPhase(TestCollisionDetection):
    def test_collision_detect(self):
        self.assertTrue(rect_broad_phase.broad_phase(self.simpleRect1, self.simpleRect2))
        self.assertFalse(rect_broad_phase.broad_phase(self.simpleRect3, self.simpleRect4))

class TestVector2(unittest.TestCase):
    def test_constructor(self):
        vec1 = vector2.Vector2(0, 5)
        self.assertEqual(0, vec1.x)
        self.assertEqual(5, vec1.y)
        
        vec2 = vector2.Vector2(x = 2, y = 3)
        self.assertEqual(2, vec2.x)
        self.assertEqual(3, vec2.y)
        
        vec3 = vector2.Vector2(vec2)
        self.assertEqual(2, vec3.x)
        self.assertEqual(3, vec3.y)
        
        vec4 = vector2.Vector2( (7, 11) )
        self.assertEqual(7,  vec4.x)
        self.assertEqual(11, vec4.y)
    
    def test_add(self):
        vec1 = vector2.Vector2(3, 5)
        vec2 = vector2.Vector2(2, 6)
        
        vec3 = vec1 + vec2
        self.assertEqual(5, vec3.x)
        self.assertEqual(11, vec3.y)
        
        vec4 = vec2 + vec1
        self.assertEqual(5, vec4.x)
        self.assertEqual(11, vec4.y)
        
        vec5 = vec3 + vec2
        self.assertEqual(7, vec5.x)
        self.assertEqual(17, vec5.y)
        
    def test_subtract(self):
        vec1 = vector2.Vector2(3, -5)
        vec2 = vector2.Vector2(2, 3)
        
        vec3 = vec1 - vec2
        self.assertEqual(1, vec3.x)
        self.assertEqual(-8, vec3.y)
        
        vec4 = vec2 - vec1
        self.assertEqual(-1, vec4.x)
        self.assertEqual(8, vec4.y)
        
    def test_mul_scale(self):
        vec1 = vector2.Vector2(3, 5)
        
        vec2 = vec1 * 2
        self.assertEqual(6, vec2.x)
        self.assertEqual(10, vec2.y)
        
        vec3 = vec1 * 0.5
        self.assertAlmostEqual(1.5, vec3.x)
        self.assertAlmostEqual(2.5, vec3.y)
        
    def test_mul_vector(self):
        vec1 = vector2.Vector2(2, 7)
        vec2 = vector2.Vector2(3, 5)
        
        with self.assertRaises(TypeError):
            vec3 = vec1 * vec2
        
    def test_rmul_scale(self):
        vec1 = vector2.Vector2(2, 3)
        
        vec2 = 2 * vec1
        self.assertEqual(4, vec2.x)
        self.assertEqual(6, vec2.y)
        
        vec3 = 0.5 * vec1
        self.assertEqual(1, vec3.x)
        self.assertAlmostEqual(1.5, vec3.y)
        
    def test_repr(self):
        vec = vector2.Vector2(7, 11)
        
        vec_repr = repr(vec)
        
        self.assertEqual('vector2(x=7, y=11)', vec_repr)
    
    def test_str(self):
        vec = vector2.Vector2(7, 11)
        
        vec_str = str(vec)
        self.assertEqual('<7, 11>', vec_str)
        
        vec2 = vector2.Vector2(0.70712356, 1)
        
        vec2_str = str(vec2)
        self.assertEqual('<0.707, 1>', vec2_str)
        
        vec3 = vector2.Vector2(1, 105.567812354)
        
        vec3_str = str(vec3)
        self.assertEqual('<1, 105.568>', vec3_str)
        
        vec4 = vector2.Vector2(1.5, 2.5)
        
        vec4_str = str(vec4)
        self.assertEqual('<1.5, 2.5>', vec4_str)
    
    def test_dot(self):
        vec1 = vector2.Vector2(3, 5)
        vec2 = vector2.Vector2(7, 11)
        
        dot_12 = vec1.dot(vec2)
        self.assertEqual(76, dot_12)
        
        dot_21 = vec2.dot(vec1)
        self.assertEqual(76, dot_21)
    
    def test_cross(self):
        vec1 = vector2.Vector2(3, 5)
        vec2 = vector2.Vector2(7, 11)
        
        cross_12 = vec1.cross(vec2)
        self.assertEqual(-2, cross_12)
        
        cross_21 = vec2.cross(vec1)
        self.assertEqual(2, cross_21)
    
    def test_rotate(self):
        vec1 = vector2.Vector2(1, 0)
        
        vec2 = vec1.rotate(math.pi * 0.25)
        self.assertAlmostEqual(0.70710678118, vec2.x)
        self.assertAlmostEqual(0.70710678118, vec2.y)
        
        vec3 = vec1.rotate(degrees = 45)
        self.assertAlmostEqual(0.70710678118, vec3.x)
        self.assertAlmostEqual(0.70710678118, vec3.y)
        
        vec4 = vec1.rotate(math.pi, vector2.Vector2(1, 1))
        self.assertAlmostEqual(1, vec4.x)
        self.assertAlmostEqual(2, vec4.y)
        
        vec5 = vec1.rotate(radians = math.pi, about = vector2.Vector2(1, 1))
        self.assertAlmostEqual(1, vec5.x)
        self.assertAlmostEqual(2, vec5.y)
        
        vec6 = vec1.rotate(degrees = 180, about = vector2.Vector2(1, 1))
        self.assertAlmostEqual(1, vec6.x)
        self.assertAlmostEqual(2, vec6.y)
        
        vec7 = vec1.rotate(vector2.Vector2(1, 1), degrees = 180)
        self.assertAlmostEqual(1, vec7.x)
        self.assertAlmostEqual(2, vec7.y)
        
    def test_normalize(self):
        vec1 = vector2.Vector2(2, 0)
        
        vec2 = vec1.normalize()
        self.assertEqual(2, vec1.x)
        self.assertEqual(0, vec1.y)
        self.assertEqual(1, vec2.x)
        self.assertEqual(0, vec2.y)
        
        vec3 = vec2.normalize()
        self.assertEqual(1, vec3.x)
        self.assertEqual(0, vec3.y)
        
        vec3.y = 1
        self.assertEqual(1, vec2.x)
        self.assertEqual(0, vec2.y)
        self.assertEqual(1, vec3.x)
        self.assertEqual(1, vec3.y)
    
    def test_magnitude_squared(self):
        vec1 = vector2.Vector2(5, 12)
        
        magn_sq = vec1.magnitude_squared()
        self.assertEqual(13*13, magn_sq)
        
        vec2 = vector2.Vector2(0, 0)
        
        magn_sq_2 = vec2.magnitude_squared()
        self.assertEqual(0, magn_sq_2)
        
        vec2.x = 2
        
        magn_sq_3 = vec2.magnitude_squared()
        self.assertEqual(4, magn_sq_3)
        
    def test_magnitude(self):
        vec1 = vector2.Vector2(3, 4)
        
        magn = vec1.magnitude()
        self.assertEqual(5, magn)
        
class TestLine2(unittest.TestCase):
    def setUp(self):
        random.seed()
        
        self.vec_origin = vector2.Vector2(0, 0)
        self.vec_1_1 = vector2.Vector2(1, 1)
        self.vec_2_1 = vector2.Vector2(2, 1)
        self.vec_1_2 = vector2.Vector2(1, 2)
        self.vec_3_4 = vector2.Vector2(3, 4)
        self.vec_neg_1_neg_1 = vector2.Vector2(-1, -1)
        
        self.line_origin_1_1 = line2.Line2(self.vec_origin, self.vec_1_1)
        self.line_1_1_3_4 = line2.Line2(self.vec_1_1, self.vec_3_4)
        self.line_1_1_2_1 = line2.Line2(self.vec_1_1, self.vec_2_1)
        self.line_1_1_1_2 = line2.Line2(self.vec_1_1, self.vec_1_2)
        
    def test_constructor(self):
        _line = self.line_origin_1_1
        
        self.assertIsNotNone(_line.start)
        self.assertIsNotNone(_line.end)
        
        self.assertEqual(0, _line.start.x)
        self.assertEqual(0, _line.start.y)
        self.assertEqual(1, _line.end.x)
        self.assertEqual(1, _line.end.y)
        
        with self.assertRaises(ValueError):
            _line2 = line2.Line2(self.vec_origin, self.vec_origin)
    
    def test_delta(self):
        self.assertEqual(1, self.line_origin_1_1.delta.x)
        self.assertEqual(1, self.line_origin_1_1.delta.y)
        self.assertEqual(2, self.line_1_1_3_4.delta.x)
        self.assertEqual(3, self.line_1_1_3_4.delta.y)
        
    def test_axis(self):
        self.assertAlmostEqual(0.70710678118, self.line_origin_1_1.axis.x)
        self.assertAlmostEqual(0.70710678118, self.line_origin_1_1.axis.y)
        self.assertAlmostEqual(0.55470019622, self.line_1_1_3_4.axis.x)
        self.assertAlmostEqual(0.83205029433, self.line_1_1_3_4.axis.y)
        self.assertEqual(1, self.line_1_1_2_1.axis.x)
        self.assertEqual(0, self.line_1_1_2_1.axis.y)
        self.assertEqual(0, self.line_1_1_1_2.axis.x)
        self.assertEqual(1, self.line_1_1_1_2.axis.y)
        
    def test_normal(self):
        self.assertAlmostEqual(-0.70710678118, self.line_origin_1_1.normal.x)
        self.assertAlmostEqual(0.70710678118,  self.line_origin_1_1.normal.y)
        self.assertAlmostEqual(-0.83205029433, self.line_1_1_3_4.normal.x)
        self.assertAlmostEqual(0.55470019622, self.line_1_1_3_4.normal.y)
        self.assertEqual(0, self.line_1_1_2_1.normal.x)
        self.assertEqual(1, self.line_1_1_2_1.normal.y)
        self.assertEqual(-1, self.line_1_1_1_2.normal.x)
        self.assertEqual(0, self.line_1_1_1_2.normal.y)
        
    def test_magnitude_squared(self):
        self.assertAlmostEqual(2, self.line_origin_1_1.magnitude_squared)
        self.assertAlmostEqual(13, self.line_1_1_3_4.magnitude_squared)
        self.assertEqual(1, self.line_1_1_2_1.magnitude_squared)
        self.assertEqual(1, self.line_1_1_1_2.magnitude_squared)
        
    def test_magnitude(self):
        self.assertAlmostEqual(1.41421356237, self.line_origin_1_1.magnitude)
        self.assertAlmostEqual(3.60555127546, self.line_1_1_3_4.magnitude)
        self.assertEqual(1, self.line_1_1_2_1.magnitude)
        self.assertEqual(1, self.line_1_1_1_2.magnitude)
        
    def test_line_boundaries_x(self): # min_x, min_y, max_x, max_y
        _line = line2.Line2(vector2.Vector2(-2, 3), vector2.Vector2(1, -1))
        self.assertEqual(-2, _line.min_x)
        self.assertEqual(1, _line.max_x)
        self.assertEqual(-1, _line.min_y)
        self.assertEqual(3, _line.max_y)
    
    def test_slope(self):
        self.assertEqual(1, self.line_origin_1_1.slope)
        self.assertAlmostEqual(1.5, self.line_1_1_3_4.slope)
        self.assertEqual(float('+inf'), self.line_1_1_1_2.slope)
        self.assertEqual(0, self.line_1_1_2_1.slope)
        
    def test_y_intercept(self):
        self.assertEqual(0, self.line_origin_1_1.y_intercept)
        self.assertAlmostEqual(-0.5, self.line_1_1_3_4.y_intercept)
        self.assertIsNone(self.line_1_1_1_2.y_intercept)
        self.assertEqual(1, self.line_1_1_2_1.y_intercept)
    
    def test_horizontal(self):
        self.assertFalse(self.line_origin_1_1.horizontal)
        self.assertFalse(self.line_1_1_3_4.horizontal)
        self.assertFalse(self.line_1_1_1_2.horizontal)
        self.assertTrue(self.line_1_1_2_1.horizontal)
    
    def test_vertical(self):
        self.assertFalse(self.line_origin_1_1.vertical)
        self.assertFalse(self.line_1_1_3_4.vertical)
        self.assertTrue(self.line_1_1_1_2.vertical)
        self.assertFalse(self.line_1_1_2_1.vertical)
    
    def test_repr(self):
        self.assertEqual('line2(start=vector2(x=1, y=1), end=vector2(x=3, y=4))', repr(self.line_1_1_3_4))
    
    def test_str(self):
        self.assertEqual('<1, 1> -> <3, 4>', str(self.line_1_1_3_4))
    
    def test_calculate_y_intercept(self):
        self.assertAlmostEqual(-1, self.line_1_1_3_4.calculate_y_intercept(self.vec_1_1))
    
    def test_are_parallel(self):
        self.assertFalse(line2.Line2.are_parallel(self.line_origin_1_1, self.line_1_1_3_4))
        
        _line = line2.Line2(vector2.Vector2(5, 4), vector2.Vector2(3, 1))
        self.assertTrue(line2.Line2.are_parallel(self.line_1_1_3_4, _line))
        
    def _find_intr_fuzzer(self, v1, v2, v3, v4, exp_touching, exp_overlap, exp_intr, number_fuzzes = 3):
        for i in range(number_fuzzes):
            offset1 = vector2.Vector2(random.uniform(-1000, 1000), random.uniform(-1000, 1000))
            offset2 = vector2.Vector2(random.uniform(-1000, 1000), random.uniform(-1000, 1000))
            
            _line1 = line2.Line2(v1 - offset1, v2 - offset1)
            _line2 = line2.Line2(v3 - offset2, v4 - offset2)
            
            help_msg = 'v1={}, v2={}, offset1={}\n_line1={}\nv3={}, v4={}, offset2={}\n_line2={}'.format(repr(v1), \
                repr(v2), repr(offset1), repr(_line1), repr(v3), repr(v4), repr(offset2), repr(_line2))
            
            touching, overlap, intr = line2.Line2.find_intersection(_line1, _line2, offset1, offset2)
            self.assertEqual(exp_touching, touching, help_msg)
            self.assertEqual(exp_overlap, overlap, help_msg)
            
            if exp_intr is None:
                self.assertIsNone(intr, help_msg)
            else:
                self.assertIsNotNone(intr, help_msg)
                
                if isinstance(exp_intr, vector2.Vector2):
                    self.assertIsInstance(intr, vector2.Vector2, help_msg)
                    
                    self.assertAlmostEqual(exp_intr.x, intr.x)
                    self.assertAlmostEqual(exp_intr.y, intr.y)
                else:
                    self.assertIsInstance(exp_intr, line2.Line2, help_msg)
                    self.assertIsInstance(intr, line2.Line2, help_msg)
                    
                    self.assertAlmostEqual(exp_intr.start.x, intr.start.x)
                    self.assertAlmostEqual(exp_intr.start.y, intr.start.y)
                    self.assertAlmostEqual(exp_intr.end.x, intr.end.x)
                    self.assertAlmostEqual(exp_intr.end.y, intr.end.y)
                
            
    def test_find_intersection_non_parallel_no_intersection(self):
        self._find_intr_fuzzer(vector2.Vector2(3, 4), vector2.Vector2(5, 6), 
                               vector2.Vector2(5, 4), vector2.Vector2(7, 3),
                               False, False, None)
   
    def test_find_intersection_parallel_no_intersection(self):
        self._find_intr_fuzzer(vector2.Vector2(1, 1), vector2.Vector2(3, 3),
                               vector2.Vector2(2, 1), vector2.Vector2(4, 3),
                               False, False, None)
        
    def test_find_intersection_non_parallel_intersect_at_edge(self):
        self._find_intr_fuzzer(vector2.Vector2(3, 4), vector2.Vector2(5, 6),
                               vector2.Vector2(1, 6), vector2.Vector2(5, 2),
                               True, False, vector2.Vector2(3, 4))
    
    def test_find_intersection_non_parallel_intersect_not_edge(self):
        self._find_intr_fuzzer(vector2.Vector2(3, 4), vector2.Vector2(5, 6),
                               vector2.Vector2(3.5, 7), vector2.Vector2(4.5, 4),
                               False, True, vector2.Vector2(4.125, 5.125))
   
    def test_find_intersection_parallel_intersect_at_edge(self):
        self._find_intr_fuzzer(vector2.Vector2(3, 4), vector2.Vector2(5, 6),
                               vector2.Vector2(5, 6), vector2.Vector2(7, 8),
                               True, False, vector2.Vector2(5, 6))
                               
    def test_find_intersection_parallel_intersect_overlap(self):
        self._find_intr_fuzzer(vector2.Vector2(3, 4), vector2.Vector2(5, 6),
                               vector2.Vector2(4, 5), vector2.Vector2(7, 8),
                               False, True, line2.Line2(vector2.Vector2(4, 5), vector2.Vector2(5, 6)))
       
    def test_find_intersection_parallel_overlap_compeletely(self):
        self._find_intr_fuzzer(vector2.Vector2(3, 4), vector2.Vector2(5, 6),
                               vector2.Vector2(2, 3), vector2.Vector2(7, 8),
                               False, True, line2.Line2(vector2.Vector2(3, 4), vector2.Vector2(5, 6)))
                               
    
class TestAxisAlignedLine(unittest.TestCase):
    def setUp(self):
        self.vec_1_1 = vector2.Vector2(1, 1)
        
    def test_constructor(self):
        _aal = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        
        self.assertIsNotNone(_aal.axis)
        self.assertIsNotNone(_aal.min)
        self.assertIsNotNone(_aal.max)
        
        self.assertEqual(1, _aal.axis.x)
        self.assertEqual(1, _aal.axis.y)
        self.assertEqual(0, _aal.min)
        self.assertEqual(1, _aal.max)
        
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, 1, 0)
        
        self.assertEqual(0, _aal.min)
        self.assertEqual(1, _aal.max)
    
    def test_intersects_false(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, 2, 3)
        
        touching, overlapping = axisall.AxisAlignedLine.intersects(_aal1, _aal2)
        self.assertFalse(touching)
        self.assertFalse(overlapping)
        
        touching, overlapping = axisall.AxisAlignedLine.intersects(_aal2, _aal1)
        self.assertFalse(touching)
        self.assertFalse(overlapping)
    
    def test_intersects_touching(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, 1, 2)
        
        touching, overlapping = axisall.AxisAlignedLine.intersects(_aal1, _aal2)
        self.assertTrue(touching)
        self.assertFalse(overlapping)
        
        touching, overlapping = axisall.AxisAlignedLine.intersects(_aal2, _aal1)
        self.assertTrue(touching)
        self.assertFalse(overlapping)
        
    def test_intersects_overlapping(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, -1, -3)
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, -2, 5)
        
        touching, overlapping = axisall.AxisAlignedLine.intersects(_aal1, _aal2)
        self.assertFalse(touching)
        self.assertTrue(overlapping)
        
        touching, overlapping = axisall.AxisAlignedLine.intersects(_aal2, _aal1)
        self.assertFalse(touching)
        self.assertTrue(overlapping)
        
        
    def test_find_intersection_false(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, 2, 3)
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal1, _aal2)
        self.assertFalse(touching)
        self.assertIsNone(mtv)
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal2, _aal1)
        self.assertFalse(touching)
        self.assertIsNone(mtv)
        
    def test_find_intersection_touching(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, 1, 2)
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal1, _aal2)
        self.assertTrue(touching)
        self.assertIsNotNone(mtv)
        self.assertIsNone(mtv[0])
        self.assertEqual(1, mtv[1])
        self.assertEqual(1, mtv[2])
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal2, _aal1)
        self.assertTrue(touching)
        self.assertIsNotNone(mtv)
        self.assertIsNone(mtv[0])
        self.assertEqual(1, mtv[1])
        self.assertEqual(1, mtv[2])
        
    def test_find_intersection_overlapping(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, -3, -1)
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, -2, 5)
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal1, _aal2)
        self.assertTrue(touching)
        self.assertEqual(-1, mtv[0])
        self.assertEqual(-2, mtv[1])
        self.assertEqual(-1, mtv[2])
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal2, _aal1)
        self.assertTrue(touching)
        self.assertEqual(1, mtv[0])
        self.assertEqual(-2, mtv[1])
        self.assertEqual(-1, mtv[2])
        
    def test_contains_point_false(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        
        outer, inner = axisall.AxisAlignedLine.contains_point(_aal1, -1)
        self.assertFalse(outer)
        self.assertFalse(inner)
        
        outer, inner = axisall.AxisAlignedLine.contains_point(_aal1, 1.5)
        self.assertFalse(outer)
        self.assertFalse(inner)
        
    def test_contains_point_outer(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        
        outer, inner = axisall.AxisAlignedLine.contains_point(_aal1, 0)
        self.assertTrue(outer)
        self.assertFalse(inner)
        
        outer, inner = axisall.AxisAlignedLine.contains_point(_aal1, 1)
        self.assertTrue(outer)
        self.assertFalse(inner)
        
    def test_contains_point_inner(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        
        outer, inner = axisall.AxisAlignedLine.contains_point(_aal1, 0.25)
        self.assertFalse(outer)
        self.assertTrue(inner)
        
        outer, inner = axisall.AxisAlignedLine.contains_point(_aal1, 0.75)
        self.assertFalse(outer)
        self.assertTrue(inner)
        
    def test_repr(self):
        _aal = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        
        exp = "AxisAlignedLine(axis=vector2(x=1, y=1), min=0, max=1)"
        self.assertEqual(exp, repr(_aal))
        
    def test_str(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, 0, 1)
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, 0.707123, 0.707123)
        
        exp1 = "axisall(along <1, 1> from 0 to 1)"
        exp2 = "axisall(along <1, 1> from 0.707 to 0.707)"
        
        self.assertEqual(exp1, str(_aal1))
        self.assertEqual(exp2, str(_aal2))

class TestPolygon(unittest.TestCase):
    def setUp(self):
        random.seed()
        
    def test_constructor_standard(self):
        poly = polygon2.Polygon2([ vector2.Vector2(0, 1), 
                                   vector2.Vector2(1, 1),
                                   vector2.Vector2(1, 0),
                                   vector2.Vector2(0, 0) ])
        
        self.assertEqual(4, len(poly.points))
        self.assertEqual(4, len(poly.lines))
        self.assertEqual(2, len(poly.normals))
        
        self.assertEqual(0, poly.points[0].x)
        self.assertEqual(1, poly.points[0].y)
        self.assertEqual(1, poly.points[1].x)
        self.assertEqual(1, poly.points[1].y)
        self.assertEqual(1, poly.points[2].x)
        self.assertEqual(0, poly.points[2].y)
        self.assertEqual(0, poly.points[3].x)
        self.assertEqual(0, poly.points[3].y)
        
        self.assertEqual(0, poly.lines[0].start.x)
        self.assertEqual(1, poly.lines[0].start.y)
        self.assertEqual(1, poly.lines[0].end.x)
        self.assertEqual(1, poly.lines[0].end.y)
        self.assertEqual(1, poly.lines[1].start.x)
        self.assertEqual(1, poly.lines[1].start.y)
        self.assertEqual(1, poly.lines[1].end.x)
        self.assertEqual(0, poly.lines[1].end.y)
        self.assertEqual(1, poly.lines[2].start.x)
        self.assertEqual(0, poly.lines[2].start.y)
        self.assertEqual(0, poly.lines[2].end.x)
        self.assertEqual(0, poly.lines[2].end.y)
        self.assertEqual(0, poly.lines[3].start.x)
        self.assertEqual(0, poly.lines[3].start.y)
        self.assertEqual(0, poly.lines[3].end.x)
        self.assertEqual(1, poly.lines[3].end.y)
        
        self.assertIsNotNone(next((vec for vec in poly.normals if vec.y == 0), None))
        self.assertIsNotNone(next((vec for vec in poly.normals if vec.x == 0), None))
        
        self.assertAlmostEqual(0.5, poly.center.x)
        self.assertAlmostEqual(0.5, poly.center.y)
        
        poly2 = polygon2.Polygon2([ (0, 1), (1, 1), (1, 0), (0, 0) ])
        
        self.assertEqual(4, len(poly2.points))
        self.assertEqual(4, len(poly2.lines))
        self.assertEqual(2, len(poly2.normals))
        
        with self.assertRaises(StopIteration):
            next(i for i in range(4) if poly.points[i].x != poly2.points[i].x or poly.points[i].y != poly2.points[i].y)
    
    def test_constructor_repeated(self):
        with self.assertRaises(ValueError):
            poly = polygon2.Polygon2([ (0, 1), (1, 1), (1, 0), (0, 0), (0, 1) ])
    
    def test_constructor_two_points(self):
        with self.assertRaises(ValueError):
            poly = polygon2.Polygon2([ (0, 1), (1, 1) ])
        
    def test_constructor_not_convex(self):
        with self.assertRaises(ValueError):
            poly = polygon2.Polygon2([ (0, 1), (0.5, 0.8), (1, 1), (1, 0), (0, 0) ])
    
    def test_constructor_not_clockwise(self):
        with self.assertRaises(ValueError):
            poly = polygon2.Polygon2([ (0, 0), (1, 0), (1, 1), (0, 1) ])
    
    def test_from_regular(self):
        diamond = polygon2.Polygon2.from_regular(4, 1.414213562373095)
        
        self.assertAlmostEqual(2, diamond.points[0].x)
        self.assertAlmostEqual(1, diamond.points[0].y)
        self.assertAlmostEqual(1, diamond.points[1].x)
        self.assertAlmostEqual(0, diamond.points[1].y)
        self.assertAlmostEqual(0, diamond.points[2].x)
        self.assertAlmostEqual(1, diamond.points[2].y)
        self.assertAlmostEqual(1, diamond.points[3].x)
        self.assertAlmostEqual(2, diamond.points[3].y)
        
        diamond_shifted = polygon2.Polygon2.from_regular(4, 1.414213562373095, center = vector2.Vector2(0, 0))
        
        for i in range(4):
            self.assertAlmostEqual(diamond.points[i].x, diamond_shifted.points[i].x + 1)
            self.assertAlmostEqual(diamond.points[i].y, diamond_shifted.points[i].y + 1)
        
        square = polygon2.Polygon2.from_regular(4, 1, math.pi / 4)
        
        self.assertAlmostEqual(1, square.points[0].x)
        self.assertAlmostEqual(1, square.points[0].y)
        self.assertAlmostEqual(1, square.points[1].x)
        self.assertAlmostEqual(0, square.points[1].y)
        self.assertAlmostEqual(0, square.points[2].x)
        self.assertAlmostEqual(0, square.points[2].y)
        self.assertAlmostEqual(0, square.points[3].x)
        self.assertAlmostEqual(1, square.points[3].y)
        
        square2 = polygon2.Polygon2.from_regular(4, 1, start_degs = 45)
        
        for i in range(4):
            self.assertAlmostEqual(square.points[i].x, square2.points[i].x)
            self.assertAlmostEqual(square.points[i].y, square2.points[i].y)
            
    def test_from_regular_center(self):
        for i in range(3, 13):
            _poly = polygon2.Polygon2.from_regular(i, 1)
            
            foundx0 = False
            foundy0 = False
            for p in _poly.points:
                if math.isclose(p.x, 0, abs_tol=1e-07):
                    foundx0 = True
                    if foundy0:
                        break
                if math.isclose(p.y, 0, abs_tol=1e-07):
                    foundy0 = True
                    if foundx0:
                        break
            helpmsg = "\ni={}\nfoundx0={}, foundy0={}, center={}\nrepr={}\n\nstr={}".format(i, foundx0, foundy0, _poly.center, repr(_poly), str(_poly))
            self.assertTrue(foundx0, msg=helpmsg)
            self.assertTrue(foundy0, msg=helpmsg)
        
        
    def test_from_rotated(self):
        # isos triangle 
        # weighted total = (0 + 1 + 2, 0 + 1 + 1) = (3, 2)
        # center = (1, 2/3)
        triangle = polygon2.Polygon2([ (0, 0), (1, 1), (2, 1) ])
        
        triangle_rot = polygon2.Polygon2.from_rotated(triangle, math.pi / 4)
        
        # example of how to calculate:
        # shift so you rotate about origin (subtract center)
        # (0, 0) - (1, 2/3) = (-1, -2/3)
        # rotate 45 degrees clockwise = (-1 * cos(45) - (-2/3) * sin(45), (-2/3) * cos(45) + (-1) * sin(45)) = (-0.23570226039, -1.17851130198)
        # shift back (add center): (0.76429773961, -0.51184463531)
        self.assertAlmostEqual(0.76429773961, triangle_rot.points[0].x, msg='original={}\n\nrotated={}'.format(triangle, triangle_rot))
        self.assertAlmostEqual(-0.51184463531, triangle_rot.points[0].y, msg='original={}\n\nrotated={}'.format(triangle, triangle_rot))
        self.assertAlmostEqual(0.76429773960, triangle_rot.points[1].x, msg='original={}\n\nrotated={}'.format(triangle, triangle_rot))
        self.assertAlmostEqual(0.90236892706, triangle_rot.points[1].y, msg='original={}\n\nrotated={}'.format(triangle, triangle_rot))
        self.assertAlmostEqual(1.47140452079, triangle_rot.points[2].x, msg='original={}\n\nrotated={}'.format(triangle, triangle_rot))
        self.assertAlmostEqual(1.60947570825, triangle_rot.points[2].y, msg='original={}\n\nrotated={}'.format(triangle, triangle_rot))
        self.assertAlmostEqual(1, triangle_rot.center.x, msg='original={}\n\nrotated={}'.format(triangle, triangle_rot))
        self.assertAlmostEqual(0.66666666667, triangle_rot.center.y, msg='original={}\n\nrotated={}'.format(triangle, triangle_rot))
        
        
    def test_area(self):
        # https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php helpful for checking
        poly = polygon2.Polygon2.from_regular(4, 1)
        self.assertAlmostEqual(1, poly.area)
        
        poly2 = polygon2.Polygon2.from_regular(4, 2)
        self.assertAlmostEqual(4, poly2.area)
        
        poly3 = polygon2.Polygon2.from_regular(8, 3.7)
        self.assertAlmostEqual(66.1011673, poly3.area, msg=str(poly3))
        
        poly4 = polygon2.Polygon2([ (0, 0), (1, 1), (2, 1) ])
        self.assertAlmostEqual(0.5, poly4.area)
        
        poly5 = polygon2.Polygon2([ (0, 0), (1, 1), (2, 1), (1, -0.25) ])
        self.assertAlmostEqual(1.25, poly5.area)
    
    def _proj_onto_axis_fuzzer(self, points, axis, expected):
        for i in range(3):
            offset = vector2.Vector2(random.uniform(-1000, 1000), random.uniform(-1000, 1000))
            
            new_points = []
            for pt in points:
                new_points.append(pt - offset)
            
            new_poly = polygon2.Polygon2(new_points)
            
            proj = polygon2.Polygon2.project_onto_axis(new_poly, offset, axis)
            
            help_msg = "points={}, axis={}, expected={} proj={} [offset = {}, new_points={}]".format(points, axis, expected, proj, offset, new_points)
            self.assertAlmostEqual(expected.min, proj.min, help_msg)
            self.assertAlmostEqual(expected.max, proj.max, help_msg)
            
            
    def test_project_onto_axis(self):
        poly = polygon2.Polygon2.from_regular(4, 1, math.pi / 4)
        
        _axis = vector2.Vector2(0, 1)
        self._proj_onto_axis_fuzzer(poly.points, _axis, axisall.AxisAlignedLine(_axis, 0, 1))
        
        _axis2 = vector2.Vector2(1, 0)
        self._proj_onto_axis_fuzzer(poly.points, _axis2, axisall.AxisAlignedLine(_axis2, 0, 1))
        
        _axis3 = vector2.Vector2(0.70710678118, 0.70710678118)
        self._proj_onto_axis_fuzzer(poly.points, _axis3, axisall.AxisAlignedLine(_axis3, 0, 1.41421356236))
        
    def _contains_point_fuzzer(self, points, point, expected_edge, expected_contains):
        for i in range(3):
            offset = vector2.Vector2(random.uniform(-1000, 1000), random.uniform(-1000, 1000))
            
            new_points = []
            for pt in points:
                new_points.append(pt - offset)
            
            new_poly = polygon2.Polygon2(new_points)
            
            edge, cont = polygon2.Polygon2.contains_point(new_poly, offset, point)
            
            help_msg = "points={}, point={}, expected_edge={}, expected_contains={}, edge={}, cont={}".format(points, point, expected_edge, expected_contains, edge, cont)
            self.assertEqual(expected_edge, edge, msg=help_msg)
            self.assertEqual(expected_contains, cont, msg=help_msg)
            
    def test_contains_point_false(self):
        poly = polygon2.Polygon2([ (1, 1), (2, 3), (4, 0) ])
        
        self._contains_point_fuzzer(poly.points, vector2.Vector2(1, 2), False, False)
        self._contains_point_fuzzer(poly.points, vector2.Vector2(4, 2), False, False)
        self._contains_point_fuzzer(poly.points, vector2.Vector2(3, 0), False, False)
        
    def test_contains_point_edge(self):
        poly = polygon2.Polygon2([ (2, 3), (3, 5), (5, 4), (3, 2) ])
        
        self._contains_point_fuzzer(poly.points, vector2.Vector2(4, 3), True, False)
        self._contains_point_fuzzer(poly.points, vector2.Vector2(2.5, 2.5), True, False)
        self._contains_point_fuzzer(poly.points, vector2.Vector2(4, 4.5), True, False)
        
    def test_contains_point_contained(self):
        poly = polygon2.Polygon2([ (-3, -6), (-2, -3), (2, -2), (0, -5) ])
        
        self._contains_point_fuzzer(poly.points, vector2.Vector2(-1, -4), False, True)
        self._contains_point_fuzzer(poly.points, vector2.Vector2(-1, -5), False, True)
        self._contains_point_fuzzer(poly.points, vector2.Vector2(1, -3), False, True)
    
    def _find_intersection_fuzzer(self, points1, points2, exp_touching, exp_overlap, exp_mtv):
        if type(points1) != list:
            points1 = points1.points
        if type(points2) != list:
            points2 = points2.points
        
        for i in range(3):
            offset1 = vector2.Vector2(random.uniform(-1000, 1000), random.uniform(-1000, 1000))
            offset2 = vector2.Vector2(random.uniform(-1000, 1000), random.uniform(-1000, 1000))
            
            new_points1 = []
            for pt in points1:
                new_points1.append(pt - offset1)
            
            new_points2 = []
            for pt in points2:
                new_points2.append(pt - offset2)
            
            new_poly1 = polygon2.Polygon2(new_points1)
            new_poly2 = polygon2.Polygon2(new_points2)
            
            touch, overlap, mtv = polygon2.Polygon2.find_intersection(new_poly1, new_poly2, offset1, offset2, True)
            _invtouch, _invoverlap, _invmtv = polygon2.Polygon2.find_intersection(new_poly2, new_poly1, offset2, offset1, True)
            
            help_msg = "\n\npoints1={}, points2={}, offset1={}, offset2={}\n\nexp_touching={}, " \
                       "exp_overlap={}, exp_mtv={}\n\ntouch={}, overlap={}, mtv={}\n\n" \
                       "_invtouch={}, _invoverlap={}, _invmtv={}\n\n" \
                       "orig_poly1={}\n\n" \
                       "orig_poly2={}\n\n".format(points1, points2, offset1, 
                       offset2, exp_touching, exp_overlap, exp_mtv, touch, overlap, mtv, 
                       _invtouch, _invoverlap, _invmtv, polygon2.Polygon2(points1),
                       polygon2.Polygon2(points2))
            self.assertEqual(exp_touching, touch, msg=help_msg)
            self.assertEqual(exp_overlap, overlap, msg=help_msg)
            self.assertEqual(exp_touching, _invtouch, msg=help_msg)
            self.assertEqual(exp_overlap, _invoverlap, msg=help_msg)
            
            if exp_mtv is not None:
                self.assertIsNotNone(mtv, msg=help_msg)
                exp_mult_x = exp_mtv[0] * exp_mtv[1].x
                exp_mult_y = exp_mtv[0] * exp_mtv[1].y
                mult_x = mtv[0] * mtv[1].x
                mult_y = mtv[0] * mtv[1].y
                self.assertAlmostEqual(exp_mult_x, mult_x, msg=help_msg)
                self.assertAlmostEqual(exp_mult_y, mult_y, msg=help_msg)
                
                self.assertIsNotNone(_invmtv, msg=help_msg)
                inv_mult_x = _invmtv[0] * _invmtv[1].x
                inv_mult_y = _invmtv[0] * _invmtv[1].y
                self.assertAlmostEqual(-exp_mult_x, inv_mult_x, msg=help_msg)
                self.assertAlmostEqual(-exp_mult_y, inv_mult_y, msg=help_msg)
            else:
                self.assertIsNone(mtv, msg=help_msg)
                self.assertIsNone(_invmtv, msg=help_msg)
                
            _touch, _overlap, _mtv = polygon2.Polygon2.find_intersection(new_poly1, new_poly2, offset1, offset2, False)
            
            self.assertEqual(exp_touching, _touch, msg=help_msg)
            self.assertEqual(exp_overlap, _overlap, msg=help_msg)
            self.assertIsNone(_mtv, msg=help_msg)
            
    def test_find_intersection_false(self):
        poly1 = polygon2.Polygon2([ (0, 1), (0, 3), (5, 3), (5, 1) ])
        poly2 = polygon2.Polygon2([ (3, 4), (2, 6), (7, 5) ])
        poly3 = polygon2.Polygon2([ (6, 2), (9, 3), (9, 1) ])
        
        self._find_intersection_fuzzer(poly1, poly2, False, False, None)
        self._find_intersection_fuzzer(poly1, poly3, False, False, None)
        self._find_intersection_fuzzer(poly2, poly3, False, False, None)
        
    def test_find_intersection_touching(self):
        poly1 = polygon2.Polygon2([ (3, 3), (3, 6), (7, 5), (5, 3) ])
        poly2 = polygon2.Polygon2([ (4, 3), (8, 2), (6, -1) ])
        poly3 = polygon2.Polygon2([ (5, 5.5), (1, 6.5), (3, 7), (7, 6) ])
        
        self._find_intersection_fuzzer(poly1, poly2, True, False, None)
        self._find_intersection_fuzzer(poly1, poly3, True, False, None)
        
    def test_find_intersection_overlapping(self):
        poly1 = polygon2.Polygon2([ (2, 1), (4, 3), (6, 3), (6, 1) ])
        poly2 = polygon2.Polygon2([ (5, 2.5), (5, 5), (7, 5) ])
        poly3 = polygon2.Polygon2([ (1, 3), (3, 3), (3, 1), (1, 1) ])
        
        self._find_intersection_fuzzer(poly1, poly2, False, True, (0.5, vector2.Vector2(0, -1)))
        self._find_intersection_fuzzer(poly1, poly3, False, True, (0.70710678118, vector2.Vector2(0.70710678118, -0.70710678118)))

class TestRect2(unittest.TestCase):
    def test_constructor_defaults(self):
        _rect = rect2.Rect2(1, 1)
        
        self.assertIsNotNone(_rect)
        self.assertEqual(1, _rect.width)
        self.assertEqual(1, _rect.height)
        self.assertIsNotNone(_rect.mincorner)
        self.assertEqual(0, _rect.mincorner.x)
        self.assertEqual(0, _rect.mincorner.y)
    
    def test_constructor_specified(self):
        _rect = rect2.Rect2(1, 3, vector2.Vector2(-1, -1))
        
        self.assertEqual(1, _rect.width)
        self.assertEqual(3, _rect.height)
        self.assertIsNotNone(_rect.mincorner)
        self.assertEqual(-1, _rect.mincorner.x)
        self.assertEqual(-1, _rect.mincorner.y)
        
    def test_constructor_errors(self):
        with self.assertRaises(ValueError):
            _rect = rect2.Rect2(-1, 1)
            
        with self.assertRaises(ValueError):
            _rect = rect2.Rect2(1, -1)
        
        with self.assertRaises(ValueError):
            _rect = rect2.Rect2(0, 1)
        
        with self.assertRaises(ValueError):
            _rect = rect2.Rect2(5, 0)
        
        with self.assertRaises(ValueError):
            _rect = rect2.Rect2(0, 0)
                
        with self.assertRaises(ValueError):
            _rect = rect2.Rect2(-3, -3)
    
    def test_width(self):
        _rect = rect2.Rect2(1, 1)
        
        self.assertEqual(1, _rect.width)
        
        _rect.width = 3
        
        self.assertEqual(3, _rect.width)
        
        with self.assertRaises(ValueError):
            _rect.width = 0
        
        _rect = rect2.Rect2(1, 1)
        with self.assertRaises(ValueError):
            _rect.width = -3
    
    def test_height(self):
        _rect = rect2.Rect2(7, 11)
        
        self.assertEqual(11, _rect.height)
        
        _rect.height = 5
        
        self.assertEqual(5, _rect.height)
        
        with self.assertRaises(ValueError):
            _rect.height = 0
            
        _rect = rect2.Rect2(1, 1)
        with self.assertRaises(ValueError):
            _rect.height = -15
        
        _rect = rect2.Rect2(1, 1)
        with self.assertRaises(ValueError):
            _rect.height = 1e-09
        
    def test_polygon_unshifted(self):
        _rect = rect2.Rect2(1, 1)
        
        self.assertIsNotNone(_rect.polygon)
        self.assertEqual(0, _rect.polygon.points[0].x)
        self.assertEqual(0, _rect.polygon.points[0].y)
        self.assertEqual(0, _rect.polygon.points[1].x)
        self.assertEqual(1, _rect.polygon.points[1].y)
        self.assertEqual(1, _rect.polygon.points[2].x)
        self.assertEqual(1, _rect.polygon.points[2].y)
        self.assertEqual(1, _rect.polygon.points[3].x)
        self.assertEqual(0, _rect.polygon.points[3].y)
        self.assertEqual(4, len(_rect.polygon.points))
    
    def test_polygon_shifted(self):
        _rect = rect2.Rect2(1, 1, vector2.Vector2(1, 1))
        
        self.assertIsNotNone(_rect.polygon)
        self.assertEqual(0, _rect.polygon.points[0].x)
        self.assertEqual(0, _rect.polygon.points[0].y)
        self.assertEqual(0, _rect.polygon.points[1].x)
        self.assertEqual(1, _rect.polygon.points[1].y)
        self.assertEqual(1, _rect.polygon.points[2].x)
        self.assertEqual(1, _rect.polygon.points[2].y)
        self.assertEqual(1, _rect.polygon.points[3].x)
        self.assertEqual(0, _rect.polygon.points[3].y)
        self.assertEqual(4, len(_rect.polygon.points))
    
    def test_polygon_resized(self):
        _rect = rect2.Rect2(1, 1)
        
        self.assertIsNotNone(_rect.polygon)
        self.assertEqual(0, _rect.polygon.points[0].x)
        self.assertEqual(0, _rect.polygon.points[0].y)
        self.assertEqual(0, _rect.polygon.points[1].x)
        self.assertEqual(1, _rect.polygon.points[1].y)
        self.assertEqual(1, _rect.polygon.points[2].x)
        self.assertEqual(1, _rect.polygon.points[2].y)
        self.assertEqual(1, _rect.polygon.points[3].x)
        self.assertEqual(0, _rect.polygon.points[3].y)
        self.assertEqual(4, len(_rect.polygon.points))
        
        _rect.width = 3
        
        self.assertIsNotNone(_rect.polygon)
        self.assertEqual(0, _rect.polygon.points[0].x)
        self.assertEqual(0, _rect.polygon.points[0].y)
        self.assertEqual(0, _rect.polygon.points[1].x)
        self.assertEqual(1, _rect.polygon.points[1].y)
        self.assertEqual(3, _rect.polygon.points[2].x)
        self.assertEqual(1, _rect.polygon.points[2].y)
        self.assertEqual(3, _rect.polygon.points[3].x)
        self.assertEqual(0, _rect.polygon.points[3].y)
        self.assertEqual(4, len(_rect.polygon.points))
        
        _rect.height = 0.5
        
        self.assertIsNotNone(_rect.polygon)
        self.assertEqual(0, _rect.polygon.points[0].x)
        self.assertEqual(0, _rect.polygon.points[0].y)
        self.assertEqual(0, _rect.polygon.points[1].x)
        self.assertEqual(0.5, _rect.polygon.points[1].y)
        self.assertEqual(3, _rect.polygon.points[2].x)
        self.assertEqual(0.5, _rect.polygon.points[2].y)
        self.assertEqual(3, _rect.polygon.points[3].x)
        self.assertEqual(0, _rect.polygon.points[3].y)
        self.assertEqual(4, len(_rect.polygon.points))
        
    def test_area(self):
        _rect = rect2.Rect2(1, 1)
        
        self.assertEqual(1, _rect.area)
        
        _rect.width = 3
        
        self.assertEqual(3, _rect.area)
        
        _rect.height = 7
        
        self.assertEqual(21, _rect.area)
    
    def test_project_onto_axis_horizontal_unshifted(self):
        _rect = rect2.Rect2(3, 7)
        
        proj = rect2.Rect2.project_onto_axis(_rect, vector2.Vector2(1, 0))
        
        self.assertEqual(0, proj.min)
        self.assertEqual(3, proj.max)
        self.assertEqual(1, proj.axis.x)
        self.assertEqual(0, proj.axis.y)
        
        proj2 = rect2.Rect2.project_onto_axis(_rect, vector2.Vector2(-1, 0))
        
        self.assertEqual(-3, proj2.min)
        self.assertEqual(0, proj2.max)
        self.assertEqual(-1, proj2.axis.x)
        self.assertEqual(0, proj2.axis.y)
    
    def test_project_onto_axis_vertical_unshifted(self):
        _rect = rect2.Rect2(5, 11)
        
        proj = rect2.Rect2.project_onto_axis(_rect, vector2.Vector2(0, 1))
        
        self.assertEqual(0, proj.min)
        self.assertEqual(11, proj.max)
        self.assertEqual(0, proj.axis.x)
        self.assertEqual(1, proj.axis.y)
        
        proj2 = rect2.Rect2.project_onto_axis(_rect, vector2.Vector2(0, -1))
        
        self.assertEqual(-11, proj2.min)
        self.assertEqual(0, proj2.max)
        self.assertEqual(0, proj2.axis.x)
        self.assertEqual(-1, proj2.axis.y)
        
    def test_project_onto_axis_diagonal_unshifted(self):
        _rect = rect2.Rect2(1, 3)
        _axis = vector2.Vector2(1, 1).normalize()
        
        proj = rect2.Rect2.project_onto_axis(_rect, _axis)
        
        self.assertAlmostEqual(0, proj.min)
        self.assertAlmostEqual(2.82842712472, proj.max)
        self.assertAlmostEqual(_axis.x, proj.axis.x)
        self.assertAlmostEqual(_axis.y, proj.axis.y)
        
        _axis2 = vector2.Vector2(-1, -1).normalize()
        proj2 = rect2.Rect2.project_onto_axis(_rect, _axis2)
        
        self.assertAlmostEqual(-2.82842712472, proj2.min)
        self.assertAlmostEqual(0, proj2.max)
        self.assertAlmostEqual(_axis2.x, proj2.axis.x)
        self.assertAlmostEqual(_axis2.y, proj2.axis.y)
        
        
    def test_project_onto_axis_horizontal_shifted(self):
        _rect = rect2.Rect2(3, 2, vector2.Vector2(2, 2))
        
        proj = rect2.Rect2.project_onto_axis(_rect, vector2.Vector2(1, 0))
        
        self.assertEqual(2, proj.min)
        self.assertEqual(5, proj.max)
        self.assertEqual(1, proj.axis.x)
        self.assertEqual(0, proj.axis.y)
        
        proj2 = rect2.Rect2.project_onto_axis(_rect, vector2.Vector2(-1, 0))
        
        self.assertEqual(-5, proj2.min)
        self.assertEqual(-2, proj2.max)
        self.assertEqual(-1, proj2.axis.x)
        self.assertEqual(0,  proj2.axis.y)
        
        _rect2 = rect2.Rect2(3, 2, vector2.Vector2(-1, 2))
        
        proj3 = rect2.Rect2.project_onto_axis(_rect2, vector2.Vector2(-1, 0))
        
        self.assertEqual(-2, proj3.min)
        self.assertEqual(1,  proj3.max)
        self.assertEqual(-1, proj3.axis.x)
        self.assertEqual(0,  proj3.axis.y)
    
    def test_project_onto_axis_vertical_shifted(self):
        _rect = rect2.Rect2(4, 7, vector2.Vector2(1, 3))
        
        proj = rect2.Rect2.project_onto_axis(_rect, vector2.Vector2(0, 1))
        
        self.assertEqual(3,  proj.min)
        self.assertEqual(10, proj.max)
        self.assertEqual(0,  proj.axis.x)
        self.assertEqual(1,  proj.axis.y)
        
        proj2 = rect2.Rect2.project_onto_axis(_rect, vector2.Vector2(0, -1))
        
        self.assertEqual(-10, proj2.min)
        self.assertEqual(-3,  proj2.max)
        self.assertEqual(0,   proj2.axis.x)
        self.assertEqual(-1,  proj2.axis.y)
        
        _rect2 = rect2.Rect2(4, 7, vector2.Vector2(1, -2))
        
        proj3 = rect2.Rect2.project_onto_axis(_rect2, vector2.Vector2(0, -1))
        
        self.assertEqual(-5, proj3.min)
        self.assertEqual(2,  proj3.max)
        self.assertEqual(0,  proj3.axis.x)
        self.assertEqual(-1, proj3.axis.y)
        
    def test_project_onto_axis_diagonal_shifted(self):
        _rect = rect2.Rect2(3, 5, vector2.Vector2(2, 2))
        _axis = vector2.Vector2(1, 1).normalize()
        
        proj = rect2.Rect2.project_onto_axis(_rect, _axis)
        
        self.assertAlmostEqual(2.82842712, proj.min)
        self.assertAlmostEqual(8.48528137, proj.max)
        self.assertAlmostEqual(_axis.x,    proj.axis.x)
        self.assertAlmostEqual(_axis.y,    proj.axis.y)
        
        _axis2 = vector2.Vector2(-1, -1).normalize()
        proj2 = rect2.Rect2.project_onto_axis(_rect, _axis2)
        
        self.assertAlmostEqual(-8.48528137, proj2.min)
        self.assertAlmostEqual(-2.82842712, proj2.max)
        self.assertAlmostEqual(_axis2.x,    proj2.axis.x)
        self.assertAlmostEqual(_axis2.y,    proj2.axis.y)
        
        _rect2 = rect2.Rect2(3, 5, vector2.Vector2(-1, -2))
        proj3 = rect2.Rect2.project_onto_axis(_rect2, _axis2)
        
        self.assertAlmostEqual(-3.53553391, proj3.min)
        self.assertAlmostEqual(2.12132034,  proj3.max)
        self.assertAlmostEqual(_axis2.x,    proj3.axis.x)
        self.assertAlmostEqual(_axis2.y,    proj3.axis.y)
        
    def test_contains_point_false(self):
        _rect = rect2.Rect2(1, 2, vector2.Vector2(2, 2))
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(0, 0))
        self.assertFalse(edge)
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(4, 2))
        self.assertFalse(edge)
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(2, 5))
        self.assertFalse(edge)
        self.assertFalse(inner)
    
    def test_contains_point_edge(self):
        _rect = rect2.Rect2(3, 2, vector2.Vector2(-2, -2))
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(-2, -2))
        self.assertTrue(edge, msg="mincorner")
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(1, -2))
        self.assertTrue(edge, msg="corner")
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(1, 0))
        self.assertTrue(edge, msg="maxcorner")
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(-2, 0))
        self.assertTrue(edge, msg="corner")
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(-1, -2))
        self.assertTrue(edge, msg="y-min side")
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(0, 0))
        self.assertTrue(edge, msg="y-max side")
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(-2, -1))
        self.assertTrue(edge, msg="x-min side")
        self.assertFalse(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(1, -0.5))
        self.assertTrue(edge, msg="x-max side, floating")
        self.assertFalse(inner)
    
    def test_contains_point_contained(self):
        _rect = rect2.Rect2(4, 5, vector2.Vector2(3, 3))
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(5, 6))
        self.assertFalse(edge)
        self.assertTrue(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(5.5, 6.5))
        self.assertFalse(edge)
        self.assertTrue(inner)
        
        edge, inner = rect2.Rect2.contains_point(_rect, vector2.Vector2(4.5, 7.5))
        self.assertFalse(edge)
        self.assertTrue(inner)
    
    def _create_help_msg(*args):
        # this function produced links for rects or polygons using _create_link
        self = args[0]
        allpts = []
        result = ""
        i = 1
        while i < len(args):
            a = args[i]
            result += "\n\n"
            is_rect = type(a) == rect2.Rect2
            
            if is_rect:
                result += "rect: {}\n".format(str(a))
                pts = list(p + a.mincorner for p in a.polygon.points)
                allpts += pts
                result += polygon2.Polygon2._create_link(pts)
                i += 1
            else:
                offset = args[i + 1]
                result += "polygon: {} at {}\n".format(str(a), str(offset))
                pts = list(p + offset for p in a.points)
                allpts += pts
                result += polygon2.Polygon2._create_link(pts)
                i += 2
        result += "\n\ntogether: {}".format(polygon2.Polygon2._create_link(allpts))
        return result
    
    def test_find_intersection_rect_poly_false(self):
        _rect = rect2.Rect2(3, 2, vector2.Vector2(2, 1))
        _poly = polygon2.Polygon2.from_regular(5, 1)
        _offset = vector2.Vector2(0, 0.5)
        visualize = self._create_help_msg(_rect, _poly, _offset)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect, _poly, _offset)
        
        self.assertFalse(touching, msg=visualize)
        self.assertFalse(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_find_intersection_rect_poly_edge(self):
        _rect = rect2.Rect2(2, 1, vector2.Vector2(0, 2.118033988749895))
        _poly = polygon2.Polygon2.from_regular(5, 1)
        _offset = vector2.Vector2(0, 0.5)
        visualize = self._create_help_msg(_rect, _poly, _offset)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect, _poly, _offset)
        
        self.assertTrue(touching, msg=visualize)
        self.assertFalse(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_find_intersection_rect_poly_mtv(self):
        _rect = rect2.Rect2(1, 3, vector2.Vector2(0.5, -0.5))
        _poly = polygon2.Polygon2.from_regular(5, 1)
        _offset = vector2.Vector2(1, 0)
        visualize = self._create_help_msg(_rect, _poly, _offset)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect, _poly, _offset)
        
        self.assertFalse(touching, msg=visualize)
        self.assertTrue(overlapping, msg=visualize)
        self.assertIsNotNone(mtv, msg=visualize)
        self.assertAlmostEqual(-0.5, mtv[0] * mtv[1].x)
        self.assertAlmostEqual(0, mtv[0] * mtv[1].y)
    
    def test_find_intersection_rect_poly_coll_findmtv_false(self):
        _rect = rect2.Rect2(1, 3, vector2.Vector2(0.5, -0.5))
        _poly = polygon2.Polygon2.from_regular(5, 1)
        _offset = vector2.Vector2(1, 0)
        visualize = self._create_help_msg(_rect, _poly, _offset)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect, _poly, _offset, find_mtv=False)
        
        self.assertFalse(touching, msg=visualize)
        self.assertTrue(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_find_intersection_poly_rect_false(self):
        _rect = rect2.Rect2(3, 2, vector2.Vector2(2, 1))
        _poly = polygon2.Polygon2.from_regular(5, 1)
        _offset = vector2.Vector2(0, 0.5)
        visualize = self._create_help_msg(_poly, _offset, _rect)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_poly, _offset, _rect)
        
        self.assertFalse(touching, msg=visualize)
        self.assertFalse(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_find_intersection_poly_rect_edge(self):
        _rect = rect2.Rect2(2, 1, vector2.Vector2(0, 2.118033988749895))
        _poly = polygon2.Polygon2.from_regular(5, 1)
        _offset = vector2.Vector2(0, 0.5)
        visualize = self._create_help_msg(_poly, _offset, _rect)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_poly, _offset, _rect)
        
        self.assertTrue(touching, msg=visualize)
        self.assertFalse(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_find_intersection_poly_rect_mtv(self):
        _rect = rect2.Rect2(1, 3, vector2.Vector2(0.5, -0.5))
        _poly = polygon2.Polygon2.from_regular(5, 1)
        _offset = vector2.Vector2(1, 0)
        visualize = self._create_help_msg(_poly, _offset, _rect)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_poly, _offset, _rect)
        
        self.assertFalse(touching, msg=visualize)
        self.assertTrue(overlapping, msg=visualize)
        self.assertIsNotNone(mtv, msg=visualize)
        self.assertAlmostEqual(0.5, mtv[0] * mtv[1].x)
        self.assertAlmostEqual(0, mtv[0] * mtv[1].y)
    
    def test_find_intersection_poly_rect_coll_findmtv_false(self):
        _rect = rect2.Rect2(1, 3, vector2.Vector2(0.5, -0.5))
        _poly = polygon2.Polygon2.from_regular(5, 1)
        _offset = vector2.Vector2(1, 0)
        visualize = self._create_help_msg(_poly, _offset, _rect)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_poly, _offset, _rect, find_mtv=False)
        
        self.assertFalse(touching, msg=visualize)
        self.assertTrue(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_find_intersection_rect_rect_false(self):
        _rect1 = rect2.Rect2(2, 3, vector2.Vector2(0.5, 0.5))
        _rect2 = rect2.Rect2(1, 1, vector2.Vector2(-1, 0))
        visualize = self._create_help_msg(_rect1, _rect2)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect1, _rect2)
        
        self.assertFalse(touching, msg=visualize)
        self.assertFalse(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_find_intersection_rect_rect_edge(self):
        _rect1 = rect2.Rect2(3, 4, vector2.Vector2(1, 0.70723))
        _rect2 = rect2.Rect2(1, 1, vector2.Vector2(2, 4.70723))
        visualize = self._create_help_msg(_rect1, _rect2)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect1, _rect2)
        
        self.assertTrue(touching, msg=visualize)
        self.assertFalse(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_find_intersection_rect_rect_mtv(self):
        _rect1 = rect2.Rect2(3, 5, vector2.Vector2(-2, -6))
        _rect2 = rect2.Rect2(2, 1, vector2.Vector2(0, -3))
        visualize = self._create_help_msg(_rect1, _rect2)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect1, _rect2)
        
        self.assertFalse(touching, msg=visualize)
        self.assertTrue(overlapping, msg=visualize)
        self.assertIsNotNone(mtv, msg=visualize)
        self.assertEqual(-1, mtv[0] * mtv[1].x, msg="touching={}, overlapping={}, mtv={}\n\n{}".format(touching, overlapping, mtv, visualize))
        self.assertEqual(0, mtv[0] * mtv[1].y, msg=visualize)
        
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect2, _rect1)
        
        self.assertFalse(touching, msg=visualize)
        self.assertTrue(overlapping, msg=visualize)
        self.assertIsNotNone(mtv, msg=visualize)
        self.assertEqual(1, mtv[0] * mtv[1].x)
        self.assertEqual(0, mtv[0] * mtv[1].y)
        
    
    def test_find_intersection_rect_rect_coll_findmtv_false(self):
        _rect1 = rect2.Rect2(3, 5, vector2.Vector2(-2, -6))
        _rect2 = rect2.Rect2(2, 1, vector2.Vector2(0, -3))
        visualize = self._create_help_msg(_rect1, _rect2)
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect1, _rect2, find_mtv=False)
        
        self.assertFalse(touching, msg=visualize)
        self.assertTrue(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
        
        touching, overlapping, mtv = rect2.Rect2.find_intersection(_rect2, _rect1, find_mtv=False)
        
        self.assertFalse(touching, msg=visualize)
        self.assertTrue(overlapping, msg=visualize)
        self.assertIsNone(mtv, msg=visualize)
    
    def test_repr(self):
        unit_square = rect2.Rect2(1, 1, vector2.Vector2(3, 4))
        
        self.assertEqual("rect2(width=1, height=1, mincorner=vector2(x=3, y=4))", repr(unit_square))
         
    def test_str(self):
        unit_square = rect2.Rect2(1, 1, vector2.Vector2(3, 4))
        ugly_rect = rect2.Rect2(0.7071234, 0.7079876, vector2.Vector2(0.56789123, 0.876543))
        
        self.assertEqual("rect(1x1 at <3, 4>)", str(unit_square))
        self.assertEqual("rect(0.707x0.708 at <0.568, 0.877>)", str(ugly_rect))

class TestExtrapolatedIntersection(unittest.TestCase):
    def test_one_moving_one_stationary_no_intr(self):
        pass
    def test_one_moving_one_stationary_touching(self):
        pass
    def test_one_moving_one_stationary_intr_at_start(self):
        pass
    def test_one_moving_one_stationary_intr_later(self):
        pass
    
    def test_one_moving_one_stationary_distlimit_no_intr(self):
        pass
    def test_one_moving_one_stationary_distlimit_touching(self):
        pass
    def test_one_moving_one_stationary_distlimit_intr_at_start(self):
        pass
    def test_one_moving_one_stationary_distlimit_intr_later(self):
        pass
    def test_one_moving_one_stationary_distlimit_touch_at_limit(self):
        pass
    def test_one_moving_one_stationary_distlimit_intr_after_limit(self):
    
    def test_one_moving_one_stationary_along_path_no_intr(self):
        pass
    def test_one_moving_one_stationary_along_path_touching(self):
        pass
    def test_one_moving_one_stationary_along_path_intr_at_start(self):
        pass
    def test_one_moving_one_stationary_along_path_intr_later(self):
        pass
    def test_one_moving_one_stationary_distlimit_touch_at_end(self):
        pass
    def test_one_moving_one_stationary_distlimit_intr_after_end(self):
    
    def test_one_moving_many_stationary_no_intr(self):
        pass
    def test_one_moving_many_stationary_touching(self):
        pass
    def test_one_moving_many_stationary_intr_at_start(self):
        pass
    def test_one_moving_many_stationary_intr_later(self):
        pass
    
    def test_one_moving_many_stationary_distlimit_no_intr(self):
        pass
    def test_one_moving_many_stationary_distlimit_touching(self):
        pass
    def test_one_moving_many_stationary_distlimit_intr_at_start(self):
        pass
    def test_one_moving_many_stationary_distlimit_intr_later(self):
        pass
    def test_one_moving_many_stationary_distlimit_touch_at_limit(self):
        pass
    def test_one_moving_many_stationary_distlimit_intr_after_limit(self):
        pass
    
    def test_one_moving_many_stationary_along_path_no_intr(self):
        pass
    def test_one_moving_many_stationary_along_path_touching(self):
        pass
    def test_one_moving_many_stationary_along_path_intr_at_start(self):
        pass
    def test_one_moving_many_stationary_along_path_intr_later(self):
        pass
    def test_one_moving_many_stationary_along_path_touch_at_limit(self):
        pass
    def test_one_moving_many_stationary_along_path_intr_after_limit(self):
        pass
        
    def test_two_moving_no_intr(self):
        pass
    def test_two_moving_touching_miss(self):
        pass
    def test_two_moving_touching_miss_diff_vel(self):
        pass
    def test_two_moving_intr_ones_start_but_later(self):
        pass
    def test_two_moving_intr_at_start(self):
        pass
    def test_two_moving_intr_later(self):
        pass
    def test_two_moving_intr_later_diff_vel(self):
        pass

if __name__ == '__main__':
    unittest.main()