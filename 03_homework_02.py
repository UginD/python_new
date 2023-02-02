# 02.  Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя:
# имя,
# фамилия,
# год рождения,
# город проживания,
# email,
# телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def user_inf(name, surname, year_of_birth, city, email, telephone):
    print(name, surname, year_of_birth, city, email, telephone)


user_inf(name='Kate', surname='Moss', year_of_birth=1974, city='London', email='aaa@bbb', telephone=123456)


#  Такой вариант (без именованных параметров) мне нравится больше >>

user_information = ["Имя", "Фамилия", "год рождения", "город проживания", "email", "Телефон"]
new_inf = []


def user_inf():
    """
    принимает несколько параметров, описывающих данные пользователя
    :param : данные пользователя
    :return: печать данных о пользователе одной строкой
    """
    for i in user_information:
        i = input(f'Введите {i} >> ')
        new_inf.append(i)
    print(' '.join(new_inf))


user_inf()
