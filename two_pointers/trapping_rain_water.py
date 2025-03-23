def trapping_rain_water(heights: list[int]) -> int:
    max_heights_left = [0] * len(heights)
    max_heights_right = [0] * len(heights)
    total_water = 0

    for left_pointer in range(1, len(heights)):
        right_pointer = -left_pointer - 1
        max_heights_left[left_pointer] = max(
            max_heights_left[left_pointer - 1], heights[left_pointer - 1]
        )
        max_heights_right[right_pointer] = max(
            max_heights_right[right_pointer + 1], heights[right_pointer + 1]
        )

    for index in range(len(heights)):
        water = min(max_heights_left[index], max_heights_right[index]) - heights[index]
        if water > 0:
            total_water += water

    return total_water


print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trapping_rain_water([4, 2, 0, 3, 2, 5]))
