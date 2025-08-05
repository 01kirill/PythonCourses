number = ""
try:
    number = int(input("Введите число: "))
    print("Все четные числа от 1 до ", number, ":", sep="")
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(i, end=" ")
except ValueError:
    print("Некорректный ввод")