numero = int(input("\nDigite um número positivo menor que 1000: "))

if numero < 0 or numero >= 1000:
    print("\nO número deve ser POSITIVO e MENOR que 1000.\n")
    exit()
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    
    termo_cen = ""
    termo_dez = ""
    termo_uni = ""
    
    tem_centena = centenas > 0
    tem_dezena = dezenas > 0
    tem_unidade = unidades > 0

    if tem_centena:
        termo_cen = f"{centenas} centena"
        if centenas > 1:
            termo_cen += "s"

    if tem_dezena:
        termo_dez = f"{dezenas} dezena"
        if dezenas > 1:
            termo_dez += "s"

    if tem_unidade:
        termo_uni = f"{unidades} unidade"
        if unidades > 1:
            termo_uni += "s"

    mensagem = f"{numero} = "

    if tem_centena:
        mensagem += termo_cen

        if tem_dezena and tem_unidade:
            mensagem += ", "
        elif tem_dezena or tem_unidade:
            mensagem += " e "

    if tem_dezena:
        mensagem += termo_dez

        if tem_unidade and not tem_centena:
            mensagem += " e "
        elif tem_unidade and tem_centena:
            pass 

    if tem_unidade and not (tem_centena and tem_dezena):
        mensagem += termo_uni
    elif tem_unidade and tem_centena and tem_dezena:
        mensagem += termo_uni
    elif tem_unidade and tem_centena and not tem_dezena:
        mensagem += termo_uni
        
    print("-" * 50)
    print(f"Decomposição: {mensagem}")
    print("-" * 50)