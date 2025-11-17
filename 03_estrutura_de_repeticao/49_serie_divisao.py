while True:
    n_str = input("\nDigite a quantidade de termos (n) da série: ")
    n = int(n_str)
    if n > 0:
        break
    else:
        print("A quantidade de termos deve ser um número positivo.")

soma_serie = 0.0
numerador = 1
denominador = 1
i = 1 

print("\nS:")

while i <= n:
    
    termo = numerador / denominador
    soma_serie += termo
    
    print(f"{numerador}/{denominador}", end="")
    
    if i < n:
        print(" + ", end="")
    
    numerador += 1
    denominador += 2
    i += 1

print(f"\nSoma da Série: {soma_serie:.2f}\n")