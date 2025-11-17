num_tabuada = int(input("\nMontar tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar por: "))

if inicio >= fim:
    print("\nERRO: O final não pode ser menor que o início.\n")
    exit()

print(f"Montando tabuada de {num_tabuada}, começando em {inicio}, terminando em {fim}:")

for i in range(inicio, fim + 1):
    print(f"{num_tabuada} x {i} = {num_tabuada * i}")

print()