def majority_element_ii(nums: list[int]) -> list[int]:
    n = len(nums)
    table = dict()

    for num in nums:
        if num in table:
            table[num] += 1
        else:
            table[num] = 1

        keys_to_delete = []
        if len(table) == 3:
            for key in table:
                table[key] -= 1
                if not table[key]:
                    keys_to_delete.append(key)

        for key in keys_to_delete:
            del table[key]

    candidates = set(table.keys())
    real_count = {c: 0 for c in candidates}

    for num in nums:
        if num in real_count:
            real_count[num] += 1

    return [c for c, count in real_count.items() if count > n // 3]


# print(majority_element_ii([3, 2, 3]))
# print(majority_element_ii([1]))
# print(majority_element_ii([1, 2]))
print(majority_element_ii([2, 2, 1, 3]))
# print(majority_element_ii([3, 2, 3]))
