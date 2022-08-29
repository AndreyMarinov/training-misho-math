'''Moduls that calculates the factorial and recursive factorial'''
def factorial(first_number):
    '''Factorial - function that multiplies a number by every number below it till 1'''
    return first_number * factorial(first_number - 1) if first_number > 1 else 1

print(factorial(4)) #printing the returned value from the function


def recursive_factorial(number):
    '''Recursive factorial - Nonleaf function that calls itself.'''
    return 1 if number in (0, 1)  else number * recursive_factorial(number - 1)

print(recursive_factorial(1)) #printing the returned value from the function
