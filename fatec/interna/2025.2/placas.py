import string

TESTE = True


def is_letter(value: str):
    return value.isalpha() and value in string.ascii_uppercase


def is_number(value: str):
    return value.isdigit()


def placas(plate: str):
    if len(plate) != 7:
        print("INVALIDA")
        return

    if (
        is_letter(plate[0])
        and is_letter(plate[1])
        and is_letter(plate[2])
        and is_number(plate[3])
        and is_letter(plate[4])
        and is_number(plate[5])
        and is_number(plate[6])
    ):
        print("VALIDA")
        return

    print("INVALIDA")


if TESTE:
    placas("ABC4E67")
    placas("PQR1S23")
    placas("FATEC2026")
else:
    placas(input())
