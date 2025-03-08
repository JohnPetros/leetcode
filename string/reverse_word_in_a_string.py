def reverse_words_in_a_string(string: str) -> str:
    words = string.split()
    return " ".join(words[::-1])


print(reverse_words_in_a_string("the sky is blue"))
print(reverse_words_in_a_string("  hello world  "))
print(reverse_words_in_a_string("a good   example"))
