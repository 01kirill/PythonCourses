"""
Программа с классом Sphere для представления сферы
в трёхмерном пространстве. Реализовать методы:
● конструктор, принимающий 4 числа: радиус и координаты
центра сферы x, y, z. Если конструктор вызывается без
аргументов, создать объект сферы с единичным радиусом
и центром в начале координат. Если конструктор
вызывается только с радиусом, создать объект с
соответствующим радиусом и центром в начале
координат
● метод get_volume(), возвращающий число – объем шара,
ограниченного текущей сферой
● метод get_square(), возвращающий число – площадь
внешней поверхности сферы
● метод get_radius(), возвращающий число – радиус текущей
сферы
● метод get_center(), возвращающий кортеж с координатами
центра сферы
● метод set_radius(radius), который принимает новое
значение радиуса, меняет радиус текущей сферы и ничего
не возвращает
● метод set_center(x, y, z), который принимает новые
значения для координат центра радиуса, меняет
координаты текущей сферы и ничего не возвращает
● метод is_point_inside(x, y, z), который принимает
координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимости от того,
находится ли точка внутри сферы
"""

from math import pi

class Sphere:
    def __init__(self, radius = 1, x = 0, y = 0, z = 0):
        self.__radius = radius
        self.__x = x
        self.__y = y
        self.__z = z

    def get_volume(self):
        return round(4/3 * pi * self.__radius ** 3, 2)

    def get_square(self):
        return round(4 * pi * self.__radius ** 2, 2)

    def is_point_inside(self, x, y, z):
        return ((x - self.__x) ** 2 + (y - self.__y) ** 2 + (z - self.__z) ** 2) ** 0.5 <= self.__radius

    @property
    def center(self):
        return tuple((self.__x, self.__y, self.__z))

    @center.setter
    def center(self, center):
        self.__x = center[0]
        self.__y = center[1]
        self.__z = center[2]

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

sphere = Sphere()
print(sphere.get_square())
print(sphere.get_volume())
print(sphere.is_point_inside(1, 0, 0))
