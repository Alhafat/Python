"""
Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""


def get_array(n, count, number):
    array = [number]
    while len(array) < n:
        array.append(array[-1] + count)
    print(*array)



def main():
    n = int(input('Введите размер последовательности: '))
    count = int(input('Введите шаг последовательности: '))
    number = int(input('Введите первый элемент последовательности: '))
    get_array(n, count, number)


if __name__ == '__main__':
    main()