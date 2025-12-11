from collections import Counter


def majority_element(nums: list[int]):
    counter = Counter()
    half = len(nums) / 2

    for num in nums:
        counter[num] += 1

    for key, value in counter.items():
        if value > half:
            return key


# print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
