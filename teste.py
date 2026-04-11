import string

texto = "Olá, mundo! Como você está? (Tudo bem?)"

# Cria uma tabela de mapeamento que troca cada pontuação por None
tabela = str.maketrans("", "", string.punctuation)
texto_limpo = texto.translate(tabela)

print(texto_limpo)
# Saída: Olá mundo Como você está Tudo bem
