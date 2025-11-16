valor_hora = float(input("\nDigite o valor/hora de trabalho: "))
horas_mes = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = valor_hora * horas_mes

percentual_sindicato = 3
percentual_fgts = 11
percentual_ir = 0
sindicato_desconto = salario_bruto * (percentual_sindicato / 100)
valor_fgts = salario_bruto * (percentual_fgts / 100)

if salario_bruto <= 900.00:
    percentual_ir = 0
elif salario_bruto <= 1500.00:
    percentual_ir = 5
elif salario_bruto <= 2500.00:
    percentual_ir = 10
else:
    percentual_ir = 20

valor_ir = salario_bruto * (percentual_ir / 100)
total_descontos = valor_ir + sindicato_desconto
salario_liquido = salario_bruto - total_descontos

print()

print("-" * 50)
print(f"{'* * * * RELATÓRIO * * * *':^45}")
print("-" * 50)
print(f"{'Salário Bruto:':<30} : R$ {salario_bruto:>10.2f}")
print(f"{'(-) IR (' + str(percentual_ir) + '%)':<30} : R$ {valor_ir:>10.2f}")
print(f"{'(-) Sindicato (' + str(percentual_sindicato) + '%)':<30} : R$ {sindicato_desconto:>10.2f}")
print(f"{'FGTS (' + str(percentual_fgts) + '%)':<30} : R$ {valor_fgts:>10.2f}")
print("-" * 50)
print(f"{'Total de descontos':<30} : R$ {total_descontos:>10.2f}")
print(f"{'Salário Líquido':<30} : R$ {salario_liquido:>10.2f}\n")
print("-" * 50)

print()
