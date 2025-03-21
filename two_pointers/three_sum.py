def three_sum(numbers: list[int]):
    numbers.sort()
    triplets = []

    for index in range(len(numbers)):
        if numbers[index] > 0:
            break
        elif index > 0 and numbers[index] == numbers[index - 1]:
            continue

        left_pointer = index + 1
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            tripplet = [numbers[index], numbers[left_pointer], numbers[right_pointer]]
            total = sum(tripplet)
            if total == 0:
                triplets.append(tripplet)
                left_pointer += 1
                right_pointer -= 1
                while (
                    left_pointer < right_pointer
                    and numbers[left_pointer] == numbers[left_pointer - 1]
                ):
                    left_pointer += 1
                while (
                    left_pointer < right_pointer
                    and numbers[right_pointer] == numbers[right_pointer + 1]
                ):
                    right_pointer -= 1
            elif total < 0:
                left_pointer += 1
            else:
                right_pointer -= 1

    return triplets


# print(three_sum([-1, 0, 1, 2, -1, -4]))
# print(three_sum([0, 1, 1]))
# print(three_sum([0, 0, 0]))
print(three_sum([0, 0, 0, 0]))
