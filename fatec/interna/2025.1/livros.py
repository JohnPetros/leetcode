TESTE = True


def livros(ids: list[str]):
    digits = list(dict.fromkeys([id[-1] for id in ids]).keys())
    digits.sort()
    sorted_ids = []

    while digits:
        for id in ids:
            if id[-1] == digits[0]:
                sorted_ids.append(id)
        digits.pop(0)

    print(" ".join(sorted_ids))


if TESTE:
    livros(["31", "43", "53", "181", "77", "33", "17"])
    livros(["13", "41", "1", "241", "13", "24", "87", "90", "17", "88", "67"])

else:
    total = int(input())
    ids = []
    for _ in range(total):
        ids = input().split()
    livros(ids)
