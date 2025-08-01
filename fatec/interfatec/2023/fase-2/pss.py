candidates_count = 4
candidates = [
    (1, 0, 1, 1, 5),
    (0, 0, 0, 0, 5),
    (1, 1, 0, 0, 5),
    (1, 1, 1, 1, 2),
]


for index in range(candidates_count):
    g, e, a, d, expierence = candidates[index]

    if (g or d) and expierence >= 3:
        print(f"Cand. {index + 1} deferido (comprovar 3 anos)")

    elif (g and e) and expierence >= 5:
        print(f"Cand. {index + 1} deferido (comprovar 5 anos)")

    else:
        if (g or a) or (g and e):
            print(f"Cand. {index + 1}. INDEFERIDO (exp)")
        else:
            print(f"Cand. {index + 1}. INDEFERIDO (acad)")
