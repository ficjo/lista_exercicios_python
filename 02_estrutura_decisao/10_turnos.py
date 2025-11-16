turno = input("\nDigite o turno [M/V/N]: ").upper()

print()

match turno:
    case 'M':
        print("Bom dia!")
    case 'V':
        print("Boa tarde!")
    case 'N':
        print("Boa noite!")
    case _:
        print("Turno inválido!")

print()