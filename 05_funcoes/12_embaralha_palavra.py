import random

def embaralha_palavra(palavra):
    palavra_padronizada = palavra.lower()
    caracteres = list(palavra_padronizada)
    caracteres_embaralhados = random.sample(caracteres, len(caracteres))
    string_embaralhada = "".join(caracteres_embaralhados)
    return string_embaralhada

palavra_original = input("\nDigite uma palavra para embaralhar: ")
palavra_embaralhada = embaralha_palavra(palavra_original)

print(f"\nPalavra original (padronizada): {palavra_original.lower()}")
print(f"Palavra embaralhada: {palavra_embaralhada}")
print(f"Outra combinação possível: {embaralha_palavra(palavra_original)}")
