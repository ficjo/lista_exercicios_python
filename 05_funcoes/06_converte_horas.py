print()

def converter_horas(hora_24):
    if 0 <= hora_24 < 12:
        indicador_ampm = 'A'
    else:
        indicador_ampm = 'P'

    if hora_24 == 0 or hora_24 == 12:
        hora_12 = 12
    elif hora_24 > 12:
        hora_12 = hora_24 - 12
    else:
        hora_12 = hora_24
        
    return hora_12, indicador_ampm


def mostrar_resultado(hora_12, minutos, indicador_ampm):
    ampm_extenso = "A.M." if indicador_ampm == 'A' else "P.M."
    print(f"Resultado: {hora_12}:{minutos:02d} {ampm_extenso}")

while True:
    hora_24 = int(input("Digite a hora (0-23): "))
    minutos = int(input("Digite os minutos (0-59): "))

    if not (0 <= hora_24 <= 23 and 0 <= minutos <= 59):
        print("Erro: Valores inválidos.")
        continue

    hora_12, indicador = converter_horas(hora_24)

    mostrar_resultado(hora_12, minutos, indicador)

    repetir = input("Deseja calcular novos valores? (s/n): ").strip().lower()
    if repetir != 's':
        break

print()