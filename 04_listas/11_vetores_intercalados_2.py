import random

lista_a = []
lista_b = []
lista_c = []
lista_intercalados = []

for i in range(10):
    na = random.randint(1, 10)
    nb = random.randint(1, 10)
    nc = random.randint(1, 10)
    lista_a.append(na)
    lista_b.append(nb)
    lista_c.append(nc)

for i in range(10):
    lista_intercalados.append(lista_a[i])
    lista_intercalados.append(lista_b[i])
    lista_intercalados.append(lista_c[i])

print(f"\nLista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C: {lista_c}")
print(f"Intercalados: {lista_intercalados}\n")