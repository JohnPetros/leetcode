def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda interval: interval[0])
    merged_intervals = [intervals[0]]

    for index in range(1, len(intervals)):
        if intervals[index][0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = [
                merged_intervals[-1][0],
                max(intervals[index][1], merged_intervals[-1][1]),
            ]
        else:
            merged_intervals.append(intervals[index])

    return merged_intervals


print(merge_intervals([[1, 4], [3, 7], [8, 10], [9, 12]]))
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge_intervals([[1, 4], [4, 5]]))
print(merge_intervals([[1, 4], [0, 4]]))
