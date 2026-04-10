# Cada item pode ser pego 0 ou 1 vez.
def knapsack_01(values, weights, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(values)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


capacity = 8
items = [
    (3, 10),  # weight, value
    (4, 15),
    (5, 22),
]

weights = [item[0] for item in items]
values = [item[1] for item in items]

result = knapsack_01(values, weights, capacity)
print(f"Resultado final: {result}")  # Saída esperada: 32
