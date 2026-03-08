# calculadora.py

def mostrar_menu():
    print("\n=== CALCULADORA SIMPLE ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingresa un número.")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0."
    return a / b


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Saliendo de la calculadora...")
            break

        if opcion in ["1", "2", "3", "4"]:
            num1 = pedir_numero("Ingresa el primer número: ")
            num2 = pedir_numero("Ingresa el segundo número: ")

            if opcion == "1":
                resultado = sumar(num1, num2)
                print(f"Resultado: {num1} + {num2} = {resultado}")

            elif opcion == "2":
                resultado = restar(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")

            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                print(f"Resultado: {num1} * {num2} = {resultado}")

            elif opcion == "4":
                resultado = dividir(num1, num2)
                print(f"Resultado: {resultado}")
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()