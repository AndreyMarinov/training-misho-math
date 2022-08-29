'''Testing MyMath module for proper performing on four methods - Add,Sub,Multi,Divide '''
import unittest


from my_math import MyMath


class TestMath(unittest.TestCase):
    '''Starting the tests with unittest'''

    def test_addition_of_two_positive_integers(self):
        self.assertEqual(MyMath.addition(2, 2), 4)

    def test_addition_of_positive_and_negative_integers(self):
        self.assertEqual(MyMath.addition(2, -2), 0)

    def test_addition_of_two_negative_integers(self):
        self.assertEqual(MyMath.addition(-2, -2), -4)

    def test_addition_of_two_negative_and_positive_integers(self):
        self.assertEqual(MyMath.addition(-2, 2), 0)

    def test_addition_of_two_floats(self):
        self.assertEqual(MyMath.addition(0.2, 0.1), 0.3)


  # def test_substraction(self):



   # def test_multiplication(self):



    #def test_division(self):


    #def test_divide_by_zero(self):'''


if __name__ == '__main__':
    unittest.main()
