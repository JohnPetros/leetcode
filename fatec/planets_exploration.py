import math


def planets_exploration(planet_coordinates, ships_count, ships_coordinates: list[int]):
    def calculate_distance(coordiantes_1, coordiantes_2):
        return math.sqrt(
            (int(coordiantes_1[0]) - int(coordiantes_2[0])) ** 2
            + (int(coordiantes_1[1]) - int(coordiantes_2[1])) ** 2
            + (int(coordiantes_1[2]) - int(coordiantes_2[2])) ** 2
        )

    ships = []
    count = 0
    for index in range(0, ships_count * 3, 3):
        ships.append((count, ships_coordinates[index : index + 3]))
        count += 1

    ships_distances = [
        (index, calculate_distance(ship_coordinates, planet_coordinates))
        for index, ship_coordinates in ships
    ]

    ships_distances.sort(key=lambda ship: (ship[1], ship[0]))

    print(" ".join([str(index) for index, _ in ships_distances]))


# data = "5 5 5 2 1 1 1 3 3 3".split()
# data = "2 1 0 5 1 2 8 6 3 8 7 3 1 2 2 4 9 6 0".split()
# data = "2 0 0 4 1 1 2 2 2 3 1 0 0 1 2 3".split()
# data = "10 35 29 3 12 34 75 32 49 01 12 12 12".split()
data = "2 2 2 2 1 1 1 3 3 3".split()

# planets_exploration(data[:3], int(data[3]), data[4:])
