def calcular_salarios(horas_normais, horas_extras):
    valor_hora_normal = 10.00
    valor_hora_extra = 15.00
    imposto = 0.10

    salario_bruto = (horas_normais * valor_hora_normal) + (horas_extras * valor_hora_extra)
    salario_liquido = salario_bruto * (1 - imposto)

    return salario_bruto, salario_liquido

def main():
    try:
        horas_normais = float(input("Digite o número de horas normais trabalhadas: "))
        horas_extras = float(input("Digite o número de horas extras trabalhadas: "))

        salario_bruto, salario_liquido = calcular_salarios(horas_normais, horas_extras)

        print(f"Salário bruto: R$ {salario_bruto:.2f}")
        print(f"Salário líquido: R$ {salario_liquido:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos válidos para as horas normais e horas extras.")

if __name__ == "__main__":
    main()
