numero = int(input("\nDigite um número [1 a 7]: "))

print()

match numero:
    case 1:
        print(f"{numero} - Domingo")
    case 2:
        print(f"{numero} - Segunda")
    case 3:
        print(f"{numero} - Terça")
    case 4:
        print(f"{numero} - Quarta")
    case 5:
        print(f"{numero} - Quinta")
    case 6:
        print(f"{numero} - Sexta")
    case 7:
        print(f"{numero} - Sábado")
    case _:
        print("Dia inválido.")

print()