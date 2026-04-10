# Pode pegar fração de um item. Resolvido com Greedy, não DP.
def knapsack_fractional(values, weights, capacity):
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    total = 0.0
    for value, weight in items:
        if capacity >= weight:
            total += value
            capacity -= weight
        else:
            total += value * (capacity / weight)  # fração
            break
    return total


# Teste
values = [10, 15, 22]
weights = [3, 4, 5]
print(knapsack_fractional(values, weights, 8))  # 38.2
