def imprimir_padrao_crescente(n):
    if not isinstance(n, int) or n <= 0:
        print("Entrada inválida. Por favor, forneça um número inteiro positivo (N > 0).")
        return

    for i in range(1, n + 1):
        numeros_na_linha = []
        for j in range(1, i + 1):
            numeros_na_linha.append(str(j))
        
        print(" ".join(numeros_na_linha))
        

valor_n = int(input("\nDigite um valor N (inteiro positivo) para o padrão: "))

imprimir_padrao_crescente(valor_n)
print()

