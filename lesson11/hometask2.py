"""
Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ.
"""

class Math:
    def __init__(self):
        pass

    @staticmethod
    def addition(a, b):
        print(f"{a} + {b} = {a + b}")

    @staticmethod
    def subtraction(a, b):
        print(f"{a} - {b} = {a - b}")

    @staticmethod
    def multiplication(a, b):
        print(f"{a} * {b} = {a * b}")

    @staticmethod
    def division(a, b):
        print(f"{a} / {b} = {a / b}")

calculator = Math()
calculator.addition(1, 2)
calculator.subtraction(1, 2)
calculator.multiplication(1, 2)
calculator.division(1, 2)
