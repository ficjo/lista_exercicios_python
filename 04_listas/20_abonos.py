PERCENTUAL_ABONO = 0.20
PISO_ABONO = 100.00

salarios = []
abonos = []

total_funcionarios = 0
funcionarios_piso = 0
total_gasto_abono = 0.0
maior_abono = 0.0

print("\nProjeção de Gastos com Abono")
print("----------------------------")

while True:
    salario = float(input("Salário: "))
    if salario < 0:
        print("Salário não pode ser negativo. Digite novamente.")
        continue
    if salario == 0:
        break
    
    abono_calculado = salario * PERCENTUAL_ABONO
    abono_final = max(abono_calculado, PISO_ABONO)

    salarios.append(salario)
    abonos.append(abono_final)
    total_funcionarios += 1
    total_gasto_abono += abono_final

    if abono_final == PISO_ABONO:
        funcionarios_piso += 1
    
    if abono_final > maior_abono:
        maior_abono = abono_final

if total_funcionarios == 0:
    print("\nNenhum salário. PROGRAMA ENCERRADO.\n")

print(f"\nSalário - Abono")
for salario, abono in zip(salarios, abonos):
    print(f"R$ {salario:8.2f} - R$ {abono:8.2f}")

print(f"\nForam processados {total_funcionarios} colaboradores")
print(f"Total gasto com abonos: R$ {total_gasto_abono:.2f}")
print(f"Valor mínimo pago a {funcionarios_piso} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_abono}\n")

