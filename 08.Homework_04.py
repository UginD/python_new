# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники
# (принтер,сканер,ксерокс). В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


class Storage:
    name: str
    city: str
    square: float

    def __init__(self, name, city, square):
        self.name = name
        self.city = city
        self.square = square

    def __str__(self):
        return f'Склад {self.name}\nгород {self.city}\nобщая площадь {self.square} м2'


class Equipment:
    name: str
    _price: float
    quantity: int
    __manufacturer: str

    def __init__(self, name, price, quantity, manufacturer):
        self.name = name
        self._price = price
        self.quantity = quantity
        self.__manufacturer = manufacturer

    def __str__(self):
        return f'Позиция {self.name}, производитель: {self.__manufacturer}\n' \
               f'по цене {self._price} руб., кол-во {self.quantity} шт'


class Printer(Equipment):
    print_speed: int
    memory_capacity: int
    paper_size: str

    def __init__(self, name, price, quantity, manufacturer, print_speed, memory_capacity, paper_size):
        super().__init__(name, price, quantity, manufacturer)
        self.print_speed = print_speed
        self.memory_capacity = memory_capacity
        self.paper_size = paper_size

    @staticmethod
    def printing_started():
        print('Печать начата')

    @staticmethod
    def printing_stop():
        print('Печать завершена')


class Scanner(Equipment):
    scanner_speed: int
    paper_size: str

    def __init__(self, name, price, quantity, manufacturer, scanner_speed, paper_size):
        super().__init__(name, price, quantity, manufacturer)
        self.scanner_speed = scanner_speed
        self.paper_size = paper_size

    @staticmethod
    def scanner_started():
        print('Сканирование запущено')

    @staticmethod
    def scanner_stop():
        print('Сканирование завершено')


class Copier(Equipment):
    copier_speed: int
    number_copies: int

    def __init__(self, name, price, quantity, manufacturer, copier_speed, number_copies):
        super().__init__(name, price, quantity, manufacturer)
        self.copier_speed = copier_speed
        self.number_copies = number_copies

    @staticmethod
    def copier_started():
        print('Старт копирования')

    @staticmethod
    def copier_stop():
        print('Коприрование завершено')


my_printer = Printer('Тест_1', 1000, 10, 'DELL', 500, 200, 'A3, A4')
print(my_printer)
my_printer.printing_started()
my_printer.printing_stop()

my_storage = Storage('Калинка', 'Тюмень', 1000)
print(my_storage)
