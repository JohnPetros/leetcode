TESTE = True


def knapsack_01(values, weights, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(values)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp


def bolsa(c: int, p: int, purses: list[tuple[int, int]]):
    result = knapsack_01(
        values=[purse[1] for purse in purses],
        weights=[purse[0] for purse in purses],
        capacity=c,
    )
    print(result)


if TESTE:
    bolsa(10, 2, [(5, 1), (7, 10), (9, 100)])
else:
    ...

    # bolsa(input().split())
