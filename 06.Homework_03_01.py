# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name: str, surname: str, position: str):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int, "bonus": int}


class Position(Worker):
    def get_full_name(self):
        print(self.position, self.surname, self.name)

    def get_total_income(self):
        pass
    # как это сделать???


test_1 = Position("Имя", "Фамилия", "экономист")
test_1.get_full_name()
