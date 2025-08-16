"""
Дан список чисел, отсортированных по возрастанию.
На вход принимается значение, равное одному из элементов
списка. Реализовать алгоритм бинарного поиска, на выходе
программа должна вывести позицию искомого элемента в
исходном списке.
"""

def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
    return -1

n = int(input("Введите количество элементов списка: "))
lst = []
for i in range(n):
    lst.append(int(input(f"Введите {i + 1} элемент списка: ")))
target = int(input("Введите искомый элемент: "))
index = binary_search(lst, target)
if index == -1:
    print(f"Искомого элемента {target} в списке нет")
else:
    print(f"Искомый элемент {target} находится на позиции {index + 1}")
