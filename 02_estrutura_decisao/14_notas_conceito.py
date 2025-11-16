nota_1 = float(input("\nDigite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

if media >= 9.0:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    status = "APROVADO"
else:
    status = "REPROVADO"

print()

print("-" * 40)
print(f"{'* * RESULTADOS * *':^40}")
print("-" * 40)
print(f"NOTA.........: {media:.2f}")
print(f"CONCEITO.....: {conceito}")
print(f"RESULTADO....: {status}")
print("-" * 40)

print()