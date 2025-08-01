from itertools import permutations


def calculate_max_damage(knights_count, cards_str):
    """
    Calcula o dano máximo possível no jogo Power Up Battle, considerando divisão inteira.

    Args:
        knights_count: O número inicial de cavaleiros.
        cards_str: Uma string contendo as cartas na mão.

    Returns:
        O dano máximo possível como um inteiro.
    """
    cards = list(cards_str)
    max_total_damage = 0

    # Inicia o dano máximo com o estado inicial (nenhuma carta usada)
    if knights_count > 0:
        max_total_damage = knights_count

    # Testa todas as combinações de cartas, de 1 até o total de cartas
    for i in range(1, len(cards) + 1):
        # Gera todas as permutações para o subconjunto atual de cartas
        for p in set(permutations(cards, i)):
            # Reinicia o estado para cada permutação
            current_knights = [1] * knights_count

            # Aplica os efeitos de cada carta na permutação
            for card in p:
                if not current_knights:  # Se não houver mais cavaleiros
                    break

                if card == "T":
                    # Aumenta o ataque de cada cavaleiro
                    current_knights = [k + 1 for k in current_knights]
                elif card == "R":
                    # Cada cavaleiro recebe bônus com base no número de aliados
                    # A divisão deve ser inteira, como deduzido dos exemplos.
                    bonus = len(current_knights) // 2
                    current_knights = [k + bonus for k in current_knights]
                elif card == "S":
                    # Sacrifica o cavaleiro de maior poder para maximizar o bônus
                    sacrificed_power = max(current_knights)
                    current_knights.remove(sacrificed_power)
                    if current_knights:
                        # A divisão deve ser inteira, como deduzido dos exemplos.
                        bonus = sacrificed_power // 2
                        current_knights = [k + bonus for k in current_knights]

            # Calcula o dano total para esta permutação e atualiza o máximo
            total_damage = sum(current_knights)
            if total_damage > max_total_damage:
                max_total_damage = total_damage

    return max_total_damage


# --- Verificação com os exemplos do problema ---

# Exemplo 1: 4 3 RTT -> 20
print(f"Exemplo 1: {calculate_max_damage(4, 'RTT')}")  # Saída esperada: 20

# Exemplo 2: 5 3 RST -> 24
print(f"Exemplo 2: {calculate_max_damage(5, 'RST')}")  # Saída esperada: 24

# Exemplo 3: 5 2 SS -> 5
print(
    f"Exemplo 3: {calculate_max_damage(5, 'SS')}"
)  # Saída esperada: 5 (não usar nenhuma carta é melhor)

# Exemplo 4: 21 5 STSRS -> 720
print(f"Exemplo 4: {calculate_max_damage(21, 'STSRS')}")  # Saída esperada: 720

# Exemplo 5: 33 5 TSTTR -> 960
print(f"Exemplo 5: {calculate_max_damage(33, 'TSTTR')}")  # Saída esperada: 960
