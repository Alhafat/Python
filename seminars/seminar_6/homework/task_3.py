"""
Дано 20+ значное целое число, проверить его на делимость на 7

Ввод 234523642345789812354678654323454919865

Вывод Делится
"""


def result(number):
    print(True) if (number % 1000 // 10 - number % 10 * 2) % 7 == 0 else print(False)
    # print((number % 1000 // 10 - number % 10 * 2) % 7 == 0)


def main():
    number = int(input('Введите число для проверки делимости на 7:'))
    result(number)


if __name__ == '__main__':
    main()
