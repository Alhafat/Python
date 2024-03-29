"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

Диапазон от 6 до 12

Вывод: [1, 9, 13, 14, 19]
"""


def find_min_array_max(number_min, number_max, numbers):
    print([numbers.index(i) for i in numbers if number_min < i < number_max])


def main():
    number_min = int(input('Введите значение минимума: '))
    number_max = int(input('Введите значение максимума: '))
    numbers = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    find_min_array_max(number_min, number_max, numbers)


if __name__ == '__main__':
    main()
