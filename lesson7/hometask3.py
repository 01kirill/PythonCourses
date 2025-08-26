"""
Дан список строк. С помощью filter() получить список
тех строк из исходного списка, которые являются
палиндромами (читаются в обе стороны одинаково, например,
’abcсba’)
"""

lst = ['abccba', 'abcd', 'abcdcba', 'efgh', 'aaaaaaa']

def is_palindrome(x):
    half1 = x[:len(x) // 2]
    half2 = x[len(x) // 2 + len(x) % 2:]
    half2 = half2[::-1]
    return half1 == half2

new_lst = list(filter(lambda x: is_palindrome(x), lst))
print(new_lst)
