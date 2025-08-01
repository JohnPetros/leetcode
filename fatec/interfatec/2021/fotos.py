import sys


def resolver_fotos_ana_maria():
    """
    Solução para o Problema D: As Fotos da Ana Maria.
    Calcula e imprime o histograma de uma imagem.
    """

    # 1. Lê todos os valores nk da entrada e os armazena em uma lista.
    # Cada valor é um número de pixels para um nível de intensidade.
    try:
        pixels_por_nivel = [int(line.strip()) for line in sys.stdin]
    except (ValueError, IndexError):
        print("Erro: A entrada contém valores não numéricos ou está vazia.")
        return

    if not pixels_por_nivel:
        return  # Não faz nada se a entrada estiver vazia

    # 2. Calcula o número total de pixels (n) somando todas as contagens.
    total_pixels = sum(pixels_por_nivel)

    if total_pixels == 0:
        # Evita divisão por zero se a entrada for composta apenas de zeros.
        for _ in pixels_por_nivel:
            print("0.000")
        return

    # 3. Itera sobre cada nk, calcula a probabilidade pr(k) e imprime o resultado[cite: 195].
    for nk in pixels_por_nivel:
        # A fórmula é pr(k) = nk / n
        probabilidade = nk / total_pixels
        # Formata a saída com 3 casas decimais, como no exemplo[cite: 211, 212, 213].


# Executa a função principal
if __name__ == "__main__":
    resolver_fotos_ana_maria()
