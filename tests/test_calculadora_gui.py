import unittest
import tkinter as tk

from calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    raiz_cuadrada,
    CalculadoraGUI,
)


class TestFuncionesCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 5), 15)

    def test_dividir(self):
        self.assertEqual(dividir(20, 4), 5)

    def test_dividir_entre_cero(self):
        self.assertEqual(dividir(8, 0), "Error: no se puede dividir entre 0.")

    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(25), 5.0)


class TestVentanaCalculadora(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # oculta la ventana durante las pruebas
        self.app = CalculadoraGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_titulo_ventana(self):
        self.assertEqual(self.root.title(), "Calculadora Simple")

    def test_resultado_inicial(self):
        self.assertEqual(self.app.label_resultado.cget("text"), "Resultado: ")

    def test_accion_sumar_desde_gui(self):
        self.app.entry_num1.insert(0, "8")
        self.app.entry_num2.insert(0, "2")
        self.app.accion_sumar()
        self.assertEqual(self.app.label_resultado.cget("text"), "Resultado: 10.0")

    def test_accion_restar_desde_gui(self):
        self.app.entry_num1.insert(0, "9")
        self.app.entry_num2.insert(0, "3")
        self.app.accion_restar()
        self.assertEqual(self.app.label_resultado.cget("text"), "Resultado: 6.0")

    def test_accion_multiplicar_desde_gui(self):
        self.app.entry_num1.insert(0, "4")
        self.app.entry_num2.insert(0, "5")
        self.app.accion_multiplicar()
        self.assertEqual(self.app.label_resultado.cget("text"), "Resultado: 20.0")

    def test_accion_dividir_desde_gui(self):
        self.app.entry_num1.insert(0, "16")
        self.app.entry_num2.insert(0, "4")
        self.app.accion_dividir()
        self.assertEqual(self.app.label_resultado.cget("text"), "Resultado: 4.0")

    def test_accion_raiz_desde_gui(self):
        self.app.entry_num1.insert(0, "36")
        self.app.accion_raiz()
        self.assertEqual(self.app.label_resultado.cget("text"), "Resultado: 6.0")


if __name__ == "__main__":
    unittest.main()
