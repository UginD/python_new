# 7. Продолжить работу над заданием 6.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

import re


def int_func(text):
    if text.isalpha() and text.islower() and re.search('[a-z]', text):
        return text.title()


while True:
    try:
        b = input('Введите несколько слов латинскими буквами в нижнем регистре >> ').split(' ')
        result = []
        for i in b:
            el = int_func(i)
            result.append(el)
        print(" ".join(result))
    except TypeError:
        print("Ошибка! не корректный ввод данных")
