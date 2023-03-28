"""Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3 2
Вывод:
2
"""
from random import randint

numbers = [randint(0, 5) for _ in range(10)]
print(sorted(numbers))
numbers_1=set(numbers)
# print(numbers_1)
temp=[]
for i in numbers_1:
    if numbers.count(i)>1:
        temp.append(numbers.count(i)//2)
# print(temp)
print(sum(temp))