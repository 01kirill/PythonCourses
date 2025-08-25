"""
 Реализовать функцию, которая находит сумму
элементов матрицы (матрица M x N). Определить, какую долю
в общей сумме (процент) составляет сумма элементов
каждого столбца
"""

from random import randint

def create_matrix(m, n):
    mtx = [[randint(1, 10) for _ in range(n)] for _ in range(m)]
    return mtx

def find_sum(mtx, m, n):
    sum = 0
    sums = []
    for i in range(n):
        prev_sum = sum
        for j in range(m):
            sum += mtx[j][i]
        sums.append(sum - prev_sum)
    print("Сумма матрицы:", sum)
    for i in range(len(sums)):
        print(f"Доля {i + 1}-го столбца в общей сумме: {int(sums[i] / sum * 100)}%")

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mtx = create_matrix(m, n)
print("Сгенерированная матрица.")
for row in mtx:
    print(row)
find_sum(mtx, m, n)
