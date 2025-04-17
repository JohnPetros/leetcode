def car_fleet(target: int, positions: list[int], speeds: list[int]) -> int:
    stack = list()
    cars = list(zip(positions, speeds))
    cars.sort(reverse=True, key=lambda x: x[0])
    cars_times = [(target - car[0]) / car[1] for car in cars]
    stack.append(cars_times[0])

    for car_time in cars_times[1:]:
        stack.append(car_time)
        if len(stack) > 1 and car_time <= stack[-2]:
            stack.pop()

    return len(stack)


# print(car_fleet(10, [3, 5, 7], [3, 2, 1]))
print(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
# print(car_fleet(10, [3], [3]))
# print(car_fleet(100, [0, 2, 4], [4, 2, 1]))
# print(car_fleet(10, [0, 4, 2], [2, 1, 3]))
print(car_fleet(12, [4, 0, 5, 3, 1, 2], [6, 10, 9, 6, 7, 2]))
