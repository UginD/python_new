# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    attrs: list = []

    def __init__(self, attrs: list):
        self.my_list = attrs

    def __add__(self, other: 'Matrix'):
        a = len(self.my_list)
        b = len(self.my_list[0])
        new_list = [[self.my_list[row][i] + other.my_list[row][i]
                     for i in range(b)] for row in range(a)]
        return Matrix(new_list)

    def __str__(self):
        return '\n'.join(str(row).strip('[]').replace(',', ' ') for row in self.my_list)


my_matrix_1 = Matrix([[31, 32], [37, 43], [51, 86]])
print(my_matrix_1)
print('___________________')

my_matrix_2 = Matrix([[13, 23], [73, 34], [15, 68]])
print(my_matrix_2)
print('___________________')

sum_my_matrix = my_matrix_1 + my_matrix_2
print(sum_my_matrix)
