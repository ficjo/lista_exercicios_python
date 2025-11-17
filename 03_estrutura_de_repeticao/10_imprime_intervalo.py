num_1 = int(input("\nDigite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

if num_1 < num_2:
    inicio = num_1
    fim = num_2
else:
    inicio = num_2
    fim = num_1

print()

for i in range(inicio, fim + 1):
    print(i)

print()
