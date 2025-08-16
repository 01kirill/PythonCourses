"""
Реализовать алгоритм бинарного поиска по
сдвинутому списку отсортированных чисел (например, дан
список [5, 6, 7, 1, 2, 3, 4])
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

def binary_search_shifted(lst, target):
    half_index = 0
    for i in range(len(lst) - 1):
        if lst[i + 1] < lst[i]:
            half_index = i
            break
    index1 = binary_search(lst[:half_index + 1], target)
    index2 = binary_search(lst[half_index + 1:], target)
    if index1 == -1 and index2 == -1:
        return -1
    elif index1 != -1:
        return index1
    elif index2 != -1:
        return index2 + len(lst[:half_index + 1])

n = int(input("Введите количество элементов списка: "))
lst = []
for i in range(n):
    lst.append(int(input(f"Введите {i + 1} элемент списка: ")))
target = int(input("Введите искомый элемент: "))
index = binary_search_shifted(lst, target)
if index == -1:
    print(f"Искомого элемента {target} в списке нет")
else:
    print(f"Искомый элемент {target} находится на позиции {index + 1}")
