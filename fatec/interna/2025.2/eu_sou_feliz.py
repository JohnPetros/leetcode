import unicodedata
import re

TESTE = True


def remove_accentuation(string):
    return "".join(
        char
        for char in unicodedata.normalize("NFD", string)
        if unicodedata.category(char) != "Mn"
    )


def eu_sou_feliz(phrase: str):
    is_feliz = False
    is_aprendiz = False

    phrase = remove_accentuation(phrase).lower()
    phrase = " ".join(re.findall(r"[a-záàãâéêíóôõúüç]+", phrase))

    words = phrase.split()
    is_feliz = "feliz" in words
    is_aprendiz = "aprender" in words or "aprendendo" in words

    print(phrase)
    print(len(set(words)))

    if is_feliz and is_aprendiz:
        print("FELIZ E APRENDIZ")
    elif is_feliz:
        print("FELIZ")
    elif is_aprendiz:
        print("APRENDIZ")
    else:
        print("NORMAL")


if TESTE:
    eu_sou_feliz("Eu sou feliz, vou aprender mais!")
    eu_sou_feliz("Hoje estou muito feliz por estar aqui.")
else:
    eu_sou_feliz(input())
