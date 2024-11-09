def jump_game(numbers: list[int]) -> bool:
    if len(numbers) == 1:
        return True

    last_index = len(numbers) - 1
    max_reach = 0

    for index in range(last_index + 1):
        if index > max_reach:
            return False

        max_reach = max(max_reach, index + numbers[index])

        if max_reach >= last_index:
            return True

    return False


# print(jump_game([2, 1, 3, 1, 0, 1]))
# print(jump_game([2, 3, 1, 1, 4]))
# print(jump_game([3, 2, 1, 0, 4]))
# print(jump_game([2, 0]))
print(jump_game([3, 2, 1, 0, 4]))
