"""
Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0
"""

from random import randint

lst = [randint(-20, 20) for _ in range(10)]
print(f"Сгенерированный список:\n{lst}")
new_lst = list(filter(lambda x: x > 0, lst))
print(f"Новый список:\n{new_lst}")
