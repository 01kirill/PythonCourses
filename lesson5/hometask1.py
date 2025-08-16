"""
Задание:
Используя модуль math, вычислите значения по следующим
формулам:
sin and cos

Вопрос по реализации:
Здесь реализация при помощи итеративных вычислений, у меня
в универе была такая лаба, ее смысл был в том, чтобы
экономить ресурсы на вычислениях процессора
Но здесь у меня полученные результаты не совпадают с калькулятором
хотя мне кажется что я все сделал правильно

def Sin(x:float):
    n = 50
    result = float(x)
    sign = -1.0
    power = float(x**3)
    factor = 6.0
    for i in range(1, n + 1):
        result += sign * power / factor
        sign *= -1
        power *= x**2
        factor *= (factor + 1) * (factor + 2)
    return result

def Cos(x:float):
    n = 50
    result = 1.0
    sign = -1.0
    power = float(x**2)
    factor = 2.0
    for i in range(1, n + 1):
        result += sign * power / factor
        sign *= -1
        power *= x**2
        factor *= (factor + 1) * (factor + 2)
    return result
"""

#Вот рабочая реализация задачи

from math import (factorial, pow)

def sin(x:float):
    n = 50
    result = 0
    for i in range(n + 1):
        result += pow(-1, i) * pow(x, 2 * i + 1) / factorial(2 * i + 1)
    return result

def cos(x:float):
    n = 50
    result = 0
    for i in range(n + 1):
        result += pow(-1, i) * pow(x, 2 * i) / factorial(2 * i)
    return result

x = float(input("Введите число x: "))
print(f"Cинус числа {x} : {sin(x):.6f}")
print(f"Косинус числа {x} : {cos(x):.6f}")
