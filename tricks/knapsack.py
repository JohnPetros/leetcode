def knapsack(capacity: int, items: list[tuple[int, int]]) -> int:
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for index in range(capacity, weight - 1, -1):
            dp[index] = max(dp[index], dp[index - weight] + value)

    return dp[capacity]


capacity = 8
items = [
    (3, 10),  # weight, value
    (4, 15),
    (5, 22),
]

result = knapsack(capacity, items)
print(f"Resultado final: {result}")  # Saída esperada: 32
