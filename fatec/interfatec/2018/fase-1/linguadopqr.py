TESTE = True


def linguadopqr(phrase: str):
    parts = phrase.split()
    translation = parts[0]

    for index in range(1, len(parts)):
        curr = parts[index]
        prev = parts[index - 1]

        if (curr.startswith("PQ") and prev.startswith("PQ")) or curr in "?,.!":
            translation += curr
        elif curr.startswith("PQ") and prev == "R":
            translation += f" {curr}"

    print("".join(translation).replace("PQ", ""))


if TESTE:
    linguadopqr("PQEs PQtá R PQma PQlu PQco R , R PQMai PQke R ?")
    linguadopqr(
        "PQÔ R PQLou PQco R , R PQmeu R ! R PQEs PQse R PQfe PQra R PQa PQí R !"
    )
else:
    linguadopqr(input())
