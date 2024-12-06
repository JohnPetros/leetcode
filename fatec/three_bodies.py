from math import sqrt
from itertools import combinations


def calculate_distance(coordinates_1: list[int], coordinates_2: list[int]):
    return sqrt(
        (int(coordinates_1[0]) - int(coordinates_2[0])) ** 2
        + (int(coordinates_1[1]) - int(coordinates_2[1])) ** 2
        + (int(coordinates_1[2]) - int(coordinates_2[2])) ** 2
    )


def three_bodies(bodies_count: int, bodies_coordinates: list[str]):
    bodies = []
    count = 0
    for index in range(0, bodies_count * 3, 3):
        bodies.append((count, bodies_coordinates[index : index + 3]))
        count += 1

    bodies_total_distances = []

    for bodies_combination in list(combinations(bodies, 3)):
        bodies_total_distances.append(
            (
                bodies_combination,
                sum(
                    [
                        calculate_distance(coordinates_1[1], coordinates_2[1])
                        - int(coordinates_1[1][2])
                        - int(coordinates_2[1][2])
                        for coordinates_1, coordinates_2 in list(
                            combinations(bodies_combination, 2)
                        )
                    ],
                ),
            )
        )

    bodies_total_distances.sort(
        key=lambda bodies_total_distances: bodies_total_distances[1]
    )
    indexes = [index for index in bodies_total_distances[0][0]]
    print(" ".join([str(index[0]) for index in indexes]))


bodies_count = "4"
bodies_coordinates = "1 1 2 7 1 3 8 10 1 2 5 1".split()

three_bodies(int(bodies_count), bodies_coordinates)
