def longest_repeating_character_replacement(string, k):
    left_pointer = 0
    longest_length = 0
    alphabet_frequency = [0] * 26

    for right_pointer in range(len(string)):
        righter_letter_index = ord(string[right_pointer]) - 65
        alphabet_frequency[righter_letter_index] += 1

        while right_pointer - left_pointer + 1 - max(alphabet_frequency) > k:
            lefter_letter_index = ord(string[left_pointer]) - 65
            alphabet_frequency[lefter_letter_index] -= 1
            left_pointer += 1

        length = right_pointer - left_pointer + 1
        longest_length = max(longest_length, length)

    return longest_length
    # Time Complexity: O(n)
    # Space Complexity: O(1)


print(longest_repeating_character_replacement("AABABBA", 1))
