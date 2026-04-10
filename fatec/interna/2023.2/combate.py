TESTE = True


def combate(
    monsters: list[list[int]],
    rolls: int,
    attacks: list[tuple[str, int, int]],
    damages: list[int],
):
    for index in range(rolls):
        if len(monsters) == 0:
            print("VITORIA")
            return

        attack = attacks[index]
        t = attack[0]
        p = attack[1]
        q = attack[2]

        a = p

        if t == "V":
            a = p if p > q else q
        elif t == "D":
            a = p if p < q else q

        if a > monsters[0][0]:
            monsters[0][1] -= damages[index]

            if monsters[0][1] <= 0:
                monsters.pop(0)

    if len(monsters) == 0:
        print("VITORIA")
    else:
        print("DERROTA")


if TESTE:
    combate(
        [[15, 15]],
        7,
        [
            ("N", 3, 7),
            ("N", 14, 1),
            ("N", 17, 9),
            ("V", 11, 5),
            ("N", 3, 8),
            ("D", 15, 12),
            ("V", 16, 18),
        ],
        [19, 12, 8, 13, 16, 20, 7],
    )
    combate(
        [[6, 10], [8, 15]],
        3,
        [("N", 10, 5), ("N", 10, 5), ("N", 10, 5)],
        [10, 10, 10],
    )
    combate(
        [[10, 10]],
        1,
        [("N", 8, 9)],
        [15],
    )
else:
    n = int(input())
    monsters = [list(map(int, input().split())) for _ in range(n)]
    rolls = int(input())
    attacks = []
    damages = []
    for _ in range(rolls):
        line = input().split()
        attacks.append((line[0], int(line[1]), int(line[2])))
        damages.append(int(input()))
    combate(monsters, rolls, attacks, damages)
