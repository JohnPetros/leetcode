def trapping_rain_water(heights: list[int]) -> int:
    if not heights:
        return 0

    max_left_heights = [0] * len(heights)
    max_right_heights = [0] * len(heights)

    max_left_heights[0] = heights[0]
    max_right_heights[len(heights) - 1] = heights[len(heights) - 1]

    for index in range(1, len(heights)):
        max_left_heights[index] = max(max_left_heights[index - 1], heights[index])

    for index in range(len(heights) - 2, -1, -1):
        max_right_heights[index] = max(max_right_heights[index + 1], heights[index])

    max_water_units = 0

    for index in range(len(heights)):
        min_heigth = (
            min(max_left_heights[index], max_right_heights[index]) - heights[index]
        )
        max_water_units += min_heigth

    return max_water_units


print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# def trapping_rain_water(heights: list[int]) -> int:
#     if not heights:
#         return 0

#     max_left_heights = []
#     max_right_heights = []
#     max_left_height = heights[0]
#     max_right_height = heights[-1]

#     for height in heights:
#         if height > max_left_height:
#             max_left_height = height

#         max_left_heights.append(max_left_height)

#     for height in heights[::-1]:
#         if height > max_right_height:
#             max_right_height = height

#         max_right_heights.append(max_right_height)

#     max_water_units = 0

#     print(max_right_heights)

#     for index in range(len(heights)):
#         min_heigth = (
#             min(max_left_heights[index], max_right_heights[index]) - heights[index]
#         )
#         max_water_units += min_heigth

#     return max_water_units


# print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
