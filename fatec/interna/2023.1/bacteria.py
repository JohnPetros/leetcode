import math

TESTE = True


def calculate_distance(target: tuple[int, int, int], bacteria: tuple[int, int, int]):
    dx = bacteria[0] - target[0]
    dy = bacteria[1] - target[1]

    return math.sqrt(dx**2 + dy**2)


def bacteria(total: int, bacterias: list[tuple[int, int, int]]):
    sorted_bacterias = sorted(bacterias, key=lambda bacteria: bacteria[2], reverse=True)
    table = {bacteria: 0 for bacteria in sorted_bacterias}

    for i in range(total):
        for j in range(total):
            if i != j:
                a = sorted_bacterias[i]
                b = sorted_bacterias[j]
                if calculate_distance(a, b) + b[2] <= a[2]:
                    table[a] += 1

    entries = sorted(table.items(), key=lambda item: item[1], reverse=True)
    print(f"{entries[0][1]}\n{entries[0][0][0]} {entries[0][0][1]}")


if TESTE:
    bacteria(3, [(-3, 2, 5), (-4, -1, 1), (-1, 5, 3)])
