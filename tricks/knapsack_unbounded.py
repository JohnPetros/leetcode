# Cada item pode ser pego infinitas vezes.
def knapsack_unbounded(values, weights, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(values)):
        for w in range(weights[i], capacity + 1):  # direto
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


# Teste
values = [10, 15, 22]
weights = [3, 4, 5]
print(knapsack_unbounded(values, weights, 8))  # 37 (item 0 duas vezes + item 1)
