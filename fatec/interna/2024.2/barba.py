from collections import Counter

TESTE = True


def barba(total: int, stickers: list[int]):
    half = total // 2
    counter = Counter(stickers)

    for key, value in counter.items():
        if value > half:
            print(key)
            return


if TESTE:
    barba(5, [1, 1, 1, 2, 3])
    barba(7, [4, 3, 2, 3, 4, 3, 3])
else:
    total = int(input())
    stickets = list(map(int, input().split()))
