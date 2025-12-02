idades = []
alturas = []

print()

for i in range(5):
    print(f"Pessoa {i + 1}:")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    idades.append(idade)
    alturas.append(altura)

print("\nOrdem inversa:")
for i in range(len(idades) - 1, -1, -1):
    print(f"Pessoa: {i + 1}")
    print(f"Idade: {idades[i]}")
    print(f"Altura: {alturas[i]}")

print()