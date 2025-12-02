alunos = [
    {"idade": 12, "altura": 1.55},
    {"idade": 14, "altura": 1.62},
    {"idade": 13, "altura": 1.50},
    {"idade": 15, "altura": 1.70},
    {"idade": 11, "altura": 1.48},
    {"idade": 16, "altura": 1.72},
    {"idade": 14, "altura": 1.60},
    {"idade": 13, "altura": 1.52},
    {"idade": 12, "altura": 1.49},
    {"idade": 17, "altura": 1.75},
    {"idade": 15, "altura": 1.68},
    {"idade": 14, "altura": 1.61},
    {"idade": 13, "altura": 1.53},
    {"idade": 16, "altura": 1.73},
    {"idade": 12, "altura": 1.50},
    {"idade": 15, "altura": 1.66},
    {"idade": 14, "altura": 1.59},
    {"idade": 11, "altura": 1.47},
    {"idade": 17, "altura": 1.78},
    {"idade": 13, "altura": 1.54},
    {"idade": 16, "altura": 1.71},
    {"idade": 14, "altura": 1.63},
    {"idade": 15, "altura": 1.67},
    {"idade": 12, "altura": 1.51},
    {"idade": 13, "altura": 1.56},
    {"idade": 14, "altura": 1.60},
    {"idade": 15, "altura": 1.64},
    {"idade": 16, "altura": 1.69},
    {"idade": 13, "altura": 1.55},
    {"idade": 14, "altura": 1.61}
]

soma_alturas = 0

for aluno in alunos:
    soma_alturas += aluno.get("altura")

media = soma_alturas / len(alunos)

contador = 0

for aluno in alunos:
    if aluno.get("idade") > 13 and aluno.get("altura") < media:
        contador += 1

print(f"\nMédia as alturas: {media:.2f}")
print(f"Total: {contador}\n")
