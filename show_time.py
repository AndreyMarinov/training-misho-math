'''Modul that shows the current time'''
from datetime import datetime
from datetime import timedelta
from datetime import date


def get_time():
    '''Function that represents the current time '''
    return datetime.now().strftime('%H:%M:%S.%f')


print(get_time())


def get_current_time_and_date():
    '''Function that represents the current date in order y/m/d'''
    return date.today()


print('Current date:', get_current_time_and_date())


def substract_five_days_from_current_date():
    '''Function that substract five days from the current date'''
    days_substract = 5
    return date.today() - timedelta(days_substract)


print('5 days before the current date:', substract_five_days_from_current_date())
