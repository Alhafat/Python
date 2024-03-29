"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""

import random


def get_list():
    n = int(input('введите длину списка: '))
    numbers = [random.randint(0, 5) for _ in range(n)]
    print(numbers)
    get_value(numbers)


def get_value(numbers):
    temp = [numbers.count(i) for i in numbers]
    print(f'В списке {numbers} встречается {temp.count(1)} уникальных элементов')


def main():
    get_list()


if __name__ == '__main__':
    main()
