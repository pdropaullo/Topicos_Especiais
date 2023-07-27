def celsius_para_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

def main():
    try:
        temp_celsius = float(input("Digite a temperatura em graus Celsius: "))

        temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)

        print(f"A temperatura em graus Fahrenheit é: {temp_fahrenheit:.2f} °F")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um valor numérico válido para a temperatura em graus Celsius.")

if __name__ == "__main__":
    main()
