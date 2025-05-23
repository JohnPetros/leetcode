def technology_mayor(budget: int, improvements: list[set]):
    improvements.sort(key=lambda improvement: improvement[1], reverse=True)
    total_votes_count = 0

    for improvement in improvements:
        improvement_cost = improvement[0]
        votes_count = improvement[1]

        if improvement_cost <= budget:
            budget -= improvement_cost
            total_votes_count += votes_count

    if total_votes_count == 0:
        return "NO FUNDS"

    return f"{total_votes_count} {budget}"


budget, improvements_count = input().split(" ")
improvements = []

for _ in range(int(improvements_count)):
    improvement_cost, votes_count = input().split(" ")
    improvements.append((int(improvement_cost), int(votes_count)))

print(technology_mayor(int(budget), improvements))


# print(technology_mayor(50, [(20, 50), (10, 500), (35, 750)]))
# print(technology_mayor(100, [(20, 250), (35, 4), (66, 50), (5, 156), (12, 500)]))
# print(technology_mayor(10, [(100, 5), (55, 35)]))

# Knapsack Problem


def max_votes(budget, improvements):
    """
    Função para calcular o máximo de votos que podem ser atendidos com o orçamento disponível.

    Args:
        budget: Orçamento total disponível (em milhões)
        improvements: Lista de tuplas (custo, votos) para cada melhoria

    Returns:
        tuple: (total_votes, remaining_budget) - Total de votos atendidos e orçamento restante
              ou "NO FUNDS" se nenhuma melhoria puder ser implementada
    """
    # Inicializar a tabela de programação dinâmica
    # dp[i] representa o máximo de votos que podem ser obtidos com um orçamento de i milhões
    dp = [0] * (budget + 1)

    # Para cada melhoria, atualizar a tabela de DP
    for cost, votes in improvements:
        # Ignorar melhorias que custam mais que o orçamento
        if cost > budget:
            continue

        # Começamos de trás para frente para evitar contar a mesma melhoria múltiplas vezes
        for b in range(budget, cost - 1, -1):
            dp[b] = max(dp[b], dp[b - cost] + votes)

    # Encontrar o máximo de votos
    max_votes_value = dp[budget]

    if max_votes_value == 0:
        return "NO FUNDS"

    # Calcular o orçamento restante
    # Encontrar o menor orçamento necessário para obter o máximo de votos
    min_budget_used = budget
    for b in range(budget + 1):
        if dp[b] == max_votes_value:
            min_budget_used = b
            break

    remaining_budget = budget - min_budget_used

    return (max_votes_value, remaining_budget)


def main():
    """
    Função principal para processar a entrada e saída.
    """
    # Leitura da entrada
    budget, num_improvements = map(int, input().split())

    improvements = []
    for _ in range(num_improvements):
        cost, votes = map(int, input().split())
        improvements.append((cost, votes))

    # Calcular o máximo de votos
    result = max_votes(budget, improvements)

    # Imprimir o resultado
    if result == "NO FUNDS":
        print(result)
    else:
        max_votes_value, remaining_budget = result
        print(f"{max_votes_value} {remaining_budget}")


if __name__ == "__main__":
    main()
