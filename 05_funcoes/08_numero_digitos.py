def contar_digitos(numero):
    return len(str(abs(numero)))

numero_digitado = int(input("\nDigite um número: "))
quantidade = contar_digitos(numero_digitado)
print(f"Número {numero_digitado} tem {quantidade} dígitos.\n")