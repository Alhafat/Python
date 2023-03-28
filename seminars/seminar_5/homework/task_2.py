"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""


def get_summ_numbers(a, b, summ_numbers=0):
    if a == 0 and b == 0:
        return summ_numbers
    else:
        summ_numbers += 2
        return get_summ_numbers(a - 1, b - 1, summ_numbers)


def main():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(get_summ_numbers(a, b))


if __name__ == '__main__':
    main()
