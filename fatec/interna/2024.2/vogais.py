TESTE = True

VOWALS = "aeiou"


def vogais(word: str):
    count = 0
    max_count = 0
    for i in range(len(word)):
        if word[i].lower() in VOWALS:
            count += 1
        else:
            count = 0

        max_count = max(count, max_count)

    print(max_count)


if TESTE:
    vogais("abacate")
    vogais("beautiful")
else:
    word = input()
    vogais(word)
