def reverse_words_in_a_string_iii(string: str) -> str:
    reversed_string = ""
    left_pointer = right_pointer = 0

    while right_pointer < len(string):
        if string[right_pointer] != " ":
            right_pointer += 1
        else:
            reversed_string += string[left_pointer : right_pointer + 1][::-1]
            right_pointer += 1
            left_pointer = right_pointer

    reversed_string += " "
    reversed_string += string[left_pointer : right_pointer + 1][::-1]
    return reversed_string[1:]


print(reverse_words_in_a_string_iii("Let's take LeetCode contest"))
