vetor = [1, 2, 3, 4, 5]

mult = 1
soma = 0

for i in vetor:
    mult *= i
    soma += i

print(f"\nNúmeros: {vetor}")
print(f"Soma: {soma}")
print(f"Multiplicação: {mult}\n")