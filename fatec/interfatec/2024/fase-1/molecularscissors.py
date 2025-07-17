def get_complement(nucleotide):
    """Retorna o complemento de um nucleotídeo"""
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return complement_map[nucleotide]


def is_valid_restriction_site(sequence):
    """
    Verifica se uma sequência é um sítio de restrição válido.
    Uma sequência é válida se for igual à sua sequência complementar reversa.
    """
    n = len(sequence)

    # Gera a sequência complementar
    complement = "".join(get_complement(nucleotide) for nucleotide in sequence)

    # Verifica se a sequência original é igual ao complemento reverso
    return sequence == complement[::-1]


def find_restriction_sites(dna_sequence):
    """
    Encontra todos os sítios de restrição em uma sequência de DNA
    usando sliding window de tamanhos variados.
    """
    n = len(dna_sequence)
    max_length = 0
    best_start = -1

    # Sliding window - testamos todos os tamanhos possíveis
    for length in range(2, n + 1):  # Começamos com tamanho 2 (mínimo para um sítio)
        for start in range(n - length + 1):
            # Extrai a subsequência atual
            subsequence = dna_sequence[start : start + length]

            # Verifica se é um sítio de restrição válido
            if is_valid_restriction_site(subsequence):
                # Se encontramos um sítio maior, ou o primeiro sítio deste tamanho
                if length > max_length:
                    max_length = length
                    best_start = start

    return best_start, max_length


def solve_molecular_scissors():
    """
    Solução principal para o problema Molecular Scissors
    """
    import sys

    try:
        for line in sys.stdin:
            dna_sequence = line.strip()
            if not dna_sequence:
                continue

            start_pos, length = find_restriction_sites(dna_sequence)

            if length == 0:
                print("false")
            else:
                # Posição é 1-indexed conforme o problema
                print(f"{start_pos + 1} {length}")

    except EOFError:
        pass


# Função para testar com exemplos
def test_examples():
    """Testa com os exemplos fornecidos"""
    test_cases = [
        "GAATTC",
        "AAGCTTTCGAAGCTTAAAAAA",
        "CCGGAAGGCCGG",
        "ATT",
        "AAGCTCAA",
        "AA",
        "AAGG",
    ]

    expected_outputs = ["1 6", "1 6", "1 4", "false", "2 4", "false", "false"]

    print("=== Testando exemplos ===")
    for i, dna in enumerate(test_cases):
        start_pos, length = find_restriction_sites(dna)

        if length == 0:
            result = "false"
        else:
            result = f"{start_pos + 1} {length}"

        print(f"Input: {dna}")
        print(f"Output: {result}")
        print(f"Expected: {expected_outputs[i]}")
        print(f"✓ Correct" if result == expected_outputs[i] else "✗ Wrong")
        print()


# Executa os testes
if __name__ == "__main__":
    test_examples()

    # Descomente a linha abaixo para executar a solução principal
    # solve_molecular_scissors()
