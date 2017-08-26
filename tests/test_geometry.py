import unittest
import math
import random

from pygorithm.geometry import (
    rect_broad_phase,
    vector2,
    axisall,
    line2,
    polygon2
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
        
        self.assertEqual('vector2(x=7, y=1)', vec_repr)
    
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
        
    def test_rotate(self):
        vec1 = vector2.Vector2(1, 0)
        
        vec2 = vec1.rotate(math.pi * 0.25)
        self.assertAlmostEqual(0.70710678118, vec2.x)
        self.assertAlmostEqual(0.70710678118, vec2.y)
        
        vec3 = vec1.rotate(degrees = 45)
        self.assertAlmostEqual(0.70710678118, vec3.x)
        self.assertAlmostEqual(0.70710678118, vec3.y)
        
        vec4 = vec1.rotate(math.pi, vector2.Vector2(1, 1))
        self.assertEqual(1, vec4.x)
        self.assertEqual(2, vec4.y)
        
        vec5 = vec1.rotate(radians = math.pi, about = vector2.Vector2(1, 1))
        self.assertEqual(1, vec5.x)
        self.assertEqual(2, vec5.y)
        
        vec6 = vec1.rotate(degrees = 180, about = vector2.Vector2(1, 1))
        self.assertEqual(1, vec6.x)
        self.assertEqual(2, vec6.y)
        
        vec7 = vec1.rotate(vector2.Vector2(1, 1), degrees = 180)
        self.assertEqual(1, vec7.x)
        self.assertEqual(2, vec7.y)
        
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
        self.assertEqual(0, self.line_1_1_1_2.slope)
        self.assertEqual(float('+inf'), self.line_1_1_2_1.slope)
        
    def test_y_intercept(self):
        self.assertEqual(0, self.line_origin_1_1.y_intercept)
        self.assertAlmostEqual(-0.5, self.line_1_1_3_4.y_intercept)
        self.assertTrue(math.isnan(self.line_1_1_1_2.y_intercept))
        self.assertEqul(1, self.line_1_1_2_1.y_intercept)
    
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
        self.assertAlmostEqual(0.66666666667, self.line_1_1_3_4.calculate_y_intercept(self.vec_1_1))
    
    def test_are_parallel(self):
        self.assertFalse(line2.Line2.are_parallel(self.line_origin_1_1, self.line_1_1_3_4))
        
        _line = line2.Line2(vector2.Vector2(5, 4), vector2.Vector2(3, 1))
        self.assertTrue(line2.Line2.are_parallel(self.line_1_1_3_4, _line))
        
    @staticmethod
    def _find_intr_fuzzer(v1, v2, v3, v4, exp_touching, exp_overlap, exp_intr, number_fuzzes = 3):
        for i in range(number_fuzzes):
            offset1 = vector2.Vector2(random.randrange(-1000, 1000, 0.01), random.randrange(-1000, 1000, 0.01))
            offset2 = vector2.Vector2(random.randrange(-1000, 1000, 0.01), random.randrange(-1000, 1000, 0.01))
            
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
                    self.assertAlmostEqual(exp_intr.end.y, itnr.end.y)
                
            
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
        
        self.assertEqual(1, _aal.axis.start.x)
        self.assertEqual(1, _aal.axis.start.y)
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
        self.assertIsNone(mtv)
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal2, _aal1)
        self.assertTrue(touching)
        self.assertIsNone(mtv)
        
    def test_find_intersection_overlapping(self):
        _aal1 = axisall.AxisAlignedLine(self.vec_1_1, -3, -1)
        _aal2 = axisall.AxisAlignedLine(self.vec_1_1, -2, 5)
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal1, _aal2)
        self.assertFalse(touching)
        self.assertEquals(-1, mtv)
        
        touching, mtv = axisall.AxisAlignedLine.find_intersection(_aal2, _aal1)
        self.assertFalse(touching)
        self.assertEquals(1, mtv)
        
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
        

if __name__ == '__main__':
    unittest.main()