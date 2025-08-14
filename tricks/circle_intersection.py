from math import sqrt, pi, acos


def circle_intersection(ray1, ray2, distance):
    # Caso um círculo está dentro do outro
    if distance <= abs(ray1 - ray2):
        return pi * min(ray1, ray2) ** 2

    # Caso sem interseção
    if distance >= ray1 + ray2:
        return 0

    part1 = ray1**2 * acos((distance**2 + ray1**2 - ray2**2) / (2 * distance * ray1))
    part2 = ray2**2 * acos((distance**2 + ray2**2 - ray1**2) / (2 * distance * ray2))
    part3 = 0.5 * sqrt(
        (-distance + ray1 + ray2)
        * (distance + ray1 - ray2)
        * (distance - ray1 + ray2)
        * (distance + ray1 + ray2)
    )

    return part1 + part2 - part3
