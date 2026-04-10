TESTE = True

# 1 -> 1  =   1 + 4 * 0
# 2 -> 6  =   2 + 4 * 1
# 3 -> 11 =   3 + 4 * 2
# 4 -> 16 =   4 + 4 * 3
# 5 -> 21 =   5 + 4 * 4
#         =   n + 4 * (n - 1)


def feira(n: int, m: int):
    minimum = n + 4 * (n - 1)
    print("S" if minimum <= m else "N")


if TESTE:
    feira(2, 10)
    feira(3, 10)
    feira(3, 11)
else:
    n, m = list(map(int, input().split()))
    feira(n, m)
