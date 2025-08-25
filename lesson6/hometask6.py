"""
См. предыдущую задачу, но вместо шифра Цезаря
использовать шифр Виженера
"""

def extend_key(key, alphabet, text_length):
    if text_length > len(key):
        for i in range(text_length - len(key)):
            key += key[i % len(key)]
    return key

def vigenere_cipher(text, alphabet, key):
    result = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            result += alphabet[(alphabet.find(text[i]) + alphabet.find(key[i])) % len(alphabet)]
    return result

def vigenere_decipher(text, alphabet, key):
    result = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            result += alphabet[(alphabet.find(text[i]) - alphabet.find(key[i])) % len(alphabet)]
    return result

key = "code"
alphabet = "abcdefghijklmnopqrstuvwxyz"

text = input("Введите ваш текст: ")
choice = input("Введите c, чтобы зашифровать, или d, чтобы дешифровать: ")
key = extend_key(key, alphabet, len(text))
if choice == "c":
    print("Зашифрованный текст:", vigenere_cipher(text, alphabet, key))
elif choice == "d":
    print("Дешифрованный текст:", vigenere_decipher(text, alphabet, key))
