def container_with_most_water(heights: list[int]) -> int:
    left_pointer = 0
    right_pointer = len(heights) - 1
    most_water = 0

    while left_pointer < right_pointer:
        water = (right_pointer - left_pointer) * min(
            heights[left_pointer], heights[right_pointer]
        )
        most_water = max(most_water, water)

        if heights[left_pointer] < heights[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return most_water


print(container_with_most_water([1, 7, 2, 5, 4, 7, 3, 6]))
