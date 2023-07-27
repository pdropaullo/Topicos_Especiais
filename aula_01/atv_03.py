def calcular_arrecadacao(paes, broas):
    preco_pao = 0.12
    preco_broa = 1.50

    total_arrecadado = (paes * preco_pao) + (broas * preco_broa)
    poupanca = total_arrecadado * 0.10

    return total_arrecadado, poupanca

def main():
    try:
        paes_vendidos = int(input("Digite a quantidade de pães franceses vendidos: "))
        broas_vendidas = int(input("Digite a quantidade de broas vendidas: "))

        if paes_vendidos < 0 or broas_vendidas < 0:
            print("As quantidades de pães e broas não podem ser negativas.")
            return

        total_arrecadado, poupanca = calcular_arrecadacao(paes_vendidos, broas_vendidas)

        print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
        print(f"Valor a guardar na conta poupança: R$ {poupanca:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros válidos para as quantidades de pães e broas.")

if __name__ == "__main__":
    main()
