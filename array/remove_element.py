def remove_element(numbers: list[int], value: int):
    length = 0

    for number in numbers:
        if numbers != value:
            numbers[length] = number
            length += 1

    return length


# 1 3 5 3 5
# index = 4
# length = 2
print(remove_element([2, 2, 3, 5], 2))
