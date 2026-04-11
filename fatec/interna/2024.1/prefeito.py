TESTE = True


def knapsack_01(values, weights, capacity):
    dp: list[int] = [0] * (capacity + 1)
    for i in range(len(values)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp


def prefeito(budget: int, improvements: list[tuple[int, int]]):
    dp = knapsack_01(
        values=[improvement[1] for improvement in improvements],
        weights=[improvement[0] for improvement in improvements],
        capacity=budget,
    )
    max_votes = dp[budget]
    if max_votes == 0:
        print("NO FUNDS")
        return

    min_budget = dp.index(max_votes)

    print(f"{max_votes} {budget - min_budget}")


if TESTE:
    prefeito(50, [(20, 50), (10, 500), (35, 750)])
    prefeito(100, [(20, 250), (35, 4), (66, 50), (5, 156), (12, 500)])
    prefeito(10, [(100, 5), (55, 35)])
else:
    budget, total = list(map(int, input().split()))
    improvements = []
    for _ in range(total):
        cost, votes = list(map(int, input().split()))
        improvements.append((cost, votes))

    prefeito(budget, improvements)
