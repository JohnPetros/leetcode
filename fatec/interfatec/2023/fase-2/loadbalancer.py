servers_count = 3
requests_count = 7
request_number = 6
requests = [
    (1, 10),
    (30, 1000),
    (2, 20),
    (5, 80),
    (3, 50),
    (10, 200),
    (9, 500),
]

servers = [None for _ in range(servers_count)]

for request in requests:
    server_index = 0
    while server_index < len(servers) and servers[server_index]:
        server_request = servers[server_index]
        if server_request[1] < request[0]:
            servers[server_index] = request
            break
        else:
            server_index += 1

    if server_index < len(servers):
        servers[server_index] = request


print(servers)

for index in range(servers_count):
    if servers[index] == requests[request_number - 1]:
        print(index + 1)
        break
