TESTE = False


def alturas(length: int, group1: list[int], group2: list[int]):
    def find_max(heights: list[int]):
        dp = [1] * length

        for i in range(length):
            for j in range(0, i):
                if heights[j] <= heights[i]:
                    dp[i] = max((dp[i], dp[j] + 1))

        return max(dp)

    group1_max = find_max(group1)
    group2_max = find_max(group2)

    if group1_max > group2_max:
        print(f"1 {group1_max}")
    elif group2_max > group1_max:
        print(f"2 {group2_max}")
    else:
        print(f"EMPATE {group1_max}")


if TESTE:
    alturas(
        7,
        [165, 169, 153, 155, 155, 185, 172],
        [181, 156, 160, 173, 178, 167, 179],
    )
    alturas(
        11,
        [170, 172, 180, 181, 174, 179, 179, 183, 185, 190, 192],
        [155, 157, 165, 165, 174, 172, 173, 173, 183, 182, 181],
    )
else:
    length = int(input())
    group1 = list(map(int, input().split()[:length]))
    group2 = list(map(int, input().split()[:length]))
    alturas(length, group1, group2)
