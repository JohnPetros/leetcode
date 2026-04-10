import math


def calculate_distance(target: list[int], ship: list[int]):
    dx = ship[0] - target[0]
    dy = ship[1] - target[2]
    dz = ship[2] - target[2]

    return math.sqrt(dx**2 + dy**2 + dz**2)


def naves(planet, ships):
    sorted_ships = sorted(ships, key=lambda ship: calculate_distance(planet, ship[1]))

    print(" ".join([str(ship[0]) for ship in sorted_ships]))


################################################### Teste

# naves(
#     [5, 5, 5],
#     [
#         (0, [1, 1, 1]),
#         (1, [3, 3, 3]),
#     ],
# )
# naves(
#     [2, 1, 0],
#     [
#         (0, [1, 2, 8]),
#         (1, [6, 3, 8]),
#         (2, [7, 3, 1]),
#         (3, [2, 2, 4]),
#         (4, [9, 6, 0]),
#     ],
# )
# naves(
#     [2, 0, 0],
#     [
#         (0, [1, 1, 2]),
#         (1, [2, 2, 3]),
#         (2, [1, 0, 0]),
#         (3, [1, 2, 3]),
#     ],
# )
# naves(
#     [10, 35, 29],
#     [
#         (0, [12, 34, 75]),
#         (1, [32, 49, 1]),
#         (2, [12, 12, 12]),
#     ],
# )
# naves(
#     [2, 2, 2],
#     [
#         (0, [1, 1, 1]),
#         (1, [3, 3, 3]),
#     ],
# )

################################################### Final

try:
    while True:
        inputs = list(map(int, input().split()))
        planet = [inputs[0], inputs[1], inputs[2]]
        total_ships = inputs[3]

        ships = []
        for i in range(total_ships):
            coords = inputs[4 + i * 3 : 4 + i * 3 + 3]
            ships.append((i, coords))

        naves(planet, ships)

except EOFError:
    pass
