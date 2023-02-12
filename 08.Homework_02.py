# 2. Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных,
# вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyClassDiv(Exception):
    pass


def my_divisible():
    return int(input('введите делимое>> '))


def my_divisor():
    a = int(input('введите делитель>> '))
    if a == 0:
        raise MyClassDiv
    return a


while True:
    try:
        b = my_divisible()
        c = my_divisor()
        d = b / c
        print(d)
    except MyClassDiv:
        print('деление на 0!')
