lado_1 = float(input("\nDigitie o primeiro lado: "))
lado_2 = float(input("Digite o segundo lado: "))
lado_3 = float(input("Digite o terceiro lado: "))

print()

if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
    print("TRIÂNGULO VÁLIDO")
    if lado_1 == lado_2 and lado_2 == lado_3:
        print("Triângulo EQUILÁTERO")
    elif lado_1 == lado_2 or lado_1 == lado_2 or lado_2 == lado_3:
        print("Triângulo ISÓSCELES")
    else:
        print("Triângulo ESCALENO")
else:
    print("TRIÂNGULO INVÁLIDO")
    
print()