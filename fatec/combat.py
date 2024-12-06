def combat(
    monsters: list[tuple[int, int]],
    rolls: list[tuple[str, int, int]],
    attacks: list[int],
):
    while rolls and monsters:
        status, roll_1, roll_2 = rolls.pop(0)
        roll = None
        match status:
            case "V":
                roll = max(roll_1, roll_2)
            case "D":
                roll = min(roll_1, roll_2)
            case "N":
                roll = roll_1

        monster_life = monsters[0][0]
        monster_armor = monsters[0][1]
        attack = attacks.pop(0)
        if roll > monster_armor:
            monsters[0][0] = monster_life - attack
            if monsters[0][0] <= 0:
                monsters.pop(0)

    if not monsters:
        print("VITÓRIA")
    else:
        print("DERROTA")


monsters = []
rolls = []
attacks = []

for _ in range(int(input())):
    monsters.append(map(int, input().split()))

for _ in range(int(input())):
    status, roll_1, roll_2 = input().split()
    monsters.append((status, int(roll_1), int(roll_2)))
    attacks.append(int(input()))


combat(
    [[15, 15]],
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
