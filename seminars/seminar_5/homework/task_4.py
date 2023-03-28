"""
Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел,
сумма цифр которых равна s. Запись натурального числа не может начинаться с цифры 0.
В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.

3 15 -> 69
4 16 -> 564
2 3 -> 3
6, 40 ->10746
"""


def get_numbers(k):
    numbers = [str(i) for i in range(10 ** (k - 1), 10 ** k)]
    return numbers


def find_numbers(numbers, s):
    temp = 0
    count = 0
    for i in numbers:
        for k in i:
            temp += int(k)
        if temp == s:
            count += 1
        else:
            temp = 0
            continue
    return count


def main():
    k = int(input('Введите размерность числа: '))
    s = int(input('Введите искомое значение суммы: '))
    numbers = get_numbers(k)
    # print(f' Получены следующая последовательность чисел: {numbers}')
    print(find_numbers(numbers, s))


if __name__ == '__main__':
    main()
