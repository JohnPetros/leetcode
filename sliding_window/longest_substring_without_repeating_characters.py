def longest_substring_without_repeating_characters(string):
    visited_characters = set()
    left_pointer = 0
    max_lenght = 0

    for right_pointer in range(len(string)):
        while string[right_pointer] in visited_characters:
            visited_characters.remove(string[left_pointer])
            left_pointer += 1

        visited_characters.add(string[right_pointer])
        max_lenght = max(max_lenght, right_pointer - left_pointer + 1)

    return max_lenght


print(longest_substring_without_repeating_characters("aabcab"))
print(longest_substring_without_repeating_characters("bbbbb"))
print(longest_substring_without_repeating_characters("pwwkew"))
print(longest_substring_without_repeating_characters("tmmzuxt"))
