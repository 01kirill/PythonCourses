"""
Реализовать функцию, которая находит сумму
элементов на главной диагонали и сумму элементов на
побочной диагонали (матрица M x N)
"""

from random import randint

def create_matrix(m):
    mtx = [[randint(1, 10) for _ in range(m)] for _ in range(m)]
    return mtx

def diagonals_sums(mtx, m):
    sum1 = 0
    sum2 = 0
    for i in range(m):
        sum1 += mtx[i][i]
        sum2 += mtx[i][m-1-i]
    print(f"Сумма на главной диагонали: {sum1}, сумма на побочной диагонали: {sum2}")

m = int(input("Введите количество строк и столбцов: "))
mtx = create_matrix(m)
print("Сгенерированная матрица.")
for row in mtx:
    print(row)
diagonals_sums(mtx, m)
