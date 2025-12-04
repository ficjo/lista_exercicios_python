def desenha_moldura(linhas, colunas):
    MIN_VALOR = 1
    MAX_VALOR = 20

    linhas = max(MIN_VALOR, min(linhas, MAX_VALOR))
    colunas = max(MIN_VALOR, min(colunas, MAX_VALOR))

    CANTOS = '+'
    HORIZONTAL = '-'
    VERTICAL = '|'

    if linhas == 1 and colunas == 1:
        print(CANTOS)
        return

    linha_superior = CANTOS + HORIZONTAL * (colunas - 2) + CANTOS
    print(linha_superior)

    if linhas > 2:
        conteudo_linha = ' ' * (colunas - 2)
        
        linha_meio = VERTICAL + conteudo_linha + VERTICAL
        
        for _ in range(linhas - 2):
            print(linha_meio)

    if linhas > 1:
        print(linha_superior)


print("\nDesenho de Moldura (1-20 linhas/colunas)\n")

print("\n--- Exemplo 1 (7x15) ---")
desenha_moldura(7, 15)

print("\n--- Exemplo 3 (1x1) ---")
desenha_moldura(1, 1)

print("\n--- Exemplo 4 (1x8) ---")
desenha_moldura(1, 8)