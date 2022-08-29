'''Modul that simulates different type of ppl that answers for their age,gender and name'''
class Man():
    '''Defining my class name as Man'''

    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.age = age
        self.family_name = family_name

    def print_first_and_second_name(self):
        '''Returning first and second name'''
        return f"My name is {self.first_name} {self.family_name}"

    def print_age(self):
        '''Returning the Age'''
        return f"I am {self.age} years old"

    def print_gender_male(self, gender = 'Male'):
        '''Returning the gender - Male or Female'''
        return f"I am {gender}"


class Woman(Man):
    '''Definig my class with and inherits functions from the main class Man'''
    def print_gender_female(self, gender='Female'):
        '''Returning the gender for Female'''
        return f"I am {gender}"

person=Man('Ayato', 'Haru', 21)
print(person.print_first_and_second_name())
print(person.print_age())
print(person.print_gender_male())

person=Woman('Alis', 'Vermili', 21)
print(person.print_first_and_second_name())
print(person.print_age())
print(person.print_gender_female())
