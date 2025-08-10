"""
Дана строка. Замените в этой строке все появления буквы h на
букву H, кроме первого и последнего вхождения.
Подсказка: использовать метод replace с параметрами.
Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’
"""
input_str = "hhhabchghhh"
print("Входная строка: ", input_str)
char = 'h'
replaced_char = 'H'
first_index = input_str.find(char)
last_index = input_str.rfind(char)
to_replace = input_str[first_index + 1:last_index]
to_replace = to_replace.replace(char, replaced_char)
print(input_str[:first_index + 1] + to_replace + input_str[last_index:])
