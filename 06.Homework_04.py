# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def info_car(self):
        if self.is_police is True:
            print(f'Полицейский автомобиль {self.name}, цвет {self.color}')
        else:
            print(f'Автомобиль {self.name}, цвет {self.color}')

    def go(self):
        print(f'Машина {self.name} поехала')
    # машина поехала

    def stop(self):
        print(f'Машина {self.name} остановилась')
    # машина остановилась

    def turn(self, direction: str):
        print(f'Машина {self.name} повернула {direction}')
    # машина повернула

    def show_speed(self, speed: int):
        print(f'Скорость автомобиля {self.name}: {speed} км/час')
    # показывает текущую скорость автомобиля


class TownCar(Car):

    def show_speed(self, speed: int):
        if speed > 60:
            a = speed - 60
            print(f"Превышение скорости на {a} км/час!")
        else:
            print(f'Скорость автомобиля {self.name}: {speed} км/час')
            # переопределение метод show_speed


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self, speed: int):
        if speed > 40:
            a = speed - 40
            print(f"Превышение скорости на {a} км/час!")
        else:
            print(f'Скорость автомобиля {self.name}: {speed} км/час')
    # переопределение метода show_speed


class PoliceCar(Car):
    pass


test = TownCar('test_town_car', 'красный', False)
test.info_car()
test.go()
test.stop()
test.turn('налево')
test.show_speed(100)

test_2 = SportCar('test_sport_car', 'желтый', False)
test_2.info_car()
test_2.go()
test_2.stop()
test_2.turn('направо')
test_2.show_speed(180)

test_3 = WorkCar('test_work_car', 'серый', False)
test_3.info_car()
test_3.go()
test_3.stop()
test_3.turn('в сторону стройки')
test_3.show_speed(90)

test_4 = PoliceCar('test_police_car', 'красный', True)
test_4.info_car()
test_4.go()
test_4.stop()
test_4.turn('за пончиками')
test_4.show_speed(120)
