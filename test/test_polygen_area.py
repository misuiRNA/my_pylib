import itertools
import unittest

from libs.graphic.utils import polygon_area


class TestGraphicArea(unittest.TestCase):
    four_points_list = list(itertools.permutations([[-1, 0], [3, 4], [8, 7], [5, 0]], 4))

    def test_one_point_should_0(self):
        area = polygon_area([[0, 0]])
        self.assertEqual(0, area)

    def test_tow_points_should_0(self):
        area = polygon_area([[0, 0], [0, 4]])
        self.assertEqual(0, area)

    def test_three_points_should_valid(self):
        area = polygon_area([[0, 0], [0, 4], [3, 0]])
        self.assertEqual(6, area)

    def test_permutations_points_should_success(self):
        for point_list in self.four_points_list:
            area = polygon_area(point_list)
            self.assertEqual(25, area)
