# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def div_func(a, b):
    """
    Функция деления
    :param a: делимое
    :param b: делитель
    :return: частное
    """
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на 0!')


first_number = int(input("Введите первое число >> "))
second_number = int(input("Введите второе число >> "))
print(f"Результат деления {first_number} на {second_number} является {div_func(first_number, second_number)}")
