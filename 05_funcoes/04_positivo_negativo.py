def eh_positivo_ou_negativo(n):
    if n > 0:
        return "P"
    return "N"

    
n = int(input("\nDigite um número: "))
print(eh_positivo_ou_negativo(n))
print()