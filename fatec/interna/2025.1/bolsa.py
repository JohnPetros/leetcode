TESTE = True


def knapsack_unbounded(values, weights, capacity):
    dp_profit = [0] * (capacity + 1)
    dp_purses = [0] * (capacity + 1)
    for i in range(len(values)):
        for w in range(weights[i], capacity + 1):
            new_profit = dp_profit[w - weights[i]] + values[i]
            new_purses = dp_purses[w - weights[i]] + 1

            if new_profit > dp_profit[w]:
                dp_profit[w] = new_profit
                dp_purses[w] = new_purses

    return dp_profit, dp_purses


def bolsa(c: int, p: int, purses: list[tuple[int, int]]):
    dp_profit, dp_purses = knapsack_unbounded(
        values=[purse[1] for purse in purses],
        weights=[purse[0] for purse in purses],
        capacity=c,
    )
    print(dp_profit)
    print(dp_purses)


if TESTE:
    bolsa(10, 2, [(5, 1), (7, 10), (9, 100)])
else:
    ...

    # bolsa(input().split())
