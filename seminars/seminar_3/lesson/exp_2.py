"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""

import random


def get_list():
    numbers=[1,2,3,4,5,6,7]
    print(numbers)
    return numbers


def get_new_list(numbers, n):
    # [numbers.append(numbers[i.__index__()]) for i in range(n) ]
    # del numbers[:n]
    numbers.extend(numbers[:n+1])
    del numbers[:n+1]
    print(numbers)


def main():
    n=int(input('Введите границу сдвига: '))
    numbers=get_list()
    get_new_list(numbers, n)


if __name__ == '__main__':
    main()