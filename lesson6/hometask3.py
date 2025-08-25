"""
Программа получает на вход число. Реализовать функцию,
которая определяет, является ли это число простым (делится
только на единицу и на само себя)
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Введите число: "))
print(f"Число {number} является простым? {is_prime(number)}")
