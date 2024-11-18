import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add(self):
        self.assertEqual(self.calc.add(3, 0), 3)

    def test_add(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_add(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_add(self):
        self.assertEqual(self.calc.multiply(1, 2), 3)

    def test_add(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_add(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_add(self):
        self.assertEqual(self.calc.divide(2, 2), 1)

    # def test_add(self):
        # self.assertEqual(self.calc.divide(2, 0), undefine)

    def test_add(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_add(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()