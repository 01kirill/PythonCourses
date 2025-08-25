"""
Программа получает на вход число H. Реализовать
функцию, которая определяет, какие столбцы имеют хотя бы
одно такое же число, а какие не имеют (матрица M x N)
"""

from random import randint

def create_matrix(m, n):
    mtx = [[randint(1, 10) for _ in range(n)] for _ in range(m)]
    return mtx

def check_number(mtx, h, m, n):
    lst = []
    for i in range(n):
        is_number_in_col = False
        for j in range(m):
            if mtx[j][i] == h:
                is_number_in_col = True
                break
        lst.append(is_number_in_col)
    for i in range(len(lst)):
        print(f"Столбец {i + 1} имеет число H: {lst[i]}")

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mtx = create_matrix(m, n)
h = int(input("Введите число: "))
print("Сгенерированная матрица.")
for row in mtx:
    print(row)
check_number(mtx, h, m, n)
