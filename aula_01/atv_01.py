def calcular_area_terreno(comprimento, largura):
    area = comprimento * largura
    return area

def main():
    try:
        comprimento = float(input("Digite o comprimento do terreno em metros: "))
        largura = float(input("Digite a largura do terreno em metros: "))

        area_terreno = calcular_area_terreno(comprimento, largura)

        print(f"A área do terreno é de {area_terreno:.2f} metros quadrados.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos válidos para as dimensões.")

if __name__ == "__main__":
    main()
