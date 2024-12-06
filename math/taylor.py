from math import ceil


def reco(inteiro: int):
    PI = 3.1415
    r = inteiro * PI / 180
    soma = 0
    a = 1
    b = 1

    for i in range(1, 6):
        soma = soma + (a / b)
        a = a * (-(r**2))  # ai+1 = ai * (-r²)
        b = b * (2 * i - 1) * (2 * i)  # bi+1 = bi * (2 * i - 1) * (2 * i)

    quarta_casa = int(soma * 10000 % 10)

    if quarta_casa >= 7:
        return ceil(soma * 1000) / 1000

    return int(soma * 1000) / 1000


inteiro = int(input("Entrada: "))

print(reco(inteiro))
print("\n")
