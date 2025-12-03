def imprimir_padrao_n(n):
    for i in range(1, n + 1):
        linha = ""
        
        for j in range(i):
            linha += str(i) + " "
        
        print(linha.strip()) # .strip() remove o espaço extra no final
        

valor_n = int(input("\nDigite um valor N (inteiro positivo) para o padrão: "))
imprimir_padrao_n(valor_n)

print()