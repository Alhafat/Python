"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def numbers_pow(m, n, result=1):
    if n == 0:
        return result
    return numbers_pow(m, n - 1, result * m)


def main():
    number = int(input('Введите число, возводимое в степень: '))
    degree = int(input('Введите требуемую степень числа: '))
    print(numbers_pow(number, degree))


if __name__ == '__main__':
    main()
