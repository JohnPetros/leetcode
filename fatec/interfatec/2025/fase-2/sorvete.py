client_count = 6
max_difference = 0
clients = [3, 1, 4, 1, 5, 9]
clients.sort()

group_count = 0
index = 0
while index < client_count:
    group_count += 1

    temp_base = clients[index]

    index += 1

    while index < client_count and (clients[index] - temp_base) <= max_difference:
        index += 1


def get_minimum_groups(client_count, max_difference, clients):
    clients.sort()
    group_count = 0
    index = 0


print(f"Número mínimo de grupos: {group_count}")
