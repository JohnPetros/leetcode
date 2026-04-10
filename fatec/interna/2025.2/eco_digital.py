import re

TESTE = True


def eco_digital(phrase: str):
    new_phrase = phrase[0]
    for i in range(1, len(phrase)):
        if phrase[i - 1].lower() != phrase[i].lower():
            new_phrase += phrase[i]
    new_phrase = new_phrase.lower()
    words = re.findall(r"[a-záàãâéêíóôõúüç]+", new_phrase)
    disctinct_words = set(words)
    longest_word = words[0]
    start_end_same_letter = 0

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        if word[0] == word[-1]:
            start_end_same_letter += 1

    print(f"Texto limpo: {new_phrase}")
    print(f"Palavras distintas: {len(disctinct_words)}")
    print(f"Mais longa: {longest_word}")
    print(f"Começam e terminam com mesma letra: {start_end_same_letter}")


if TESTE:
    eco_digital("Baaannaaannaaaa!!! Euuu Goossttoo deee prrrogramaarrrr...")
else:
    eco_digital(input())
