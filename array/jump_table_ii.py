def jump_table_ii(numbers: list[int]) -> int:
    n = len(numbers)

    if n == 1:
        return 0

    jumps = 0
    farthest_jump = 0
    current_end = 0

    for index in range(n - 1):
        farthest_jump = max(farthest_jump, index + numbers[index])

        if index == current_end:
            jumps += 1
            current_end = farthest_jump

            if current_end >= n - 1:
                break

    return jumps
