"""
Напишите программу, в которой пользователь вводит целое число,
а программа каждую цифру в это числе меняет на "дополнение до 9":
цифра 0 меняется на 9, 1 меняется на 8, 8 меняется на 1, 9 меняется на 0 и т.д.
"""
import math


def get_list(number, n):
    numbers = [int(number[x]) for x in range(len(number))]
    print(numbers)
    for i in range(len(numbers)):
        numbers[i] = n - numbers[i] if (n - numbers[i]) >= 0 else 0
    return numbers


def main():
    try:
        number = (input('Введите целое число: '))
        n = 9
        print(number)
        result = get_list(number, n)
        print(result)

    except:
        print('Введены некорректные значения!')


if __name__ == '__main__':
    main()
