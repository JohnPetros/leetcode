def processar_saques(bandejas, saques):
    """
    Processa uma lista de saques em um conjunto de bandejas.

    Args:
        bandejas (dict): Dicionário com o estado inicial das bandejas.
        saques (list): Lista de inteiros com os valores a serem sacados.
    """
    # 1. Preparação para o Algoritmo
    # Cria uma lista com os valores das notas disponíveis
    notas_disponiveis = [info["valor"] for info in bandejas.values()]

    # Ordena as notas em ordem decrescente para o algoritmo guloso
    notas_disponiveis.sort(reverse=True)

    # Cria um mapa reverso para encontrar a letra da bandeja a partir do valor
    mapa_valor_para_bandeja = {info["valor"]: letra for letra, info in bandejas.items()}

    # 2. Processamento de Cada Saque
    for valor_saque in saques:
        valor_restante = valor_saque

        # Algoritmo Guloso: itera das notas de maior valor para as de menor
        for nota in notas_disponiveis:
            if valor_restante >= nota:
                num_notas_usadas = valor_restante // nota
                valor_restante -= num_notas_usadas * nota

                # Atualiza a quantidade na bandeja correspondente
                letra_da_bandeja = mapa_valor_para_bandeja[nota]
                bandejas[letra_da_bandeja]["qtde"] -= num_notas_usadas

    # 3. Impressão do Resultado Final
    # Garante a ordem de saída A, B, C
    for letra in sorted(bandejas.keys()):
        qtde_final = bandejas[letra]["qtde"]
        print(f"na bandeja {letra} restaram {qtde_final} notas")


def testar_exemplo_1():
    """
    Configura e executa o teste para o Exemplo 1 do problema.
    """
    print("--- Testando com Exemplo de Entrada 1 ---")

    # [cite_start]Dados de entrada do PDF [cite: 79, 80, 81]
    bandejas_iniciais = {
        "A": {"valor": 50, "qtde": 100},
        "B": {"valor": 100, "qtde": 100},
        "C": {"valor": 20, "qtde": 100},
    }

    # [cite_start]Lista de saques do PDF [cite: 82, 83, 86, 87]
    lista_saques = [100, 120, 150]

    processar_saques(bandejas_iniciais, lista_saques)

    print("\n--- Saída Esperada (Exemplo 1) ---")
    # [cite_start]A saída esperada é definida no documento [cite: 85]
    print(
        "na bandeja A restaram 99 notas\nna bandeja B restaram 97 notas\nna bandeja C restaram 99 notas"
    )
    print("-" * 35)


def testar_exemplo_2():
    """
    Configura e executa o teste para o Exemplo 2 do problema.
    """
    print("--- Testando com Exemplo de Entrada 2 ---")

    # [cite_start]Dados de entrada do PDF [cite: 89]
    bandejas_iniciais = {
        "A": {"valor": 20, "qtde": 300},
        "B": {"valor": 50, "qtde": 300},
        "C": {"valor": 100, "qtde": 300},
    }

    # [cite_start]Lista de saques do PDF [cite: 89]
    lista_saques = [180, 70, 140, 280, 330, 1130]

    processar_saques(bandejas_iniciais, lista_saques)

    print("\n--- Saída Esperada (Exemplo 2) ---")
    # [cite_start]A saída esperada é definida no documento [cite: 89]
    print(
        "na bandeja A restaram 281 notas\nna bandeja B restaram 297 notas\nna bandeja C restaram 284 notas"
    )
    print("-" * 35)


# --- Execução Principal ---
if __name__ == "__main__":
    testar_exemplo_1()
    print()  # Adiciona uma linha em branco para separar os testes
    testar_exemplo_2()
