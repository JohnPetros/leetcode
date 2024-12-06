def schedule(ranges: list[int]):
    ranges = list(set(ranges))
    ranges.sort(key=lambda range: range[0])
    valid_ranges = []

    for _, end in ranges:
        next_range = list(filter(lambda range: range[0] > end, ranges))
        if len(next_range) and next_range[0] not in valid_ranges:
            valid_ranges.append(next_range[0])

    return len(valid_ranges) + 1


print(schedule([(1, 3), (2, 5), (4, 6)]))
# print(schedule([(1, 2), (5, 6), (3, 4), (5, 6), (1, 2)]))
