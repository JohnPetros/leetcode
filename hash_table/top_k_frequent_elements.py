def top_k_frequent_elements(numbers: list[int], k: int) -> list[int]:
    hash_table = dict()
    frequencies = [[] for _ in numbers]
    top_frequent_elements = []

    for number in numbers:
        hash_table[number] = 1 + hash_table.get(number, 0)

    for number, frequency in hash_table.items():
        frequencies[frequency - 1].append(number)

    while k:
        for index in range(len(frequencies) - 1, -1, -1):
            frequency = frequencies[index]
            if len(frequency) > 0:
                items = frequency[0:k]
                top_frequent_elements += items
                k -= len(items)

    return top_frequent_elements


print(top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent_elements([1], 1))
