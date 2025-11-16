ano = int(input("\nDigite o ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"\nO ano {ano} É BISSEXTO\n")
else:
    print(f"\nO ano {ano} NÃO É BISSEXTO\n")