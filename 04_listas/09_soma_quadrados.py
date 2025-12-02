lista_a = []

for i in range(10):
    n = int(input("Digite um número: "))
    lista_a.append(n)

soma_quadrados = 0
for n in lista_a:
    soma_quadrados += n * n

print(f"\nSoma dos quadrados: {soma_quadrados}\n")

# Usando comprehension
lista_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_quadrados = sum(x * x for x in lista_b)

print(f"Soma quadrados (b): {soma_quadrados}\n")