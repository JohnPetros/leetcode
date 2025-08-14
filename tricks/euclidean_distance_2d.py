from math import sqrt


def euclidean_distance_2d(point1: tuple[int], point2: tuple[int]) -> int:
    x1, y1 = point1
    x2, y2 = point2
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
