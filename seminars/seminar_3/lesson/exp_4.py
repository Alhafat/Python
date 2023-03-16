"""
Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""
import random


def get_list():
    # numbers=[0, -1, 5, 2, 3]
    numbers = [random.randint(-5, 5) for _ in range(10)]
    return numbers


def get_value(numbers):
    count = 0
    for index in range(1, len(numbers)):
        if numbers[index] > numbers[index - 1]:
            count += 1
    print(f'Количество элементов массива {numbers}, больших предыдущего элемента составляет {count}')

def main():
    numbers=get_list()
    get_value(numbers)


if __name__ == '__main__':
    main()