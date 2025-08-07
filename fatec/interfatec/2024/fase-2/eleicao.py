def knapsack(capacity: int, items: list[tuple[int, int]]) -> int:
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for index in range(capacity, weight - 1, -1):
            dp[index] = max(dp[index], dp[index - weight] + value)

    return dp[capacity]


# Nosso caso de teste simples
verba = 8
locais = [
    (3, 10),  # Posto A
    (4, 15),  # Posto B
    (5, 22),  # Posto C
]

resultado = knapsack(verba, locais)
print(f"Resultado final: {resultado}")  # Saída esperada: 32
