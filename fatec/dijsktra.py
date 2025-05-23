import heapq


def dijkstra(grafo, inicio):
    """
    Implementação do algoritmo de Dijkstra para encontrar o caminho mais curto

    Args:
        grafo: dicionário onde as chaves são os nós e os valores são dicionários
              com os vizinhos e os pesos das arestas
        inicio: nó inicial

    Returns:
        distancias: dicionário com as distâncias mínimas do nó inicial para todos os outros
        predecessores: dicionário com o predecessores de cada nó no caminho mais curto
    """
    # Inicializa as distâncias como infinito para todos os nós
    distancias = {nó: float("inf") for nó in grafo}
    # A distância para o nó inicial é 0
    distancias[inicio] = 0
    # Dicionário para armazenar o predecessor de cada nó no caminho mais curto
    predecessores = {nó: None for nó in grafo}
    # Fila de prioridade com os nós a serem processados
    fila_prioridade = [(0, inicio)]

    # Conjunto para manter controle dos nós já processados
    processados = set()

    # Enquanto houver nós a serem processados
    while fila_prioridade:
        # Obtém o nó com menor distância
        distancia_atual, nó_atual = heapq.heappop(fila_prioridade)

        # Ignora nós já processados
        if nó_atual in processados:
            continue

        # Marca o nó como processado
        processados.add(nó_atual)

        # Verifica todos os vizinhos do nó atual
        for vizinho, peso in grafo[nó_atual].items():
            # Se o vizinho já foi processado, ignora
            if vizinho in processados:
                continue

            # Calcula nova distância para o vizinho
            nova_distancia = distancia_atual + peso

            # Se encontrou um caminho mais curto, atualiza
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = nó_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return distancias, predecessores


# Função auxiliar para reconstruir o caminho
def reconstruir_caminho(predecessores, inicio, fim):
    """
    Reconstrói o caminho do nó inicial até o final usando a lista de predecessores

    Args:
        predecessores: dicionário com os predecessores de cada nó
        inicio: nó inicial
        fim: nó final

    Returns:
        caminho: lista com os nós que formam o caminho mais curto
    """
    caminho = []
    nó_atual = fim

    # Se não há caminho até o fim, retorna uma lista vazia
    if predecessores[fim] is None and inicio != fim:
        return caminho

    # Reconstruir o caminho de trás para frente
    while nó_atual is not None:
        caminho.append(nó_atual)
        nó_atual = predecessores[nó_atual]

    # Inverte o caminho para ficar na ordem correta
    return caminho[::-1]


# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de grafo representado como um dicionário de adjacências
    grafo = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6},
    }

    inicio = "A"
    fim = "F"

    # Executa o algoritmo de Dijkstra
    distancias, predecessores = dijkstra(grafo, inicio)

    # Imprime as distâncias mínimas do nó inicial a todos os outros
    print("Distâncias mínimas a partir do nó", inicio)
    for nó, distancia in distancias.items():
        print(f"{inicio} -> {nó}: {distancia}")

    # Reconstrói e imprime o caminho mais curto até o nó final
    caminho = reconstruir_caminho(predecessores, inicio, fim)
    print(f"\nCaminho mais curto de {inicio} até {fim}: {' -> '.join(caminho)}")
    print(f"Distância total: {distancias[fim]}")
