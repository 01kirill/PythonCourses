"""
1. Есть три целочисленные переменные, нужно посчитать:
● сумму
● разность
● произведение
● от первой переменной отнять вторую и прибавить третью
● поделить произведение двух переменных на третью
● от суммы первых двух переменных найти остаток от деления
на третью переменную
"""
first = 10
second = 20
third = 30
print("Переменная1(first): ", first, ", Переменная2(second): ", second,
      ", Переменная3(third): ", third, sep="")
print("Сумма переменных:", first + second + third)
print("Разность переменных:", first - second - third)
print("Произведение переменных:", first * second * third)
print("first - second + third:", first - second + third)
print("first * second / third:", first * second / third)
print("(first + second) % third:", (first + second) % third)
