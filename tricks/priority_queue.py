import heapq

queue = []
heapq.heappush(queue, (2, "Médio"))
heapq.heappush(queue, (1, "Alta prioridade"))
heapq.heappush(queue, (3, "Baixa prioridade"))

## Se for necessário pode se colocar mais números para definir a prioridade Ex.:
## (4, 5, "Baixa prioridade mista")

while queue:
    priority, value = heapq.heappop(queue)
    print(f"{priority}: {value}")
