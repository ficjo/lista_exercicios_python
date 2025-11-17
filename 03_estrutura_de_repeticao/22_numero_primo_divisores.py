num = int(input("\nDigite um número: "))

if num <= 1:
    print("\nNão é primo.\n")
else:
    eh_primo = True
    divisor = 2
    
    while divisor < num:
        # Se encontrar uma divisão exata, pode quebrar
        if num % divisor == 0:
            eh_primo = False
            break
        divisor += 1
    
    if eh_primo:
        print(f"\n{num} é primo.\n")
    else:
        print(f"\n{num} não é primo.")

contador = num
if not eh_primo:
    print(f"\n{num} é divisível por: \n")
    while contador >= 1:
        if num % contador == 0:
            print(f"{contador}", end = " ")
        contador -= 1

    print("\n")