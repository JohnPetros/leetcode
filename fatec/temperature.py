def temperature(interval, temperatures):
    averages = []

    for index in range(len(temperatures)):
        window = temperatures[index : index + interval]
        if len(window) != interval:
            break

        averages.append(sum(window))

    caculated_averages = list(map(lambda average: int(average / interval), averages))
    print(f"{min(caculated_averages)} {max(caculated_averages)}")


# interval = 4
# temperatures_count = 2
# temperatures = []

# for _ in range(temperatures_count):
#   temperatures.append()


temperature(4, [8, 20, 30, 50, 40, 20, -10])
temperature(2, [-5, -12, 0, 6])
temperature(
    4,
    [
        35,
        -35,
        5,
        100,
        100,
        50,
        50,
    ],
)
