medias = []

for i in range(10):
    print(f"\nAluno: {i}:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))
    
    media = (n1 + n2 + n3 + n4) / 4
    medias.append(media)

medias_aprovadas = [ media for media in medias if media >= 7 ]

print(f"\nMédias: {medias}")
print(f"Médias dos aprovados: {medias_aprovadas}")
print(f"Total de alunos aprovados: {len(medias_aprovadas)}\n")