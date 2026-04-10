# Cada item pode ser pego até K vezes.
def knapsack_bounded(values, weights, limits, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(values)):
        for _ in range(limits[i]):  # expande em K cópias
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


# Teste
values = [10, 15, 22]
weights = [3, 4, 5]
limits = [2, 1, 1]  # item 0 pode ser pego até 2 vezes
print(knapsack_bounded(values, weights, limits, 8))  # 37
