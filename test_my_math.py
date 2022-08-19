'''Testing MyMath module for proper performing on four methods - Add,Sub,Multi,Divide '''
import unittest
from my_math import MyMath


class TestMath(unittest.TestCase):
    '''Starting the tests with unittest'''

    def test_addition(self):
        '''Testing the addition method'''
        self.assertEqual(MyMath.addition(self, 15, 15), 30)
        self.assertEqual(MyMath.addition(self, 30, 15), 45)
        self.assertEqual(MyMath.addition(self, 151, 15), 166)
        self.assertEqual(MyMath.addition(self, -34, 15), -19)

    def test_substraction(self):
        '''Testing the substraction method'''
        self.assertEqual(MyMath.substraction(self, 45, 15), 30)
        self.assertEqual(MyMath.substraction(self, 15, 30), -15)
        self.assertEqual(MyMath.substraction(self, 45, 45), 0)
        self.assertEqual(MyMath.substraction(self, 45, 35), 10)


    def test_multiplication(self):
        '''Testing the multiplication method'''
        self.assertEqual(MyMath.multiplication(self, 8, 8), 64)
        self.assertEqual(MyMath.multiplication(self, 0, 0), 0)
        self.assertEqual(MyMath.multiplication(self, -10, 8), -80)
        self.assertEqual(MyMath.multiplication(self, 5, 8), 40)


    def test_division(self):
        '''Testing the divide method'''
        self.assertEqual(MyMath.division(self, 8, 8), 1)
        self.assertEqual(MyMath.division(self, 5, 8), 0.625)
        self.assertEqual(MyMath.division(self, 80, 8),10)
        self.assertEqual(MyMath.division(self, -40, 8), -5)

if __name__ == '__main__':
    unittest.main()
