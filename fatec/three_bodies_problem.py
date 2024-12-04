def three_bodies_problem(bodies):
    if bodies[0] < bodies[-1] / 100:
        return "Problema de 2 corpos"

    return "Problema de 3 corpos"


while True:
    try:
        bodies = input().split(" ")
        three_bodies_problem(list(map(int, bodies)))
    except EOFError:
        break


# print(three_bodies_problem([2, 4, 6]))
# print(three_bodies_problem([2, 4, 200]))
# print(three_bodies_problem([1, 4, 200]))
