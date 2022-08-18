'''Program for performing four methods - Addition, Substraction, Multiplication and Division'''
class MyMath():
    '''Define my class name as MyMath'''

    def addition(self, number_1, number_2):
        '''Performing the addition method between two numbers'''
        return number_1 + number_2

    def substraction(self, number_1, number_2):
        '''Performing the substraction method between two numbers'''
        return number_1 - number_2

    def multiplication(self, number_1, number_2):
        '''Performing the multiplication method between two numbers'''
        return number_1 * number_2

    def division(self, number_1, number_2):
        '''Performing the division method between two numbers'''
        return number_1 / number_2

obj=MyMath()
'''Printing one of the methods on the terminal'''
print(obj.addition(30, 40))
