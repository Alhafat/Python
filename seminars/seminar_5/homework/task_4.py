"""
Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел,
сумма цифр которых равна s. Запись натурального числа не может начинаться с цифры 0.
В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.

3 15 -> 69
4 16 -> 564
2 3 -> 3
6, 40 ->10746
"""
import time


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
        temp = 0
    return count


def main():
    k = int(input('Введите размерность числа: '))
    s = int(input('Введите искомое значение суммы: '))
    numbers = get_numbers(k)
    # print(f' Получены следующая последовательность чисел: {numbers}')
    # start_time = time.time()
    print(find_numbers(numbers, s))
    end_time = time.time()
    # print(end_time - start_time)


if __name__ == '__main__':
    main()



# k, s = [int(input(f'input {x}: ')) for x in ('k', 's')]
# count = 0
# start_time = time.time()
# for k_numbers in range(10 ** (k - 1), int('9' * k)):
#     if sum(map(int, str(k_numbers))) == s:
#         count += 1
# end_time = time.time()
# print('we have', count, 'numbers')
# print(end_time - start_time)