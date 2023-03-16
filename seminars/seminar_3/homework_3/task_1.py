"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""

import random


def get_list(x):
    n = int(input('введите длину списка: '))
    numbers = [random.randint(1, n) for _ in range(n)]
    print(numbers)
    get_value(numbers, x)


def get_value(numbers, x):
    print(f'В списке {numbers} элемент {x} не встречается') if numbers.count(x)==0 \
        else print(f'В списке {numbers} элемент {x} встречается {numbers.count(x)} раз')


def main():
    x=int(input('Введите искомое число: '))
    get_list(x)


if __name__ == '__main__':
    main()