def mochila_01(valores, pesos, capacidade):
    n = len(valores)
    # Cria uma tabela dp[n+1][capacidade+1] inicializada com zeros
    # dp[i][w] armazenará o valor máximo usando os primeiros 'i' itens
    # com uma capacidade máxima 'w'
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenche a tabela dp
    for i in range(1, n + 1):  # Itera sobre os itens (de 1 até n)
        for w in range(
            1, capacidade + 1
        ):  # Itera sobre as capacidades (de 1 até capacidade)
            # Peso do item atual (lembre-se que valores/pesos são 0-indexados)
            peso_item_atual = pesos[i - 1]
            valor_item_atual = valores[i - 1]

            if peso_item_atual <= w:
                # Opção 1: Incluir o item atual
                valor_com_item = valor_item_atual + dp[i - 1][w - peso_item_atual]
                # Opção 2: Não incluir o item atual
                valor_sem_item = dp[i - 1][w]
                dp[i][w] = max(valor_com_item, valor_sem_item)
            else:
                # Se o item não cabe, o valor é o mesmo sem considerar este item
                dp[i][w] = dp[i - 1][w]

    # O valor máximo estará em dp[n][capacidade]
    return dp[n][capacidade]


# Exemplo de uso:
if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidade = 50
    n = len(valores)

    valor_maximo = mochila_01(valores, pesos, capacidade)
    print(
        f"O valor máximo que pode ser colocado na mochila é: {valor_maximo}"
    )  # Saída esperada: 220

    valores2 = [10, 40, 30, 50]
    pesos2 = [5, 4, 6, 3]
    capacidade2 = 10
    n2 = len(valores2)

    valor_maximo2 = mochila_01(valores2, pesos2, capacidade2)
    print(
        f"O valor máximo que pode ser colocado na mochila é: {valor_maximo2}"
    )  # Saída esperada: 90
