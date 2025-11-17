maior_numero = 0

print() 

for i in range(0, 5):
    numero = int(input("Digite um número: "))
    if i == 0:
        maior_numero = numero
    elif numero >= maior_numero:
        maior_numero = numero

print(f"\nMaior número: {maior_numero}\n")