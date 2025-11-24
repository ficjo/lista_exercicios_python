notas = []
soma = 0.0

print()

for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)
    soma += nota

media = soma / len(notas)

print("\nResultados\n")
print(f"Notas: {notas}")
print(f"Soma das notas: {soma}")
print(f"Média: {media:.2f}\n")
    