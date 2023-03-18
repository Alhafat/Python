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


def get_list():
    n = int(input('введите длину списка: '))
    numbers = [random.randint(1, n) for _ in range(n)]
    return numbers


def get_value(numbers, x):
    value = f'встречается {numbers.count(x)} раз' if numbers.count(x) == 0 else f'не встречается'
    print('\n' + f'В списке {numbers} элемент {x} ' + value)


def main():
    x = int(input('Введите искомое число: '))
    get_value(get_list(), x)


if __name__ == '__main__':
    main()
