def data_por_extenso(data_str):
    partes = data_str.split('/')
    if len(partes) != 3:
        return None

    try:
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
    except ValueError:
        return None

    if not (1 <= mes <= 12):
        return None
        
    if not (1 <= dia <= 31):
        return None

    meses_extenso = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho", 
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    nome_mes = meses_extenso[mes - 1]
    
    return f"{dia} de {nome_mes} de {ano}"


data_input = input("\nDigite a data no formato DD/MM/AAAA: ")
data_formatada = data_por_extenso(data_input)

if data_formatada:
    print(f"\nData formatada: {data_formatada}\n")
else:
    print("\nData inválida. Retorno: None\n")
