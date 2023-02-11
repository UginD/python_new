# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    v: float

    def __init__(self, name: str, v: float):
        super().__init__(name)
        self.v = v

    @property
    def calculate(self):
        return round(self.v / 6.5 + 0.5, 1)


class Suit(Clothes):
    h: float

    def __init__(self, name: str, h: float):
        super().__init__(name)
        self.h = h

    @property
    def calculate(self):
        return 2 * self.h + 0.3


my_coat = Coat('Пальто демисезонное', 46)
print(my_coat.calculate)

my_suit = Suit('Костюм мужской', 54)
print(my_suit.calculate)

