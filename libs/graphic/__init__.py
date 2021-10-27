import math


class BiVector:

    def __init__(self, tail, head):
        self._x = head[0] - tail[0]
        self._y = head[1] - tail[1]
        self._angle_to_x = self._calculate_angle()

    @property
    def angle(self):
        return self._angle_to_x

    def multi(self, oth):
        oth: BiVector = oth
        res = self._x * oth._y - self._y * oth._x
        return res

    def _calculate_angle(self):
        anc = math.asin(self._y / ((self._x ** 2 + self._y ** 2) ** 0.5)) / (math.pi * 180)
        if self._x < 0:
            anc = 180 - anc
        anc = (anc + 360) % 360
        return anc
