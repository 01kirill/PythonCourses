"""
Дано трехзначное число, найти сумму его цифр. Например,
дано 123 – сумма 6, дано 555, сумма 15.
"""
number = 123
print("Число:", number)
digits_sum = 0
while number > 0:
    digits_sum += number % 10
    number //= 10
print("Сумма цифр числа:", digits_sum)
