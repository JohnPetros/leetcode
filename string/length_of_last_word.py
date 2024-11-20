def length_of_last_word(sentence: str) -> int:
    last_word = sentence.strip().split(" ")[-1]
    return len(last_word)


print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("luffy is still joyboy"))
