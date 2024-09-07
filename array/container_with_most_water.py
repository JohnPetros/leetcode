def container_with_most_water(lines: list[int]) -> int:
    max_area = 0
    left_pointer = 0
    right_pointer = len(lines) - 1

    while left_pointer != right_pointer:
        left_line = lines[left_pointer]
        right_line = lines[right_pointer]

        smaller_line = min(left_line, right_line)

        area = smaller_line * (right_pointer - left_pointer)

        if area > max_area:
            max_area = area

        if smaller_line == left_line:
            left_pointer += 1
        elif smaller_line == right_line:
            right_pointer -= 1

    return max_area


print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(container_with_most_water([1, 1]))
