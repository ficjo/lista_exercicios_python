while True:
    n_str = input("\nDigite a quantidade de termos (N): ")
    n = int(n_str)
    if n > 0:
        break
    else:
        print("O número de termos deve ser positivo.\n")

H = 0.0
i = 1

print("\nH = ", end="")

while i <= n:
    
    print(f"1/{i}", end="")
    
    H += 1.0 / i 

    if i < n:
        print(" + ", end="")
        
    i += 1


print(f" = {H:.3f}\n")