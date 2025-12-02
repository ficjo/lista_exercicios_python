idades = [
    12, 14, 13, 15, 11, 16, 14, 13, 12, 17,
    15, 14, 13, 16, 12, 15, 14, 11, 17, 13,
    16, 14, 15, 12, 13, 14, 15, 16, 13, 14
]

alturas = [
    1.55, 1.62, 1.50, 1.70, 1.48, 1.72, 1.60, 1.52, 1.49, 1.75,
    1.68, 1.61, 1.53, 1.73, 1.50, 1.66, 1.59, 1.47, 1.78, 1.54,
    1.71, 1.63, 1.67, 1.51, 1.56, 1.60, 1.64, 1.69, 1.55, 1.61
]

soma_alturas = sum(alturas)
media_altura = sum(alturas) / len(alturas)

contador = 0

for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador += 1

print(f"\nMédia das alturas: {media_altura:.2f}")
print(f"Total de alunos > 13 anos e altura < média: {contador}\n")