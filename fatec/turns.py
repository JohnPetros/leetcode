from math import sqrt, ceil


def turns(
    step: int, start_coordinates: tuple[int, int], end_coordinates: tuple[int, int]
):

    distance = sqrt(
        (start_coordinates[0] - end_coordinates[0]) ** 2
        + (start_coordinates[1] - end_coordinates[1])
    )
    print(ceil(ceil(distance) / step))


# step = int(input())
# start_coordinates = tuple(map(int, input().split()))
# end_coordinates = tuple(map(int, input().split()))

turns(1, (5, 0), (0, 0))
turns(5, (5, 0), (0, 0))
turns(5, (10, 10), (0, 0))
