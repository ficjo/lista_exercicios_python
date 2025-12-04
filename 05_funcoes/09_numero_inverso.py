def inverter_numero(numero):
    numero_invertido = int(str(abs(numero))[::-1])
    if numero < 0:
        return -numero_invertido
    return numero_invertido

numero_digitado = int(input("\nDigite um número: "))
reverso = inverter_numero(numero_digitado)

print(f"\nNúmero original: {numero_digitado}")
print(f"Número invertido: {reverso}\n")

