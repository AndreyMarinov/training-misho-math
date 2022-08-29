'''Program for performing four methods - Addition, Substraction, Multiplication and Division'''


class DivideByZeroError(Exception):
    '''DividingByZero'''


class MyMath():
    '''Define my class name as MyMath'''

    @staticmethod
    def addition(number_1, number_2):
        '''Performing the addition method between two numbers'''
        return number_1 + number_2

    @staticmethod
    def substraction(number_1, number_2):
        '''Performing the substraction method between two numbers'''
        return number_1 - number_2

    @staticmethod
    def multiplication(number_1, number_2):
        '''Performing the multiplication method between two numbers'''
        return number_1 * number_2

    @staticmethod
    def division(number_1, number_2):
        '''Performing the division method between two numbers'''
        if number_2 == 0:
            raise DivideByZeroError("Zero can't be divided by zero")
        return number_1 / number_2

obj= MyMath()
print(obj.addition(9, 0))
