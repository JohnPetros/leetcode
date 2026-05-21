TESTE = True


def horta(packs: list[tuple[int, int]]):
    pits = 0

    for pack in packs:
        pits += pack[0] // pack[1]

    print(pits)


if TESTE:
    horta([(30, 3), (10, 2), (20, 5)])
    horta([(25, 6), (20, 3), (10, 3)])
    horta([(100, 100), (100, 1), (1, 1)])
else:
    packs = []
    for _ in range(3):
        packs.append(tuple(map(int, input().split())))
    horta(packs)
