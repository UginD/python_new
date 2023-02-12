# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    real_number: float
    imaginary_unit: float

    def __init__(self, real_number: float, imaginary_unit: float):
        self.real_number = real_number
        self.imaginary_unit = imaginary_unit

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(self.real_number + other.real_number,
                             self.imaginary_unit + other.imaginary_unit)

    def __mul__(self, other: 'ComplexNumber'):
        r_1 = self.real_number * other.real_number
        r_2 = self.imaginary_unit * other.imaginary_unit * -1
        i_1 = self.real_number * other.imaginary_unit
        i_2 = self.imaginary_unit * other.real_number
        return ComplexNumber(r_1 + r_2, i_1 + i_2)

    def __str__(self):
        if self.imaginary_unit > 0:
            return f'{self.real_number} + {self.imaginary_unit}i'
        else:
            return f'{self.real_number} {self.imaginary_unit}i'


a = ComplexNumber(25, 35)
b = ComplexNumber(18, 48)
print(a + b)
print(a * b)
