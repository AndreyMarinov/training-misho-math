'''Function that'''
class Man:
    '''Defining my class as Man'''
    def __init__(self, age, first_name, last_name):
        self._age = age
        self._first_name = first_name
        self._last_name = last_name

    def get_age(self):
        '''The fget function is used for retrieving the attribute value'''
        return self._age

    def _set_age(self, ages_old):
        '''The fset function is used for setting the value of an attribute'''
        self._age = ages_old

    def del_age(self):
        '''The function is used to delete the value of an attribute'''
        del self._age


    def get_first_name(self):
        '''The fget function is used for retrieving the attribute value'''
        return self._first_name

    def _set_first_name(self, first_name):
        '''The fset function is used for setting the value of an attribute'''
        self._first_name = first_name

    def del_first_name(self):
        '''The function is used to delete the value of an attribute'''
        del self._first_name

    def get_last_name(self):
        '''The fget function is used for retrieving the attribute value'''
        return self._last_name

    def _set_last_name(self, last_name):
        '''The fset function is used for setting the value of an attribute'''
        self._last_name = last_name

    def del_last_name(self):
        '''The function is used to delete the value of an attribute'''
        del self._last_name

    def set_male_gender(self, gender = 'Male'):
        '''Setting the gender to Male '''
        return gender

    first_name = property(get_first_name, _set_first_name, del_first_name)
    age = property(get_age, _set_age, del_age)
    last_name = property(get_last_name, _set_last_name, del_last_name)


class Woman(Man):
    'Defining the class as Woman and inherits the atributes from the main class Man'
    def set_female_gender(self, gender = 'Female'):
        'Setting the gender to Female'
        return gender




John = Man(25, 'John', 'Laroy')
Henry = Man(21,'Henry','Seid')
Loid = Man (19, 'Loid', 'Loran')
Lans = Man (18, 'Lans', 'Leit')

Alis = Woman(23, 'Alis,', 'Lisenbur')
Leila = Woman(21, 'Leila,', 'Maid')
Stella = Woman(19, 'Stella,', 'Hilt')
Elana= Woman(18, 'Elana,', 'Hard')

John.age = 23
John.first_name = 'John'
John.last_name = 'Loy'
print(John.first_name,John.last_name,John.age,John.set_male_gender())

Henry.age = 21
Henry.first_name = 'Henry'
Henry.last_name = 'Seid'
print(Henry.first_name,Henry.last_name,Henry.age,Henry.set_male_gender())

Loid.age = 19
Loid.first_name = 'Loid'
Loid.last_name = 'Loran'
print(Loid.first_name,Loid.last_name,Loid.age,Loid.set_male_gender())


Lans.age = 18
Lans.first_name = 'Lans'
Lans.last_name = 'Leit'
print(Lans.first_name,Lans.last_name,Lans.age,Lans.set_male_gender())


Alis.age = 23
Alis.first_name = 'Alis'
Alis.last_name = 'Leyana'
print(Alis.first_name,Alis.last_name,Alis.age,Alis.set_female_gender())

Leila.age = 21
Leila.first_name = 'Leila'
Leila.last_name = 'Maid'
print(Leila.first_name,Leila.last_name,Leila.age,Leila.set_female_gender())

Stella.age = 19
Stella.first_name = 'Stella'
Stella.last_name = 'Hilt'
print(Stella.first_name,Stella.last_name,Stella.age,Stella.set_female_gender())

Elana.age = 18
Elana.first_name = 'Elana'
Elana.last_name = 'Hard'
print(Elana.first_name,Elana.last_name,Elana.age,Elana.set_female_gender())
