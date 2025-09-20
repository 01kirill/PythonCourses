"""
Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
• Создайте несколько классов, каждый реализует определенную
стратегию математической операции, например, Addition,
Subtraction, Multiplication, Division. Каждый класс должен
содержать метод execute, который принимает два числа и
выполняет соответствующую операцию.
• Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate, который
выполняет операцию с помощью текущей стратегии
"""

from abc import ABC, abstractmethod

class CalculatorStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(CalculatorStrategy):
    def execute(self, a, b):
        return a + b

class Subtraction(CalculatorStrategy):
    def execute(self, a, b):
        return a - b

class Multiplication(CalculatorStrategy):
    def execute(self, a, b):
        return a * b

class Division(CalculatorStrategy):
    def execute(self, a, b):
        return a / b

class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        if self.strategy is not None:
            return self.strategy.execute(a, b)
        return None
