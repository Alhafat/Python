"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""


#
# def get_pow_number(n):
#     array = [2 ** i for i in range(n)]
#     while array[-1] > n:
#         del array[len(array) - 1]
#     return array
#
#
# def main():
#     n = int(input('Введите натуральное число: '))
#     result = get_pow_number(n)
#     print(result)
#
#
# main()

def get_pow_number(n):
    p = 1
    while p <= n:
        print(p, end=' ')
        p *= 2


def main():
    n = int(input('Введите натуральное число: '))
    get_pow_number(n)


main()
