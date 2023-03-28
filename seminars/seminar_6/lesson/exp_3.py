"""Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3
Вывод:
2
"""
from random import randint


# numbers = [randint(0, 10) for _ in range(10)]
# print(sorted(numbers))
# numbers_1=set(numbers)
# # print(numbers_1)
# temp=[]
# for i in numbers_1:
#     if numbers.count(i)>1:
#         temp.append(numbers.count(i)//2)
# # print(temp)
# print(sum(temp))


def input_num(message: str) -> int:
    input_error: bool = True
    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
            return temp


# n = [randint(1, 6) for i in range(input_num('Please input size of N list: '))]
n = [1, 2, 3, 2, 3]
print(n)
l_set = set(n)
for x in l_set:
    if n.count(x) - 1:
        print(f' digit {x}, count - {(n.count(x) - 1) * (n.count(x)) / 2}', end=" //  ")
