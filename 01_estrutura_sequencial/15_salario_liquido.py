DESCONTO_IR = 0.11
DESCONTO_INSS = 0.08
DESCONTO_SINDICATO = 0.05

valor_hora = float(input("\nValor por hora: "))
horas_mes = float(input("Horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_mes

valor_desconto_ir = salario_bruto * DESCONTO_IR
valor_desconto_inss = salario_bruto * DESCONTO_INSS
valor_desconto_sindicato = salario_bruto * DESCONTO_SINDICATO
total_descontos = valor_desconto_inss + valor_desconto_ir + valor_desconto_sindicato

salario_liquido = salario_bruto - total_descontos

print("\n* * * RESULTADOS * * *")
print(f"Salário Bruto       : R$ {salario_bruto:.2f}")
print(f"- IR (11%)          : R$ {valor_desconto_ir:.2f}")
print(f"- INSS (8%)         : R$ {valor_desconto_inss:.2f}")
print(f"- Sindicato (5%)    : R$ {valor_desconto_sindicato:.2f}")
print(f"= Salário Líquido   : R$ {salario_liquido:.2f}\n")