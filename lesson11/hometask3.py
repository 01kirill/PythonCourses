"""
Программа с классом Car. При инициализации объекта
ему должны задаваться атрибуты color, type и year.
Реализовать пять методов. Запуск автомобиля – выводит
строку «Автомобиль заведён». Отключение автомобиля –
выводит строку «Автомобиль заглушен». Методы для
присвоения автомобилю года выпуска, типа и цвета
"""

class Car:
    def __init__(self, color, type, year):
        self.__color = color
        self.__type = type
        self.__year = year
        self.__is_on = False

    def start(self):
        print("engine started")
        self.__is_on = True

    def stop(self):
        print("engine stopped")
        self.__is_on = False

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

car = Car("red", "type", 2000)
car.start()
car.stop()
