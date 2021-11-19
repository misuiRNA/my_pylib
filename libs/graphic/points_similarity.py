"""
计算两个点集之间的相似度
相似度：经过平移、缩放、旋转后，两个点集的重合程度
限制：两个点集的点个数相等，并且每个点集的点个数不小于4
"""

# dependency: opencv-python==3.4.5.20

from typing import List
import cv2
import numpy as np


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def dist(self, oth):
        oth: Point = oth
        dist = ((self._x - oth._x) ** 2 + (self._y - oth._y) ** 2) ** (1 / 2)
        return dist

    def similar(self, oth):
        oth: Point = oth
        score = 1 / (self.dist(oth) ** 2 + 1)
        return score

    @classmethod
    def inst(cls, point_tuple):
        return cls(point_tuple[0], point_tuple[1])

    @staticmethod
    def similarity(point_list_left: List, point_list_right: List):
        if len(point_list_left) < 4 or len(point_list_right) < 4:
            raise Exception("too points less to compare")
        left: List[Point] = point_list_left
        right: List[Point] = point_list_right

        matrix = Point._trans_matrix(right[:4], left[:4])
        new_right = Point._transform(right, matrix)
        score = Point._flat_similarity(new_right, left)
        return score

    @staticmethod
    def _trans_matrix(src_point_list: List, target_point_list: List):
        if len(src_point_list) != 4 or len(target_point_list) != 4:
            raise Exception("invalid parameter(s)")
        src_point_list: List[Point] = src_point_list
        target_point_list: List[Point] = target_point_list
        src = [[p._x, p._y] for p in src_point_list]
        target = [[p._x, p._y] for p in target_point_list]
        matrix = cv2.getPerspectiveTransform(np.array(src, dtype=np.float32), np.array(target, dtype=np.float32))
        return matrix

    @staticmethod
    def _transform(point_list: List, matrix):
        point_list: List[Point] = point_list
        src_list = [[p._x, p._y] for p in point_list]
        pts = np.float32(src_list).reshape(-1, 1, 2)
        # pts = np.array(src_list, dtype=np.float32)
        new_pts = cv2.perspectiveTransform(pts, matrix)

        new_point_list = []
        for item in new_pts:
            new_point_list.append(Point.inst(item[0]))
        return new_point_list

    @staticmethod
    def _flat_similarity(point_list_left: List, point_list_right: List):
        left: List[Point] = point_list_left
        right: List[Point] = point_list_right
        total_score = 0
        for pl, pr in zip(left, right):
            total_score += pl.similar(pr)
        score = total_score / len(right)
        return score

    def __repr__(self):
        return f"({int(self._x)}, {int(self._y)})"

