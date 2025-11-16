salario_atual = float(input("\nDigite o salário atual: "))
percentual_aumento = 0

if salario_atual <= 200.0:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

fator_aumento = percentual_aumento / 100
valor_aumento = salario_atual * fator_aumento
novo_salario = salario_atual + valor_aumento

print("\n* * * * RELATÓRIO * * * *")
print(f"Salário antes do reajuste:   R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento:            R$ {valor_aumento:.2f}")
print(f"Novo salário após aumento:   R$ {novo_salario:.2f}\n")