alunos = [
    (12, 1.55), (14, 1.62), (13, 1.50), (15, 1.70), (11, 1.48),
    (16, 1.72), (14, 1.60), (13, 1.52), (12, 1.49), (17, 1.75),
    (15, 1.68), (14, 1.61), (13, 1.53), (16, 1.73), (12, 1.50),
    (15, 1.66), (14, 1.59), (11, 1.47), (17, 1.78), (13, 1.54),
    (16, 1.71), (14, 1.63), (15, 1.67), (12, 1.51), (13, 1.56),
    (14, 1.60), (15, 1.64), (16, 1.69), (13, 1.55), (14, 1.61)
]

soma = 0
for idade, altura in alunos:
    soma += altura

media = soma / len(alunos)

contador = 0

for idade, altura in alunos:
    if idade > 13 and altura < media:
        contador += 1

print(f"\nMédia das alturas: {media:.2f}")
print(f"Total: {contador}\n")