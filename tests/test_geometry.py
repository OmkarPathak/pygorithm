import unittest

from pygorithm.geometry import (
    rect_broad_phase
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

if __name__ == '__main__':
    unittest.main()