
soma = 0
contador = 1
num_cds = int(input("\nDigite o número de CDs: "))

print()

while contador <= num_cds:
    valor_cd = float(input(f"Digite o valor do {contador}º CD: "))
    soma += valor_cd
    contador += 1

media = soma / num_cds

print("\n* * * RESULTADOS * * *")
print(f"Número de CDs   : {num_cds}")
print(f"Total gasto     : R$ {soma}")
print(f"Média por CD    : R$ {media:.2f}\n")