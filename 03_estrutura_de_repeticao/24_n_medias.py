soma_notas = 0
num_notas = int(input("\nDigite o número de notas: "))

for i in range(num_notas):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    soma_notas += nota

media = soma_notas / num_notas

print(f"\nMédia final: {media:.2f}\n")