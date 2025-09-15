"""
Класс «Товар» содержит следующие закрытые поля:
● Название товара
● Название магазина, в котором подаётся товар
● Стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● Вывод информации о товаре со склада по индексу
● Вывод информации о товаре со склада по имени товара
● Сортировка товаров по названию, по магазину и по цене
● Перегруженная операция сложения товаров по цене
"""

from dataclasses import dataclass, field

@dataclass
class Good:
    __name: str
    __shop_name: str
    __price: float

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def shop_name(self):
        return self.__shop_name

    @shop_name.setter
    def shop_name(self, value):
        self.__shop_name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __add__(self, other):
        return Good(self.name + " " + other.name, self.shop_name + " " + other.shop_name, self.price + other.price)

@dataclass
class Warehouse:
    __list: list[Good] = field(default_factory=list)
    def get_good_by_index(self, index):
        if 0 <= index < len(self.__list):
            return self.__list[index]
        return None

    def get_good_by_name(self, name):
        for good in self.__list:
            if good.name == name:
                return good
        return None

    def sort_goods(self, parameter):
        match parameter:
            case "name":
                return sorted(self.__list, key=lambda good: good.name)
            case "shop_name":
                return sorted(self.__list, key=lambda good: good.shop_name)
            case "price":
                return sorted(self.__list, key=lambda good: good.price)
            case _:
                return None

good1 = Good("milk", "almi", 10)
good2 = Good("milk", "evroopt", 20)
print(good1 + good2)
warehouse = Warehouse([good1, good2])
print(warehouse.get_good_by_name("milk"))
print(warehouse.get_good_by_index(1))
print(warehouse.sort_goods("shop_name"))
