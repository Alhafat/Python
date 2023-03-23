"""Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes"""


def checking_number(n):
    numbers = []
    [numbers.append(int(i)) for i in range(1, n // 2 + 1) if n % i == 0]
    # print(numbers)
    result = f' является.' if len(numbers) <= 1 else f' не является.'
    print(f'Введенное число {n} простым' + result)


def main():
    n = int(input('Введите любое число: '))
    print('Получено следующее значение: ', n)
    checking_number(n)


if __name__ == '__main__':
    main()
