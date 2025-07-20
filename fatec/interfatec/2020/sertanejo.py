from collections import defaultdict, deque

inputs = [
    "Castrinho e Firmino",
    "Saracura e Bianor",
    "Edmar e Saracura",
    "Kauan e Tiberio",
    "Bianor e Castrinho",
    "Castrinho e Domingos",
    "Saracura e Edmar",
]

graph = defaultdict(list)

for input in inputs:
    composer1, composer2 = input.split(" e ")
    graph[composer1].append(composer2)
    graph[composer2].append(composer1)

distances = {composer: float("inf") for composer in graph}
distances["Saracura"] = 0


queue = deque(["Saracura"])

while queue:
    composer = queue.popleft()

    for partner in graph[composer]:
        if distances[partner] == float("inf"):
            distances[partner] = distances[composer] + 1
            queue.append(partner)

composers = [
    (composer, distance)
    for composer, distance in distances.items()
    if composer != "Saracura"
]

composers.sort(key=lambda composer: (composer[1], composer[0]))

for composer, distance in composers:
    if distance == float("inf"):
        print(f"{composer}: infinito")
    else:
        print(f"{composer}: {distance}")
