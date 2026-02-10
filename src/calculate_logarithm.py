import math

def calculate_logarithm(number):
    '''Функция, которая показывает ошибку при вычислении логарифма.'''
    if number <= 0:
        raise ValueError("Логарифм можно вычислить только для положительных чисел")
    return math.log(number)