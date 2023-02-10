# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.


# НЕ ВЕРНО, ТАК КАК НЕ ИСЧЕЗАЕТ ПРЕДЫДУЩАЯ ЗАПИСЬ

import time
import itertools


class TrafficLight:
    __color: str
    time_sleep: dict

    def __init__(self, red_time_sleep=7, yellow_time_sleep=2, green_time_sleep=8):
        self.time_sleep = {'RED': red_time_sleep, 'YELLOW': yellow_time_sleep, 'GREEN': green_time_sleep}

    def running(self):
        for i, j in itertools.cycle(self.time_sleep.items()):
            self.__color = i
            print(i)
            time.sleep(j)


my_trafficLight = TrafficLight(7, 2, 8)
my_trafficLight.running()

# как убрать надпись после окончания таймера?
