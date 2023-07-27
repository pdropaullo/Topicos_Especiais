def calcular_dias_de_vida(idade):
    dias_por_ano = 365
    dias_de_vida = idade * dias_por_ano
    return dias_de_vida

def main():
    try:
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))

        if idade < 0:
            print("A idade não pode ser negativa.")
            return

        dias_de_vida = calcular_dias_de_vida(idade)

        print(f"{nome.upper()}, VOCÊ JÁ VIVEU {dias_de_vida} DIAS.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um valor numérico válido para a idade.")

if __name__ == "__main__":
    main()
