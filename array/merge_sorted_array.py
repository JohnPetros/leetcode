def merge_sorted_array(numbers1: list[int], m, numbers2: list[int], n):
    x, y = m - 1, n - 1

    for z in range(m + n - 1, -1, -1):
        if x < 0:
            numbers1[z] = numbers2[y]
            y -= 1
        elif y < 0:
            break
        elif numbers1[x] >= numbers2[y]:
            numbers1[z] = numbers1[x]
            x -= 1
        else:
            numbers1[z] = numbers2[y]
            y -= 1

    return numbers1


# print(merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(merge_sorted_array([1], 1, [], 0))
# print(merge_sorted_array([0], 0, [1], 1))
print(merge_sorted_array([2, 0], 1, [1], 1))
