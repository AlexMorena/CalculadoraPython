def calcular():
    while True:
        print("\n=== Calculadora en Python ===")
        try:
            num1 = float(input("Ingresa el primer número: "))
            operador = input("Ingresa el operador (+, -, *, /): ")
            num2 = float(input("Ingresa el segundo número: "))

            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                    continue
                resultado = num1 / num2
            else:
                print("Error: Operador no válido.")
                continue

            print(f"Resultado: {num1} {operador} {num2} = {resultado}")

        except ValueError:
            print("Error: Entrada inválida. Ingresa números válidos.")

        otra = input("¿Deseas hacer otro cálculo? (S/N): ").strip().lower()
        if otra != 's':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    calcular()
