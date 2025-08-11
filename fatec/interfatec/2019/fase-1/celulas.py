from math import sqrt, acos

# PI conforme especificado no problema
pi = 3.1415


def circle_intersection(ray1, ray2, distance):
    """Calcula a área de interseção entre dois círculos."""
    # Caso 1: um círculo está completamente dentro do outro
    if distance <= abs(ray1 - ray2):
        return pi * min(ray1, ray2) ** 2

    # Caso 2: não há interseção
    if distance >= ray1 + ray2:
        return 0

    # Adicionado para robustez contra erros de ponto flutuante
    arg1 = (distance**2 + ray1**2 - ray2**2) / (2 * distance * ray1)
    arg1 = max(-1.0, min(1.0, arg1))  # Garante que o valor esteja em [-1, 1]

    arg2 = (distance**2 + ray2**2 - ray1**2) / (2 * distance * ray2)
    arg2 = max(-1.0, min(1.0, arg2))  # Garante que o valor esteja em [-1, 1]

    part1 = ray1**2 * acos(arg1)
    part2 = ray2**2 * acos(arg2)
    part3 = 0.5 * sqrt(
        (-distance + ray1 + ray2)
        * (distance + ray1 - ray2)
        * (distance - ray1 + ray2)
        * (distance + ray1 + ray2)
    )

    return part1 + part2 - part3


# CORREÇÃO 4: O tipo de retorno é float
def euclidean_distance_2d(point1: tuple[int, int], point2: tuple[int, int]) -> float:
    """Calcula a distância euclidiana entre dois pontos."""
    x1, y1 = point1
    x2, y2 = point2
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# No ambiente do desafio, os valores viriam de input()
# Estes são os dados do "Exemplo de Entrada 2" do PDF [cite: 224] para teste
circle_count = 3
inputs = [
    "40 40 10",
    "50 40 10",
    "136 124 5",
]

total_area = 0
circles = []

for line in inputs:
    x, y, r = map(int, line.split())
    circles.append({"x": x, "y": y, "r": r})

# Soma as áreas individuais primeiro
for c in circles:
    total_area += pi * c["r"] ** 2

# Itera sobre todos os pares únicos e subtrai a área de interseção
for i in range(circle_count):
    for j in range(i + 1, circle_count):
        c1 = circles[i]
        c2 = circles[j]

        # CORREÇÃO 1: Calcular a distância entre c1 e c2
        distance = euclidean_distance_2d((c1["x"], c1["y"]), (c2["x"], c2["y"]))

        if distance < c1["r"] + c2["r"]:
            total_area -= circle_intersection(c1["r"], c2["r"], distance)

# CORREÇÃO 2: Imprimir apenas a parte inteira do resultado
print(int(total_area))
# Saída com os dados de teste corrigidos: 584
