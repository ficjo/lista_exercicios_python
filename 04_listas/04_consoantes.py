vetor_caracteres = []
vetor_consoantes = []
vogais = "aeiou"

print()

for i in range(10):
    caractere = input(f"Digite o {i + 1}º caractere: ").lower()
    vetor_caracteres.append(caractere)
    if caractere.isalpha() and caractere not in vogais:
        vetor_consoantes.append(caractere)

print(f"\nCaracteres lidos: {vetor_caracteres}")
print(f"Total de consoantes: {len(vetor_consoantes)}")
print(f"Consoantes lidas: {vetor_consoantes}\n")