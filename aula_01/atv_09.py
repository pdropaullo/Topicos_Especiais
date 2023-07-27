def calcular_valor_arrecadado(qtd_pequenas, qtd_medias, qtd_grandes):
    preco_pequenas = 10
    preco_medias = 12
    preco_grandes = 15

    valor_arrecadado = (qtd_pequenas * preco_pequenas) + (qtd_medias * preco_medias) + (qtd_grandes * preco_grandes)
    return valor_arrecadado

def main():
    try:
        qtd_pequenas = int(input("Digite a quantidade de camisetas pequenas vendidas: "))
        qtd_medias = int(input("Digite a quantidade de camisetas médias vendidas: "))
        qtd_grandes = int(input("Digite a quantidade de camisetas grandes vendidas: "))

        valor_arrecadado = calcular_valor_arrecadado(qtd_pequenas, qtd_medias, qtd_grandes)

        print(f"O valor arrecadado com a venda das camisetas é: R$ {valor_arrecadado:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores inteiros válidos para a quantidade de camisetas vendidas.")

if __name__ == "__main__":
    main()
