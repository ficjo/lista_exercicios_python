
n = int(input("\nDigite o número de termos (n) da série de Fibonacci: "))

t1 = 0 
t2 = 1 
contador = 1
serie = ""

print("-" * 50)
print(f"\nSérie de Fibonacci até o {n}º termo:")

while contador <= n:
    proximo_termo = t1 + t2
    
    if contador == 1:
        print("1", end="")
        t1 = 1
        t2 = 1
    else:
        print(f", {t2}", end="")

    t1 = t2
    t2 = proximo_termo 
    
    contador += 1

print()
print("-" * 50)