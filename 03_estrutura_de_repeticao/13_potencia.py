
base = int(input("\nDigite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1.0
contador = 0

if expoente < 0:
    print("\nERRO: Não aceita expoentes negativos.")
elif expoente == 0:
    resultado = 1.0
else:
    while contador < expoente:
        resultado = resultado * base
        contador += 1

print(f"\n{base} ^ {expoente} = {resultado}\n")    
