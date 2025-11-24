vetor_principal = []

print()

for i in range(20):
    numero = int(input(f"Digite um número: "))
    vetor_principal.append(numero)

vetor_pares = [ num for num in vetor_principal if num % 2 == 0 ]
vetor_impares = [ num for num in vetor_principal if num % 2 != 0 ]

print(f"\nNúmeros digitados: {vetor_principal}")
print(f"Números pares: {vetor_pares}")
print(f"Números ímpares: {vetor_impares}\n")
