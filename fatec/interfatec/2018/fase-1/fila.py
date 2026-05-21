TESTE = True


def fila(correct_passwords: list[str], passwords: list[str]):
    correct_count = 0
    incorrect_count = 0
    repeated_count = 0
    used_passwords = set()

    for password in passwords:
        if password in correct_passwords and password not in used_passwords:
            correct_count += 1
        elif password not in correct_passwords and password not in used_passwords:
            incorrect_count += 1

        if password in used_passwords:
            repeated_count += 1

        used_passwords.add(password)

    print(f"{correct_count} A")
    print(f"{incorrect_count} I")
    print(f"{repeated_count} R")
    print()


if TESTE:
    fila(["1C", "2W", "300C"], ["7", "1C", "9", "1B", "1C"])
    fila(["1C"], ["7", "7"])
else:
    correct_passwords_count = int(input())
    correct_passwords = input().split()[:correct_passwords_count]
    passwords_count = int(input())
    passwords = input().split()[:passwords_count]

    fila(correct_passwords, passwords)
