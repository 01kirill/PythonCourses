"""
Дана строка, состоящая из слов, разделенных пробелами. (Вот 4
варианта тестовых данных для программы: ‘Hello world’, ‘a b c’, ‘test’,
‘test1 test2 test3 test4 test5’). Определите, сколько в ней слов
"""
input_str = "test1 test2 test3 test4 test5"
print("Входная строка: ", input_str)
print("Количество слов в строке:", len(input_str.split()))
