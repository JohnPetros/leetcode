import sys


def resolver_blaittland():
    """
    Soluciona o Problema A: Blaittland da Maratona de Programação InterFatecs 2023.

    Esta função calcula o número total de vezes que os livros foram lidos e
    determina se é possível garantir que um estudante de Sistemas de Banco de Dados
    leu um livro, com base na ordem final dos livros em uma estante.
    """
    try:
        # [cite_start]A primeira linha contém o número de livros V (1 <= N <= 26). [cite: 52]
        # Embora N seja lido, o comprimento da string da linha seguinte também pode ser usado.
        linha_n = sys.stdin.readline()
        if not linha_n:
            return
        n = int(linha_n)

        # [cite_start]A segunda linha contém a string de N letras maiúsculas representando a ordem final. [cite: 53]
        ordem_final = sys.stdin.readline().strip()

    except (IOError, ValueError):
        return

    # Um dicionário para armazenar quantas vezes cada livro foi lido.
    leituras_por_livro = {}

    # Variável para o número total de leituras, que corresponde ao total de inversões.
    total_leituras = 0

    # Itera pela ordem final para contar as inversões.
    # Uma inversão ocorre quando um livro aparece antes de outro que é alfabeticamente menor.
    # [cite_start]O número de inversões de um livro corresponde a quantas vezes ele foi lido. [cite: 46]
    for i in range(n):
        livro_atual = ordem_final[i]
        if livro_atual not in leituras_por_livro:
            leituras_por_livro[livro_atual] = 0

        for j in range(i + 1, n):
            outro_livro = ordem_final[j]
            if livro_atual > outro_livro:
                total_leituras += 1
                leituras_por_livro[livro_atual] += 1

    print(leituras_por_livro)
    # Encontra o número máximo de leituras para um único livro.
    max_leituras_individuais = 0
    if leituras_por_livro:
        max_leituras_individuais = max(leituras_por_livro.values())

    # [cite_start]Se um livro foi lido mais de cinco vezes[cite: 47], podemos afirmar com certeza
    # [cite_start]que um estudante de Sistemas de Banco de Dados o leu. [cite: 55]
    if max_leituras_individuais > 5:
        print("A Database Systems student read a book.")
    else:
        # [cite_start]Caso contrário, imprimimos o número total de vezes que qualquer livro foi pego. [cite: 55]
        print(total_leituras)


# Executa a função para resolver o problema.
resolver_blaittland()
