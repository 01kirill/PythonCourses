"""
Реализовать функцию, которая находит минимальный и
максимальный элементы в матрице (матрица M x N). Вывести
в консоль индексы найденных элементов.
"""

from random import randint

def create_matrix(m, n):
    mtx = [[randint(1, 50) for _ in range(n)] for _ in range(m)]
    return mtx

def find_min_max(mtx, m, n):
    mx_row = 0
    mx_col = 0
    mn_row = 0
    mn_col = 0
    for i in range(m):
        for j in range(n):
            if mtx[i][j] > mtx[mx_row][mx_col]:
                mx_col = j
                mx_row = i
            if mtx[i][j] < mtx[mn_row][mn_col]:
                mn_col = j
                mn_row = i
    print("Адрес максимального элемента:", mx_row + 1, mx_col + 1)
    print("Адрес минимального элемента:", mn_row + 1, mn_col + 1)

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mtx = create_matrix(m, n)
print("Сгенерированная матрица.")
for row in mtx:
    print(row)
find_min_max(mtx, m, n)
