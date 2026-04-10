def temp(total: int, interval: int, values: list[int]):
    window = sum(values[:interval])
    means = [int(window / interval)]

    for index in range(1, total - interval + 1):
        window = window - values[index - 1] + values[index + interval - 1]
        means.append(int(window / interval))

    print(f"{min(means)} {max(means)}")


################################################### Teste


temp(
    7,
    4,
    [8, 20, 30, 50, 40, 20, -10],
)
temp(4, 2, [-5, -12, 0, 6])
temp(7, 4, [35, -35, 5, 100, 100, 50, 50])


################################################### Final

total, interval = list(map(int, input().split()))
values = []
for _ in range(total):
    values.append(int(input()))

temp(total, interval, values)
