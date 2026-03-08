import unittest
from calculadora import sumar, restar, multiplicar, dividir, raiz_cuadrada


class TestCalculadora(unittest.TestCase):

    def test_sumar_dos_numeros(self):
        self.assertEqual(sumar(5, 3), 8)

    def test_restar_dos_numeros(self):
        self.assertEqual(restar(10, 4), 6)

    def test_multiplicar_dos_numeros(self):
        self.assertEqual(multiplicar(6, 7), 42)

    def test_dividir_dos_numeros(self):
        self.assertEqual(dividir(20, 5), 4)

    def test_dividir_entre_cero(self):
        self.assertEqual(dividir(8, 0), "Error: no se puede dividir entre 0.")

    def test_raiz_cuadrada_numero_positivo(self):
        self.assertEqual(raiz_cuadrada(25), 5)


if __name__ == "__main__":
    unittest.main()