"""
Задача №3. Решение в группах
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
"""

import math

numbers=int(input('Введите количество классов: '))
array=[int(input(f'Введите количество учеников {x} класса: ')) for x in range(1,numbers+1)]
# print(array)

print(math.ceil(for x in array))