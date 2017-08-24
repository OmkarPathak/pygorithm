import unittest
import math

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
        

if __name__ == '__main__':
    unittest.main()