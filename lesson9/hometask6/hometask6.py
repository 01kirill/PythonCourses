"""
В файл записано некоторое содержимое (буквы,
цифры, пробелы, специальные символы и т.д.). Числом
назовём последовательность цифр, идущих подряд. Вывести
сумму всех чисел, записанных в файле.
Пример:
Входные данные: 123 ааа456 1x2y3z 4 5 6
Выходные данные: 600
"""

import re

input_path = "input.txt"

with open(input_path, "r") as f:
    text = f.read()
numbers = re.sub(r'\D', ' ', text).split()
summ = 0
for number in numbers:
    summ += int(number)
print(f"Сумма чисел в файле: {summ}")
