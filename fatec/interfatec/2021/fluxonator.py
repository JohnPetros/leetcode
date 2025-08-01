# --- Início do Código Corrigido ---


def solve_fluxonator(entries):
    """
    Simula o dispositivo Fluxonator para uma dada sequência de entradas.

    Args:
      entries: Uma string com a sequência de entradas (ex: "ABAA").

    Returns:
      A string com a sequência de saídas correspondente (ex: "DDED").
    """
    # True representa 'Esquerda', False representa 'Direita'
    # O dispositivo é resetado com todas as alavancas para a esquerda [cite: 77]
    l1, l2, l3 = True, True, True

    exits = ""

    for entry in entries:
        passed = []  # Registra as alavancas pelas quais um elétron passa

        if entry == "A":
            passed.append(1)
            if l1:  # Se L1 está na Esquerda
                exits += "D"
            else:  # Se L1 está na Direita, o caminho continua
                passed.append(2)
                if l2:  # Se L2 está na Esquerda
                    exits += "D"
                else:  # Se L2 está na Direita
                    exits += "E"

        elif entry == "B":
            passed.append(2)
            if l2:  # Se L2 está na Esquerda, o caminho continua para L1
                passed.append(1)
                exits += "D"  # A saída é sempre D neste caso
            else:  # Se L2 está na Direita, o caminho continua para L3
                passed.append(3)
                exits += "E"  # A saída é sempre E neste caso

        elif entry == "C":
            passed.append(3)
            if l3:  # Se L3 está na Esquerda, o caminho continua para L2
                passed.append(2)
                if l2:  # Se L2 está na Esquerda, o caminho continua para L1
                    passed.append(1)
                    exits += "D"
                else:  # Se L2 está na Direita
                    exits += "E"
            else:  # Se L3 está na Direita
                exits += "E"

        # Após o elétron sair, cada alavanca pela qual ele passou inverte a posição
        if 1 in passed:
            l1 = not l1
        if 2 in passed:
            l2 = not l2
        if 3 in passed:
            l3 = not l3

    return exits


# --- Testando com os exemplos do problema ---

# Exemplo 1 [cite: 99]
entries1 = "ABAA"
print(f"Entrada: {entries1}")
print(f"Saída:   {solve_fluxonator(entries1)}")
print("-" * 20)

# Exemplo 2 [cite: 99]
entries2 = "BBBAABCCC"
print(f"Entrada: {entries2}")
print(f"Saída:   {solve_fluxonator(entries2)}")
print("-" * 20)

# Exemplo 3 [cite: 99]
entries3 = "BCABCBCAAAAACBBABACCCA"
print(f"Entrada: {entries3}")
print(f"Saída:   {solve_fluxonator(entries3)}")
print("-" * 20)
