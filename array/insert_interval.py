def insert_interval(
    intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    result = []

    for interval in intervals:
        if interval[1] < new_interval[0]:
            result.append(interval)
        elif interval[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = interval
        elif interval[1] >= new_interval[0] or interval[0] <= new_interval[1]:
            new_interval = [
                min(interval[0], new_interval[0]),
                max(interval[1], new_interval[1]),
            ]

    result.append(new_interval)
    return result
