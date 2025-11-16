num_1 = int(input("\nDigite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceior número: "))

print()

if num_1 >= num_2 and num_1 >= num_3:
    if num_2 >= num_3:
        print(f"{num_1}, {num_2}, {num_3}")
    else:
        print(f"{num_1}, {num_3}, {num_2}")

elif num_2 >= num_1 and num_2 >= num_3:
    if num_1 >= num_3:
        print(f"{num_2}, {num_1}, {num_3}")
    else:
        print(f"{num_2}, {num_3}, {num_1}")

else:
    if num_1 > num_2:
        print(f"{num_3}, {num_2}, {num_1}")
    else:
        print(f"{num_3}, {num_2}, {num_1}")
        
print()
