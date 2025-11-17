numero_str = input("\nDigite um número inteiro positivo: ")
numero = int(numero_str)

if numero < 0:
    print("\nERRO. Número deve ser positivo.\n")

novo_numero_str = ""

for numero in numero_str:
    novo_numero_str = numero + novo_numero_str

print(f"\n{numero_str} -> {novo_numero_str}\n")