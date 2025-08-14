from heapq import heappush, heappop

inputs = [
    "10 AMARELO",
    "12 VERMELHO",
    "beep",
    "33 AZUL",
    "34 AMARELO",
    "beep",
    "beep",
    "51 VERDE",
    "beep",
    "beep",
]

queue = []

priority = {
    "VERMELHO": 1,
    "LARANJA": 2,
    "AMARELO": 3,
    "VERDE": 4,
    "AZUL": 5,
}

arrival_time = 0

for input in inputs:
    if input == "beep" and queue:
        _, _, password = heappop(queue)
        print(password)
    else:
        password, risk = input.split()
        heappush(queue, (priority[risk], arrival_time, password))
        arrival_time += 1
