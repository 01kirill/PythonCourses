"""
Напишите программу, которая считывает текст из
файла (в файле может быть больше одной строки) и выводит
в новый файл самое часто встречаемое слово в каждой
строке и число – счётчик количества повторений этого слова
в строке.
"""

input_path = "input.txt"
with open(input_path, "r") as f:
    text = f.read().split()
words_dict = dict()
for word in text:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1
word = ""
count = 0
for key, value in words_dict.items():
    if value > count:
        word = key
        count = value
print(f"Самое часто встречаемое слово в тексте: '{word}', кол-во повторений: {count}")
