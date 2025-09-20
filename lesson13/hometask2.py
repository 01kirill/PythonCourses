"""
Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры
"""

def random_sequence(number):
    start = 0
    for i in range(number):
        yield start % 3 + 1
        start += 1

try:
    number = int(input("Введите число: "))
    generator = random_sequence(number)
    print("Бесконечная циклическая последовательность чисел")
    for item in generator:
        print(item, end="-")
except ValueError:
    print("Некорректный ввод")
