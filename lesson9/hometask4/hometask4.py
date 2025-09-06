"""
Напишите программу, которая получает на вход строку
с названием текстового файла и выводит на экран
содержимое этого файла, заменяя все запрещённые слова
звездочками. Запрещённые слова, разделённые символом
пробела, должны храниться в файле stop_words.txt.
Программа должна находить
запрещённые слова в любом месте файла, даже в середине
другого слова. Замена независима от регистра: если в списке
запрещённых есть слово exam, то замениться должны exam,
eXam, EXAm и другие вариации.
Пример: в stop_words.txt записаны слова: hello email
python the exam wor is
Текст файла для цензуры выглядит так: Hello, World! Python
IS the programming language of thE future. My EMAIL is...
PYTHON as AwESOME!
Тогда итоговый текст: *****, ***ld! ****** ** *** programming
language of *** future. My ***** **... ****** ** awesome!
"""

import re
import os

stop_words_path = "stop_words.txt"

with open(stop_words_path, "r") as f:
    stop_words = f.read().split()
input_path = input("Введите путь к файлу: ")
if os.path.exists(input_path):
    with open(input_path, "r") as f:
        text = " ".join(f.read().split()).lower()
        for word in stop_words:
            text = re.sub(word, "*"*len(word), text)
    print(f"Текст с цензурой: {text}")

else:
    print("Файла по введенному пути не существует")
