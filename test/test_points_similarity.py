import unittest

from libs.graphic.points_similarity import Point


class TestPointsSimilarity(unittest.TestCase):
    refer_points = [(0, 0), (1, 5), (3, 3), (5, 0), (5, 8), (9, 1)]

    def test_same_points_should_similar(self):
        same_points = [(0, 0), (1, 5), (3, 3), (5, 0), (5, 8), (9, 1)]
        score = self.do_compare(same_points)
        self.assertEqual(1, score)

    def test_similar_moved_points_should_similar(self):
        similar_moved_points = [(0, 0), (2, 10), (6, 6), (10, 0), (10, 16), (18, 2)]
        score = self.do_compare(similar_moved_points)
        self.assertEqual(1, score)

    def test_similar_points_should_similar(self):
        similar_points = [(1, 1), (3, 11), (7, 7), (11, 1), (11, 17), (19, 3)]
        score = self.do_compare(similar_points)
        self.assertEqual(1, score)

    def test_one_diff_points_should_not_similar(self):
        one_diff_points = [(0, 0), (1, 5), (3, 3), (5, 0), (5, 8), (5, 27)]
        score = self.do_compare(one_diff_points)
        self.assertLess(score, 1)

    def test_two_diff_points_should_not_similar(self):
        two_diff_points = [(0, 0), (1, 5), (3, 3), (6, 2), (5, 8), (5, 27)]
        score = self.do_compare(two_diff_points)
        self.assertLess(score, 1)

    def test_three_diff_points_should_not_similar(self):
        three_diff_points = [(0, 0), (1, 5), (10, 7), (6, 2), (5, 8), (5, 27)]
        score = self.do_compare(three_diff_points)
        self.assertLess(score, 1)

    def test_three_diff_moved_points_should_not_similar(self):
        three_diff_moved_points = [(2, 2), (3, 7), (12, 9), (8, 4), (7, 10), (7, 29)]
        score = self.do_compare(three_diff_moved_points)
        self.assertLess(score, 1)

    def do_compare(self, point_list):
        point_list_left = sorted([Point.inst(p) for p in self.refer_points], key=lambda p: (p._x, p._y))
        point_list_right = sorted([Point.inst(p) for p in point_list], key=lambda p: (p._x, p._y))
        score = Point.similarity(point_list_left, point_list_right)
        return score
