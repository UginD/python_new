# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

import re


def int_func(text):
    if text.isalpha() and text.islower() and re.search('[a-z]', text):
        return text.title()
    else:
        print("не корректный ввод данных")


a = input('Введите слово латинскими буквами в нижнем регистре >> ')
print(int_func(a))
