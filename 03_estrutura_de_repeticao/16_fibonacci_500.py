t1 = 0
t2 = 1
serie = "0, 1"

print()

print("-" * 50)
print("Série de Fibonacci até que o valor ultrapasse 500:")

while t2 <= 500:
    proximo_termo = t1 + t2
            
    serie += f", {proximo_termo}"
    
    t1 = t2
    t2 = proximo_termo

print(serie)
print("-" * 50)

print()