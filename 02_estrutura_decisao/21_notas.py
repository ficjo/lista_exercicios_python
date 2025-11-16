MIN_SAQUE = 10
MAX_SAQUE = 600

valor_saque = int(input("\nDigite o valor do saque (Mínimo R$10, Máximo R$600): "))

if valor_saque < MIN_SAQUE or valor_saque > MAX_SAQUE:
    print(f"Erro: O valor do saque deve estar entre R${MIN_SAQUE},00 e R${MAX_SAQUE},00.")
    exit()

valor_restante = valor_saque

print(f"\nPara sacar R${valor_saque},00, o programa fornece:")
print("-" * 40)

qnt_100 = valor_restante // 100
valor_restante = valor_restante % 100
if qnt_100 > 0:
    print(f"Notas de 100: {qnt_100}")

qnt_50 = valor_restante // 50
valor_restante = valor_restante % 50
if qnt_50 > 0:
    print(f"Notas de 50: {qnt_50}")

qnt_10 = valor_restante // 10
valor_restante = valor_restante % 10
if qnt_10 > 0:
    print(f"Notas de 10: {qnt_10}")

qnt_5 = valor_restante // 5
valor_restante = valor_restante % 5
if qnt_5 > 0:
    print(f"Notas de 5: {qnt_5}")

qnt_1 = valor_restante
if qnt_1 > 0:
    print(f"Notas de 1: {qnt_1}")

print("-" * 40)

print()