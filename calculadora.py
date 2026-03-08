import math
import tkinter as tk
from tkinter import messagebox


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


def main():

    def obtener_valores():
        try:
            a = float(entry_num1.get())
            b = float(entry_num2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos.")
            return None, None

    def mostrar_resultado(texto):
        label_resultado.config(text=f"Resultado: {texto}")

    def accion_sumar():
        a, b = obtener_valores()
        if a is not None:
            mostrar_resultado(sumar(a, b))

    def accion_restar():
        a, b = obtener_valores()
        if a is not None:
            mostrar_resultado(restar(a, b))

    def accion_multiplicar():
        a, b = obtener_valores()
        if a is not None:
            mostrar_resultado(multiplicar(a, b))

    def accion_dividir():
        a, b = obtener_valores()
        if a is not None:
            mostrar_resultado(dividir(a, b))

    def accion_raiz():
        try:
            a = float(entry_num1.get())
            mostrar_resultado(raiz_cuadrada(a))
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido.")

    ventana = tk.Tk()
    ventana.title("Calculadora Simple")
    ventana.geometry("320x260")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Calculadora", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(ventana, text="Número 1").pack()
    entry_num1 = tk.Entry(ventana)
    entry_num1.pack(pady=5)

    tk.Label(ventana, text="Número 2").pack()
    entry_num2 = tk.Entry(ventana)
    entry_num2.pack(pady=5)

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, text="Sumar", width=12, command=accion_sumar).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame_botones, text="Restar", width=12, command=accion_restar).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame_botones, text="Multiplicar", width=12, command=accion_multiplicar).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame_botones, text="Dividir", width=12, command=accion_dividir).grid(row=1, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Raíz cuadrada", width=25, command=accion_raiz).pack(pady=5)

    global label_resultado
    label_resultado = tk.Label(ventana, text="Resultado:", font=("Arial", 12))
    label_resultado.pack(pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()