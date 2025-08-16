"""
Реализовать вывод последовательности чисел Фибоначчи (1 1 2
3 5 8 13 21 34 55 89 ...), где каждое следующее число является
суммой двух предыдущих.
"""

n = int(input("Введите количество чисел: "))
first = 1
second = 1
print(f"Первые {n} чисел Фибоначчи:\n{first} {second} ", end = "")
for i in range(3, n + 1):
    number = first + second
    print(number, end=" ")
    first = second
    second = number
