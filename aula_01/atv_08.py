def calcular_media_ponderada(nota1, nota2, nota3):
    peso1, peso2, peso3 = 1, 2, 3
    soma_pesos = peso1 + peso2 + peso3
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / soma_pesos
    return media_ponderada

def main():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

        media_ponderada = calcular_media_ponderada(nota1, nota2, nota3)

        print(f"A média ponderada do aluno é: {media_ponderada:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos válidos para as notas.")

if __name__ == "__main__":
    main()
