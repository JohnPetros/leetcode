def longest_consecutive_sequence(numbers: list[int]) -> int:
    integers = set(numbers)
    longest_sequence = 0

    for integer in integers:
        if integer - 1 not in integers:
            sequence = 1
            current_integer = integer
            while current_integer + 1 in integers:
                sequence += 1
                current_integer += 1

            longest_sequence = max(longest_sequence, sequence)

    return longest_sequence


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
