def calcular_dias_passados(dia, mes):
    dias_por_mes = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
    dias_passados = dias_por_mes[mes - 1] + dia
    return dias_passados

def main():
    try:
        dia = int(input("Digite o dia da data: "))
        mes = int(input("Digite o mês da data: "))

        if dia <= 0 or mes <= 0 or mes > 12:
            print("Dia ou mês inválido. Certifique-se de inserir valores válidos.")
            return

        dias_passados = calcular_dias_passados(dia, mes)

        print(f"Desde o início do ano até a data informada passaram-se {dias_passados} dias.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros válidos para o dia e o mês.")

if __name__ == "__main__":
    main()
