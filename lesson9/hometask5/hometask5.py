"""
В текстовый файл построчно записаны фамилия и имя
учащихся класса и оценка за контрольную. Вывести на экран
всех учащихся, чья оценка меньше трёх баллов.
"""

input_path = "input.txt"

with open(input_path, "r") as f:
    lst = []
    lines = f.readlines()
    for line in lines:
        lst.append(line.strip().split())
print("Учащиеся, чья оценка за контрольную меньше трех баллов:")
for item in lst:
    if int(item[2]) < 3:
        print(item[0], item[1])
