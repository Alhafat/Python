"""
Напишите программу, в которой описана функция, возвращающая результатом сумму нечетных чисел.
Количество чисел передается аргументом функции.
"""
import random


def get_array(n):
    array = [2*i+1 for i in range(n)]
    array = sorted(array)
    print(array)
    print(f'Сумма нечетных чисел количеством {n} равна {sum(array)}')


def main():
    n = int(input('Введите количество нечетных чисел для расчета суммы: '))
    get_array(n)


main()