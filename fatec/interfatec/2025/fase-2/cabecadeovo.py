import time  # Vamos adicionar para medir o tempo (apenas para demonstração)


def soma_dos_digitos(n_str):
    """
    Calcula a soma dos dígitos a partir de uma string.
    É um pouco mais rápido não converter para string toda vez.
    """
    soma = 0
    for digito in n_str:
        soma += int(digito)
    return soma


def encontrar_senha(A, B):
    maior_soma = -1
    senha_resultado = 0

    # O loop principal
    # range(A, B + 1) irá iterar 10 milhões de vezes
    for numero in range(A, B + 1):
        # Esta operação é muito rápida
        soma_atual = soma_dos_digitos(str(numero))

        # Esta é uma simples comparação de inteiros
        if soma_atual > maior_soma:
            maior_soma = soma_atual
            senha_resultado = numero

    return senha_resultado, maior_soma


# --- Execução ---

# Definindo o intervalo que você pediu
start = 1
end = 10**7  # 10 milhões

print(f"Testando o intervalo de {start} a {end}...")
inicio_tempo = time.time()

# Executa a função
resultado, soma = encontrar_senha(start, end)

fim_tempo = time.time()

# --- Resultados ---
print("\n--- Resultado ---")
print(f"A senha encontrada é: {resultado}")
print(f"A maior soma de dígitos foi: {soma}")
print(f"Tempo de execução: {fim_tempo - inicio_tempo:.4f} segundos")
