def can_place_flowers(flowerbed: list[int], new_flowers: int):
    if len(flowerbed) == 1 and flowerbed[0] == 0:
        return True

    flower_index = first_flower_index = 0
    last_flower_index = len(flowerbed) - 1

    while new_flowers and flower_index <= last_flower_index:
        flower = flowerbed[flower_index]

        if flower == 0:
            if flower_index > first_flower_index and flower_index < last_flower_index:
                if (
                    flowerbed[flower_index - 1] != 1
                    and flowerbed[flower_index + 1] != 1
                ):
                    flowerbed[flower_index] = 1
                    new_flowers -= 1
            else:
                if (
                    flower_index == first_flower_index
                    and flowerbed[flower_index + 1] != 1
                ) or (
                    flower_index == last_flower_index
                    and flowerbed[flower_index - 1] != 1
                ):
                    flowerbed[flower_index] = 1
                    new_flowers -= 1

        flower_index += 1

    return flowerbed, new_flowers


print(can_place_flowers([1, 0, 0, 0, 1], 1))
# print(can_place_flowers([1, 0, 0, 0, 1], 2))
# print(can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2))
