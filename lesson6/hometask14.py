"""
Дана матрица M x N. Исходная матрица состоит из
нулей и единиц. Реализовать функцию, которая добавит к
матрице ещё один столбец, элементы которого делает
количество единиц в соответствующей строке чётным.
"""

from random import randint

def create_matrix(m, n):
    mtx = [[randint(0, 1) for _ in range(n)] for _ in range(m)]
    return mtx

def add_column(mtx):
    for row in mtx:
        count = 0
        for col in row:
            count += col
        row.append(count % 2)
    print("Новая матрица.")
    for row in mtx:
        print(row)

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mtx = create_matrix(m, n)
print("Сгенерированная матрица.")
for row in mtx:
    print(row)
add_column(mtx)
