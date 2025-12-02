import random

lista_a = []
lista_b = []
lista_intercalados = []

for i in range(10):
    n = random.randint(1, 10)
    lista_a.append(n)

for i in range(10):
    n = random.randint(1, 10)
    lista_b.append(n)

for i in range(10):
    lista_intercalados.append(lista_a[i])
    lista_intercalados.append(lista_b[i])

print(f"\nLista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Intercalados: {lista_intercalados}\n")
    