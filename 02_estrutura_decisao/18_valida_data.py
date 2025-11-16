data = input("\nDigite a data [dd/mm/aaaa]: ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

data_valida = True

print()

if mes < 1 or mes > 12:
    data_valida = False

if mes in (1, 3, 5, 7, 8, 10, 12):
    if dia < 1 or dia > 31:
        data_valida = False
elif mes in (4, 6, 9, 11):
    if dia < 1 or dia > 30:
        data_valida = False
elif mes == 2:
    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
    if bissexto:
        if dia < 1 or dia > 29:
            data_valida = False
    else:
        if dia < 1 or dia > 28:
            data_valida = False

if data_valida:
    print(f"A data {data} é VÁLIDA")
else:
    print(f"A data {data} é INVÁLIDA")

print()

