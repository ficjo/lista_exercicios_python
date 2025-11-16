import math

a = float(input("\nDigite o valor de A: "))

if a == 0:
    print("\nEquação inválida: A não pode ser 0.")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    
    print()
    
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Não possui raízes reais (delta negativo)")
    elif delta == 0:
        x = (-b) / (2 * a)
        print("A equação possui apenas uma raíz real (delta zero).")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        
        print("A equação possui duas raízes reais (delta positivo).")
        print(f"Raiz 1: {x1:.2f}")
        print(f"Raiz 2: {x2:.2f}")

print()