total_pares = 0
soma_pares = 0
total_impares = 0
soma_impares = 0

print()

for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        total_pares += 1
        soma_pares += num
    else:
        total_impares += 1
        soma_impares += num

print("\n* * * RESULTADOS * * *")
print(f"Total de números pares      : {total_pares}")
print(f"Soma dos números pares      : {soma_pares}")
print(f"Total de números impares    : {total_impares}")
print(f"Soma dos números impares    : {soma_impares}\n")
