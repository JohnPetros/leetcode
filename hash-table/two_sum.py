def two_sum(numbers, target):
    complements = {}

    for index, number in enumerate(numbers):
        complement = target - number

        if complement in complements:
            return [complements[complement], index]

        complements[number] = index


print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))  # [1, 2]
print(two_sum([3, 3], 6))  # [0, 1]
print(two_sum([3, 2, 3], 6))  # [0, 2]
print(two_sum([-3, 4, 3, 90], 0))  # [0, 2]
