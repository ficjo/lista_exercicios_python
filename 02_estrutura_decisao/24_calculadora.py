num_1 = int(input("\nDigite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

print("\nEscolha uma operação:")
print("[1] - Soma")
print("[2] - Subtração")
print("[3] - Multiplicação")
print("[4] - Divisão")
operacao = int(input("\nDigite o número da operação: "))

resultado = 0
nome_operacao = ""

match operacao:
    case 1:
        resultado = num_1 + num_2
        nome_operacao = "Soma"
    case 2:
        resultado = num_1 - num_2
        nome_operacao = "Subtração"
    case 3:
        resultado = num_1 * num_2
        nome_operacao = "Multiplicação"
    case 4:
        resultado = num_1 / num_2
        nome_operacao = "Divisão"
    case _:
        print("ERRO: Operação inválida.")

print()

print("=" * 40)
print(f"OPERAÇÃO    : {nome_operacao}")
print(f"RESULTADO   : {resultado}")
print(f"O NÚMERO É  : {'Par' if resultado % 2 == 0 else 'Ímpar'} ")
print(f"            : {'Positivo' if resultado >= 0 else 'Negativo'}")
print(f"            : {'Inteiro' if resultado == int(resultado) else 'Decimal'}\n")
print("=" * 40)