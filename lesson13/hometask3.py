"""
Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions, bacon.
• Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
• Создайте класс PizzaDirector, который принимает экземпляр
PizzaBuilder и содержит метод make_pizza, который
использует PizzaBuilder для создания Pizza
"""

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        lst = list()
        lst.append(str(self.size))
        if self.cheese:
            lst.append("cheese")
        if self.pepperoni:
            lst.append("pepperoni")
        if self.mushrooms:
            lst.append("mushrooms")
        if self.onions:
            lst.append("onions")
        if self.bacon:
            lst.append("bacon")
        return " ".join(lst)

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_cheese(self):
        self.pizza.cheese = True
        return self

    def set_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def set_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def set_onions(self):
        self.pizza.onions = True
        return self

    def set_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, size):
        return (self.builder
        .set_size(size)
        .set_cheese()
        .set_pepperoni()
        .set_mushrooms()
        .set_onions()
        .set_bacon()
        .build())

director = PizzaDirector(PizzaBuilder())
print(director.make_pizza(10))
