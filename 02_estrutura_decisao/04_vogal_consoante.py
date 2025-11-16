letra = input("\nDigite uma letra: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"{letra} é uma VOGAL")
else:
    print(f"{letra} é uma CONSOANTE")

# Outra maneira

letra_2 = input("\nDigite outra letra: ").lower()

if letra in "aeiou":
    print(f"{letra_2} é uma VOGAL")
else:
    print(f"{letra_2} é uma CONSOANTE")
    
print()