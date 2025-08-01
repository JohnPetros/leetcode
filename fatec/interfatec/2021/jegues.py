inputs = [
    "Willa 65877 128839 207488",
    "Hayley 65287 124817 193510",
    "Ina 60175 122192 198273",
    "Ezekiel 78636 121501 198047",
    "Desirae 69080 134192 216968",
    "Xandra 62580 136605 198388",
    "Gillian 75148 134331 199639",
    "Pascale 71783 130409 192810",
    "Fay 68518 121211 191793",
    "Roth 65954 131476 214952",
]

results = []

for input in inputs:
    name, t1, t2, t3 = input.strip().split()
    results.append((name, int(t1), int(t2), int(t3)))

t1_winners = sorted(results, key=lambda result: result[1])
t2_winners = sorted(results, key=lambda result: result[2])
t3_winners = sorted(results, key=lambda result: result[3])

print(f"T1 {t1_winners[0][0]} {t1_winners[1][0]} {t1_winners[2][0]}")
print(f"T2 {t2_winners[0][0]} {t2_winners[1][0]} {t2_winners[2][0]}")
print(f"CHEGADA {t3_winners[0][0]} {t3_winners[1][0]} {t3_winners[2][0]}")
