"""
Паттерн «Фабричный метод»
• Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
• Создайте классы Dog и Cat, которые наследуют от Animal и
реализуют метод speak.
• Создайте класс AnimalFactory, который использует паттерн
«Фабричный метод» для создания экземпляра Animal. Этот
класс должен иметь метод create_animal, который принимает
строку («dog» или «cat») и возвращает соответствующий
объект (Dog или Cat)
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Гав")

class Cat(Animal):
    def speak(self):
        print("Мяу")

class AnimalFactory:
    @staticmethod
    def create_animal(animal: str):
        match animal:
            case "Dog":
                return Dog()
            case "Cat":
                return Cat()
            case _:
                return None

print(AnimalFactory.create_animal("Dog"))
print(AnimalFactory.create_animal("Cat"))
print(AnimalFactory.create_animal("Animal"))
