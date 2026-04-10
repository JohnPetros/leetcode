TESTE = True


def arthur(dictionary: dict, phrase: str):
    new_phrase = ""

    i = 0

    while i < len(phrase):
        has_match = False

        for slang, traslation in dictionary.items():
            if phrase[i : i + len(slang)] == slang:
                new_phrase += traslation
                i += len(slang)
                has_match = True
                break

        if not has_match:
            new_phrase += phrase[i]
            i += 1

    print(new_phrase)


if TESTE:
    arthur(
        {"abs": "abraco", "pr": "pirata"},
        "nossa isso foi muito bizu na proxima vou dar um abs no pr",
    )
    arthur(
        {"e": "o"},
        "ei ceme vae as ceisas per ai",
    )
else:
    total_slangs = int(input())
    dictionary = dict()
    for _ in range(total_slangs):
        slang, translation = input().split()
        dictionary[slang] = translation
    phrase = input()
    dictionary = dict(
        sorted(dictionary.items(), key=lambda item: len(item[0]), reverse=True)
    )
    arthur(dictionary, phrase)
