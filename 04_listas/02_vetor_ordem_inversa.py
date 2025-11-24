vetor = []

print()

for i in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)

vetor_inverso = vetor[::-1]

print()
print(vetor_inverso)
print()

# Alternativa
for i in range(len(vetor) -1, -1, -1):
    print(vetor[i])

print()