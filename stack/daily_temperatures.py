def daily_temperatures(temperatures: list[int]) -> list[int]:
    days = [0] * len(temperatures)
    stack = list()

    for index in range(len(temperatures)):
        while len(stack) and temperatures[index] > stack[-1][0]:
            _, index_of_temperature = stack.pop()
            days[index_of_temperature] = index - index_of_temperature
        stack.append((temperatures[index], index))

    return days


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_temperatures([30, 40, 50, 60]))
print(daily_temperatures([30, 60, 90]))
