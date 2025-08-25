"""
Реализовать функцию, которая суммирует элементы
каждой строки матрицы с соответствующими элементами L-й
строки (матрица M x N
"""

from random import randint

def create_matrix(m, n):
    mtx = [[randint(1, 10) for _ in range(n)] for _ in range(m)]
    return mtx

def summarize_rows(mtx, l, m, n):
    for i in range(m):
        if i != l:
            for j in range(n):
                mtx[i][j] += mtx[l][j]
    for j in range(n):
        mtx[l][j] += mtx[l][j]
    print("Новая матрица.")
    for row in mtx:
        print(row)

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mtx = create_matrix(m, n)
l = int(input("Введите номер строки: "))
print("Сгенерированная матрица.")
for row in mtx:
    print(row)
summarize_rows(mtx, l - 1, m, n)
