def dividir_conta(valor_total):
    valor_felipe = valor_total // 3
    valor_resto = valor_total % 3

    valor_carlos = valor_felipe
    valor_andre = valor_felipe

    if valor_resto >= 1:
        valor_carlos += 1
        valor_resto -= 1

    if valor_resto >= 1:
        valor_andre += 1

    return valor_carlos, valor_andre, valor_felipe

def main():
    try:
        valor_total_conta = float(input("Digite o valor total da conta: "))

        valor_carlos, valor_andre, valor_felipe = dividir_conta(valor_total_conta)

        print(f"Carlos deve pagar: R$ {valor_carlos:.2f}")
        print(f"André deve pagar: R$ {valor_andre:.2f}")
        print(f"Felipe deve pagar: R$ {valor_felipe:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um valor numérico válido para o valor total da conta.")

if __name__ == "__main__":
    main()
