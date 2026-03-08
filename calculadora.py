import math

def mostrar_menu():
    print("\n=== CALCULADORA SIMPLE ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz cuadrada")
    print("6. Salir")

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

def raiz_cuadrada(a):
    if a < 0:
        return "Error: no se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(a)

def raiz_cuadrada(a):
    if a < 0:
        return "Error: no se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(a)


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "6":
            print("Saliendo de la calculadora...")
            break

        if opcion in ["1", "2", "3", "4"]:
            num1 = pedir_numero("Ingresa el primer número: ")
            num2 = pedir_numero("Ingresa el segundo número: ")

            if opcion == "1":
                print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado: {restar(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == "4":
                print(f"Resultado: {dividir(num1, num2)}")

        elif opcion == "5":
            num = pedir_numero("Ingresa un número: ")
            print(f"Resultado: {raiz_cuadrada(num)}")

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()