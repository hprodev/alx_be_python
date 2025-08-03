import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator object before each test"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition method"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test subtraction method"""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(0, 4), -4)
        self.assertEqual(self.calc.subtract(-3, -4), -7)

    def test_multiply(self):
        """Test multiplication method"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_divide(self):
        """Test division method"""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)

    def test_divide_by_zero(self):
        """Test divide method for zero division"""
        self.assertIsNone(self.calc.divide(10, 0))
