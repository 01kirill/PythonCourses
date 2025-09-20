"""
Реализовать программу для вывода
последовательности чисел Фибоначчи до определённого
числа в последовательности. Номер числа, до которого нужно
выводить, задаётся пользователем с клавиатуры. Для
реализации последовательности использовать генераторную
функцию
"""

def fibonacci(number):
    param1 = 0
    param2 = 1
    yield param1
    yield param2
    while param1 + param2 <= number:
        param = param1 + param2
        yield param
        param1 = param2
        param2 = param

try:
    number = int(input("Введите число: "))
    generator = fibonacci(number)
    print(f"Числа Фиббоначи от 0 до {number} (включая)")
    for item in generator:
        print(item, end=" ")
except ValueError:
    print("Некорректный ввод")
