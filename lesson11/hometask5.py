"""
Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
● метод is_repeatance(s), который принимает некоторую
строку и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая
строка не содержит повторов
● метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом
"""

class SuperStr(str):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def is_palindrome(self):
        if len(self.value) == 0:
            return True
        else:
            string = self.value.lower()
            half1 = string[:len(string) // 2]
            half2 = string[len(string) // 2 + len(string) % 2:]
            half2 = half2[::-1]
            return half1 == half2

    def is_repeatance(self, x):
        if len(x) == 0:
            return False
        else:
            i = 1
            while len(x * i) <= len(self.value):
                if self.value == x * i:
                    return True
                i += 1
            return False

a = SuperStr('abccba')
print(a.is_palindrome())
b = SuperStr('abcdabcdabcd')
print(b.is_repeatance('abcd'))
