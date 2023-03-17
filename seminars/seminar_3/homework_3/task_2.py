"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
"""

from random import randint


def get_list():
    n = int(input('введите длину списка: '))
    numbers = sorted([randint(1, 1000) for _ in range(n)])
    print(numbers)
    return numbers


def get_value(result, x):
    text_result = f'Самым близким по величине элемент к заданному числу {x} является '
    if x > result[-1]:
        print(text_result, result[-1])
        return
    elif x < result[0]:
        print(text_result, result[0])
        return
    else:
        for i in range(len(result))[-2::-1]:
            if x==result[i]:
                print(text_result, result[i])
                return
            elif x > result[i]:
                if x-result[i]>result[i+1]-x:
                    print(text_result, result[i+1])
                    return
                elif x-result[i]==result[i+1]-x:
                    print(text_result, result[i], 'и', result[i+1] )
                    return
                else:
                    print(text_result, result[i])
                    return


def main():
    x = int(input('Введите искомое число: '))
    result = get_list()
    get_value(result, x)


if __name__ == '__main__':
    main()
