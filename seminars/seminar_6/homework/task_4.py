"""
Даны числа a и b.
Определите, сколько существует последовательностей из a нулей и b единиц,
в которых никакие два нуля не стоят рядом.

Ввод 5 8
Вывод 126
"""


def find_numbers_f_1(a, b, array=[], text=''):
    if a == b == 0:
        if '00' not in text:
            array.append(text)
        # print(text)
        return
    if b:
        find_numbers_f_1(a, b - 1, array, text + '1')
    if a:
        find_numbers_f_1(a - 1, b, array, text + '0')


def main():
    a = int(input('Введите количество 0: '))
    b = int(input('Введите количество 1: '))
    if a > b and a - b != 1:
        print('Решений нет')
        return
    elif a == b:
        print('Существует 2 варианта последовательности')
        return
    find_numbers_f_1(a, b, result := [])
    print(len(result))


if __name__ == '__main__':
    main()
