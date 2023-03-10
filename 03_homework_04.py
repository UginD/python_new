# 4. Программа принимает действительное положительное число x и
# целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    """
    возведение числа в степень без использования встроенной функции
    :param x: действительное положительное число, которое возводим в степень
    :param y: степень - целое отрицательное число
    :return: результат возведения х в степень y
    """

    if (x > 0) and (y < 0):
        count = 0
        my_list = []
        while count < abs(y):
            my_list.append(x)
            count += 1
        result = 1
        for i in my_list:
            result = result * i
        result = 1 / result
        return print(f'Число {x} в степени {y} составляет: {result}')
    else:
        print('Введены не корректные данные!')


a = int(input('Введите действительное положительное число x >> '))
b = int(input('Введите целое отрицательное число y >> '))
my_func(a, b)
