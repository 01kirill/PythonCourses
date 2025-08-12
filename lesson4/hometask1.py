"""
Используя модуль math, вычислите значения по следующим
формулам:
Значения a, b, x ввести с клавиатуры, вывести 4 рассчитанных по
формулам значения. Сделать красиво оформленные ввод и вывод
данных.
"""

import math

def function1(a:float, b:float):
    result = math.pow(a, 2) / 3
    result += (math.pow(a, 2)  + 4) / b
    result += math.sqrt(math.pow(a, 2) + 4) / 4
    result += math.sqrt(math.pow((math.pow(a, 2) + 4), 3)) / 4
    return result

def function2(x:float):
    result = math.pow(math.cos(math.pow(x, 2)), 2)
    result += math.pow(math.sin(2 * x - 1), 2)
    result = math.pow(result, 1/3)
    return result

def function3(x:float):
    return math.cos(x) + math.sin(x)

def function4(x:float):
    result = math.sqrt(1 + math.pow(math.sin(x), 2))
    result *= 3 * math.pow(x, 2)
    result += 5 * x
    return result

a = float(input("Введите число а: "))
b = float(input("Введите число b: "))
x = float(input("Введите число x: "))
print("Результат вычисления первой функции: y =", function1(a, b))
print("Результат вычисления второй функции: y =", function2(x))
print("Результат вычисления третьей функции: y =", function3(x))
print("Результат вычисления четвертой функции: y =", function4(x))
