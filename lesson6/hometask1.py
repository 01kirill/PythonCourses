"""
Дан список чисел, отсортированных по возрастанию. На
вход принимается значение, равное одному из элементов списка.
Реализовать функцию, выполняющую рекурсивный алгоритм
бинарного поиска, на выходе программа должна вывести позицию
искомого элемента в исходном списке
"""

def binary_search_recursive(lst, target, start, end):
    if start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid + 1
        if lst[mid] > target:
            return binary_search_recursive(lst, target, start, mid - 1)
        return binary_search_recursive(lst, target, mid + 1, end)
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Введите искомое число: "))
print("Исходный список:", lst)
print(f"Искомый элемент {target} находится под индексом "
      f"{binary_search_recursive(lst, target, 0, len(lst) - 1)}")
