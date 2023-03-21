"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a _1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""

text = ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']
    # input('Введите строку: ').split()
print(text)
for i in range(len(text))[::-1]:
    count = text[:i].count(text[i])
    print(count)
    if count > 0:
        text[i] = text[i] + '_' + str(count)
        # print(count)
print(text)
