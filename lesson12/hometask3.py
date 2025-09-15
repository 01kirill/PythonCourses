"""
Класс содержит свойства:
● Скорость
● Максимальное количество посадочных мест
● Максимальная скорость
● Список фамилий пассажиров
● Флаг наличия свободных мест
● Словарь мест в автобусе
Методы:
● Посадка и высадка одного или нескольких пассажиров
● Увеличение и уменьшение скорости на заданное значение
● Операции in, += и -= (посадка и высадка пассажира по
фамилии)
"""

from dataclasses import dataclass, field

@dataclass
class Bus:
    __velocity: int
    __seats_count: int
    __max_velocity: int
    __passengers: list = field(default_factory=list)
    __is_full: bool = False
    __places_dict: dict = field(default_factory=dict)

    def fill_dict(self, lst):
        for i in range(len(lst)):
            self.__places_dict[i + 1] = lst[i]

    def is_passenger_in(self, passenger):
        if passenger in self.__passengers:
            print(f"Пассажир {passenger} есть в автобусе")
        else:
            print(f"Пассажира {passenger} нет в автобусе")

    def passenger_enter(self):
        if not self.__is_full:
            passenger = input("Введите фамилию: ")
            self.__passengers.append(passenger)
            for key, value in self.__places_dict.items():
                if value == "":
                    self.__places_dict[key] = passenger
                    break
            if len(self.__passengers) == self.__seats_count:
                self.__is_full = True
            print(f"Пассажир {passenger} вошел")
        else:
            print("Автобус полный")

    def passenger_leave(self):
        passenger = input("Введите фамилию: ")
        self.__passengers.remove(passenger)
        for key, value in self.__places_dict.items():
            if value == passenger:
                self.__places_dict[key] = ""
                break
        self.__is_full = False
        print(f"Пассажир {passenger} вышел")

    def increase_velocity(self, value):
        self.__velocity += value
        if self.__velocity > self.__max_velocity:
            self.__velocity = self.__max_velocity
        print(f"Текущая скорость: {self.__velocity}")

    def decrease_velocity(self, value):
        self.__velocity -= value
        if self.__velocity < 0:
            self.__velocity = 0
        print(f"Текущая скорость: {self.__velocity}")

lst = ["Smith", "Pitt", "Jackson"]

bus = Bus(50, 30, 100, lst, False, {i + 1: "" for i in range(30)})
bus.fill_dict(lst)
bus.is_passenger_in("Jackson")
#bus.passenger_leave()
#bus.passenger_enter()
print(bus)
bus.increase_velocity(10)
print(bus)
