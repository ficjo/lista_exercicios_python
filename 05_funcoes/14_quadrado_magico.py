"""
Não consegui resolver esse sozinho, precisei de ajuda.
"""

import itertools

def verifica_quadrado_magico(quadrado):
    soma_magica = 15

    soma_linha1 = quadrado[0] + quadrado[1] + quadrado[2]
    soma_linha2 = quadrado[3] + quadrado[4] + quadrado[5]
    soma_linha3 = quadrado[6] + quadrado[7] + quadrado[8]

    if not (soma_linha1 == soma_magica and soma_linha2 == soma_magica and soma_linha3 == soma_magica):
        return False

    soma_coluna1 = quadrado[0] + quadrado[3] + quadrado[6]
    soma_coluna2 = quadrado[1] + quadrado[4] + quadrado[7]
    soma_coluna3 = quadrado[2] + quadrado[5] + quadrado[8]

    if not (soma_coluna1 == soma_magica and soma_coluna2 == soma_magica and soma_coluna3 == soma_magica):
        return False

    soma_diag_principal = quadrado[0] + quadrado[4] + quadrado[8]
    soma_diag_secundaria = quadrado[2] + quadrado[4] + quadrado[6]

    if not (soma_diag_principal == soma_magica and soma_diag_secundaria == soma_magica):
        return False

    return True


def mostra_quadrado(quadrado):
    print(f"{quadrado[0]:>3} {quadrado[1]:>3} {quadrado[2]:>3}")
    print(f"{quadrado[3]:>3} {quadrado[4]:>3} {quadrado[5]:>3}")
    print(f"{quadrado[6]:>3} {quadrado[7]:>3} {quadrado[8]:>3}")
    print("-" * 11)


def encontra_quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    contador = 0

    for quadrado_tentativa in itertools.permutations(numeros):
        if verifica_quadrado_magico(quadrado_tentativa):
            contador += 1
            print(f"Quadrado Mágico Encontrado #{contador} (Soma Mágica: 15):")
            mostra_quadrado(quadrado_tentativa)

    print(f"\nTotal de Quadrados Mágicos únicos (rotações/reflexões excluídas): {contador}")

encontra_quadrados_magicos()
