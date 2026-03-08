
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


class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Simple")
        self.root.geometry("360x330")
        self.root.resizable(False, False)

        titulo = tk.Label(root, text="Calculadora Simple", font=("Arial", 14, "bold"))
        titulo.pack(pady=10)

        tk.Label(root, text="Número 1").pack()
        self.entry_num1 = tk.Entry(root, width=25)
        self.entry_num1.pack(pady=5)

        tk.Label(root, text="Número 2").pack()
        self.entry_num2 = tk.Entry(root, width=25)
        self.entry_num2.pack(pady=5)

        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        btn_sumar = tk.Button(frame_botones, text="Sumar", width=12, command=self.accion_sumar)
        btn_sumar.grid(row=0, column=0, padx=5, pady=5)

        btn_restar = tk.Button(frame_botones, text="Restar", width=12, command=self.accion_restar)
        btn_restar.grid(row=0, column=1, padx=5, pady=5)

        btn_multiplicar = tk.Button(frame_botones, text="Multiplicar", width=12, command=self.accion_multiplicar)
        btn_multiplicar.grid(row=1, column=0, padx=5, pady=5)

        btn_dividir = tk.Button(frame_botones, text="Dividir", width=12, command=self.accion_dividir)
        btn_dividir.grid(row=1, column=1, padx=5, pady=5)

        btn_raiz = tk.Button(root, text="Raíz cuadrada (usa Número 1)", width=28, command=self.accion_raiz)
        btn_raiz.pack(pady=8)

        self.label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12))
        self.label_resultado.pack(pady=12)

    def mostrar_resultado(self, texto):
        self.label_resultado.config(text=f"Resultado: {texto}")

    def obtener_dos_valores(self):
        try:
            a = float(self.entry_num1.get())
            b = float(self.entry_num2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos en ambos campos.")
            return None, None

    def obtener_un_valor(self):
        try:
            return float(self.entry_num1.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido en Número 1.")
            return None

    def accion_sumar(self):
        a, b = self.obtener_dos_valores()
        if a is not None and b is not None:
            self.mostrar_resultado(sumar(a, b))

    def accion_restar(self):
        a, b = self.obtener_dos_valores()
        if a is not None and b is not None:
            self.mostrar_resultado(restar(a, b))

    def accion_multiplicar(self):
        a, b = self.obtener_dos_valores()
        if a is not None and b is not None:
            self.mostrar_resultado(multiplicar(a, b))

    def accion_dividir(self):
        a, b = self.obtener_dos_valores()
        if a is not None and b is not None:
            self.mostrar_resultado(dividir(a, b))

    def accion_raiz(self):
        a = self.obtener_un_valor()
        if a is not None:
            self.mostrar_resultado(raiz_cuadrada(a))


def main():
    root = tk.Tk()
    CalculadoraGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
