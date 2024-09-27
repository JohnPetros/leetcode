CITIES_GRAPH = [
    # A  B  C  D  E  F
    [0, 1, 0, 0, 0, 0],  # A
    [0, 0, 1, 0, 0, 0],  # B
    [0, 0, 0, 0, 1, 0],  # C
    [0, 0, 1, 0, 1, 0],  # D
    [1, 0, 0, 0, 0, 0],  # E
    [0, 1, 0, 0, 0, 0],  # F
]


def calculate_distance(number_of_cities, origin):
    distances = [-1] * number_of_cities  # marca para dizer local novo
    distances[origin] = 0
    queue = []
    queue.append(origin)
    while len(queue) > 0:  # fila não vazia = possibilidades
        first_city_index = queue.pop(0)  # retiro o primeiro da fila
        for current_city_index in range(number_of_cities):  # percorro cidades
            if (
                CITIES_GRAPH[first_city_index][current_city_index] == 1
                and distances[current_city_index] == -1
            ):
                # A[x][y] = 1 significa tem caminho de x a y
                # d[y] = -1 nunca estive na cidade destino y
                # chego lá e nunca visitei antes (-1)
                distances[current_city_index] = distances[first_city_index] + 1
                print(distances)
                queue.append(current_city_index)  # enfilero onde cheguei
                # para ir mais para frente depois
    return distances


print(calculate_distance(len(CITIES_GRAPH), 3))
