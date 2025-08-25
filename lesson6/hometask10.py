"""
Реализовать функцию, которая перемножает
элементы каждого столбца матрицы с соответствующими
элементами K-го столбца (матрица M x N).
"""

from random import randint

def create_matrix(m, n):
    mtx = [[randint(1, 10) for _ in range(n)] for _ in range(m)]
    return mtx

def multiply_columns(mtx, k, m, n):
    for i in range(n):
        if i != k:
            for j in range(m):
                mtx[j][i] *= mtx[j][k]
    for j in range(m):
        mtx[j][k] *= mtx[j][k]
    print("Новая матрица.")
    for row in mtx:
        print(row)

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mtx = create_matrix(m, n)
k = int(input("Введите номер столбца: "))
print("Сгенерированная матрица.")
for row in mtx:
    print(row)
multiply_columns(mtx, k - 1, m, n)
