def calcular_ferraduras(cavalos_comprados):
    ferraduras_por_cavalo = 4
    total_ferraduras = cavalos_comprados * ferraduras_por_cavalo
    return total_ferraduras

def main():
    try:
        cavalos_comprados = int(input("Digite o número de cavalos comprados: "))

        if cavalos_comprados < 0:
            print("O número de cavalos comprados não pode ser negativo.")
            return

        total_ferraduras = calcular_ferraduras(cavalos_comprados)

        print(f"Serão necessárias {total_ferraduras} ferraduras para equipar todos os cavalos.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número inteiro válido.")

if __name__ == "__main__":
    main()
