def taylor(inteiro: int):
    PI = 3.1415
    r = inteiro * PI / 180
    soma = 0
    a = 1
    b = 1

    for i in range(1, 6):
        soma = soma + (a / b)
        a = a * (-(r**2))  # ai+1 = ai.(-r²)
        b = b * (2 * i - 1) * (2 * i)  # bi+1 = bi.(2i-1).(2i)

    quarta_casa = int(soma * 10000 % 10)

    if quarta_casa in [7, 8, 9]:
        return soma_com_vai_um(int(soma * 100), 1) / 100

    return int(soma * 1000) / 1000


def soma_com_vai_um(num1, num2):
    num1, num2 = str(num1)[::-1], str(num2)[::-1]

    max_length = max(len(num1), len(num2))
    vai_um = 0
    resultado = []

    for i in range(max_length):
        digito1 = int(num1[i]) if i < len(num1) else 0
        digito2 = int(num2[i]) if i < len(num2) else 0

        total = digito1 + digito2 + vai_um
        vai_um = total // 10
        resultado.append(total % 10)

    if vai_um:
        resultado.append(vai_um)

    return int("".join(map(str, resultado[::-1])))


inteiro = int(input("Entrada: "))

print(taylor(inteiro))
