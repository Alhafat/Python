"""
Задача 8: Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
3 2 4 -> yes
3 2 1 -> no
"""
n = int(input('Введите количество долек по длине: '))
m = int(input('Введите количество долек по ширине: '))
k = int(input('Введите количество долек к отлому: '))

condition = (k % n == 0 or k % m == 0) and n>k<m
print('Отломить можно') if condition else print('Отломить нельзя')