'''Modul that reads the input entered by the user and print it on the terminal'''

def read_input():
    '''Function that reads the input entered from the user'''
    input_text_try = input(('Enter random text or value: ')) #Getting input from the user
    return input_text_try

def print_text(my_input):
    '''Function that prints on the terminal'''
    print(my_input)
print_text('test')
#print(read_input())
