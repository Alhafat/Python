"""Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного.
Ввод: Ввод:
5 5
1 2 3 4 5 1 5 1 5 1
Вывод: Вывод:
0 2
(каждое число вводится с новой строки)"""

from random import randint

n=int(input())
numbers=[randint(0,n) for _ in range(n)]
print(numbers)
count=0
for i in range(1,len(numbers)-1):
    if numbers[i-1]<numbers[i]>numbers[i+1]:
        # print(numbers[i])
        count+=1
print(count)