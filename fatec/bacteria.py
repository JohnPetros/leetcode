from math import sqrt


def bacteria(circles: list[tuple[int, int, int]]):
    bacterias = [[circle, 0] for circle in circles]

    def contains_circle(circle1, circle2):
        distance = sqrt((circle1[0] - circle2[0]) ** 2 + (circle1[1] - circle2[1]) ** 2)
        return distance + circle2[2] <= circle1[2]

    for index, first_circle in enumerate(circles):
        for second_circle in circles:
            if first_circle != second_circle and contains_circle(
                first_circle, second_circle
            ):
                bacterias[index][1] += 1

    bacterias.sort(key=lambda bacteria: bacteria[1], reverse=True)
    print(bacterias[0][1])
    print(f"{bacterias[0][0][0]} {bacterias[0][0][1]}")


# circles = []

# for _ in range(int(input())):
#     circles.append(list(map(int, input().split())))


bacteria([(-3, 2, 5), (-4, -1, 1), (-1, 5, 3)])
