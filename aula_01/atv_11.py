def calcular_quantidade_ingredientes(num_sanduiches):
    queijo_por_sanduiche = 2 * 50 / 1000  # Duas fatias de queijo, cada fatia pesa 50 gramas, em quilos (1000 gramas = 1 quilo)
    presunto_por_sanduiche = 1 * 50 / 1000  # Uma fatia de presunto, pesa 50 gramas, em quilos
    carne_por_sanduiche = 1 * 100 / 1000  # Uma rodela de hambúrguer, pesa 100 gramas, em quilos

    total_queijo = queijo_por_sanduiche * num_sanduiches
    total_presunto = presunto_por_sanduiche * num_sanduiches
    total_carne = carne_por_sanduiche * num_sanduiches

    return total_queijo, total_presunto, total_carne

def main():
    try:
        num_sanduiches = int(input("Digite a quantidade de sanduíches a fazer: "))

        if num_sanduiches <= 0:
            print("A quantidade de sanduíches deve ser maior que zero.")
            return

        queijo, presunto, carne = calcular_quantidade_ingredientes(num_sanduiches)

        print(f"Quantidade de queijo necessária: {queijo:.2f} kg")
        print(f"Quantidade de presunto necessária: {presunto:.2f} kg")
        print(f"Quantidade de carne necessária: {carne:.2f} kg")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um valor inteiro válido para a quantidade de sanduíches.")

if __name__ == "__main__":
    main()
