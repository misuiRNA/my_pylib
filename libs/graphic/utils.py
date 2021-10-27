from . import BiVector


def polygon_area(point_list):
    """计算凸多边形的面积，顶点无顺序要求"""
    vec_list = []
    for index in range(1, len(point_list)):
        vec_list.append(BiVector(point_list[0], point_list[index]))
    vec_list.sort(key=lambda vec: vec.angle, reverse=True)

    vec_couple_list = []
    for index in range(0, len(vec_list)):
        vec_couple_list.append((vec_list[index - 1], vec_list[index]))
    vec_couple_list.sort(key=lambda cup: (cup[0].angle - cup[1].angle + 360) % 360)

    s = sum([cup[0].multi(cup[1]) for cup in vec_couple_list[:len(vec_couple_list) - 1]])
    return abs(s) / 2.0
