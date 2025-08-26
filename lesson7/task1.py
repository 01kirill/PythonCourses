from functools import reduce

transactions_dollars = [120, 350, 50, 400, 90, 220]
transactions_euros = [t * 0.92 for t in transactions_dollars if t > 200]
print(transactions_euros)
#
words = ["apple", "banana", "cherry", "kiwi"]
fruits_dict = {word : len(word) for word in words}
print(fruits_dict)
#
celsius = [0, 10, 20, 30, 40]
fahrenheit_dict = {value : (value * 9 / 5 + 32) for value in celsius}
print(fahrenheit_dict)
#
double_sum = lambda x, y: 2 * (x + y)
print(double_sum(5, 6))
#
reversed_string = lambda str: str[::-1]
print(reversed_string("qwerty"))
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_list = list(map(lambda x: x * x, numbers))
print(squares_list)
#
even_numbers = list(filter(lambda x: x % 2 == 0, squares_list))
print(even_numbers)
#
summ = reduce(lambda x, y: x + y, even_numbers)
print(summ)
