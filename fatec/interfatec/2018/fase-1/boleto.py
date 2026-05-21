from datetime import date

TESTE = True


def boleto(boletos: list[str]):
    def to_date(str):
        return date(
            day=int(str[0:2]),
            month=int(str[2:4]),
            year=int("20" + str[4:6]),
        )

    regular_amount = 0
    irregular_amount = 0

    for boleto in boletos:
        deadline = boleto[4:10]
        integer_amount = boleto[10:16]
        float_amount = boleto[16:18]
        payday = boleto[22:28]

        if to_date(deadline) >= to_date(payday):
            regular_amount += float(f"{integer_amount}.{float_amount}")
        else:
            irregular_amount += float(f"{integer_amount}.{float_amount}")

    print(f"{regular_amount:.2f}-ADIMPLENTE")
    print(f"{irregular_amount:.2f}-INADIMPLENTE")


if TESTE:
    boleto(
        [
            "006712101800023230012317051815",
            "003808111800044000065217051816",
            "008907061700023150235617051817",
            "006329051800023234672317051812",
            "003220041800056290341117051814",
        ]
    )
    boleto(
        [
            "006731101800123230012310011815",
            "003816111801213000065227051816",
            "008917061700233150235614051817",
            "006329051809923234672323071812",
            "003230041800156290341107051814",
        ]
    )
else:
    import sys

    billets = [line.rstrip("\n") for line in sys.stdin]
    boleto(billets)
