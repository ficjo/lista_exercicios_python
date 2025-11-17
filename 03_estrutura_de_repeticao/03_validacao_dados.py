nome = input("\nDigite um nome: ")
while len(nome) <= 3:
    print("ERRO: O nome deve ter mais de 3 caracteres.")
    nome = input("Digite o nome novamente: ")

while True:
    idade = int(input("\nDigite uma idade: "))
    if idade >= 0 and idade <= 150:
        break
    else:
        print("ERRO: A idade deve estar entre 0 e 150.")

while True:
    salario = float(input("\nDigite o salário: "))
    if salario > 0:
        break
    else:
        print("ERRO: O salário deve ser maior que 0.")

while True:
    estado_civil = input("\nDigite o estado civil [S, C, V, D]: ").upper()
    if estado_civil not in ('S', 'C', 'V', 'D'):
        print("ERRO: Estado civil inválido.")
        estado_civil = input("Digite o estado civil [S, C, V, D]: ")
    else:
        break

print("\nRESULTADOS")
print(f"Nome            : {nome}")
print(f"Idade           : {idade}")
print(f"Salário         : R$ {salario:.2f}")
print(f"Estado civil    : {estado_civil.upper()}\n")
