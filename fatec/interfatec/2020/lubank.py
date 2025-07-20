keyboard_inputs = [
    "7;y;d;s;z;B",
    "9;h;H;S;1;J",
    "10;2;Q;n;j;K",
    "11;c;W;9;v;o",
    "12;w;N;r;R;E",
    "1;4;6;7;3;Y",
    "2;U;q;u;F;k",
    "4;Z;0;p;g;X;8",
    "5;e;O;t;T;b",
    "3;x;L;D;I;f;m",
    "8;V;l;5;a;A",
    "6;i;M;P;G;C",
]

correct_logins_inputs = [
    "BiaCavalcante;abcXYZ",
    "AnaMaria;12345",
    "duda2;AbCdEfG",
]

logins_inputs = [
    "BiaCavalcante;8;5;11;4;1;4",
    "BiaCavalcante;8;7;6;3;7;7",
    "AnaMaria;9;10;1;1;8",
    "BiaCavalcante;8;7;6;3;7;7",
    "AnaMaria;9;10;1;1;8",
    "BiaCavalcante;8;7;6;3;7;7",
    "duda3;8;5;6;7;12;3;6;9",
    "duda2;8;5;6;7;12;3;6;9",
    "duda2;8;5;6;7;12;3;6",
    "BiaCavalcante;8;5;11;4;1;4",
    "duda2;8;5;6;7;12;3;6;12",
    "duda2;8;5;6;7;12;3;6;10",
    "duda2;8;5;6;7;12;3;6",
]

keyboard = {}

for input in keyboard_inputs:
    characters = input.split(";")
    keyboard[characters[0]] = characters[1:]

correct_logins = {}
incorrect_attemps = {}
blocked_users = set()

for input in correct_logins_inputs:
    username, password = input.split(";")
    correct_logins[username] = password
    incorrect_attemps[username] = 0

for input in logins_inputs:
    values = input.split(";")
    username = values[0]
    if username not in correct_logins:
        print(f"{username}: usuário inexistente")

    if username in correct_logins:
        if username in blocked_users:
            print(f"{username}: usuário bloqueado")
            continue

        correct_password = correct_logins[username]
        password = values[1:]

        is_correct = True
        if len(password) > len(correct_password):
            is_correct = False
        else:
            for index in range(len(correct_password)):
                if correct_password[index] not in keyboard[password[index]]:
                    is_correct = False

        if is_correct:
            print(f"{username}: acesso concedido")
            incorrect_attemps[username] = 0
        else:
            incorrect_attemps[username] += 1
            if incorrect_attemps[username] == 3:
                print(f"{username}: usuário bloqueado")
                blocked_users.add(username)
            else:
                print(f"{username}: acesso negado")
