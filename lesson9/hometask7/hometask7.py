"""
Дан текстовый файл с несколькими строками.
Зашифровать шифром Цезаря, при этом шаг зависит от
номера строки: для первой строки шаг 1, для второй – 2 и т.д.
Пример:
Входные данные:
Hello
Hello
Hello
Hello
Выходные данные:
Ifmmp
Jgnnq
Khoor
Lipps
"""

def ceasar_cipher(text, alphabet, key):
    result = ""
    for letter in text:
        if letter in alphabet:
            result += alphabet[(alphabet.find(letter) + key) % len(alphabet)]
    return result

alphabet = "abcdefghijklmnopqrstuvwxyz"
input_path = "input.txt"

with open(input_path, "r") as f:
    lines = f.readlines()
lines = [line.split("\n")[0].lower() for line in lines]
for i in range(len(lines)):
    print(ceasar_cipher(lines[i], alphabet, i + 1))
