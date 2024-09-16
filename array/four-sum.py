def four_sum(numbers: list[int], target: int) -> list[list[int]]:
    numbers.sort()
    numbers_count = len(numbers)
    quadruplets = []

    for first_pointer in range(numbers_count):
        if first_pointer > 0 and numbers[first_pointer] == numbers[first_pointer - 1]:
            continue

        for second_pointer in range(first_pointer + 1, numbers_count):
            if (
                second_pointer > first_pointer + 1
                and numbers[second_pointer] == numbers[second_pointer - 1]
            ):
                continue

            third_pointer = second_pointer + 1
            fourth_pointer = numbers_count - 1

            while third_pointer < fourth_pointer:
                quadruplet = [
                    numbers[first_pointer],
                    numbers[second_pointer],
                    numbers[third_pointer],
                    numbers[fourth_pointer],
                ]

                current_sum = sum(quadruplet)

                if current_sum == target:
                    quadruplets.append(quadruplet)
                    third_pointer += 1
                    fourth_pointer -= 1
                    while (
                        third_pointer < fourth_pointer
                        and numbers[third_pointer] == numbers[third_pointer - 1]
                    ):
                        third_pointer += 1
                    while (
                        third_pointer < fourth_pointer
                        and numbers[fourth_pointer] == numbers[fourth_pointer + 1]
                    ):
                        fourth_pointer -= 1
                elif current_sum < target:
                    third_pointer += 1
                else:
                    fourth_pointer -= 1

    return quadruplets


print(four_sum([1, 0, -1, 0, -2, 2], 0))
