# Função para determinar o tamanho da maior subsequência ordenada de uma lista
def maior_subsequencia_ordenada(alturas):
    n = len(alturas)
    dp = [1] * n  # Vetor para armazenar o tamanho da maior subsequência até cada índice

    for i in range(1, n):
        for j in range(i):
            print("i", alturas[i])
            print("j", alturas[j])
            if alturas[i] >= alturas[j]:  # Permite alturas iguais consecutivas
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp)
    return max(dp)  # Retorna o maior valor em dp


# Entrada de dados
# tamanho_grupo = int(input())
alturas_grupo1 = "150 149 167 175".split()
alturas_grupo2 = "161 173 172 180".split()

# Cálculo das maiores subsequências ordenadas
organizados_grupo1 = maior_subsequencia_ordenada(alturas_grupo1)
organizados_grupo2 = maior_subsequencia_ordenada(alturas_grupo2)

# Determinação do vencedor
if organizados_grupo1 > organizados_grupo2:
    print(f"1 {organizados_grupo1}")
elif organizados_grupo2 > organizados_grupo1:
    print(f"2 {organizados_grupo2}")
else:
    print(f"EMPATE {organizados_grupo1}")
