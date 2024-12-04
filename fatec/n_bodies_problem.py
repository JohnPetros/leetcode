def n_bodies_problem(bodies):
    bodies.sort()
    greatest_body = bodies[-1] / 100
    n_bodies_count = 0

    for index in range(len(bodies) - 1):
        if bodies[index] >= greatest_body:
            n_bodies_count += 1

    if n_bodies_count <= 2:
        return "Problema de 2 corpos"

    return "Problema de N corpos"


# while True:
#     try:
#         bodies_count = int(input())
#         bodies = map(int, (input().split(" ")))
#         n_bodies_problem(bodies)
#     except EOFError:
#         break


print(n_bodies_problem([2, 4, 200]))
print(n_bodies_problem([1, 2, 3, 4, 500]))
# print(n_bodies_problem([1, 4, 200]))
