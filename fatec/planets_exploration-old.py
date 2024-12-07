import math


def calcular_distancia(coord1, coord2):
    """Calcula a distância euclidiana entre duas coordenadas no espaço 3D."""
    return math.sqrt(
        (coord1[0] - coord2[0]) ** 2
        + (coord1[1] - coord2[1]) ** 2
        + (coord1[2] - coord2[2]) ** 2
    )


def ordenar_naves(planeta, naves):
    """Ordena as naves com base na distância ao planeta."""
    distancias = [
        (i, calcular_distancia(planeta, nave)) for i, nave in enumerate(naves)
    ]
    # Ordena por distância, depois por índice (para desempate)
    distancias.sort(key=lambda x: (x[1], x[0]))
    return [i for i, _ in distancias]


# Entrada e saída
def resolver_problema(casos):
    resultados = []
    for caso in casos:
        dados = list(map(int, caso.split()))
        planeta = dados[:3]
        n = dados[3]
        naves = [dados[i : i + 3] for i in range(4, len(dados), 3)]
        resultado = ordenar_naves(planeta, naves)
        resultados.append(" ".join(map(str, resultado)))
    return resultados


# Teste
casos_teste = [
    "5 5 5 2 1 1 1 3 3 3",
    "2 1 0 5 1 2 8 6 3 8 7 3 1 2 2 4 9 6 0",
    "2 0 0 4 1 1 2 2 2 3 1 0 0 1 2 3",
    "10 35 29 3 12 34 75 32 49 01 12 12 12",
    "2 2 2 2 1 1 1 3 3 3",
]

resultados = resolver_problema(casos_teste)
for resultado in resultados:
    print(resultado)
