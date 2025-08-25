"""
Реализовать функцию, которая создаёт матрицу
размером M строк на N столбцов и заполняет её рандомными
числами.
"""

from random import randint

def create_matrix(m, n):
    mtx = [[randint(1, 50) for _ in range(n)] for _ in range(m)]
    return mtx

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mtx = create_matrix(m, n)
print("Сгенерированная матрица.")
for row in mtx:
    print(row)
