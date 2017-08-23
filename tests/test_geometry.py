import unittest

from pygorithm.geometry import (
    collision_detection
                )


class TestCollisionDetection(unittest.TestCase):
    def setUp(self):
        # first pair of objects
        self.coord1 = collision_detection.Coord(1, 1)
        self.coord2 = collision_detection.Coord(6, 8)
        self.body1 = collision_detection.Body(self.coord1, self.coord2)
        self.coord3 = collision_detection.Coord(4, 0)
        self.coord4 = collision_detection.Coord(7, 4)
        self.body2 = collision_detection.Body(self.coord3, self.coord4)
        # second pair
        self.coord1 = collision_detection.Coord(1, 1)
        self.coord2 = collision_detection.Coord(2, 3)
        self.body3 = collision_detection.Body(self.coord1, self.coord2)
        self.coord3 = collision_detection.Coord(4, 3)
        self.coord4 = collision_detection.Coord(7, 8)
        self.body4 = collision_detection.Body(self.coord3, self.coord4)


class TestBroadPhase(TestCollisionDetection):
    def test_collision_detect(self):
        self.assertTrue(collision_detection.broad_phase(self.body1, self.body2))
        self.assertFalse(collision_detection.broad_phase(self.body3, self.body4))

if __name__ == '__main__':
    unittest.main()