def add_numbers(a,b):
    """Функция, складывающая два числа"""
    return a + b


def is_even(a):
    """Функция, проверяющая, является ли число четным"""
    return a % 2 == 0


def find_max(my_list):
    """Функция, находящая максимальное значение из списка чисел"""
    if len(my_list) > 0:
        return max(my_list)
    return 0



if __name__ == '__main__':
    assert add_numbers(2, 2) == 4

    assert is_even(2) == True

    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([]) == 0
