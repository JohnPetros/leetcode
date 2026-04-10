TESTE = False


def agenda(total, intervals):
    count = 1
    sorted_intervals = sorted(intervals, key=lambda interval: interval[1])
    last_end_time = sorted_intervals[0][1]

    for index in range(1, total):
        interval_start_time, interval_end_time = sorted_intervals[index]
        if interval_start_time >= last_end_time:
            count += 1
            last_end_time = interval_end_time

    print(count)


if TESTE:
    total = 3
    intervals = [[1, 3], [2, 5], [4, 6]]
    total = 5
    intervals = [
        [1, 2],
        [5, 6],
        [3, 4],
        [5, 6],
        [1, 2],
    ]

    agenda(total, intervals)
else:
    try:
        while True:
            total = int(input())
            intervals = []

            for _ in range(total):
                a, b = map(int, input().split())
                intervals.append((a, b))

            agenda(total, intervals)
    except EOFError:
        pass
