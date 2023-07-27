def calcular_litros_gasolina(preco_litro, valor_pagamento):
    litros_gasolina = valor_pagamento / preco_litro
    return litros_gasolina

def main():
    try:
        preco_litro = float(input("Digite o preço do litro da gasolina em reais: "))
        valor_pagamento = float(input("Digite o valor do pagamento em reais: "))

        if preco_litro <= 0 or valor_pagamento <= 0:
            print("O preço do litro e o valor do pagamento devem ser maiores que zero.")
            return

        litros_gasolina = calcular_litros_gasolina(preco_litro, valor_pagamento)

        print(f"O motorista conseguiu colocar {litros_gasolina:.2f} litros de gasolina no tanque.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos válidos para o preço do litro e o valor do pagamento.")

if __name__ == "__main__":
    main()
