num = int(input("\nDigite um número: "))

fatorial = 1
contador = num

if num > 1:
    print(f"\n{num}! = {num} *", end = " ")
    while contador > 1:
        fatorial = fatorial * contador
        contador -= 1
        if contador > 1:
            print(contador, end = " * ")
        else:
            print(contador, end = " = ")

    print(f"{fatorial}\n")
elif num >= 0:
    print(f"Fatorial de {num} = {num}\n")
else:
    print(f"\nNão aceita números negativos.\n")