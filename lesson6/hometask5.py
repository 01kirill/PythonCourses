"""
Программа получает на вход строку – сообщение и
указание, что нужно сделать: шифровать или дешифровать.
Реализовать две функции: первая шифрует заданное
сообщение шифром Цезаря, вторая расшифровывает. В
зависимости от выбора пользователя (шифровать или
дешифровать) вызывается соответствующая функция,
результат выводится в консоль.
"""

def ceasar_cipher(text, alphabet, key):
    result = ""
    for letter in text:
        if letter in alphabet:
            result += alphabet[(alphabet.find(letter) + key) % len(alphabet)]
    return result

def ceasar_decipher(text, alphabet, key):
    result = ""
    for letter in text:
        if letter in alphabet:
            result += alphabet[(alphabet.find(letter) - key) % len(alphabet)]
    return result

key = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"

text = input("Введите ваш текст: ")
choice = input("Введите c, чтобы зашифровать, или d, чтобы дешифровать: ")
if choice == "c":
    print("Зашифрованный текст:", ceasar_cipher(text, alphabet, key))
elif choice == "d":
    print("Дешифрованный текст:", ceasar_decipher(text, alphabet, key))
