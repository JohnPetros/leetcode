from heapq import heappush, heappop

inputs = [
    "0 210 2000",
    "0 211 450",
    "0 212 950",
    "300 213 1360",
    "350 214 200",
    "500 215 280",
]

future_batches = []
ready_batches = []
outputs = []

current_time = 0

for input in inputs:
    start, id, time = input.split()
    future_batches.append((id, int(start), int(time)))

future_batches.sort(key=lambda batch: batch[1], reverse=True)

while future_batches or ready_batches:
    while future_batches and future_batches[-1][1] <= current_time:
        ready_batch = future_batches.pop()
        heappush(ready_batches, ((ready_batch[2], ready_batch[0]), ready_batch))

    if ready_batches:
        _, batch = heappop(ready_batches)
        end_time = current_time + batch[2]
        outputs.append((batch[0], current_time, end_time))
        current_time += end_time
    elif future_batches:
        current_time = future_batches[-1][1]


for id, start_time, end_time in outputs:
    print(f"{id} {start_time} {end_time}")
