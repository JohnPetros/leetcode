def two_sum(numbers, target):
    hash_table = dict()

    for index in range(len(numbers)):
        if numbers[index] in hash_table:
            return [hash_table[numbers[index]], index]

        hash_table[target - numbers[index]] = index


print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))  # [1, 2]
print(two_sum([3, 3], 6))  # [0, 1]
print(two_sum([3, 2, 3], 6))  # [0, 2]
print(two_sum([-3, 4, 3, 90], 0))  # [0, 2]
